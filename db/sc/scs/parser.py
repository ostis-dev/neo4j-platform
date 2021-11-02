import antlr4

from antlr4.error.Errors import ParseCancellationException
from antlr4.error.ErrorListener import ErrorListener, ConsoleErrorListener
from antlr4.error.ErrorStrategy import BailErrorStrategy

from enum import Enum
from typing import List, Tuple


from .antlr import SCsLexerAntlr, SCsParserAntlr
from .parse_issue import ParseIssue
from .parser_impl import SCsParserImpl, Triple


class SCsParser:

    class SyntaxErrorListener(ErrorListener):

        def __init__(self) -> None:
            super().__init__()
            self._errors = []

        @property
        def errors(self):
            return self._errors

        def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
            error = ParseIssue(
                line=line,
                char_pos=column,
                token=e.offendingToken.text if e.offendingToken else None,
                msg=msg,
                type=ParseIssue.Type.ERROR)

            self._errors.append(error)

    def __init__(self) -> None:
        self._error_listener = SCsParser.SyntaxErrorListener()
        self._impl = SCsParserImpl()
        self._errors = []
        self._warnings = []

    @property
    def errors(self) -> List[ParseIssue]:
        """Returns list of errors"""
        return self._errors

    @property
    def warnings(self) -> List[ParseIssue]:
        """Returns list of warnings"""
        return self._warnings

    @property
    def triples(self) -> List[Triple]:
        """Returns list of parsed triples in format (src, edge, trg)"""
        return self._impl.triples

    @property
    def type_triples(self) -> List[Tuple]:
        """Returns list of parsed type triples in format (src, edge, trg).

        Source of each triple is a keynode that determines type of sc-element.
        """
        return self._impl.triples

    def has_errors(self) -> bool:
        return len(self.errors) > 0

    def has_warnings(self) -> bool:
        return len(self.warnings)

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

        lexer = SCsLexerAntlr(input=stream)
        lexer.addErrorListener(self._error_listener)
        lexer.removeErrorListener(ConsoleErrorListener.INSTANCE)

        stream = antlr4.CommonTokenStream(lexer=lexer)
        parser = SCsParserAntlr(input=stream)

        parser._impl = self._impl
        parser._errHandler = BailErrorStrategy()
        parser.addErrorListener(self._error_listener)
        # do not print errors to console
        parser.removeErrorListener(ConsoleErrorListener.INSTANCE)

        try:
            parser.syntax()
        except ParseCancellationException as ex:
            if len(self._error_listener.errors) + len(self._impl.errors) == 0:
                self._errors.append(ParseIssue(
                    0, 0, '', "Wasn't able to parse input", ParseIssue.Type.ERROR))

        self._errors.extend(self._error_listener.errors)
        self._errors.extend(self._impl.errors)

        self._warnings.extend(self._impl.warnings)

        return len(self.errors) == 0
