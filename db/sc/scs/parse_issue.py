from enum import Enum


class ParseIssue:
    class Type(Enum):
        WARNING = 1
        ERROR = 2

    def __init__(self, line: int, char_pos: int, offending_symbol: str, msg: str, type: Type) -> None:
        self._line = line
        self._char_pos = char_pos
        self._offending_symbol = offending_symbol
        self._msg = msg
        self._type = type

    def __repr__(self) -> str:
        return f"[{self._type.name}] {self._msg}. Line {self._line}:{self._char_pos}. Symbol: {self._offending_symbol}"
