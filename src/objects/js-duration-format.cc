// Copyright 2022 the V8 project authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#ifndef V8_INTL_SUPPORT
#error Internationalization is expected to be enabled.
#endif  // V8_INTL_SUPPORT

#include "src/objects/js-duration-format.h"

#include <map>
#include <memory>
#include <string>
#include <string_view>

#include "src/execution/isolate.h"
#include "src/heap/factory.h"
#include "src/objects/intl-objects.h"
#include "src/objects/js-duration-format-inl.h"
#include "src/objects/js-number-format.h"
#include "src/objects/js-temporal-objects.h"
#include "src/objects/managed-inl.h"
#include "src/objects/objects-inl.h"
#include "src/objects/option-utils.h"
#include "unicode/listformatter.h"
#include "unicode/locid.h"
#include "unicode/numberformatter.h"
#include "unicode/ulistformatter.h"
#include "unicode/unumberformatter.h"

namespace v8 {
namespace internal {

using temporal::DurationRecord;

namespace {

// #sec-getdurationunitoptions
enum class StylesList { k3Styles, k4Styles, k5Styles };
enum class UnitKind { kMinutesOrSeconds, kOthers };
struct DurationUnitOptions {
  JSDurationFormat::FieldStyle style;
  JSDurationFormat::Display display;
};
Maybe<DurationUnitOptions> GetDurationUnitOptions(
    Isolate* isolate, const char* unit, const char* display_field,
    Handle<JSReceiver> options, JSDurationFormat::Style base_style,
    StylesList styles_list, JSDurationFormat::FieldStyle prev_style,
    UnitKind unit_kind, const char* method_name) {
  JSDurationFormat::FieldStyle style;
  JSDurationFormat::FieldStyle digital_base;
  // 1. Let style be ? GetOption(options, unit, "string", stylesList,
  // undefined).
  switch (styles_list) {
    case StylesList::k3Styles:
      // For years, months, weeks, days
      MAYBE_ASSIGN_RETURN_ON_EXCEPTION_VALUE(
          isolate, style,
          GetStringOption<JSDurationFormat::FieldStyle>(
              isolate, options, unit, method_name, {"long", "short", "narrow"},
              {JSDurationFormat::FieldStyle::kLong,
               JSDurationFormat::FieldStyle::kShort,
               JSDurationFormat::FieldStyle::kNarrow},
              JSDurationFormat::FieldStyle::kUndefined),
          Nothing<DurationUnitOptions>());
      digital_base = JSDurationFormat::FieldStyle::kShort;
      break;
    case StylesList::k4Styles:
      // For milliseconds, microseconds, nanoseconds
      MAYBE_ASSIGN_RETURN_ON_EXCEPTION_VALUE(
          isolate, style,
          GetStringOption<JSDurationFormat::FieldStyle>(
              isolate, options, unit, method_name,
              {"long", "short", "narrow", "numeric"},
              {JSDurationFormat::FieldStyle::kLong,
               JSDurationFormat::FieldStyle::kShort,
               JSDurationFormat::FieldStyle::kNarrow,
               JSDurationFormat::FieldStyle::kNumeric},
              JSDurationFormat::FieldStyle::kUndefined),
          Nothing<DurationUnitOptions>());
      digital_base = JSDurationFormat::FieldStyle::kNumeric;
      break;
    case StylesList::k5Styles:
      // For hours, minutes, seconds
      MAYBE_ASSIGN_RETURN_ON_EXCEPTION_VALUE(
          isolate, style,
          GetStringOption<JSDurationFormat::FieldStyle>(
              isolate, options, unit, method_name,
              {"long", "short", "narrow", "numeric", "2-digit"},
              {JSDurationFormat::FieldStyle::kLong,
               JSDurationFormat::FieldStyle::kShort,
               JSDurationFormat::FieldStyle::kNarrow,
               JSDurationFormat::FieldStyle::kNumeric,
               JSDurationFormat::FieldStyle::k2Digit},
              JSDurationFormat::FieldStyle::kUndefined),
          Nothing<DurationUnitOptions>());
      digital_base = JSDurationFormat::FieldStyle::kNumeric;
      break;
  }

  // 2. Let displayDefault be "always".
  JSDurationFormat::Display display_default =
      JSDurationFormat::Display::kAlways;
  // 3. If style is undefined, then
  if (style == JSDurationFormat::FieldStyle::kUndefined) {
    // a. If baseStyle is "digital", then
    if (base_style == JSDurationFormat::Style::kDigital) {
      // i. If unit is not one of "hours", "minutes", or "seconds", then
      if (styles_list != StylesList::k5Styles) {
        DCHECK_NE(0, strcmp(unit, "hours"));
        DCHECK_NE(0, strcmp(unit, "minutes"));
        DCHECK_NE(0, strcmp(unit, "seconds"));
        // a. Set displayDefault to "auto".
        display_default = JSDurationFormat::Display::kAuto;
      }
      // ii. Set style to digitalBase.
      style = digital_base;
      // b. Else
    } else {
      // i. Set displayDefault to "auto".
      display_default = JSDurationFormat::Display::kAuto;
      // ii. if prevStyle is "numeric" or "2-digit", then
      if (prev_style == JSDurationFormat::FieldStyle::kNumeric ||
          prev_style == JSDurationFormat::FieldStyle::k2Digit) {
        // 1. Set style to "numeric".
        style = JSDurationFormat::FieldStyle::kNumeric;
        // iii. Else,
      } else {
        // 1. Set style to baseStyle.
        switch (base_style) {
          case JSDurationFormat::Style::kLong:
            style = JSDurationFormat::FieldStyle::kLong;
            break;
          case JSDurationFormat::Style::kShort:
            style = JSDurationFormat::FieldStyle::kShort;
            break;
          case JSDurationFormat::Style::kNarrow:
            style = JSDurationFormat::FieldStyle::kNarrow;
            break;
          default:
            UNREACHABLE();
        }
      }
    }
  }
  // 4. Let displayField be the string-concatenation of unit and "Display".
  // 5. Let display be ? GetOption(options, displayField, "string", « "auto",
  // "always" », displayDefault).
  JSDurationFormat::Display display;
  MAYBE_ASSIGN_RETURN_ON_EXCEPTION_VALUE(
      isolate, display,
      GetStringOption<JSDurationFormat::Display>(
          isolate, options, display_field, method_name, {"auto", "always"},
          {JSDurationFormat::Display::kAuto,
           JSDurationFormat::Display::kAlways},
          display_default),
      Nothing<DurationUnitOptions>());
  // 6. If prevStyle is "numeric" or "2-digit", then
  if (prev_style == JSDurationFormat::FieldStyle::kNumeric ||
      prev_style == JSDurationFormat::FieldStyle::k2Digit) {
    // a. If style is not "numeric" or "2-digit", then
    if (style != JSDurationFormat::FieldStyle::kNumeric &&
        style != JSDurationFormat::FieldStyle::k2Digit) {
      // i. Throw a RangeError exception.
      // b. Else if unit is "minutes" or "seconds", then
    } else if (unit_kind == UnitKind::kMinutesOrSeconds) {
      CHECK(strcmp(unit, "minutes") == 0 || strcmp(unit, "seconds") == 0);
      // i. Set style to "2-digit".
      style = JSDurationFormat::FieldStyle::k2Digit;
    }
  }
  // 7. Return the Record { [[Style]]: style, [[Display]]: display }.
  return Just(DurationUnitOptions({style, display}));
}

}  // namespace
MaybeHandle<JSDurationFormat> JSDurationFormat::New(
    Isolate* isolate, Handle<Map> map, Handle<Object> locales,
    Handle<Object> input_options) {
  Factory* factory = isolate->factory();
  const char* method_name = "Intl.DurationFormat";

  // 3. Let requestedLocales be ? CanonicalizeLocaleList(locales).
  std::vector<std::string> requested_locales;
  MAYBE_ASSIGN_RETURN_ON_EXCEPTION_VALUE(
      isolate, requested_locales,
      Intl::CanonicalizeLocaleList(isolate, locales),
      Handle<JSDurationFormat>());

  // 4. Let options be ? GetOptionsObject(options).
  Handle<JSReceiver> options;
  ASSIGN_RETURN_ON_EXCEPTION(
      isolate, options, GetOptionsObject(isolate, input_options, method_name),
      JSDurationFormat);

  // 5. Let matcher be ? GetOption(options, "localeMatcher", "string", «
  // "lookup", "best fit" », "best fit").
  Intl::MatcherOption matcher;
  MAYBE_ASSIGN_RETURN_ON_EXCEPTION_VALUE(
      isolate, matcher, Intl::GetLocaleMatcher(isolate, options, method_name),
      Handle<JSDurationFormat>());

  // 6. Let numberingSystem be ? GetOption(options, "numberingSystem", "string",
  // undefined, undefined).
  //
  // 7. If numberingSystem is not undefined, then
  //
  // a. If numberingSystem does not match the Unicode Locale Identifier type
  // nonterminal, throw a RangeError exception.
  // Note: The matching test and throw in Step 7-a is throw inside
  // Intl::GetNumberingSystem.
  std::unique_ptr<char[]> numbering_system_str = nullptr;
  bool get;
  MAYBE_ASSIGN_RETURN_ON_EXCEPTION_VALUE(
      isolate, get,
      Intl::GetNumberingSystem(isolate, options, method_name,
                               &numbering_system_str),
      Handle<JSDurationFormat>());

  // 8. Let opt be the Record { [[localeMatcher]]: matcher, [[nu]]:
  // numberingSystem }.
  // 9. Let r be ResolveLocale(%DurationFormat%.[[AvailableLocales]],
  // requestedLocales, opt, %DurationFormat%.[[RelevantExtensionKeys]],
  // %DurationFormat%.[[LocaleData]]).
  std::set<std::string> relevant_extension_keys{"nu"};
  Intl::ResolvedLocale r;
  MAYBE_ASSIGN_RETURN_ON_EXCEPTION_VALUE(
      isolate, r,
      Intl::ResolveLocale(isolate, JSDurationFormat::GetAvailableLocales(),
                          requested_locales, matcher, relevant_extension_keys),
      Handle<JSDurationFormat>());

  // 10. Let locale be r.[[locale]].
  icu::Locale r_locale = r.icu_locale;
  UErrorCode status = U_ZERO_ERROR;
  // 11. Set durationFormat.[[Locale]] to locale.
  // 12. Set durationFormat.[[NumberingSystem]] to r.[[nu]].
  if (numbering_system_str != nullptr) {
    auto nu_extension_it = r.extensions.find("nu");
    if (nu_extension_it != r.extensions.end() &&
        nu_extension_it->second != numbering_system_str.get()) {
      r_locale.setUnicodeKeywordValue("nu", nullptr, status);
      DCHECK(U_SUCCESS(status));
    }
  }
  icu::Locale icu_locale = r_locale;
  if (numbering_system_str != nullptr &&
      Intl::IsValidNumberingSystem(numbering_system_str.get())) {
    r_locale.setUnicodeKeywordValue("nu", numbering_system_str.get(), status);
    DCHECK(U_SUCCESS(status));
  }
  std::string numbering_system = Intl::GetNumberingSystem(r_locale);

  // 13. Let style be ? GetOption(options, "style", "string", « "long", "short",
  // "narrow", "digital" », "long").
  Style style;
  MAYBE_ASSIGN_RETURN_ON_EXCEPTION_VALUE(
      isolate, style,
      GetStringOption<Style>(
          isolate, options, "style", method_name,
          {"long", "short", "narrow", "digital"},
          {Style::kLong, Style::kShort, Style::kNarrow, Style::kDigital},
          Style::kShort),
      Handle<JSDurationFormat>());

  // 14. Set durationFormat.[[Style]] to style.
  // 15. Set durationFormat.[[DataLocale]] to r.[[dataLocale]].
  Handle<Managed<icu::Locale>> managed_locale =
      Managed<icu::Locale>::FromRawPtr(isolate, 0, icu_locale.clone());
  // 16. Let prevStyle be the empty String.
  FieldStyle prev_style = FieldStyle::kUndefined;
  // 17. For each row of Table 1, except the header row, in table order, do
  //   a. Let styleSlot be the Style Slot value of the current row.
  //   b. Let displaySlot be the Display Slot value of the current row.
  //   c. Let unit be the Unit value.
  //   d. Let valueList be the Values value.
  //   e. Let digitalBase be the Digital Default value.
  //   f. Let unitOptions be ? GetDurationUnitOptions(unit, options, style,
  //      valueList, digitalBase, prevStyle).
  //      of durationFormat to unitOptions.[[Style]].
  //   h. Set the value of the
  //      displaySlot slot of durationFormat to unitOptions.[[Display]].
  //   i. If unit is one of "hours", "minutes", "seconds", "milliseconds",
  //      or "microseconds", then
  //      i. Set prevStyle to unitOptions.[[Style]].
  //   g. Set the value of the styleSlot slot
  DurationUnitOptions years_option;
  DurationUnitOptions months_option;
  DurationUnitOptions weeks_option;
  DurationUnitOptions days_option;
  DurationUnitOptions hours_option;
  DurationUnitOptions minutes_option;
  DurationUnitOptions seconds_option;
  DurationUnitOptions milliseconds_option;
  DurationUnitOptions microseconds_option;
  DurationUnitOptions nanoseconds_option;

#define CALL_GET_DURATION_UNIT_OPTIONS(u, sl, uk)                           \
  MAYBE_ASSIGN_RETURN_ON_EXCEPTION_VALUE(                                   \
      isolate, u##_option,                                                  \
      GetDurationUnitOptions(isolate, #u, #u "Display", options, style, sl, \
                             prev_style, uk, method_name),                  \
      Handle<JSDurationFormat>());
  CALL_GET_DURATION_UNIT_OPTIONS(years, StylesList::k3Styles, UnitKind::kOthers)
  CALL_GET_DURATION_UNIT_OPTIONS(months, StylesList::k3Styles,
                                 UnitKind::kOthers)
  CALL_GET_DURATION_UNIT_OPTIONS(weeks, StylesList::k3Styles, UnitKind::kOthers)
  CALL_GET_DURATION_UNIT_OPTIONS(days, StylesList::k3Styles, UnitKind::kOthers)
  CALL_GET_DURATION_UNIT_OPTIONS(hours, StylesList::k5Styles, UnitKind::kOthers)
  prev_style = hours_option.style;
  CALL_GET_DURATION_UNIT_OPTIONS(minutes, StylesList::k5Styles,
                                 UnitKind::kMinutesOrSeconds)
  prev_style = minutes_option.style;
  CALL_GET_DURATION_UNIT_OPTIONS(seconds, StylesList::k5Styles,
                                 UnitKind::kMinutesOrSeconds)
  prev_style = seconds_option.style;
  CALL_GET_DURATION_UNIT_OPTIONS(milliseconds, StylesList::k4Styles,
                                 UnitKind::kOthers)
  prev_style = milliseconds_option.style;
  CALL_GET_DURATION_UNIT_OPTIONS(microseconds, StylesList::k4Styles,
                                 UnitKind::kOthers)
  prev_style = microseconds_option.style;
  CALL_GET_DURATION_UNIT_OPTIONS(nanoseconds, StylesList::k4Styles,
                                 UnitKind::kOthers)
#undef CALL_GET_DURATION_UNIT_OPTIONS
  // 18. Set durationFormat.[[FractionalDigits]] to ? GetNumberOption(options,
  // "fractionalDigits", 0, 9, undefined).
  int fractional_digits;
  MAYBE_ASSIGN_RETURN_ON_EXCEPTION_VALUE(
      isolate, fractional_digits,
      GetNumberOption(isolate, options, factory->fractionalDigits_string(), 0,
                      9, 0),
      Handle<JSDurationFormat>());

  icu::number::LocalizedNumberFormatter fmt =
      icu::number::UnlocalizedNumberFormatter()
          .roundingMode(UNUM_ROUND_HALFUP)
          .locale(icu_locale);
  if (!numbering_system.empty() && numbering_system != "latn") {
    fmt = fmt.adoptSymbols(icu::NumberingSystem::createInstanceByName(
        numbering_system.c_str(), status));
    DCHECK(U_SUCCESS(status));
  }
  Handle<Managed<icu::number::LocalizedNumberFormatter>>
      managed_number_formatter =
          Managed<icu::number::LocalizedNumberFormatter>::FromRawPtr(
              isolate, 0, new icu::number::LocalizedNumberFormatter(fmt));

  // 19. Return durationFormat.
  Handle<JSDurationFormat> duration_format = Handle<JSDurationFormat>::cast(
      factory->NewFastOrSlowJSObjectFromMap(map));
  duration_format->set_style_flags(0);
  duration_format->set_display_flags(0);
  duration_format->set_style(style);
  duration_format->set_years_style(years_option.style);
  duration_format->set_months_style(months_option.style);
  duration_format->set_weeks_style(weeks_option.style);
  duration_format->set_days_style(days_option.style);
  duration_format->set_hours_style(hours_option.style);
  duration_format->set_minutes_style(minutes_option.style);
  duration_format->set_seconds_style(seconds_option.style);
  duration_format->set_milliseconds_style(milliseconds_option.style);
  duration_format->set_microseconds_style(microseconds_option.style);
  duration_format->set_nanoseconds_style(nanoseconds_option.style);

  duration_format->set_years_display(years_option.display);
  duration_format->set_months_display(months_option.display);
  duration_format->set_weeks_display(weeks_option.display);
  duration_format->set_days_display(days_option.display);
  duration_format->set_hours_display(hours_option.display);
  duration_format->set_minutes_display(minutes_option.display);
  duration_format->set_seconds_display(seconds_option.display);
  duration_format->set_milliseconds_display(milliseconds_option.display);
  duration_format->set_microseconds_display(microseconds_option.display);
  duration_format->set_nanoseconds_display(nanoseconds_option.display);

  duration_format->set_fractional_digits(fractional_digits);

  duration_format->set_icu_locale(*managed_locale);
  duration_format->set_icu_number_formatter(*managed_number_formatter);

  return duration_format;
}

namespace {

Handle<String> StyleToString(Isolate* isolate, JSDurationFormat::Style style) {
  switch (style) {
    case JSDurationFormat::Style::kLong:
      return ReadOnlyRoots(isolate).long_string_handle();
    case JSDurationFormat::Style::kShort:
      return ReadOnlyRoots(isolate).short_string_handle();
    case JSDurationFormat::Style::kNarrow:
      return ReadOnlyRoots(isolate).narrow_string_handle();
    case JSDurationFormat::Style::kDigital:
      return ReadOnlyRoots(isolate).digital_string_handle();
  }
}

Handle<String> StyleToString(Isolate* isolate,
                             JSDurationFormat::FieldStyle style) {
  switch (style) {
    case JSDurationFormat::FieldStyle::kLong:
      return ReadOnlyRoots(isolate).long_string_handle();
    case JSDurationFormat::FieldStyle::kShort:
      return ReadOnlyRoots(isolate).short_string_handle();
    case JSDurationFormat::FieldStyle::kNarrow:
      return ReadOnlyRoots(isolate).narrow_string_handle();
    case JSDurationFormat::FieldStyle::kNumeric:
      return ReadOnlyRoots(isolate).numeric_string_handle();
    case JSDurationFormat::FieldStyle::k2Digit:
      return ReadOnlyRoots(isolate).two_digit_string_handle();
    case JSDurationFormat::FieldStyle::kUndefined:
      UNREACHABLE();
  }
}

Handle<String> DisplayToString(Isolate* isolate,
                               JSDurationFormat::Display display) {
  switch (display) {
    case JSDurationFormat::Display::kAuto:
      return ReadOnlyRoots(isolate).auto_string_handle();
    case JSDurationFormat::Display::kAlways:
      return ReadOnlyRoots(isolate).always_string_handle();
  }
}

}  // namespace

Handle<JSObject> JSDurationFormat::ResolvedOptions(
    Isolate* isolate, Handle<JSDurationFormat> format) {
  Factory* factory = isolate->factory();
  Handle<JSObject> options = factory->NewJSObject(isolate->object_function());

  Handle<String> locale = factory->NewStringFromAsciiChecked(
      Intl::ToLanguageTag(*format->icu_locale()->raw()).FromJust().c_str());
  UErrorCode status = U_ZERO_ERROR;
  icu::UnicodeString skeleton =
      format->icu_number_formatter()->raw()->toSkeleton(status);
  DCHECK(U_SUCCESS(status));

  Handle<String> numbering_system;
  CHECK(Intl::ToString(isolate,
                       JSNumberFormat::NumberingSystemFromSkeleton(skeleton))
            .ToHandle(&numbering_system));

  Handle<Smi> fractional_digits =
      handle(Smi::FromInt(format->fractional_digits()), isolate);

  bool created;

#define OUTPUT_PROPERTY(s, f)                                           \
  MAYBE_ASSIGN_RETURN_ON_EXCEPTION_VALUE(                               \
      isolate, created,                                                 \
      JSReceiver::CreateDataProperty(isolate, options, factory->s(), f, \
                                     Just(kDontThrow)),                 \
      Handle<JSObject>());                                              \
  CHECK(created);
#define OUTPUT_STYLE_PROPERTY(p) \
  OUTPUT_PROPERTY(p##_string, StyleToString(isolate, format->p##_style()))
#define OUTPUT_DISPLAY_PROPERTY(p)   \
  OUTPUT_PROPERTY(p##Display_string, \
                  DisplayToString(isolate, format->p##_display()))
#define OUTPUT_STYLE_AND_DISPLAY_PROPERTIES(p) \
  OUTPUT_STYLE_PROPERTY(p);                    \
  OUTPUT_DISPLAY_PROPERTY(p);

  OUTPUT_PROPERTY(locale_string, locale);
  OUTPUT_PROPERTY(style_string, StyleToString(isolate, format->style()));

  OUTPUT_STYLE_AND_DISPLAY_PROPERTIES(years);
  OUTPUT_STYLE_AND_DISPLAY_PROPERTIES(months);
  OUTPUT_STYLE_AND_DISPLAY_PROPERTIES(weeks);
  OUTPUT_STYLE_AND_DISPLAY_PROPERTIES(days);
  OUTPUT_STYLE_AND_DISPLAY_PROPERTIES(hours);
  OUTPUT_STYLE_AND_DISPLAY_PROPERTIES(minutes);
  OUTPUT_STYLE_AND_DISPLAY_PROPERTIES(seconds);
  OUTPUT_STYLE_AND_DISPLAY_PROPERTIES(milliseconds);
  OUTPUT_STYLE_AND_DISPLAY_PROPERTIES(microseconds);
  OUTPUT_STYLE_AND_DISPLAY_PROPERTIES(nanoseconds);

  OUTPUT_PROPERTY(fractionalDigits_string, fractional_digits);
  OUTPUT_PROPERTY(numberingSystem_string, numbering_system);
#undef OUTPUT_PROPERTY
#undef OUTPUT_STYLE_PROPERTY
#undef OUTPUT_DISPLAY_PROPERTY
#undef OUTPUT_STYLE_AND_DISPLAY_PROPERTIES

  return options;
}

namespace {

UNumberUnitWidth ToUNumberUnitWidth(JSDurationFormat::FieldStyle style) {
  switch (style) {
    case JSDurationFormat::FieldStyle::kShort:
      return UNumberUnitWidth::UNUM_UNIT_WIDTH_SHORT;
    case JSDurationFormat::FieldStyle::kLong:
      return UNumberUnitWidth::UNUM_UNIT_WIDTH_FULL_NAME;
    case JSDurationFormat::FieldStyle::kNarrow:
      return UNumberUnitWidth::UNUM_UNIT_WIDTH_NARROW;
    default:
      UNREACHABLE();
  }
}

void Output(std::vector<icu::UnicodeString>* out, double value,
            const icu::number::LocalizedNumberFormatter& fmt) {
  UErrorCode status = U_ZERO_ERROR;
  out->push_back(fmt.formatDouble(value, status).toString(status));
  CHECK(U_SUCCESS(status));
}

void Output3Styles(std::vector<icu::UnicodeString>* out,
                   std::vector<std::string>* types, const char* type,
                   double value, JSDurationFormat::Display display,
                   const icu::number::LocalizedNumberFormatter& fmt) {
  if (value == 0 && display == JSDurationFormat::Display::kAuto) return;
  types->push_back(type);
  Output(out, value, fmt);
}

void Output4Styles(std::vector<icu::UnicodeString>* out,
                   std::vector<std::string>* types, const char* type,
                   double value, JSDurationFormat::Display display,
                   JSDurationFormat::FieldStyle style,
                   const icu::number::LocalizedNumberFormatter& fmt,
                   icu::MeasureUnit unit) {
  if (value == 0 && display == JSDurationFormat::Display::kAuto) return;
  if (style == JSDurationFormat::FieldStyle::kNumeric) {
    types->push_back(type);
    return Output(out, value, fmt);
  }
  Output3Styles(out, types, type, value, display,
                fmt.unit(unit).unitWidth(ToUNumberUnitWidth(style)));
}
void Output5Styles(std::vector<icu::UnicodeString>* out,
                   std::vector<std::string>* types, const char* type,
                   double value, JSDurationFormat::Display display,
                   JSDurationFormat::FieldStyle style,
                   const icu::number::LocalizedNumberFormatter& fmt,
                   icu::MeasureUnit unit) {
  if (value == 0 && display == JSDurationFormat::Display::kAuto) return;
  if (style == JSDurationFormat::FieldStyle::k2Digit) {
    types->push_back(type);
    return Output(out, value,
                  fmt.integerWidth(icu::number::IntegerWidth::zeroFillTo(2)));
  }
  Output4Styles(out, types, type, value, display, style, fmt, unit);
}

void DurationRecordToListOfStrings(
    std::vector<icu::UnicodeString>* out, std::vector<std::string>* types,
    Handle<JSDurationFormat> df,
    const icu::number::LocalizedNumberFormatter& fmt,
    const DurationRecord& record) {
  // The handling of "2-digit" or "numeric" style of
  // step l.i.6.c.i-ii "Let separator be
  // dataLocaleData.[[digitalFormat]].[[separator]]." and
  // "Append the new Record { [[Type]]: "literal", [[Value]]: separator} to the
  // end of result." are not implemented following the spec due to unresolved
  // issues in
  // https://github.com/tc39/proposal-intl-duration-format/issues/55
  Output3Styles(out, types, "years", record.years, df->years_display(),
                fmt.unit(icu::MeasureUnit::getYear())
                    .unitWidth(ToUNumberUnitWidth(df->years_style())));
  Output3Styles(out, types, "months", record.months, df->months_display(),
                fmt.unit(icu::MeasureUnit::getMonth())
                    .unitWidth(ToUNumberUnitWidth(df->months_style())));
  Output3Styles(out, types, "weeks", record.weeks, df->weeks_display(),
                fmt.unit(icu::MeasureUnit::getWeek())
                    .unitWidth(ToUNumberUnitWidth(df->weeks_style())));
  Output3Styles(out, types, "days", record.time_duration.days,
                df->days_display(),
                fmt.unit(icu::MeasureUnit::getDay())
                    .unitWidth(ToUNumberUnitWidth(df->days_style())));
  Output5Styles(out, types, "hours", record.time_duration.hours,
                df->hours_display(), df->hours_style(), fmt,
                icu::MeasureUnit::getHour());
  Output5Styles(out, types, "minutes", record.time_duration.minutes,
                df->minutes_display(), df->minutes_style(), fmt,
                icu::MeasureUnit::getMinute());
  int32_t fractional_digits = df->fractional_digits();
  if (df->milliseconds_style() == JSDurationFormat::FieldStyle::kNumeric) {
    // a. Set value to value + duration.[[Milliseconds]] / 10^3 +
    // duration.[[Microseconds]] / 10^6 + duration.[[Nanoseconds]] / 10^9.
    double value = record.time_duration.seconds +
                   record.time_duration.milliseconds / 1e3 +
                   record.time_duration.microseconds / 1e6 +
                   record.time_duration.nanoseconds / 1e9;
    Output5Styles(out, types, "seconds", value, df->seconds_display(),
                  df->seconds_style(),
                  fmt.precision(icu::number::Precision::minMaxFraction(
                      fractional_digits, fractional_digits)),
                  icu::MeasureUnit::getSecond());
    return;
  }
  Output5Styles(out, types, "seconds", record.time_duration.seconds,
                df->seconds_display(), df->seconds_style(), fmt,
                icu::MeasureUnit::getSecond());

  if (df->microseconds_style() == JSDurationFormat::FieldStyle::kNumeric) {
    // a. Set value to value + duration.[[Microseconds]] / 10^3 +
    // duration.[[Nanoseconds]] / 10^6.
    double value = record.time_duration.milliseconds +
                   record.time_duration.microseconds / 1e3 +
                   record.time_duration.nanoseconds / 1e6;
    Output4Styles(out, types, "milliseconds", value, df->milliseconds_display(),
                  df->milliseconds_style(),
                  fmt.precision(icu::number::Precision::minMaxFraction(
                      fractional_digits, fractional_digits)),
                  icu::MeasureUnit::getMillisecond());
    return;
  }
  Output4Styles(out, types, "milliseconds", record.time_duration.milliseconds,
                df->milliseconds_display(), df->milliseconds_style(), fmt,
                icu::MeasureUnit::getMillisecond());

  if (df->nanoseconds_style() == JSDurationFormat::FieldStyle::kNumeric) {
    // a. Set value to value + duration.[[Nanoseconds]] / 10^3.
    double value = record.time_duration.microseconds +
                   record.time_duration.nanoseconds / 1e3;
    Output4Styles(out, types, "microseconds", value, df->microseconds_display(),
                  df->microseconds_style(),
                  fmt.precision(icu::number::Precision::minMaxFraction(
                      fractional_digits, fractional_digits)),
                  icu::MeasureUnit::getMicrosecond());
    return;
  }
  Output4Styles(out, types, "microseconds", record.time_duration.microseconds,
                df->microseconds_display(), df->microseconds_style(), fmt,
                icu::MeasureUnit::getMicrosecond());

  Output4Styles(out, types, "nanoseconds", record.time_duration.nanoseconds,
                df->nanoseconds_display(), df->nanoseconds_style(), fmt,
                icu::MeasureUnit::getNanosecond());
}

UListFormatterWidth StyleToWidth(JSDurationFormat::Style style) {
  switch (style) {
    case JSDurationFormat::Style::kLong:
      return ULISTFMT_WIDTH_WIDE;
    case JSDurationFormat::Style::kShort:
      return ULISTFMT_WIDTH_SHORT;
    case JSDurationFormat::Style::kNarrow:
    case JSDurationFormat::Style::kDigital:
      return ULISTFMT_WIDTH_NARROW;
  }
  UNREACHABLE();
}

template <typename T,
          MaybeHandle<T> (*Format)(Isolate*, const icu::FormattedValue&,
                                   const std::vector<std::string>&)>
MaybeHandle<T> PartitionDurationFormatPattern(Isolate* isolate,
                                              Handle<JSDurationFormat> df,
                                              const DurationRecord& record,
                                              const char* method_name) {
  // 4. Let lfOpts be ! OrdinaryObjectCreate(null).
  // 5. Perform ! CreateDataPropertyOrThrow(lfOpts, "type", "unit").
  UListFormatterType type = ULISTFMT_TYPE_UNITS;
  // 6. Let listStyle be durationFormat.[[Style]].
  // 7. If listStyle is "digital", then
  // a. Set listStyle to "narrow".
  // 8. Perform ! CreateDataPropertyOrThrow(lfOpts, "style", listStyle).
  UListFormatterWidth list_style = StyleToWidth(df->style());
  // 9. Let lf be ! Construct(%ListFormat%, « durationFormat.[[Locale]], lfOpts
  // »).
  UErrorCode status = U_ZERO_ERROR;
  icu::Locale icu_locale = *df->icu_locale()->raw();
  std::unique_ptr<icu::ListFormatter> formatter(
      icu::ListFormatter::createInstance(icu_locale, type, list_style, status));
  CHECK(U_SUCCESS(status));

  std::vector<icu::UnicodeString> list;
  std::vector<std::string> types;

  DurationRecordToListOfStrings(&list, &types, df,
                                *(df->icu_number_formatter()->raw()), record);

  icu::FormattedList formatted = formatter->formatStringsToValue(
      list.data(), static_cast<int32_t>(list.size()), status);
  CHECK(U_SUCCESS(status));
  return Format(isolate, formatted, types);
}

// #sec-todurationrecord
// ToDurationRecord is almost the same as temporal::ToPartialDuration
// except:
// 1) In the beginning it will throw RangeError if the type of input is String,
// 2) In the end it will throw RangeError if IsValidDurationRecord return false.
Maybe<DurationRecord> ToDurationRecord(Isolate* isolate, Handle<Object> input,
                                       const DurationRecord& default_value) {
  // 1-a. If Type(input) is String, throw a RangeError exception.
  if (input->IsString()) {
    THROW_NEW_ERROR_RETURN_VALUE(
        isolate,
        NewRangeError(MessageTemplate::kInvalid,
                      isolate->factory()->object_string(), input),
        Nothing<DurationRecord>());
  }
  // Step 1-b - 23. Same as ToTemporalPartialDurationRecord.
  DurationRecord record;
  MAYBE_ASSIGN_RETURN_ON_EXCEPTION_VALUE(
      isolate, record,
      temporal::ToPartialDuration(isolate, input, default_value),
      Nothing<DurationRecord>());
  // 24. If IsValidDurationRecord(result) is false, throw a RangeError
  // exception.
  if (!temporal::IsValidDuration(isolate, record)) {
    THROW_NEW_ERROR_RETURN_VALUE(
        isolate,
        NewRangeError(MessageTemplate::kInvalid,
                      isolate->factory()->object_string(), input),
        Nothing<DurationRecord>());
  }
  return Just(record);
}

template <typename T,
          MaybeHandle<T> (*Format)(Isolate*, const icu::FormattedValue&,
                                   const std::vector<std::string>&)>
MaybeHandle<T> FormatCommon(Isolate* isolate, Handle<JSDurationFormat> df,
                            Handle<Object> duration, const char* method_name) {
  // 1. Let df be this value.
  // 2. Perform ? RequireInternalSlot(df, [[InitializedDurationFormat]]).
  // 3. Let record be ? ToDurationRecord(duration).
  DurationRecord record;
  MAYBE_ASSIGN_RETURN_ON_EXCEPTION_VALUE(
      isolate, record,
      ToDurationRecord(isolate, duration, {0, 0, 0, {0, 0, 0, 0, 0, 0, 0}}),
      Handle<T>());
  // 5. Let parts be ! PartitionDurationFormatPattern(df, record).
  return PartitionDurationFormatPattern<T, Format>(isolate, df, record,
                                                   method_name);
}

}  // namespace

MaybeHandle<String> FormattedToString(Isolate* isolate,
                                      const icu::FormattedValue& formatted,
                                      const std::vector<std::string>&) {
  return Intl::FormattedToString(isolate, formatted);
}

MaybeHandle<JSArray> FormattedListToJSArray(
    Isolate* isolate, const icu::FormattedValue& formatted,
    const std::vector<std::string>& types) {
  Factory* factory = isolate->factory();
  Handle<JSArray> array = factory->NewJSArray(0);
  icu::ConstrainedFieldPosition cfpos;
  cfpos.constrainCategory(UFIELD_CATEGORY_LIST);
  int index = 0;
  int type_index = 0;
  UErrorCode status = U_ZERO_ERROR;
  icu::UnicodeString string = formatted.toString(status);
  Handle<String> substring;
  while (formatted.nextPosition(cfpos, status) && U_SUCCESS(status)) {
    ASSIGN_RETURN_ON_EXCEPTION(
        isolate, substring,
        Intl::ToString(isolate, string, cfpos.getStart(), cfpos.getLimit()),
        JSArray);
    Handle<String> type_string = factory->literal_string();
    if (cfpos.getField() == ULISTFMT_ELEMENT_FIELD) {
      type_string =
          factory->NewStringFromAsciiChecked(types[type_index].c_str());
      type_index++;
    }
    Intl::AddElement(isolate, array, index++, type_string, substring);
  }
  if (U_FAILURE(status)) {
    THROW_NEW_ERROR(isolate, NewTypeError(MessageTemplate::kIcuError), JSArray);
  }
  JSObject::ValidateElements(*array);
  return array;
}

MaybeHandle<String> JSDurationFormat::Format(Isolate* isolate,
                                             Handle<JSDurationFormat> df,
                                             Handle<Object> duration) {
  const char* method_name = "Intl.DurationFormat.prototype.format";
  return FormatCommon<String, FormattedToString>(isolate, df, duration,
                                                 method_name);
}

MaybeHandle<JSArray> JSDurationFormat::FormatToParts(
    Isolate* isolate, Handle<JSDurationFormat> df, Handle<Object> duration) {
  const char* method_name = "Intl.DurationFormat.prototype.formatToParts";
  return FormatCommon<JSArray, FormattedListToJSArray>(isolate, df, duration,
                                                       method_name);
}

const std::set<std::string>& JSDurationFormat::GetAvailableLocales() {
  return JSNumberFormat::GetAvailableLocales();
}

}  // namespace internal
}  // namespace v8
