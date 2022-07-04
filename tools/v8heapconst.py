#!/usr/bin/env python3
# Copyright 2019 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can
# be found in the LICENSE file.

# This file is automatically generated by mkgrokdump and should not
# be modified manually.

# List of known V8 instance types.
# yapf: disable

INSTANCE_TYPES = {
  0: "INTERNALIZED_STRING_TYPE",
  2: "EXTERNAL_INTERNALIZED_STRING_TYPE",
  8: "ONE_BYTE_INTERNALIZED_STRING_TYPE",
  10: "EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  18: "UNCACHED_EXTERNAL_INTERNALIZED_STRING_TYPE",
  26: "UNCACHED_EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  32: "STRING_TYPE",
  33: "CONS_STRING_TYPE",
  34: "EXTERNAL_STRING_TYPE",
  35: "SLICED_STRING_TYPE",
  37: "THIN_STRING_TYPE",
  40: "ONE_BYTE_STRING_TYPE",
  41: "CONS_ONE_BYTE_STRING_TYPE",
  42: "EXTERNAL_ONE_BYTE_STRING_TYPE",
  43: "SLICED_ONE_BYTE_STRING_TYPE",
  45: "THIN_ONE_BYTE_STRING_TYPE",
  50: "UNCACHED_EXTERNAL_STRING_TYPE",
  58: "UNCACHED_EXTERNAL_ONE_BYTE_STRING_TYPE",
  96: "SHARED_STRING_TYPE",
  101: "SHARED_THIN_STRING_TYPE",
  104: "SHARED_ONE_BYTE_STRING_TYPE",
  109: "SHARED_THIN_ONE_BYTE_STRING_TYPE",
  128: "SYMBOL_TYPE",
  129: "BIG_INT_BASE_TYPE",
  130: "HEAP_NUMBER_TYPE",
  131: "ODDBALL_TYPE",
  132: "PROMISE_FULFILL_REACTION_JOB_TASK_TYPE",
  133: "PROMISE_REJECT_REACTION_JOB_TASK_TYPE",
  134: "CALLABLE_TASK_TYPE",
  135: "CALLBACK_TASK_TYPE",
  136: "PROMISE_RESOLVE_THENABLE_JOB_TASK_TYPE",
  137: "LOAD_HANDLER_TYPE",
  138: "STORE_HANDLER_TYPE",
  139: "FUNCTION_TEMPLATE_INFO_TYPE",
  140: "OBJECT_TEMPLATE_INFO_TYPE",
  141: "ACCESS_CHECK_INFO_TYPE",
  142: "ACCESSOR_PAIR_TYPE",
  143: "ALIASED_ARGUMENTS_ENTRY_TYPE",
  144: "ALLOCATION_MEMENTO_TYPE",
  145: "ALLOCATION_SITE_TYPE",
  146: "ARRAY_BOILERPLATE_DESCRIPTION_TYPE",
  147: "ASM_WASM_DATA_TYPE",
  148: "ASYNC_GENERATOR_REQUEST_TYPE",
  149: "BREAK_POINT_TYPE",
  150: "BREAK_POINT_INFO_TYPE",
  151: "CACHED_TEMPLATE_OBJECT_TYPE",
  152: "CALL_SITE_INFO_TYPE",
  153: "CLASS_POSITIONS_TYPE",
  154: "DEBUG_INFO_TYPE",
  155: "ENUM_CACHE_TYPE",
  156: "ERROR_STACK_DATA_TYPE",
  157: "FEEDBACK_CELL_TYPE",
  158: "FUNCTION_TEMPLATE_RARE_DATA_TYPE",
  159: "INTERCEPTOR_INFO_TYPE",
  160: "INTERPRETER_DATA_TYPE",
  161: "MODULE_REQUEST_TYPE",
  162: "PROMISE_CAPABILITY_TYPE",
  163: "PROMISE_ON_STACK_TYPE",
  164: "PROMISE_REACTION_TYPE",
  165: "PROPERTY_DESCRIPTOR_OBJECT_TYPE",
  166: "PROTOTYPE_INFO_TYPE",
  167: "REG_EXP_BOILERPLATE_DESCRIPTION_TYPE",
  168: "SCRIPT_TYPE",
  169: "SCRIPT_OR_MODULE_TYPE",
  170: "SOURCE_TEXT_MODULE_INFO_ENTRY_TYPE",
  171: "STACK_FRAME_INFO_TYPE",
  172: "TEMPLATE_OBJECT_DESCRIPTION_TYPE",
  173: "TUPLE2_TYPE",
  174: "WASM_CONTINUATION_OBJECT_TYPE",
  175: "WASM_EXCEPTION_TAG_TYPE",
  176: "WASM_INDIRECT_FUNCTION_TABLE_TYPE",
  177: "FIXED_ARRAY_TYPE",
  178: "HASH_TABLE_TYPE",
  179: "EPHEMERON_HASH_TABLE_TYPE",
  180: "GLOBAL_DICTIONARY_TYPE",
  181: "NAME_DICTIONARY_TYPE",
  182: "NAME_TO_INDEX_HASH_TABLE_TYPE",
  183: "NUMBER_DICTIONARY_TYPE",
  184: "ORDERED_HASH_MAP_TYPE",
  185: "ORDERED_HASH_SET_TYPE",
  186: "ORDERED_NAME_DICTIONARY_TYPE",
  187: "REGISTERED_SYMBOL_TABLE_TYPE",
  188: "SIMPLE_NUMBER_DICTIONARY_TYPE",
  189: "CLOSURE_FEEDBACK_CELL_ARRAY_TYPE",
  190: "OBJECT_BOILERPLATE_DESCRIPTION_TYPE",
  191: "SCRIPT_CONTEXT_TABLE_TYPE",
  192: "BYTE_ARRAY_TYPE",
  193: "BYTECODE_ARRAY_TYPE",
  194: "FIXED_DOUBLE_ARRAY_TYPE",
  195: "INTERNAL_CLASS_WITH_SMI_ELEMENTS_TYPE",
  196: "SLOPPY_ARGUMENTS_ELEMENTS_TYPE",
  197: "TURBOFAN_BITSET_TYPE_TYPE",
  198: "TURBOFAN_HEAP_CONSTANT_TYPE_TYPE",
  199: "TURBOFAN_OTHER_NUMBER_CONSTANT_TYPE_TYPE",
  200: "TURBOFAN_RANGE_TYPE_TYPE",
  201: "TURBOFAN_UNION_TYPE_TYPE",
  202: "ABSTRACT_INTERNAL_CLASS_SUBCLASS1_TYPE",
  203: "ABSTRACT_INTERNAL_CLASS_SUBCLASS2_TYPE",
  204: "FOREIGN_TYPE",
  205: "WASM_INTERNAL_FUNCTION_TYPE",
  206: "WASM_TYPE_INFO_TYPE",
  207: "AWAIT_CONTEXT_TYPE",
  208: "BLOCK_CONTEXT_TYPE",
  209: "CATCH_CONTEXT_TYPE",
  210: "DEBUG_EVALUATE_CONTEXT_TYPE",
  211: "EVAL_CONTEXT_TYPE",
  212: "FUNCTION_CONTEXT_TYPE",
  213: "MODULE_CONTEXT_TYPE",
  214: "NATIVE_CONTEXT_TYPE",
  215: "SCRIPT_CONTEXT_TYPE",
  216: "WITH_CONTEXT_TYPE",
  217: "UNCOMPILED_DATA_WITH_PREPARSE_DATA_TYPE",
  218: "UNCOMPILED_DATA_WITH_PREPARSE_DATA_AND_JOB_TYPE",
  219: "UNCOMPILED_DATA_WITHOUT_PREPARSE_DATA_TYPE",
  220: "UNCOMPILED_DATA_WITHOUT_PREPARSE_DATA_WITH_JOB_TYPE",
  221: "WASM_FUNCTION_DATA_TYPE",
  222: "WASM_CAPI_FUNCTION_DATA_TYPE",
  223: "WASM_EXPORTED_FUNCTION_DATA_TYPE",
  224: "WASM_JS_FUNCTION_DATA_TYPE",
  225: "EXPORTED_SUB_CLASS_BASE_TYPE",
  226: "EXPORTED_SUB_CLASS_TYPE",
  227: "EXPORTED_SUB_CLASS2_TYPE",
  228: "SMALL_ORDERED_HASH_MAP_TYPE",
  229: "SMALL_ORDERED_HASH_SET_TYPE",
  230: "SMALL_ORDERED_NAME_DICTIONARY_TYPE",
  231: "DESCRIPTOR_ARRAY_TYPE",
  232: "STRONG_DESCRIPTOR_ARRAY_TYPE",
  233: "SOURCE_TEXT_MODULE_TYPE",
  234: "SYNTHETIC_MODULE_TYPE",
  235: "WEAK_FIXED_ARRAY_TYPE",
  236: "TRANSITION_ARRAY_TYPE",
  237: "ACCESSOR_INFO_TYPE",
  238: "CALL_HANDLER_INFO_TYPE",
  239: "CELL_TYPE",
  240: "CODE_TYPE",
  241: "CODE_DATA_CONTAINER_TYPE",
  242: "COVERAGE_INFO_TYPE",
  243: "EMBEDDER_DATA_ARRAY_TYPE",
  244: "FEEDBACK_METADATA_TYPE",
  245: "FEEDBACK_VECTOR_TYPE",
  246: "FILLER_TYPE",
  247: "FREE_SPACE_TYPE",
  248: "INTERNAL_CLASS_TYPE",
  249: "INTERNAL_CLASS_WITH_STRUCT_ELEMENTS_TYPE",
  250: "MAP_TYPE",
  251: "MEGA_DOM_HANDLER_TYPE",
  252: "ON_HEAP_BASIC_BLOCK_PROFILER_DATA_TYPE",
  253: "PREPARSE_DATA_TYPE",
  254: "PROPERTY_ARRAY_TYPE",
  255: "PROPERTY_CELL_TYPE",
  256: "SCOPE_INFO_TYPE",
  257: "SHARED_FUNCTION_INFO_TYPE",
  258: "SMI_BOX_TYPE",
  259: "SMI_PAIR_TYPE",
  260: "SORT_STATE_TYPE",
  261: "SWISS_NAME_DICTIONARY_TYPE",
  262: "WASM_API_FUNCTION_REF_TYPE",
  263: "WASM_RESUME_DATA_TYPE",
  264: "WEAK_ARRAY_LIST_TYPE",
  265: "WEAK_CELL_TYPE",
  266: "WASM_ARRAY_TYPE",
  267: "WASM_STRUCT_TYPE",
  268: "JS_PROXY_TYPE",
  1057: "JS_OBJECT_TYPE",
  269: "JS_GLOBAL_OBJECT_TYPE",
  270: "JS_GLOBAL_PROXY_TYPE",
  271: "JS_MODULE_NAMESPACE_TYPE",
  1040: "JS_SPECIAL_API_OBJECT_TYPE",
  1041: "JS_PRIMITIVE_WRAPPER_TYPE",
  1058: "JS_API_OBJECT_TYPE",
  2058: "JS_LAST_DUMMY_API_OBJECT_TYPE",
  2059: "JS_DATA_VIEW_TYPE",
  2060: "JS_TYPED_ARRAY_TYPE",
  2061: "JS_ARRAY_BUFFER_TYPE",
  2062: "JS_PROMISE_TYPE",
  2063: "JS_BOUND_FUNCTION_TYPE",
  2064: "JS_WRAPPED_FUNCTION_TYPE",
  2065: "JS_FUNCTION_TYPE",
  2066: "BIGINT64_TYPED_ARRAY_CONSTRUCTOR_TYPE",
  2067: "BIGUINT64_TYPED_ARRAY_CONSTRUCTOR_TYPE",
  2068: "FLOAT32_TYPED_ARRAY_CONSTRUCTOR_TYPE",
  2069: "FLOAT64_TYPED_ARRAY_CONSTRUCTOR_TYPE",
  2070: "INT16_TYPED_ARRAY_CONSTRUCTOR_TYPE",
  2071: "INT32_TYPED_ARRAY_CONSTRUCTOR_TYPE",
  2072: "INT8_TYPED_ARRAY_CONSTRUCTOR_TYPE",
  2073: "UINT16_TYPED_ARRAY_CONSTRUCTOR_TYPE",
  2074: "UINT32_TYPED_ARRAY_CONSTRUCTOR_TYPE",
  2075: "UINT8_CLAMPED_TYPED_ARRAY_CONSTRUCTOR_TYPE",
  2076: "UINT8_TYPED_ARRAY_CONSTRUCTOR_TYPE",
  2077: "JS_ARRAY_CONSTRUCTOR_TYPE",
  2078: "JS_PROMISE_CONSTRUCTOR_TYPE",
  2079: "JS_REG_EXP_CONSTRUCTOR_TYPE",
  2080: "JS_CLASS_CONSTRUCTOR_TYPE",
  2081: "JS_ARRAY_ITERATOR_PROTOTYPE_TYPE",
  2082: "JS_ITERATOR_PROTOTYPE_TYPE",
  2083: "JS_MAP_ITERATOR_PROTOTYPE_TYPE",
  2084: "JS_OBJECT_PROTOTYPE_TYPE",
  2085: "JS_PROMISE_PROTOTYPE_TYPE",
  2086: "JS_REG_EXP_PROTOTYPE_TYPE",
  2087: "JS_SET_ITERATOR_PROTOTYPE_TYPE",
  2088: "JS_SET_PROTOTYPE_TYPE",
  2089: "JS_STRING_ITERATOR_PROTOTYPE_TYPE",
  2090: "JS_TYPED_ARRAY_PROTOTYPE_TYPE",
  2091: "JS_MAP_KEY_ITERATOR_TYPE",
  2092: "JS_MAP_KEY_VALUE_ITERATOR_TYPE",
  2093: "JS_MAP_VALUE_ITERATOR_TYPE",
  2094: "JS_SET_KEY_VALUE_ITERATOR_TYPE",
  2095: "JS_SET_VALUE_ITERATOR_TYPE",
  2096: "JS_GENERATOR_OBJECT_TYPE",
  2097: "JS_ASYNC_FUNCTION_OBJECT_TYPE",
  2098: "JS_ASYNC_GENERATOR_OBJECT_TYPE",
  2099: "JS_MAP_TYPE",
  2100: "JS_SET_TYPE",
  2101: "JS_WEAK_MAP_TYPE",
  2102: "JS_WEAK_SET_TYPE",
  2103: "JS_ARGUMENTS_OBJECT_TYPE",
  2104: "JS_ARRAY_TYPE",
  2105: "JS_ARRAY_ITERATOR_TYPE",
  2106: "JS_ASYNC_FROM_SYNC_ITERATOR_TYPE",
  2107: "JS_ATOMICS_MUTEX_TYPE",
  2108: "JS_COLLATOR_TYPE",
  2109: "JS_CONTEXT_EXTENSION_OBJECT_TYPE",
  2110: "JS_DATE_TYPE",
  2111: "JS_DATE_TIME_FORMAT_TYPE",
  2112: "JS_DISPLAY_NAMES_TYPE",
  2113: "JS_ERROR_TYPE",
  2114: "JS_EXTERNAL_OBJECT_TYPE",
  2115: "JS_FINALIZATION_REGISTRY_TYPE",
  2116: "JS_LIST_FORMAT_TYPE",
  2117: "JS_LOCALE_TYPE",
  2118: "JS_MESSAGE_OBJECT_TYPE",
  2119: "JS_NUMBER_FORMAT_TYPE",
  2120: "JS_PLURAL_RULES_TYPE",
  2121: "JS_REG_EXP_TYPE",
  2122: "JS_REG_EXP_STRING_ITERATOR_TYPE",
  2123: "JS_RELATIVE_TIME_FORMAT_TYPE",
  2124: "JS_SEGMENT_ITERATOR_TYPE",
  2125: "JS_SEGMENTER_TYPE",
  2126: "JS_SEGMENTS_TYPE",
  2127: "JS_SHADOW_REALM_TYPE",
  2128: "JS_SHARED_ARRAY_TYPE",
  2129: "JS_SHARED_STRUCT_TYPE",
  2130: "JS_STRING_ITERATOR_TYPE",
  2131: "JS_TEMPORAL_CALENDAR_TYPE",
  2132: "JS_TEMPORAL_DURATION_TYPE",
  2133: "JS_TEMPORAL_INSTANT_TYPE",
  2134: "JS_TEMPORAL_PLAIN_DATE_TYPE",
  2135: "JS_TEMPORAL_PLAIN_DATE_TIME_TYPE",
  2136: "JS_TEMPORAL_PLAIN_MONTH_DAY_TYPE",
  2137: "JS_TEMPORAL_PLAIN_TIME_TYPE",
  2138: "JS_TEMPORAL_PLAIN_YEAR_MONTH_TYPE",
  2139: "JS_TEMPORAL_TIME_ZONE_TYPE",
  2140: "JS_TEMPORAL_ZONED_DATE_TIME_TYPE",
  2141: "JS_V8_BREAK_ITERATOR_TYPE",
  2142: "JS_WEAK_REF_TYPE",
  2143: "WASM_EXCEPTION_PACKAGE_TYPE",
  2144: "WASM_GLOBAL_OBJECT_TYPE",
  2145: "WASM_INSTANCE_OBJECT_TYPE",
  2146: "WASM_MEMORY_OBJECT_TYPE",
  2147: "WASM_MODULE_OBJECT_TYPE",
  2148: "WASM_SUSPENDER_OBJECT_TYPE",
  2149: "WASM_TABLE_OBJECT_TYPE",
  2150: "WASM_TAG_OBJECT_TYPE",
  2151: "WASM_VALUE_OBJECT_TYPE",
}

# List of known V8 maps.
KNOWN_MAPS = {
    ("read_only_space", 0x02139): (250, "MetaMap"),
    ("read_only_space", 0x02161): (131, "NullMap"),
    ("read_only_space", 0x02189): (232, "StrongDescriptorArrayMap"),
    ("read_only_space", 0x021b1): (264, "WeakArrayListMap"),
    ("read_only_space", 0x021f5): (155, "EnumCacheMap"),
    ("read_only_space", 0x02229): (177, "FixedArrayMap"),
    ("read_only_space", 0x02275): (8, "OneByteInternalizedStringMap"),
    ("read_only_space", 0x022c1): (247, "FreeSpaceMap"),
    ("read_only_space", 0x022e9): (246, "OnePointerFillerMap"),
    ("read_only_space", 0x02311): (246, "TwoPointerFillerMap"),
    ("read_only_space", 0x02339): (131, "UninitializedMap"),
    ("read_only_space", 0x023b1): (131, "UndefinedMap"),
    ("read_only_space", 0x023f5): (130, "HeapNumberMap"),
    ("read_only_space", 0x02429): (131, "TheHoleMap"),
    ("read_only_space", 0x02489): (131, "BooleanMap"),
    ("read_only_space", 0x0252d): (192, "ByteArrayMap"),
    ("read_only_space", 0x02555): (177, "FixedCOWArrayMap"),
    ("read_only_space", 0x0257d): (178, "HashTableMap"),
    ("read_only_space", 0x025a5): (128, "SymbolMap"),
    ("read_only_space", 0x025cd): (40, "OneByteStringMap"),
    ("read_only_space", 0x025f5): (256, "ScopeInfoMap"),
    ("read_only_space", 0x0261d): (257, "SharedFunctionInfoMap"),
    ("read_only_space", 0x02645): (240, "CodeMap"),
    ("read_only_space", 0x0266d): (239, "CellMap"),
    ("read_only_space", 0x02695): (255, "GlobalPropertyCellMap"),
    ("read_only_space", 0x026bd): (204, "ForeignMap"),
    ("read_only_space", 0x026e5): (236, "TransitionArrayMap"),
    ("read_only_space", 0x0270d): (45, "ThinOneByteStringMap"),
    ("read_only_space", 0x02735): (245, "FeedbackVectorMap"),
    ("read_only_space", 0x0276d): (131, "ArgumentsMarkerMap"),
    ("read_only_space", 0x027cd): (131, "ExceptionMap"),
    ("read_only_space", 0x02829): (131, "TerminationExceptionMap"),
    ("read_only_space", 0x02891): (131, "OptimizedOutMap"),
    ("read_only_space", 0x028f1): (131, "StaleRegisterMap"),
    ("read_only_space", 0x02951): (191, "ScriptContextTableMap"),
    ("read_only_space", 0x02979): (189, "ClosureFeedbackCellArrayMap"),
    ("read_only_space", 0x029a1): (244, "FeedbackMetadataArrayMap"),
    ("read_only_space", 0x029c9): (177, "ArrayListMap"),
    ("read_only_space", 0x029f1): (129, "BigIntMap"),
    ("read_only_space", 0x02a19): (190, "ObjectBoilerplateDescriptionMap"),
    ("read_only_space", 0x02a41): (193, "BytecodeArrayMap"),
    ("read_only_space", 0x02a69): (241, "CodeDataContainerMap"),
    ("read_only_space", 0x02a91): (242, "CoverageInfoMap"),
    ("read_only_space", 0x02ab9): (194, "FixedDoubleArrayMap"),
    ("read_only_space", 0x02ae1): (180, "GlobalDictionaryMap"),
    ("read_only_space", 0x02b09): (157, "ManyClosuresCellMap"),
    ("read_only_space", 0x02b31): (251, "MegaDomHandlerMap"),
    ("read_only_space", 0x02b59): (177, "ModuleInfoMap"),
    ("read_only_space", 0x02b81): (181, "NameDictionaryMap"),
    ("read_only_space", 0x02ba9): (157, "NoClosuresCellMap"),
    ("read_only_space", 0x02bd1): (183, "NumberDictionaryMap"),
    ("read_only_space", 0x02bf9): (157, "OneClosureCellMap"),
    ("read_only_space", 0x02c21): (184, "OrderedHashMapMap"),
    ("read_only_space", 0x02c49): (185, "OrderedHashSetMap"),
    ("read_only_space", 0x02c71): (182, "NameToIndexHashTableMap"),
    ("read_only_space", 0x02c99): (187, "RegisteredSymbolTableMap"),
    ("read_only_space", 0x02cc1): (186, "OrderedNameDictionaryMap"),
    ("read_only_space", 0x02ce9): (253, "PreparseDataMap"),
    ("read_only_space", 0x02d11): (254, "PropertyArrayMap"),
    ("read_only_space", 0x02d39): (237, "AccessorInfoMap"),
    ("read_only_space", 0x02d61): (238, "SideEffectCallHandlerInfoMap"),
    ("read_only_space", 0x02d89): (238, "SideEffectFreeCallHandlerInfoMap"),
    ("read_only_space", 0x02db1): (238, "NextCallSideEffectFreeCallHandlerInfoMap"),
    ("read_only_space", 0x02dd9): (188, "SimpleNumberDictionaryMap"),
    ("read_only_space", 0x02e01): (228, "SmallOrderedHashMapMap"),
    ("read_only_space", 0x02e29): (229, "SmallOrderedHashSetMap"),
    ("read_only_space", 0x02e51): (230, "SmallOrderedNameDictionaryMap"),
    ("read_only_space", 0x02e79): (233, "SourceTextModuleMap"),
    ("read_only_space", 0x02ea1): (261, "SwissNameDictionaryMap"),
    ("read_only_space", 0x02ec9): (234, "SyntheticModuleMap"),
    ("read_only_space", 0x02ef1): (262, "WasmApiFunctionRefMap"),
    ("read_only_space", 0x02f19): (222, "WasmCapiFunctionDataMap"),
    ("read_only_space", 0x02f41): (223, "WasmExportedFunctionDataMap"),
    ("read_only_space", 0x02f69): (205, "WasmInternalFunctionMap"),
    ("read_only_space", 0x02f91): (224, "WasmJSFunctionDataMap"),
    ("read_only_space", 0x02fb9): (263, "WasmResumeDataMap"),
    ("read_only_space", 0x02fe1): (206, "WasmTypeInfoMap"),
    ("read_only_space", 0x03009): (235, "WeakFixedArrayMap"),
    ("read_only_space", 0x03031): (179, "EphemeronHashTableMap"),
    ("read_only_space", 0x03059): (243, "EmbedderDataArrayMap"),
    ("read_only_space", 0x03081): (265, "WeakCellMap"),
    ("read_only_space", 0x030a9): (32, "StringMap"),
    ("read_only_space", 0x030d1): (41, "ConsOneByteStringMap"),
    ("read_only_space", 0x030f9): (33, "ConsStringMap"),
    ("read_only_space", 0x03121): (37, "ThinStringMap"),
    ("read_only_space", 0x03149): (35, "SlicedStringMap"),
    ("read_only_space", 0x03171): (43, "SlicedOneByteStringMap"),
    ("read_only_space", 0x03199): (34, "ExternalStringMap"),
    ("read_only_space", 0x031c1): (42, "ExternalOneByteStringMap"),
    ("read_only_space", 0x031e9): (50, "UncachedExternalStringMap"),
    ("read_only_space", 0x03211): (0, "InternalizedStringMap"),
    ("read_only_space", 0x03239): (2, "ExternalInternalizedStringMap"),
    ("read_only_space", 0x03261): (10, "ExternalOneByteInternalizedStringMap"),
    ("read_only_space", 0x03289): (18, "UncachedExternalInternalizedStringMap"),
    ("read_only_space", 0x032b1): (26, "UncachedExternalOneByteInternalizedStringMap"),
    ("read_only_space", 0x032d9): (58, "UncachedExternalOneByteStringMap"),
    ("read_only_space", 0x03301): (104, "SharedOneByteStringMap"),
    ("read_only_space", 0x03329): (96, "SharedStringMap"),
    ("read_only_space", 0x03351): (109, "SharedThinOneByteStringMap"),
    ("read_only_space", 0x03379): (101, "SharedThinStringMap"),
    ("read_only_space", 0x033a1): (131, "SelfReferenceMarkerMap"),
    ("read_only_space", 0x033c9): (131, "BasicBlockCountersMarkerMap"),
    ("read_only_space", 0x0340d): (146, "ArrayBoilerplateDescriptionMap"),
    ("read_only_space", 0x0350d): (159, "InterceptorInfoMap"),
    ("read_only_space", 0x05f59): (132, "PromiseFulfillReactionJobTaskMap"),
    ("read_only_space", 0x05f81): (133, "PromiseRejectReactionJobTaskMap"),
    ("read_only_space", 0x05fa9): (134, "CallableTaskMap"),
    ("read_only_space", 0x05fd1): (135, "CallbackTaskMap"),
    ("read_only_space", 0x05ff9): (136, "PromiseResolveThenableJobTaskMap"),
    ("read_only_space", 0x06021): (139, "FunctionTemplateInfoMap"),
    ("read_only_space", 0x06049): (140, "ObjectTemplateInfoMap"),
    ("read_only_space", 0x06071): (141, "AccessCheckInfoMap"),
    ("read_only_space", 0x06099): (142, "AccessorPairMap"),
    ("read_only_space", 0x060c1): (143, "AliasedArgumentsEntryMap"),
    ("read_only_space", 0x060e9): (144, "AllocationMementoMap"),
    ("read_only_space", 0x06111): (147, "AsmWasmDataMap"),
    ("read_only_space", 0x06139): (148, "AsyncGeneratorRequestMap"),
    ("read_only_space", 0x06161): (149, "BreakPointMap"),
    ("read_only_space", 0x06189): (150, "BreakPointInfoMap"),
    ("read_only_space", 0x061b1): (151, "CachedTemplateObjectMap"),
    ("read_only_space", 0x061d9): (152, "CallSiteInfoMap"),
    ("read_only_space", 0x06201): (153, "ClassPositionsMap"),
    ("read_only_space", 0x06229): (154, "DebugInfoMap"),
    ("read_only_space", 0x06251): (156, "ErrorStackDataMap"),
    ("read_only_space", 0x06279): (158, "FunctionTemplateRareDataMap"),
    ("read_only_space", 0x062a1): (160, "InterpreterDataMap"),
    ("read_only_space", 0x062c9): (161, "ModuleRequestMap"),
    ("read_only_space", 0x062f1): (162, "PromiseCapabilityMap"),
    ("read_only_space", 0x06319): (163, "PromiseOnStackMap"),
    ("read_only_space", 0x06341): (164, "PromiseReactionMap"),
    ("read_only_space", 0x06369): (165, "PropertyDescriptorObjectMap"),
    ("read_only_space", 0x06391): (166, "PrototypeInfoMap"),
    ("read_only_space", 0x063b9): (167, "RegExpBoilerplateDescriptionMap"),
    ("read_only_space", 0x063e1): (168, "ScriptMap"),
    ("read_only_space", 0x06409): (169, "ScriptOrModuleMap"),
    ("read_only_space", 0x06431): (170, "SourceTextModuleInfoEntryMap"),
    ("read_only_space", 0x06459): (171, "StackFrameInfoMap"),
    ("read_only_space", 0x06481): (172, "TemplateObjectDescriptionMap"),
    ("read_only_space", 0x064a9): (173, "Tuple2Map"),
    ("read_only_space", 0x064d1): (174, "WasmContinuationObjectMap"),
    ("read_only_space", 0x064f9): (175, "WasmExceptionTagMap"),
    ("read_only_space", 0x06521): (176, "WasmIndirectFunctionTableMap"),
    ("read_only_space", 0x06549): (196, "SloppyArgumentsElementsMap"),
    ("read_only_space", 0x06571): (231, "DescriptorArrayMap"),
    ("read_only_space", 0x06599): (219, "UncompiledDataWithoutPreparseDataMap"),
    ("read_only_space", 0x065c1): (217, "UncompiledDataWithPreparseDataMap"),
    ("read_only_space", 0x065e9): (220, "UncompiledDataWithoutPreparseDataWithJobMap"),
    ("read_only_space", 0x06611): (218, "UncompiledDataWithPreparseDataAndJobMap"),
    ("read_only_space", 0x06639): (252, "OnHeapBasicBlockProfilerDataMap"),
    ("read_only_space", 0x06661): (197, "TurbofanBitsetTypeMap"),
    ("read_only_space", 0x06689): (201, "TurbofanUnionTypeMap"),
    ("read_only_space", 0x066b1): (200, "TurbofanRangeTypeMap"),
    ("read_only_space", 0x066d9): (198, "TurbofanHeapConstantTypeMap"),
    ("read_only_space", 0x06701): (199, "TurbofanOtherNumberConstantTypeMap"),
    ("read_only_space", 0x06729): (248, "InternalClassMap"),
    ("read_only_space", 0x06751): (259, "SmiPairMap"),
    ("read_only_space", 0x06779): (258, "SmiBoxMap"),
    ("read_only_space", 0x067a1): (225, "ExportedSubClassBaseMap"),
    ("read_only_space", 0x067c9): (226, "ExportedSubClassMap"),
    ("read_only_space", 0x067f1): (202, "AbstractInternalClassSubclass1Map"),
    ("read_only_space", 0x06819): (203, "AbstractInternalClassSubclass2Map"),
    ("read_only_space", 0x06841): (195, "InternalClassWithSmiElementsMap"),
    ("read_only_space", 0x06869): (249, "InternalClassWithStructElementsMap"),
    ("read_only_space", 0x06891): (227, "ExportedSubClass2Map"),
    ("read_only_space", 0x068b9): (260, "SortStateMap"),
    ("read_only_space", 0x068e1): (145, "AllocationSiteWithWeakNextMap"),
    ("read_only_space", 0x06909): (145, "AllocationSiteWithoutWeakNextMap"),
    ("read_only_space", 0x069d5): (137, "LoadHandler1Map"),
    ("read_only_space", 0x069fd): (137, "LoadHandler2Map"),
    ("read_only_space", 0x06a25): (137, "LoadHandler3Map"),
    ("read_only_space", 0x06a4d): (138, "StoreHandler0Map"),
    ("read_only_space", 0x06a75): (138, "StoreHandler1Map"),
    ("read_only_space", 0x06a9d): (138, "StoreHandler2Map"),
    ("read_only_space", 0x06ac5): (138, "StoreHandler3Map"),
    ("map_space", 0x02139): (2114, "ExternalMap"),
    ("map_space", 0x02161): (2118, "JSMessageObjectMap"),
}

# List of known V8 objects.
KNOWN_OBJECTS = {
  ("read_only_space", 0x021d9): "EmptyWeakArrayList",
  ("read_only_space", 0x021e5): "EmptyDescriptorArray",
  ("read_only_space", 0x0221d): "EmptyEnumCache",
  ("read_only_space", 0x02251): "EmptyFixedArray",
  ("read_only_space", 0x02259): "NullValue",
  ("read_only_space", 0x02361): "UninitializedValue",
  ("read_only_space", 0x023d9): "UndefinedValue",
  ("read_only_space", 0x0241d): "NanValue",
  ("read_only_space", 0x02451): "TheHoleValue",
  ("read_only_space", 0x0247d): "HoleNanValue",
  ("read_only_space", 0x024b1): "TrueValue",
  ("read_only_space", 0x024f1): "FalseValue",
  ("read_only_space", 0x02521): "empty_string",
  ("read_only_space", 0x0275d): "EmptyScopeInfo",
  ("read_only_space", 0x02795): "ArgumentsMarker",
  ("read_only_space", 0x027f5): "Exception",
  ("read_only_space", 0x02851): "TerminationException",
  ("read_only_space", 0x028b9): "OptimizedOut",
  ("read_only_space", 0x02919): "StaleRegister",
  ("read_only_space", 0x033f1): "EmptyPropertyArray",
  ("read_only_space", 0x033f9): "EmptyByteArray",
  ("read_only_space", 0x03401): "EmptyObjectBoilerplateDescription",
  ("read_only_space", 0x03435): "EmptyArrayBoilerplateDescription",
  ("read_only_space", 0x03441): "EmptyClosureFeedbackCellArray",
  ("read_only_space", 0x03449): "EmptySlowElementDictionary",
  ("read_only_space", 0x0346d): "EmptyOrderedHashMap",
  ("read_only_space", 0x03481): "EmptyOrderedHashSet",
  ("read_only_space", 0x03495): "EmptyFeedbackMetadata",
  ("read_only_space", 0x034a1): "EmptyPropertyDictionary",
  ("read_only_space", 0x034c9): "EmptyOrderedPropertyDictionary",
  ("read_only_space", 0x034e1): "EmptySwissPropertyDictionary",
  ("read_only_space", 0x03535): "NoOpInterceptorInfo",
  ("read_only_space", 0x0355d): "EmptyArrayList",
  ("read_only_space", 0x03569): "EmptyWeakFixedArray",
  ("read_only_space", 0x03571): "InfinityValue",
  ("read_only_space", 0x0357d): "MinusZeroValue",
  ("read_only_space", 0x03589): "MinusInfinityValue",
  ("read_only_space", 0x03595): "SelfReferenceMarker",
  ("read_only_space", 0x035d5): "BasicBlockCountersMarker",
  ("read_only_space", 0x03619): "OffHeapTrampolineRelocationInfo",
  ("read_only_space", 0x03625): "GlobalThisBindingScopeInfo",
  ("read_only_space", 0x03655): "EmptyFunctionScopeInfo",
  ("read_only_space", 0x03679): "NativeScopeInfo",
  ("read_only_space", 0x03691): "HashSeed",
  ("old_space", 0x04231): "ArgumentsIteratorAccessor",
  ("old_space", 0x04259): "ArrayLengthAccessor",
  ("old_space", 0x04281): "BoundFunctionLengthAccessor",
  ("old_space", 0x042a9): "BoundFunctionNameAccessor",
  ("old_space", 0x042d1): "ErrorStackAccessor",
  ("old_space", 0x042f9): "FunctionArgumentsAccessor",
  ("old_space", 0x04321): "FunctionCallerAccessor",
  ("old_space", 0x04349): "FunctionNameAccessor",
  ("old_space", 0x04371): "FunctionLengthAccessor",
  ("old_space", 0x04399): "FunctionPrototypeAccessor",
  ("old_space", 0x043c1): "SharedArrayLengthAccessor",
  ("old_space", 0x043e9): "StringLengthAccessor",
  ("old_space", 0x04411): "ValueUnavailableAccessor",
  ("old_space", 0x04439): "WrappedFunctionLengthAccessor",
  ("old_space", 0x04461): "WrappedFunctionNameAccessor",
  ("old_space", 0x04489): "InvalidPrototypeValidityCell",
  ("old_space", 0x04491): "EmptyScript",
  ("old_space", 0x044d5): "ManyClosuresCell",
  ("old_space", 0x044e1): "ArrayConstructorProtector",
  ("old_space", 0x044f5): "NoElementsProtector",
  ("old_space", 0x04509): "MegaDOMProtector",
  ("old_space", 0x0451d): "IsConcatSpreadableProtector",
  ("old_space", 0x04531): "ArraySpeciesProtector",
  ("old_space", 0x04545): "TypedArraySpeciesProtector",
  ("old_space", 0x04559): "PromiseSpeciesProtector",
  ("old_space", 0x0456d): "RegExpSpeciesProtector",
  ("old_space", 0x04581): "StringLengthProtector",
  ("old_space", 0x04595): "ArrayIteratorProtector",
  ("old_space", 0x045a9): "ArrayBufferDetachingProtector",
  ("old_space", 0x045bd): "PromiseHookProtector",
  ("old_space", 0x045d1): "PromiseResolveProtector",
  ("old_space", 0x045e5): "MapIteratorProtector",
  ("old_space", 0x045f9): "PromiseThenProtector",
  ("old_space", 0x0460d): "SetIteratorProtector",
  ("old_space", 0x04621): "StringIteratorProtector",
  ("old_space", 0x04635): "SingleCharacterStringCache",
  ("old_space", 0x04a3d): "StringSplitCache",
  ("old_space", 0x04e45): "RegExpMultipleCache",
  ("old_space", 0x0524d): "BuiltinsConstantsTable",
  ("old_space", 0x05691): "AsyncFunctionAwaitRejectSharedFun",
  ("old_space", 0x056b5): "AsyncFunctionAwaitResolveSharedFun",
  ("old_space", 0x056d9): "AsyncGeneratorAwaitRejectSharedFun",
  ("old_space", 0x056fd): "AsyncGeneratorAwaitResolveSharedFun",
  ("old_space", 0x05721): "AsyncGeneratorYieldResolveSharedFun",
  ("old_space", 0x05745): "AsyncGeneratorReturnResolveSharedFun",
  ("old_space", 0x05769): "AsyncGeneratorReturnClosedRejectSharedFun",
  ("old_space", 0x0578d): "AsyncGeneratorReturnClosedResolveSharedFun",
  ("old_space", 0x057b1): "AsyncIteratorValueUnwrapSharedFun",
  ("old_space", 0x057d5): "PromiseAllResolveElementSharedFun",
  ("old_space", 0x057f9): "PromiseAllSettledResolveElementSharedFun",
  ("old_space", 0x0581d): "PromiseAllSettledRejectElementSharedFun",
  ("old_space", 0x05841): "PromiseAnyRejectElementSharedFun",
  ("old_space", 0x05865): "PromiseCapabilityDefaultRejectSharedFun",
  ("old_space", 0x05889): "PromiseCapabilityDefaultResolveSharedFun",
  ("old_space", 0x058ad): "PromiseCatchFinallySharedFun",
  ("old_space", 0x058d1): "PromiseGetCapabilitiesExecutorSharedFun",
  ("old_space", 0x058f5): "PromiseThenFinallySharedFun",
  ("old_space", 0x05919): "PromiseThrowerFinallySharedFun",
  ("old_space", 0x0593d): "PromiseValueThunkFinallySharedFun",
  ("old_space", 0x05961): "ProxyRevokeSharedFun",
  ("old_space", 0x05985): "ShadowRealmImportValueFulfilledSFI",
  ("old_space", 0x059a9): "SourceTextModuleExecuteAsyncModuleFulfilledSFI",
  ("old_space", 0x059cd): "SourceTextModuleExecuteAsyncModuleRejectedSFI",
}

# Lower 32 bits of first page addresses for various heap spaces.
HEAP_FIRST_PAGES = {
  0x000c0000: "old_space",
  0x00100000: "map_space",
  0x00000000: "read_only_space",
}

# List of known V8 Frame Markers.
FRAME_MARKERS = (
  "ENTRY",
  "CONSTRUCT_ENTRY",
  "EXIT",
  "WASM",
  "WASM_TO_JS",
  "JS_TO_WASM",
  "STACK_SWITCH",
  "WASM_DEBUG_BREAK",
  "C_WASM_ENTRY",
  "WASM_EXIT",
  "WASM_COMPILE_LAZY",
  "INTERPRETED",
  "BASELINE",
  "MAGLEV",
  "TURBOFAN",
  "STUB",
  "BUILTIN_CONTINUATION",
  "JAVA_SCRIPT_BUILTIN_CONTINUATION",
  "JAVA_SCRIPT_BUILTIN_CONTINUATION_WITH_CATCH",
  "INTERNAL",
  "CONSTRUCT",
  "BUILTIN",
  "BUILTIN_EXIT",
  "NATIVE",
)

# This set of constants is generated from a shipping build.
