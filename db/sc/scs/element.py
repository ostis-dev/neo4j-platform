from enum import Enum
from typing import Union


class Element:

    class Kind(Enum):
        NODE = 1
        EDGE = 2
        ARC = 3
        LINK = 4

    def __init__(self, kind: Kind, name: str) -> None:
        self._kind = kind
        self._name = name

    @property
    def kind(self) -> Kind:
        return self._kind

    @property
    def name(self) -> str:
        return self._name

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(kind: {self.kind.name}, name: {self._name})"


class Node(Element):

    def __init__(self, name: str) -> None:
        super().__init__(kind=Element.Kind.NODE, name=name)


class Edge(Element):

    def __init__(self, name: str) -> None:
        super().__init__(Element.Kind.EDGE, name=name)


class Arc(Element):

    def __init__(self, name: str) -> None:
        super().__init__(Element.Kind.ARC, name=name)


class Link(Element):

    Value = Union[str, int, float]

    class Type(Enum):
        UNKNOWN = 0
        INT = 1
        FLOAT = 2
        STR = 3
        URL = 4

    def __init__(self, name: str, value: Value, type: Type) -> None:
        super().__init__(Element.Kind.LINK, name=name)

        self._value = value
        self._type = type

    @property
    def value(self) -> Value:
        return self._value

    @property
    def type(self) -> Type:
        return self._type
