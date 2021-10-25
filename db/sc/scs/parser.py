import antlr4

from antlr4.error.ErrorListener import ErrorListener, ConsoleErrorListener

from enum import Enum
from typing import List

from ._parser import SCsLexerImpl, SCsParserImpl


class SCsParser:

    class Error:

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

    class SyntaxErrorListener(ErrorListener):

        def __init__(self) -> None:
            super().__init__()
            self._errors = []

        @property
        def errors(self):
            return self._errors

        def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
            error = SCsParser.Error(
                line=line,
                char_pos=column,
                offending_symbol=offendingSymbol,
                msg=msg,
                type=SCsParser.Error.Type.ERROR)

            self._errors.append(error)

    def __init__(self) -> None:
        self._error_listener = SCsParser.SyntaxErrorListener()

    @property
    def errors(self) -> List[Error]:
        """Returns list of errors"""
        return self._error_listener.errors

    def parse(self, data: str) -> bool:
        """Runs SCs-text parsing from string `data`.

        If there were any errors during parser, then returns `False`. `errors`
        list will contain all errors occured during parsing.
        """
        return self._parseImpl(antlr4.InputStream(data))

    def parseFile(self, file_path: str) -> bool:
        """Runs SCs-test parsing from file

        If there were any errors during parser, then returns `False`. `errors`
        list will contain all errors occured during parsing.
        """
        return self._parseImpl(antlr4.FileStream(file_path, encoding='utf-8'))

    def _parseImpl(self, stream: antlr4.InputStream) -> bool:

        lexer = SCsLexerImpl(input=stream)
        stream = antlr4.CommonTokenStream(lexer=lexer)
        parser = SCsParserImpl(input=stream)
        parser.addErrorListener(self._error_listener)
        # do not print errors to console
        parser.removeErrorListener(ConsoleErrorListener.INSTANCE)
        parser.syntax()

        return len(self.errors) == 0
