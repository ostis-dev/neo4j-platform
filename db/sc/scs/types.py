from enum import Enum
from sys import is_finalizing
from typing import Union

import re


class TokenContext:

    def __init__(self, line: int, column: int, text: str) -> None:
        self.line = line
        self.column = column
        self.text = text

    def __repr__(self) -> str:
        return f"{{ line: {self.line}, column: {self.column}, text: `{self.text}`}}"


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
        return self.__to_str()

    def _to_str(self, **kwargs):
        attrs = ', '.join([f"{k}: {v}" for k, v in kwargs.items()])
        return f"{self.__class__.__name__}(ctx: {self.ctx}, kind: {self.kind.name}, name: {self.name}, {attrs})"


class Alias(Element):

    def __init__(self, name: str, ctx: TokenContext, target: Element) -> None:
        super().__init__(Element.Kind.ALIAS, name, ctx)

        self.target = target

    def __repr__(self) -> str:
        return self._to_str(target=self.target)


class Node(Element):

    def __init__(self, name: str, ctx: TokenContext) -> None:
        super().__init__(Element.Kind.NODE, name, ctx)


class Edge(Element):

    VALID = {'<>', '<=>', '_<>', '_<=>', '>',
             '<', '=>', '<=', '_=>', '_<='}
    BACKWARD = {'<', '<=', '_<='}
    REVERSE_DICT = {
        '<': '>',
        '<=': '=>',
        '_<=': '_=>'
    }

    def __init__(self, connector: str, name: str, ctx: TokenContext) -> None:
        super().__init__(Element.Kind.EDGE, name, ctx)

        self.connector = connector
        if self.connector not in Edge.VALID:
            raise KeyError(
                f"Connector `{connector}` is not supported. List of supported connectors: {Edge.VALID}")

    def _reverse_if_back(self) -> bool:
        """Reverse connector to forward direction.

        If connector was reversed, then returns True.
        """
        if self.connector in Edge.BACKWARD:
            self.connector = Edge.REVERSE_DICT[self.connector]

        return False

    def __repr__(self) -> str:
        return self._to_str(connector=self.connector)


class Arc(Element):

    VALID = {'..>', '<..', '->', '<-', '-|>', '<|-', '-/>', '</-', '~>', '<~', '~|>', '<|~', '~/>', '</~',
             '_..>', '_<..', '_->', '_<-', '_-|>', '_<|-', '_-/>', '_</-', '_~>', '_<~', '_~|>', '_<|~', '_~/>', '_</~'}
    BACKWARD = {'<..', '<-', '<|-', '</-', '<~', '<|~',  '</~',
                '_<..',  '_<-', '_<|-', '_</-',  '_<~',  '_<|~', '_</~'}
    REVERSE_DICT = {
        '<..': '..>',
        '<-': '->', '<|-': '-|>', '</-': '-/>', '<~': '~>', '<|~': "~|>",  '</~': '~/>',
        '_<..': '_..>',  '_<-': '_->', '_<|-': '_-|>', '_</-': '_-/>',  '_<~': '_~>',  '_<|~': '_~|>', '_</~': '_~/>'
    }

    def __init__(self, connector: str, name: str, ctx: TokenContext) -> None:
        super().__init__(Element.Kind.ARC, name, ctx)

        self.connector = connector

        if self.connector not in Arc.VALID:
            raise KeyError(
                f"Connector `{connector}` is not supported. List of supported connectors: {Arc.VALID}")

    def _reverse_if_back(self) -> bool:
        """Reverse connector to forward direction.

        If connector was reversed, then returns True.
        """
        if self.connector in Arc.BACKWARD:
            self.connector = Arc.REVERSE_DICT[self.connector]
            return True

        return False

    def __repr__(self) -> str:
        return self._to_str(connector=self.connector)


class Link(Element):

    Value = Union[str, int, float]

    class Type(Enum):
        STRING = 0
        URL = 1

    def __init__(self, name: str, value: Value, type_: Type, ctx: TokenContext) -> None:
        super().__init__(Element.Kind.LINK, name, ctx)

        self.value = value
        self.type = type_

    def __repr__(self) -> str:
        return self._to_str(value=self.value, type=self.type.name)
