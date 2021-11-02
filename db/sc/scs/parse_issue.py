from enum import Enum


class ParseIssue:
    class Type(Enum):
        WARNING = 1
        ERROR = 2

    def __init__(self, line: int, char_pos: int, token: str, msg: str, type: Type) -> None:
        self._line = line
        self._char_pos = char_pos
        self._token = token
        self._msg = msg
        self._type = type

    def __repr__(self) -> str:
        token = self._token if self._token is not None else ""
        return (f"{self._type.name}: {self._msg}. "
                f"Line {self._line}:{self._char_pos} - '{token}'")
