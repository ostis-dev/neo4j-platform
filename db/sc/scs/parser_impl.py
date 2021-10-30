from sc.core.keynodes import KeynodeNames

from typing import Dict, List, Set, Tuple, Union

from .parse_issue import ParseIssue
from .types import Alias, Arc, Edge, Element, Link, Node, TokenContext

from antlr4.error.Errors import ParseCancellationException


Triple = Tuple[Element, Union[Arc, Edge], Element]


class SCsParserImpl:

    def __init__(self) -> None:
        # list of parsed triples
        self._triples = []

        # Dictionary of element types.
        # They should be in format: {element.name, set(str)}
        self._types = {}

        # Counter for generated names
        self._names_counter = 0

        # Set of type keynodes (for fast access)
        self._type_keynodes = set()
        self._type_keynodes.update(KeynodeNames.CORE_TYPES)
        self._type_keynodes.update(KeynodeNames.CONST_TYPES)
        self._type_keynodes.update(KeynodeNames.NODE_TYPES)
        self._type_keynodes.update(KeynodeNames.ARC_PERM_TYPES)
        self._type_keynodes.update(KeynodeNames.ARC_POS_TYPES)

        # Dictionary of alias definitions <str, AliasDefinition>
        self._aliases = {}

        # List of warnings
        self._errors = []
        self._warnings = []

        # Stack of contours
        self._contour_stack = []

    @property
    def errors(self) -> List[ParseIssue]:
        return self._errors

    @property
    def warnings(self) -> List[ParseIssue]:
        return self._warnings

    @property
    def types(self) -> Dict[str, Set[str]]:
        """Returns dictionary with element types"""
        return self._types

    @property
    def triples(self) -> List[Triple]:
        """Returns list of triples"""
        return self._triples

    def _process_name(self, name: str, prefix: str = "el", force_var: bool = False) -> str:
        def next_id():
            self._names_counter += 1
            return self._names_counter

        if name is None or name == "..." or name == "{":
            name = f"..{'_' if force_var else ''}{prefix}_generated_{next_id()}"

        return name

    def _is_type_keynode(self, name: str) -> bool:
        """Checks if specified name if a type keynode"""
        return name in self._type_keynodes

    def _break_parsing(self, msg: str):
        """Raises error to break parsing"""
        raise ParseCancellationException(msg)

    def create_alias(self, ctx: TokenContext) -> Alias:
        return Alias(ctx.text, ctx, None)

    def create_node(self, ctx: TokenContext) -> Node:
        return Node(self._process_name(ctx.text, prefix="node"), ctx)

    def create_link(self, ctx: TokenContext, value: Link.Value, type: Link.Type, is_var: bool) -> Link:
        return Link(self._process_name(None, prefix="link", force_var=is_var),
                    self._link_remove_escape_symbols(value),
                    type, ctx)

    def create_edge(self, ctx: TokenContext, connector: str) -> Edge:
        return Edge(connector, self._process_name(None, prefix="edge"), ctx)

    def create_arc(self, ctx: TokenContext, connector: str) -> Arc:
        return Arc(connector, self._process_name(None, prefix="arc"), ctx)

    def append_triple(self, src: Element, edge: Union[Edge, Arc], trg: Element):
        def _resolve_alias(alias: Alias) -> Element:
            try:
                return self._aliases[alias.name].target
            except KeyError:
                self._new_error(alias.ctx,
                                f"Alias {alias.name} is not defined")
                self._break_parsing(f"Alias {alias.name} is not defined")

        if src.kind == Element.Kind.ALIAS:
            src = _resolve_alias(src)
        if trg.kind == Element.Kind.ALIAS:
            trg = _resolve_alias(trg)

        triples = self._contour_stack[-1] if len(self._contour_stack) > 0 else self._triples

        if edge._reverse_if_back():
            triples.append((trg, edge, src))
        else:
            triples.append((src, edge, trg))

    def define_alias(self, alias: Alias, target: Element) -> Alias:
        """Create new alias to specified element"""
        assert alias.target is None
        try:
            prev_alias = self._aliases[alias.name]
            self._new_warning(alias.ctx,
                              (f"Alias {alias.name} was previously defined at line: {prev_alias.ctx.line}"
                               " column: {prev_alias.ctx.column}"))
        except KeyError:
            pass

        new_alias = Alias(alias.name, alias.ctx, target)
        self._aliases[new_alias.name] = new_alias
        return new_alias

    def _new_error(self, ctx: TokenContext, msg: str):
        self._errors.append(
            ParseIssue(ctx.line, ctx.column, ctx.text, msg, ParseIssue.Type.ERROR))

    def _new_warning(self, ctx: TokenContext, msg: str):
        self._warnings.append(
            ParseIssue(ctx.line, ctx.column, ctx.text, msg, ParseIssue.Type.ERROR))

    def _add_type(self, name: str, type_keynode: str):
        try:
            self._types[name].add(type_keynode)
        except KeyError:
            self._types[name] = {type_keynode}

    def _link_remove_escape_symbols(self, input: str) -> str:
        return input.replace("\\[", "[").replace("\\]", "]").replace("\\\\", "\\")

    def start_contour(self):
        self._contour_stack.append([])

    def end_contour(self, contour: Node):
        contour_triples = self._contour_stack.pop()
        self._triples.extend(contour_triples)

        # append elements into contour
        added = set()

        def add_element(child: Element):
            if child.name not in added:
                edge = self.create_arc(TokenContext(-1, -1, "->"), "->")
                self._triples.append((contour, edge, child))
                added.add(child.name)

        for src, edge, trg in contour_triples:
            add_element(src)
            add_element(edge)
            add_element(trg)
