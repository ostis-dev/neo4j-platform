from enum import Enum
from typing import Union

import re


class TokenContext:

    def __init__(self, line: int, column: int, text: str) -> None:
        self.line = line
        self.column = column
        self.text = text

    def __repr__(self) -> str:
        return f"{{ line: {self._line}, column: {self._column}, text: `{self._text}`}}"


class Element:

    class Kind(Enum):
        ALIAS = 0
        NODE = 1
        EDGE = 2
        ARC = 3
        LINK = 4

    def __init__(self, kind: Kind, name: str, ctx: TokenContext) -> None:
        self.kind = kind
        self.name = name
        self.ctx = ctx

    def is_const(self) -> bool:
        return not self.is_var()

    def is_var(self) -> bool:
        return re.fullmatch(re.compile("^\.{0,2}_.*$"), self.name) is not None

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(ctx: {self.ctx}, kind: {self.kind.name}, name: {self.name})"


class Alias(Element):

    def __init__(self, name: str, ctx: TokenContext, target: Element) -> None:
        super().__init__(Element.Kind.ALIAS, name, ctx)

        self.target = target


class Node(Element):

    def __init__(self, name: str, ctx: TokenContext) -> None:
        super().__init__(Element.Kind.NODE, name, ctx)


class Edge(Element):

    def __init__(self, connector: str, name: str, ctx: TokenContext) -> None:
        super().__init__(Element.Kind.EDGE, name, ctx)

        self.conenctor = connector


class Arc(Element):

    def __init__(self, connector: str, name: str, ctx: TokenContext) -> None:
        super().__init__(Element.Kind.ARC, name, ctx)

        self.connector = connector


class Link(Element):

    Value = Union[str, int, float]

    class Type(Enum):
        UNKNOWN = 0
        INT = 1
        FLOAT = 2
        STR = 3
        URL = 4

    def __init__(self, name: str, value: Value, type: Type, ctx: TokenContext) -> None:
        super().__init__(Element.Kind.LINK, name, ctx)

        self.value = value
        self.type = type
