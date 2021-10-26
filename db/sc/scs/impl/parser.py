from sc.scs.element import *
from typing import Dict, List, Set, Tuple, Union

from sc.core.keynodes import KeynodeNames
from .error import AlreadyExistError, UnsupportedError

Alias = str
TripleElement = Union[Element, Alias]
Triple = Tuple[TripleElement, TripleElement, TripleElement]


class SCsParserImpl:

    class AliasDefinition:
        def __init__(self, alias: str, line: int, element: Element) -> None:
            self._alias = alias
            self._line = line
            self._element = element

        @property
        def alias(self) -> str:
            return self._alias

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(alias: {self._alias}, line: {self._line}, element: {self._element})"

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

    @property
    def types(self) -> Dict[str, Set[str]]:
        """Returns dictionary with element types"""
        return self._types

    @property
    def triples(self) -> List[Triple]:
        """Returns list of triples"""
        return self._triples

    def _process_name(self, name: str, prefix: str = "el") -> str:
        def next_id():
            self._names_counter += 1
            return self._names_counter

        return name if name is not None else f"..{prefix}_generated_{next_id()}"

    def _is_type_keynode(self, name: str) -> bool:
        """Checks if specified name if a type keynode"""
        return name in self._type_keynodes

    def define_alias(self, alias: str, element: Element, line: int) -> str:
        """Create definition of alias

        If alias already exists, then raises AlreadyExistError
        """
        try:
            found_alias = self._aliases[alias]
            raise AlreadyExistError(
                f"Alias `{alias}` already defined before in line {found_alias.line}")
        except AlreadyExistError:
            self._aliases[alias] = SCsParserImpl.AliasDefinition(
                alias=alias, line=line, element=element)
        return

    def create_node(self, name: str = None) -> Node:
        return Node(name=self._process_name(name, prefix="node"))

    def create_link(self, name: str = None, value: Link.Value = None, type: Link.Type = Link.Type.UNKNOWN) -> Link:
        return Link(name=self._process_name(name, prefix="link"), value=value, type=type)

    def create_edge(self, connector: str = None, name: str = None) -> Edge:
        return Edge(self._process_name(name, prefix="edge"))

    def create_arc(self, connector: str = None, name: str = None) -> Arc:
        return Arc(self._process_name(name, prefix="arc"))

    def append_triple(self, src: Union[Element, Alias], edge: Union[Edge, Arc], trg: Union[Element, Alias]):
        if self._is_type_keynode(src.name):
            self._type_triples.append((src, edge, trg))
        else:
            self._triples.append((src, edge, trg))

    def _add_type(self, name: str, type_keynode: str):
        try:
            self._types[name].add(type_keynode)
        except KeyError:
            self._types[name] = {type_keynode}

    def _processIdtfLevel1(self, type_: str, name: str) -> Element:
        """Determines which element should be created by identifier from scs-level-1."""
        if type_ == KeynodeNames.SC_NODE:
            return self.create_node(name=name)
        elif type_ == KeynodeNames.SC_ARC:
            return self.create_arc(name=name)
        elif type_ == KeynodeNames.SC_EDGE:
            return self.create_edge(name=name)
        elif type_ == KeynodeNames.SC_LINK:
            return self.create_link(name)
        else:
            raise UnsupportedError(f"Type {type_} is not supported")
