// Copyright 2015 the V8 project authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

import { PhaseView } from "./view";
import { isIterable } from "../common/util";
import { SelectionMap } from "../selection/selection-map";
import { SourceResolver } from "../source-resolver";
import { SelectionBroker } from "../selection/selection-broker";
import { ViewElements } from "../common/view-elements";
import {
  NodeSelectionHandler,
  BlockSelectionHandler,
  RegisterAllocationSelectionHandler,
  ClearableHandler
} from "../selection/selection-handler";

export abstract class TextView extends PhaseView {
  selectionHandler: NodeSelectionHandler & ClearableHandler;
  blockSelectionHandler: BlockSelectionHandler & ClearableHandler;
  registerAllocationSelectionHandler: RegisterAllocationSelectionHandler & ClearableHandler;
  selection: SelectionMap;
  blockSelection: SelectionMap;
  registerAllocationSelection: SelectionMap;
  textListNode: HTMLUListElement;
  instructionIdToHtmlElementsMap: Map<string, Array<HTMLElement>>;
  nodeIdToHtmlElementsMap: Map<string, Array<HTMLElement>>;
  blockIdToHtmlElementsMap: Map<string, Array<HTMLElement>>;
  blockIdToNodeIds: Map<string, Array<string>>;
  nodeIdToBlockId: Array<string>;
  patterns: Array<Array<any>>;
  sourceResolver: SourceResolver;
  broker: SelectionBroker;

  constructor(id, broker) {
    super(id);
    const view = this;
    view.broker = broker;
    view.sourceResolver = broker.sourceResolver;
    view.textListNode = view.divNode.getElementsByTagName("ul")[0];
    view.patterns = null;
    view.instructionIdToHtmlElementsMap = new Map<string, Array<HTMLElement>>();
    view.nodeIdToHtmlElementsMap = new Map<string, Array<HTMLElement>>();
    view.blockIdToHtmlElementsMap = new Map<string, Array<HTMLElement>>();
    view.blockIdToNodeIds = new Map<string, Array<string>>();
    view.nodeIdToBlockId = new Array<string>();

    view.selection = new SelectionMap(node => String(node));
    view.blockSelection = new SelectionMap(block => String(block));
    view.registerAllocationSelection = new SelectionMap(register => String(register));

    view.selectionHandler = this.initializeNodeSelectionHandler();
    view.blockSelectionHandler = this.initializeBlockSelectionHandler();
    view.registerAllocationSelectionHandler = this.initializeRegisterAllocationSelectionHandler();

    broker.addNodeHandler(view.selectionHandler);
    broker.addBlockHandler(view.blockSelectionHandler);
    broker.addRegisterAllocatorHandler(view.registerAllocationSelectionHandler);

    view.divNode.addEventListener("click", e => {
      if (!e.shiftKey) {
        view.selectionHandler.clear();
      }
      e.stopPropagation();
    });
  }

  // TODO (danylo boiko) Change data type
  public initializeContent(data: any, _): void {
    this.clearText();
    this.processText(data);
    this.show();
  }

  public updateSelection(scrollIntoView: boolean = false): void {
    if (this.divNode.parentNode == null) return;
    const mkVisible = new ViewElements(this.divNode.parentNode as HTMLElement);
    const elementsToSelect = this.divNode.querySelectorAll(`[data-pc-offset]`);

    for (const el of elementsToSelect) {
      el.classList.toggle("selected", false);
    }
    for (const [blockId, elements] of this.blockIdToHtmlElementsMap.entries()) {
      const isSelected = this.blockSelection.isSelected(blockId);
      for (const element of elements) {
        mkVisible.consider(element, isSelected);
        element.classList.toggle("selected", isSelected);
      }
    }

    for (const key of this.instructionIdToHtmlElementsMap.keys()) {
      for (const element of this.instructionIdToHtmlElementsMap.get(key)) {
        element.classList.toggle("selected", false);
      }
    }
    for (const instrId of this.registerAllocationSelection.selectedKeys()) {
      const elements = this.instructionIdToHtmlElementsMap.get(instrId);
      if (!elements) continue;
      for (const element of elements) {
        mkVisible.consider(element, true);
        element.classList.toggle("selected", true);
      }
    }

    for (const key of this.nodeIdToHtmlElementsMap.keys()) {
      for (const element of this.nodeIdToHtmlElementsMap.get(key)) {
        element.classList.toggle("selected", false);
      }
    }
    for (const nodeId of this.selection.selectedKeys()) {
      const elements = this.nodeIdToHtmlElementsMap.get(nodeId);
      if (!elements) continue;
      for (const element of elements) {
        mkVisible.consider(element, true);
        element.classList.toggle("selected", true);
      }
    }

    mkVisible.apply(scrollIntoView);
  }

  public processLine(line: string): Array<HTMLSpanElement> {
    const result = new Array<HTMLSpanElement>();
    let patternSet = 0;
    while (true) {
      const beforeLine = line;
      for (const pattern of this.patterns[patternSet]) {
        const matches = line.match(pattern[0]);
        if (matches) {
          if (matches[0].length > 0) {
            const style = pattern[1] != null ? pattern[1] : {};
            const text = matches[0];
            if (text.length > 0) {
              const fragment = this.createFragment(matches[0], style);
              if (fragment !== null) result.push(fragment);
            }
            line = line.substr(matches[0].length);
          }
          let nextPatternSet = patternSet;
          if (pattern.length > 2) {
            nextPatternSet = pattern[2];
          }
          if (line.length == 0) {
            if (nextPatternSet != -1) {
              throw (`illegal parsing state in text-view in patternSet: ${patternSet}`);
            }
            return result;
          }
          patternSet = nextPatternSet;
          break;
        }
      }
      if (beforeLine == line) {
        throw (`input not consumed in text-view in patternSet: ${patternSet}`);
      }
    }
  }

  public onresize(): void {}

  // instruction-id are the divs for the register allocator phase
  protected addHtmlElementForInstructionId(anyInstructionId: any, htmlElement: HTMLElement): void {
    const instructionId = String(anyInstructionId);
    if (!this.instructionIdToHtmlElementsMap.has(instructionId)) {
      this.instructionIdToHtmlElementsMap.set(instructionId, new Array<HTMLElement>());
    }
    this.instructionIdToHtmlElementsMap.get(instructionId).push(htmlElement);
  }

  protected addHtmlElementForNodeId(anyNodeId: any, htmlElement: HTMLElement): void {
    const nodeId = String(anyNodeId);
    if (!this.nodeIdToHtmlElementsMap.has(nodeId)) {
      this.nodeIdToHtmlElementsMap.set(nodeId, new Array<HTMLElement>());
    }
    this.nodeIdToHtmlElementsMap.get(nodeId).push(htmlElement);
  }

  protected addHtmlElementForBlockId(anyBlockId: any, htmlElement: HTMLElement): void {
    const blockId = String(anyBlockId);
    if (!this.blockIdToHtmlElementsMap.has(blockId)) {
      this.blockIdToHtmlElementsMap.set(blockId, new Array<HTMLElement>());
    }
    this.blockIdToHtmlElementsMap.get(blockId).push(htmlElement);
  }

  protected createFragment(text: string, style): HTMLSpanElement {
    const fragment = document.createElement("span");

    if (typeof style.associateData === "function") {
      if (!style.associateData(text, fragment)) return null;
    } else {
      if (style.css !== undefined) {
        const css = isIterable(style.css) ? style.css : [style.css];
        for (const cls of css) {
          fragment.classList.add(cls);
        }
      }
      fragment.innerText = text;
    }

    return fragment;
  }

  protected setPatterns(patterns: Array<Array<any>>): void {
    this.patterns = patterns;
  }

  private initializeNodeSelectionHandler(): NodeSelectionHandler & ClearableHandler {
    const view = this;
    return {
      select: function (nodeIds: Array<string>, selected: boolean) {
        view.selection.select(nodeIds, selected);
        view.updateSelection();
        view.broker.broadcastNodeSelect(this, view.selection.selectedKeys(), selected);
      },
      clear: function () {
        view.selection.clear();
        view.updateSelection();
        view.broker.broadcastClear(this);
      },
      brokeredNodeSelect: function (nodeIds: Set<string>, selected: boolean) {
        const firstSelect = view.blockSelection.isEmpty();
        view.selection.select(nodeIds, selected);
        view.updateSelection(firstSelect);
      },
      brokeredClear: function () {
        view.selection.clear();
        view.updateSelection();
      }
    };
  }

  private initializeBlockSelectionHandler(): BlockSelectionHandler & ClearableHandler {
    const view = this;
    return {
      select: function (blockIds: Array<string>, selected: boolean) {
        view.blockSelection.select(blockIds, selected);
        view.updateSelection();
        view.broker.broadcastBlockSelect(this, blockIds, selected);
      },
      clear: function () {
        view.blockSelection.clear();
        view.updateSelection();
        view.broker.broadcastClear(this);
      },
      brokeredBlockSelect: function (blockIds: Array<string>, selected: boolean) {
        const firstSelect = view.blockSelection.isEmpty();
        view.blockSelection.select(blockIds, selected);
        view.updateSelection(firstSelect);
      },
      brokeredClear: function () {
        view.blockSelection.clear();
        view.updateSelection();
      }
    };
  }

  private initializeRegisterAllocationSelectionHandler(): RegisterAllocationSelectionHandler
    & ClearableHandler {
    const view = this;
    return {
      select: function (instructionIds: Array<number>, selected: boolean) {
        view.registerAllocationSelection.select(instructionIds, selected);
        view.updateSelection();
        view.broker.broadcastInstructionSelect(null, [instructionIds], selected);
      },
      clear: function () {
        view.registerAllocationSelection.clear();
        view.updateSelection();
        view.broker.broadcastClear(this);
      },
      brokeredRegisterAllocationSelect: function (instructionIds: Array<number>,
                                                  selected: boolean) {
        const firstSelect = view.blockSelection.isEmpty();
        view.registerAllocationSelection.select(instructionIds, selected);
        view.updateSelection(firstSelect);
      },
      brokeredClear: function () {
        view.registerAllocationSelection.clear();
        view.updateSelection();
      }
    };
  }

  private clearText(): void {
    while (this.textListNode.firstChild) {
      this.textListNode.removeChild(this.textListNode.firstChild);
    }
  }

  private processText(text: string): void {
    const textLines = text.split(/[\n]/);
    let lineNo = 0;
    for (const line of textLines) {
      const li = document.createElement("li");
      li.className = "nolinenums";
      li.dataset.lineNo = String(lineNo++);
      const fragments = this.processLine(line);
      for (const fragment of fragments) {
        li.appendChild(fragment);
      }
      this.textListNode.appendChild(li);
    }
  }
}
