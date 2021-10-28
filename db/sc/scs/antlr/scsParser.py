# Generated from sc/scs/scs.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


from sc.scs.types import *
from enum import Enum

def create_token_context(ctx: any) -> TokenContext:
	return TokenContext(line=ctx.line, column=ctx.column, text=ctx.text)

class ConnectorType:
	ARC = 0
	EDGE = 1


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3D")
        buf.write("\u00ed\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\3\2\5\2\66\n\2\3\2\3\2\3\2\3\3\3\3\3\3")
        buf.write("\7\3>\n\3\f\3\16\3A\13\3\3\3\3\3\3\3\3\4\3\4\3\4\3\5\3")
        buf.write("\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\5\6R\n\6\3\7\7\7U\n\7\f")
        buf.write("\7\16\7X\13\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\5\tb\n\t")
        buf.write("\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3")
        buf.write("\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\5")
        buf.write("\17{\n\17\3\17\3\17\3\17\3\17\3\20\3\20\5\20\u0083\n\20")
        buf.write("\3\20\3\20\3\20\5\20\u0088\n\20\3\20\7\20\u008b\n\20\f")
        buf.write("\20\16\20\u008e\13\20\3\20\3\20\3\21\3\21\3\21\3\21\3")
        buf.write("\21\3\21\5\21\u0098\n\21\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\5\23\u00ab\n\23\3\24\3\24\3\24\5\24\u00b0\n\24\3\24\3")
        buf.write("\24\3\24\3\24\5\24\u00b6\n\24\7\24\u00b8\n\24\f\24\16")
        buf.write("\24\u00bb\13\24\3\25\3\25\5\25\u00bf\n\25\3\25\3\25\3")
        buf.write("\25\3\26\3\26\3\26\3\26\6\26\u00c8\n\26\r\26\16\26\u00c9")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\5\30\u00d7\n\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3")
        buf.write("\31\7\31\u00e1\n\31\f\31\16\31\u00e4\13\31\3\32\3\32\3")
        buf.write("\32\6\32\u00e9\n\32\r\32\16\32\u00ea\3\32\2\2\33\2\4\6")
        buf.write("\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\2\6\3")
        buf.write("\2\4\r\3\2\16)\4\2**\67\67\3\2,/\2\u00eb\2\65\3\2\2\2")
        buf.write("\4:\3\2\2\2\6E\3\2\2\2\bH\3\2\2\2\nQ\3\2\2\2\fV\3\2\2")
        buf.write("\2\16[\3\2\2\2\20a\3\2\2\2\22c\3\2\2\2\24f\3\2\2\2\26")
        buf.write("i\3\2\2\2\30n\3\2\2\2\32q\3\2\2\2\34v\3\2\2\2\36\u0080")
        buf.write("\3\2\2\2 \u0097\3\2\2\2\"\u0099\3\2\2\2$\u00aa\3\2\2\2")
        buf.write("&\u00ac\3\2\2\2(\u00bc\3\2\2\2*\u00c3\3\2\2\2,\u00cd\3")
        buf.write("\2\2\2.\u00d4\3\2\2\2\60\u00dc\3\2\2\2\62\u00e8\3\2\2")
        buf.write("\2\64\66\7\3\2\2\65\64\3\2\2\2\65\66\3\2\2\2\66\67\3\2")
        buf.write("\2\2\678\7;\2\289\b\2\1\29\3\3\2\2\2:;\79\2\2;?\6\3\2")
        buf.write("\2<>\5\16\b\2=<\3\2\2\2>A\3\2\2\2?=\3\2\2\2?@\3\2\2\2")
        buf.write("@B\3\2\2\2A?\3\2\2\2BC\7:\2\2CD\b\3\1\2D\5\3\2\2\2EF\t")
        buf.write("\2\2\2FG\b\4\1\2G\7\3\2\2\2HI\t\3\2\2IJ\b\5\1\2J\t\3\2")
        buf.write("\2\2KL\5\6\4\2LM\b\6\1\2MR\3\2\2\2NO\5\b\5\2OP\b\6\1\2")
        buf.write("PR\3\2\2\2QK\3\2\2\2QN\3\2\2\2R\13\3\2\2\2SU\5\16\b\2")
        buf.write("TS\3\2\2\2UX\3\2\2\2VT\3\2\2\2VW\3\2\2\2WY\3\2\2\2XV\3")
        buf.write("\2\2\2YZ\7\2\2\3Z\r\3\2\2\2[\\\5\20\t\2\\]\7B\2\2]\17")
        buf.write("\3\2\2\2^b\5,\27\2_b\5\26\f\2`b\5\60\31\2a^\3\2\2\2a_")
        buf.write("\3\2\2\2a`\3\2\2\2b\21\3\2\2\2cd\78\2\2de\b\n\1\2e\23")
        buf.write("\3\2\2\2fg\t\4\2\2gh\b\13\1\2h\25\3\2\2\2ij\78\2\2jk\7")
        buf.write("+\2\2kl\5$\23\2lm\b\f\1\2m\27\3\2\2\2no\t\5\2\2op\b\r")
        buf.write("\1\2p\31\3\2\2\2qr\5\30\r\2rs\7C\2\2st\7\67\2\2tu\b\16")
        buf.write("\1\2u\33\3\2\2\2vw\7\60\2\2wx\5 \21\2xz\5\n\6\2y{\5\62")
        buf.write("\32\2zy\3\2\2\2z{\3\2\2\2{|\3\2\2\2|}\5 \21\2}~\7\61\2")
        buf.write("\2~\177\b\17\1\2\177\35\3\2\2\2\u0080\u0082\7\62\2\2\u0081")
        buf.write("\u0083\5\62\32\2\u0082\u0081\3\2\2\2\u0082\u0083\3\2\2")
        buf.write("\2\u0083\u0084\3\2\2\2\u0084\u008c\5$\23\2\u0085\u0087")
        buf.write("\7\63\2\2\u0086\u0088\5\62\32\2\u0087\u0086\3\2\2\2\u0087")
        buf.write("\u0088\3\2\2\2\u0088\u0089\3\2\2\2\u0089\u008b\5$\23\2")
        buf.write("\u008a\u0085\3\2\2\2\u008b\u008e\3\2\2\2\u008c\u008a\3")
        buf.write("\2\2\2\u008c\u008d\3\2\2\2\u008d\u008f\3\2\2\2\u008e\u008c")
        buf.write("\3\2\2\2\u008f\u0090\7\64\2\2\u0090\37\3\2\2\2\u0091\u0092")
        buf.write("\5\22\n\2\u0092\u0093\b\21\1\2\u0093\u0098\3\2\2\2\u0094")
        buf.write("\u0095\5\24\13\2\u0095\u0096\b\21\1\2\u0096\u0098\3\2")
        buf.write("\2\2\u0097\u0091\3\2\2\2\u0097\u0094\3\2\2\2\u0098!\3")
        buf.write("\2\2\2\u0099\u009a\7<\2\2\u009a\u009b\b\22\1\2\u009b#")
        buf.write("\3\2\2\2\u009c\u009d\5 \21\2\u009d\u009e\b\23\1\2\u009e")
        buf.write("\u00ab\3\2\2\2\u009f\u00a0\5\34\17\2\u00a0\u00a1\b\23")
        buf.write("\1\2\u00a1\u00ab\3\2\2\2\u00a2\u00ab\5\36\20\2\u00a3\u00ab")
        buf.write("\5\4\3\2\u00a4\u00a5\5\2\2\2\u00a5\u00a6\b\23\1\2\u00a6")
        buf.write("\u00ab\3\2\2\2\u00a7\u00a8\5\"\22\2\u00a8\u00a9\b\23\1")
        buf.write("\2\u00a9\u00ab\3\2\2\2\u00aa\u009c\3\2\2\2\u00aa\u009f")
        buf.write("\3\2\2\2\u00aa\u00a2\3\2\2\2\u00aa\u00a3\3\2\2\2\u00aa")
        buf.write("\u00a4\3\2\2\2\u00aa\u00a7\3\2\2\2\u00ab%\3\2\2\2\u00ac")
        buf.write("\u00ad\5$\23\2\u00ad\u00af\b\24\1\2\u00ae\u00b0\5*\26")
        buf.write("\2\u00af\u00ae\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00b9")
        buf.write("\3\2\2\2\u00b1\u00b2\7\63\2\2\u00b2\u00b3\5$\23\2\u00b3")
        buf.write("\u00b5\b\24\1\2\u00b4\u00b6\5*\26\2\u00b5\u00b4\3\2\2")
        buf.write("\2\u00b5\u00b6\3\2\2\2\u00b6\u00b8\3\2\2\2\u00b7\u00b1")
        buf.write("\3\2\2\2\u00b8\u00bb\3\2\2\2\u00b9\u00b7\3\2\2\2\u00b9")
        buf.write("\u00ba\3\2\2\2\u00ba\'\3\2\2\2\u00bb\u00b9\3\2\2\2\u00bc")
        buf.write("\u00be\5\n\6\2\u00bd\u00bf\5\62\32\2\u00be\u00bd\3\2\2")
        buf.write("\2\u00be\u00bf\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0\u00c1")
        buf.write("\5&\24\2\u00c1\u00c2\b\25\1\2\u00c2)\3\2\2\2\u00c3\u00c7")
        buf.write("\7\65\2\2\u00c4\u00c5\5(\25\2\u00c5\u00c6\7B\2\2\u00c6")
        buf.write("\u00c8\3\2\2\2\u00c7\u00c4\3\2\2\2\u00c8\u00c9\3\2\2\2")
        buf.write("\u00c9\u00c7\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca\u00cb\3")
        buf.write("\2\2\2\u00cb\u00cc\7\66\2\2\u00cc+\3\2\2\2\u00cd\u00ce")
        buf.write("\5\32\16\2\u00ce\u00cf\7D\2\2\u00cf\u00d0\5\32\16\2\u00d0")
        buf.write("\u00d1\7D\2\2\u00d1\u00d2\5\32\16\2\u00d2\u00d3\b\27\1")
        buf.write("\2\u00d3-\3\2\2\2\u00d4\u00d6\5\n\6\2\u00d5\u00d7\5\62")
        buf.write("\32\2\u00d6\u00d5\3\2\2\2\u00d6\u00d7\3\2\2\2\u00d7\u00d8")
        buf.write("\3\2\2\2\u00d8\u00d9\5&\24\2\u00d9\u00da\3\2\2\2\u00da")
        buf.write("\u00db\b\30\1\2\u00db/\3\2\2\2\u00dc\u00dd\5$\23\2\u00dd")
        buf.write("\u00e2\5.\30\2\u00de\u00df\7\63\2\2\u00df\u00e1\5.\30")
        buf.write("\2\u00e0\u00de\3\2\2\2\u00e1\u00e4\3\2\2\2\u00e2\u00e0")
        buf.write("\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3\61\3\2\2\2\u00e4\u00e2")
        buf.write("\3\2\2\2\u00e5\u00e6\7\67\2\2\u00e6\u00e7\7=\2\2\u00e7")
        buf.write("\u00e9\b\32\1\2\u00e8\u00e5\3\2\2\2\u00e9\u00ea\3\2\2")
        buf.write("\2\u00ea\u00e8\3\2\2\2\u00ea\u00eb\3\2\2\2\u00eb\63\3")
        buf.write("\2\2\2\25\65?QVaz\u0082\u0087\u008c\u0097\u00aa\u00af")
        buf.write("\u00b5\u00b9\u00be\u00c9\u00d6\u00e2\u00ea")
        return buf.getvalue()


class scsParser ( Parser ):

    grammarFileName = "scs.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'_'", "'<>'", "'<=>'", "'_<>'", "'_<=>'", 
                     "'>'", "'<'", "'=>'", "'<='", "'_=>'", "'_<='", "'..>'", 
                     "'<..'", "'->'", "'<-'", "'-|>'", "'<|-'", "'-/>'", 
                     "'</-'", "'~>'", "'<~'", "'~|>'", "'<|~'", "'~/>'", 
                     "'</~'", "'_..>'", "'_<..'", "'_->'", "'_<-'", "'_-|>'", 
                     "'_<|-'", "'_-/>'", "'_</-'", "'_~>'", "'_<~'", "'_~|>'", 
                     "'_<|~'", "'_~/>'", "'_</~'", "'...'", "'='", "'sc_node'", 
                     "'sc_link'", "'sc_edge'", "'sc_arc'", "'('", "')'", 
                     "'{'", "';'", "'}'", "'(*'", "'*)'", "<INVALID>", "<INVALID>", 
                     "'[*'", "'*]'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "';;'", "'#'", "'|'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID_SYSTEM", "ALIAS_SYMBOLS", "CONTOUR_BEGIN", 
                      "CONTOUR_END", "CONTENT_BODY", "LINK", "EDGE_ATTR", 
                      "LINE_TERMINATOR", "LINE_COMMENT", "MULTINE_COMMENT", 
                      "WS", "SENTENCE_SEP", "LVL1_TYPE_SEP", "LVL1_ITEM_SEP" ]

    RULE_content = 0
    RULE_contour = 1
    RULE_connector_edge = 2
    RULE_connector_arc = 3
    RULE_connector = 4
    RULE_syntax = 5
    RULE_sentence_wrap = 6
    RULE_sentence = 7
    RULE_ifdf_alias = 8
    RULE_idtf_system = 9
    RULE_sentence_assign = 10
    RULE_idtf_lvl1_preffix = 11
    RULE_idtf_lvl1 = 12
    RULE_idtf_edge = 13
    RULE_idtf_set = 14
    RULE_idtf_atomic = 15
    RULE_idtf_url = 16
    RULE_idtf_common = 17
    RULE_idtf_list = 18
    RULE_internal_sentence = 19
    RULE_internal_sentence_list = 20
    RULE_sentence_lvl1 = 21
    RULE_sentence_lvl_4_list_item = 22
    RULE_sentence_lvl_common = 23
    RULE_attr_list = 24

    ruleNames =  [ "content", "contour", "connector_edge", "connector_arc", 
                   "connector", "syntax", "sentence_wrap", "sentence", "ifdf_alias", 
                   "idtf_system", "sentence_assign", "idtf_lvl1_preffix", 
                   "idtf_lvl1", "idtf_edge", "idtf_set", "idtf_atomic", 
                   "idtf_url", "idtf_common", "idtf_list", "internal_sentence", 
                   "internal_sentence_list", "sentence_lvl1", "sentence_lvl_4_list_item", 
                   "sentence_lvl_common", "attr_list" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    T__41=42
    T__42=43
    T__43=44
    T__44=45
    T__45=46
    T__46=47
    T__47=48
    T__48=49
    T__49=50
    T__50=51
    T__51=52
    ID_SYSTEM=53
    ALIAS_SYMBOLS=54
    CONTOUR_BEGIN=55
    CONTOUR_END=56
    CONTENT_BODY=57
    LINK=58
    EDGE_ATTR=59
    LINE_TERMINATOR=60
    LINE_COMMENT=61
    MULTINE_COMMENT=62
    WS=63
    SENTENCE_SEP=64
    LVL1_TYPE_SEP=65
    LVL1_ITEM_SEP=66

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ContentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.el = None
            self._CONTENT_BODY = None # Token

        def CONTENT_BODY(self):
            return self.getToken(scsParser.CONTENT_BODY, 0)

        def getRuleIndex(self):
            return scsParser.RULE_content




    def content(self):

        localctx = scsParser.ContentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_content)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==scsParser.T__0:
                self.state = 50
                self.match(scsParser.T__0)


            self.state = 53
            localctx._CONTENT_BODY = self.match(scsParser.CONTENT_BODY)

            localctx.el = self._impl.create_link(create_token_context(localctx._CONTENT_BODY), (None if localctx._CONTENT_BODY is None else localctx._CONTENT_BODY.text)[1:-1], Link.Type.STRING)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContourContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTOUR_BEGIN(self):
            return self.getToken(scsParser.CONTOUR_BEGIN, 0)

        def CONTOUR_END(self):
            return self.getToken(scsParser.CONTOUR_END, 0)

        def sentence_wrap(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(scsParser.Sentence_wrapContext)
            else:
                return self.getTypedRuleContext(scsParser.Sentence_wrapContext,i)


        def getRuleIndex(self):
            return scsParser.RULE_contour




    def contour(self):

        localctx = scsParser.ContourContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_contour)
        count = 1
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(scsParser.CONTOUR_BEGIN)
            self.state = 57
            if not count > 0:
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "count > 0")

            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << scsParser.T__0) | (1 << scsParser.T__39) | (1 << scsParser.T__41) | (1 << scsParser.T__42) | (1 << scsParser.T__43) | (1 << scsParser.T__44) | (1 << scsParser.T__45) | (1 << scsParser.T__47) | (1 << scsParser.ID_SYSTEM) | (1 << scsParser.ALIAS_SYMBOLS) | (1 << scsParser.CONTOUR_BEGIN) | (1 << scsParser.CONTENT_BODY) | (1 << scsParser.LINK))) != 0):
                self.state = 58
                self.sentence_wrap()
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 64
            self.match(scsParser.CONTOUR_END)

            count -= 1
            if count == 0:
                pass
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Connector_edgeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.el = None
            self.symbol = None # Token


        def getRuleIndex(self):
            return scsParser.RULE_connector_edge




    def connector_edge(self):

        localctx = scsParser.Connector_edgeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_connector_edge)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            localctx.symbol = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << scsParser.T__1) | (1 << scsParser.T__2) | (1 << scsParser.T__3) | (1 << scsParser.T__4) | (1 << scsParser.T__5) | (1 << scsParser.T__6) | (1 << scsParser.T__7) | (1 << scsParser.T__8) | (1 << scsParser.T__9) | (1 << scsParser.T__10))) != 0)):
                localctx.symbol = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            localctx.el = self._impl.create_edge(create_token_context(localctx.symbol), (None if localctx.symbol is None else localctx.symbol.text))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Connector_arcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.el = None
            self.symbol = None # Token


        def getRuleIndex(self):
            return scsParser.RULE_connector_arc




    def connector_arc(self):

        localctx = scsParser.Connector_arcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_connector_arc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            localctx.symbol = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << scsParser.T__11) | (1 << scsParser.T__12) | (1 << scsParser.T__13) | (1 << scsParser.T__14) | (1 << scsParser.T__15) | (1 << scsParser.T__16) | (1 << scsParser.T__17) | (1 << scsParser.T__18) | (1 << scsParser.T__19) | (1 << scsParser.T__20) | (1 << scsParser.T__21) | (1 << scsParser.T__22) | (1 << scsParser.T__23) | (1 << scsParser.T__24) | (1 << scsParser.T__25) | (1 << scsParser.T__26) | (1 << scsParser.T__27) | (1 << scsParser.T__28) | (1 << scsParser.T__29) | (1 << scsParser.T__30) | (1 << scsParser.T__31) | (1 << scsParser.T__32) | (1 << scsParser.T__33) | (1 << scsParser.T__34) | (1 << scsParser.T__35) | (1 << scsParser.T__36) | (1 << scsParser.T__37) | (1 << scsParser.T__38))) != 0)):
                localctx.symbol = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            localctx.el = self._impl.create_arc(create_token_context(localctx.symbol), (None if localctx.symbol is None else localctx.symbol.text))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConnectorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.el = None
            self._connector_edge = None # Connector_edgeContext
            self._connector_arc = None # Connector_arcContext

        def connector_edge(self):
            return self.getTypedRuleContext(scsParser.Connector_edgeContext,0)


        def connector_arc(self):
            return self.getTypedRuleContext(scsParser.Connector_arcContext,0)


        def getRuleIndex(self):
            return scsParser.RULE_connector




    def connector(self):

        localctx = scsParser.ConnectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_connector)
        try:
            self.state = 79
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [scsParser.T__1, scsParser.T__2, scsParser.T__3, scsParser.T__4, scsParser.T__5, scsParser.T__6, scsParser.T__7, scsParser.T__8, scsParser.T__9, scsParser.T__10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 73
                localctx._connector_edge = self.connector_edge()
                localctx.el = localctx._connector_edge.el
                pass
            elif token in [scsParser.T__11, scsParser.T__12, scsParser.T__13, scsParser.T__14, scsParser.T__15, scsParser.T__16, scsParser.T__17, scsParser.T__18, scsParser.T__19, scsParser.T__20, scsParser.T__21, scsParser.T__22, scsParser.T__23, scsParser.T__24, scsParser.T__25, scsParser.T__26, scsParser.T__27, scsParser.T__28, scsParser.T__29, scsParser.T__30, scsParser.T__31, scsParser.T__32, scsParser.T__33, scsParser.T__34, scsParser.T__35, scsParser.T__36, scsParser.T__37, scsParser.T__38]:
                self.enterOuterAlt(localctx, 2)
                self.state = 76
                localctx._connector_arc = self.connector_arc()
                localctx.el = localctx._connector_arc.el
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SyntaxContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(scsParser.EOF, 0)

        def sentence_wrap(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(scsParser.Sentence_wrapContext)
            else:
                return self.getTypedRuleContext(scsParser.Sentence_wrapContext,i)


        def getRuleIndex(self):
            return scsParser.RULE_syntax




    def syntax(self):

        localctx = scsParser.SyntaxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_syntax)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << scsParser.T__0) | (1 << scsParser.T__39) | (1 << scsParser.T__41) | (1 << scsParser.T__42) | (1 << scsParser.T__43) | (1 << scsParser.T__44) | (1 << scsParser.T__45) | (1 << scsParser.T__47) | (1 << scsParser.ID_SYSTEM) | (1 << scsParser.ALIAS_SYMBOLS) | (1 << scsParser.CONTOUR_BEGIN) | (1 << scsParser.CONTENT_BODY) | (1 << scsParser.LINK))) != 0):
                self.state = 81
                self.sentence_wrap()
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 87
            self.match(scsParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sentence_wrapContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sentence(self):
            return self.getTypedRuleContext(scsParser.SentenceContext,0)


        def SENTENCE_SEP(self):
            return self.getToken(scsParser.SENTENCE_SEP, 0)

        def getRuleIndex(self):
            return scsParser.RULE_sentence_wrap




    def sentence_wrap(self):

        localctx = scsParser.Sentence_wrapContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_sentence_wrap)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.sentence()
            self.state = 90
            self.match(scsParser.SENTENCE_SEP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sentence_lvl1(self):
            return self.getTypedRuleContext(scsParser.Sentence_lvl1Context,0)


        def sentence_assign(self):
            return self.getTypedRuleContext(scsParser.Sentence_assignContext,0)


        def sentence_lvl_common(self):
            return self.getTypedRuleContext(scsParser.Sentence_lvl_commonContext,0)


        def getRuleIndex(self):
            return scsParser.RULE_sentence




    def sentence(self):

        localctx = scsParser.SentenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_sentence)
        try:
            self.state = 95
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 92
                self.sentence_lvl1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 93
                self.sentence_assign()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 94
                self.sentence_lvl_common()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ifdf_aliasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.el = None
            self._ALIAS_SYMBOLS = None # Token

        def ALIAS_SYMBOLS(self):
            return self.getToken(scsParser.ALIAS_SYMBOLS, 0)

        def getRuleIndex(self):
            return scsParser.RULE_ifdf_alias




    def ifdf_alias(self):

        localctx = scsParser.Ifdf_aliasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_ifdf_alias)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            localctx._ALIAS_SYMBOLS = self.match(scsParser.ALIAS_SYMBOLS)

            localctx.el = self._impl.create_alias(create_token_context(localctx._ALIAS_SYMBOLS))

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Idtf_systemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.el = None
            self.value = None # Token

        def ID_SYSTEM(self):
            return self.getToken(scsParser.ID_SYSTEM, 0)

        def getRuleIndex(self):
            return scsParser.RULE_idtf_system




    def idtf_system(self):

        localctx = scsParser.Idtf_systemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_idtf_system)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            localctx.value = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==scsParser.T__39 or _la==scsParser.ID_SYSTEM):
                localctx.value = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()

            localctx.el = self._impl.create_node(create_token_context(localctx.value))

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sentence_assignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ALIAS_SYMBOLS = None # Token
            self._idtf_common = None # Idtf_commonContext

        def ALIAS_SYMBOLS(self):
            return self.getToken(scsParser.ALIAS_SYMBOLS, 0)

        def idtf_common(self):
            return self.getTypedRuleContext(scsParser.Idtf_commonContext,0)


        def getRuleIndex(self):
            return scsParser.RULE_sentence_assign




    def sentence_assign(self):

        localctx = scsParser.Sentence_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_sentence_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            localctx._ALIAS_SYMBOLS = self.match(scsParser.ALIAS_SYMBOLS)
            self.state = 104
            self.match(scsParser.T__40)
            self.state = 105
            localctx._idtf_common = self.idtf_common()


            context = create_token_context(localctx._ALIAS_SYMBOLS)
            self._impl.define_alias(self._impl.create_alias(context), localctx._idtf_common.el)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Idtf_lvl1_preffixContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.context = None
            self.value = None # Token


        def getRuleIndex(self):
            return scsParser.RULE_idtf_lvl1_preffix




    def idtf_lvl1_preffix(self):

        localctx = scsParser.Idtf_lvl1_preffixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_idtf_lvl1_preffix)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            localctx.value = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << scsParser.T__41) | (1 << scsParser.T__42) | (1 << scsParser.T__43) | (1 << scsParser.T__44))) != 0)):
                localctx.value = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()

            localctx.context = create_token_context(localctx.value)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Idtf_lvl1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.el = None
            self._idtf_lvl1_preffix = None # Idtf_lvl1_preffixContext
            self._ID_SYSTEM = None # Token

        def idtf_lvl1_preffix(self):
            return self.getTypedRuleContext(scsParser.Idtf_lvl1_preffixContext,0)


        def LVL1_TYPE_SEP(self):
            return self.getToken(scsParser.LVL1_TYPE_SEP, 0)

        def ID_SYSTEM(self):
            return self.getToken(scsParser.ID_SYSTEM, 0)

        def getRuleIndex(self):
            return scsParser.RULE_idtf_lvl1




    def idtf_lvl1(self):

        localctx = scsParser.Idtf_lvl1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_idtf_lvl1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            localctx._idtf_lvl1_preffix = self.idtf_lvl1_preffix()
            self.state = 112
            self.match(scsParser.LVL1_TYPE_SEP)
            self.state = 113
            localctx._ID_SYSTEM = self.match(scsParser.ID_SYSTEM)

            context = create_token_context(localctx._ID_SYSTEM)
            localctx.el = self._impl._processIdtfLevel1(context, (None if localctx._idtf_lvl1_preffix is None else self._input.getText(localctx._idtf_lvl1_preffix.start,localctx._idtf_lvl1_preffix.stop)))

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Idtf_edgeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.el = None
            self.src = None # Idtf_atomicContext
            self._connector = None # ConnectorContext
            self.attr = None # Attr_listContext
            self.trg = None # Idtf_atomicContext

        def connector(self):
            return self.getTypedRuleContext(scsParser.ConnectorContext,0)


        def idtf_atomic(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(scsParser.Idtf_atomicContext)
            else:
                return self.getTypedRuleContext(scsParser.Idtf_atomicContext,i)


        def attr_list(self):
            return self.getTypedRuleContext(scsParser.Attr_listContext,0)


        def getRuleIndex(self):
            return scsParser.RULE_idtf_edge




    def idtf_edge(self):

        localctx = scsParser.Idtf_edgeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_idtf_edge)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(scsParser.T__45)
            self.state = 117
            localctx.src = self.idtf_atomic()
            self.state = 118
            localctx._connector = self.connector()
            self.state = 120
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 119
                localctx.attr = self.attr_list()


            self.state = 122
            localctx.trg = self.idtf_atomic()
            self.state = 123
            self.match(scsParser.T__46)

            self._impl.append_triple(localctx.src.el, localctx._connector.el, localctx.trg.el)
            localctx.el = localctx._connector.el

            if localctx.attr is not None:
            	for a, e in localctx.attr.items:
            		self._impl.append_triple(a, e, localctx._connector.el)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Idtf_setContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idtf_common(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(scsParser.Idtf_commonContext)
            else:
                return self.getTypedRuleContext(scsParser.Idtf_commonContext,i)


        def attr_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(scsParser.Attr_listContext)
            else:
                return self.getTypedRuleContext(scsParser.Attr_listContext,i)


        def getRuleIndex(self):
            return scsParser.RULE_idtf_set




    def idtf_set(self):

        localctx = scsParser.Idtf_setContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_idtf_set)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(scsParser.T__47)
            self.state = 128
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 127
                self.attr_list()


            self.state = 130
            self.idtf_common()
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==scsParser.T__48:
                self.state = 131
                self.match(scsParser.T__48)
                self.state = 133
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 132
                    self.attr_list()


                self.state = 135
                self.idtf_common()
                self.state = 140
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 141
            self.match(scsParser.T__49)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Idtf_atomicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.el = None
            self._ifdf_alias = None # Ifdf_aliasContext
            self._idtf_system = None # Idtf_systemContext

        def ifdf_alias(self):
            return self.getTypedRuleContext(scsParser.Ifdf_aliasContext,0)


        def idtf_system(self):
            return self.getTypedRuleContext(scsParser.Idtf_systemContext,0)


        def getRuleIndex(self):
            return scsParser.RULE_idtf_atomic




    def idtf_atomic(self):

        localctx = scsParser.Idtf_atomicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_idtf_atomic)
        try:
            self.state = 149
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [scsParser.ALIAS_SYMBOLS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                localctx._ifdf_alias = self.ifdf_alias()
                localctx.el = localctx._ifdf_alias.el
                pass
            elif token in [scsParser.T__39, scsParser.ID_SYSTEM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                localctx._idtf_system = self.idtf_system()
                localctx.el = localctx._idtf_system.el
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Idtf_urlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.el = None
            self._LINK = None # Token

        def LINK(self):
            return self.getToken(scsParser.LINK, 0)

        def getRuleIndex(self):
            return scsParser.RULE_idtf_url




    def idtf_url(self):

        localctx = scsParser.Idtf_urlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_idtf_url)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            localctx._LINK = self.match(scsParser.LINK)

            context = create_token_context(localctx._LINK)
            localctx.el = self._impl.create_link(context, (None if localctx._LINK is None else localctx._LINK.text)[1:-1], Link.Type.URL)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Idtf_commonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.el = None
            self._idtf_atomic = None # Idtf_atomicContext
            self._idtf_edge = None # Idtf_edgeContext
            self._content = None # ContentContext
            self._idtf_url = None # Idtf_urlContext

        def idtf_atomic(self):
            return self.getTypedRuleContext(scsParser.Idtf_atomicContext,0)


        def idtf_edge(self):
            return self.getTypedRuleContext(scsParser.Idtf_edgeContext,0)


        def idtf_set(self):
            return self.getTypedRuleContext(scsParser.Idtf_setContext,0)


        def contour(self):
            return self.getTypedRuleContext(scsParser.ContourContext,0)


        def content(self):
            return self.getTypedRuleContext(scsParser.ContentContext,0)


        def idtf_url(self):
            return self.getTypedRuleContext(scsParser.Idtf_urlContext,0)


        def getRuleIndex(self):
            return scsParser.RULE_idtf_common




    def idtf_common(self):

        localctx = scsParser.Idtf_commonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_idtf_common)
        try:
            self.state = 168
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [scsParser.T__39, scsParser.ID_SYSTEM, scsParser.ALIAS_SYMBOLS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                localctx._idtf_atomic = self.idtf_atomic()
                localctx.el = localctx._idtf_atomic.el
                pass
            elif token in [scsParser.T__45]:
                self.enterOuterAlt(localctx, 2)
                self.state = 157
                localctx._idtf_edge = self.idtf_edge()
                localctx.el = localctx._idtf_edge.el
                pass
            elif token in [scsParser.T__47]:
                self.enterOuterAlt(localctx, 3)
                self.state = 160
                self.idtf_set()
                pass
            elif token in [scsParser.CONTOUR_BEGIN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 161
                self.contour()
                pass
            elif token in [scsParser.T__0, scsParser.CONTENT_BODY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 162
                localctx._content = self.content()
                localctx.el = localctx._content.el
                pass
            elif token in [scsParser.LINK]:
                self.enterOuterAlt(localctx, 6)
                self.state = 165
                localctx._idtf_url = self.idtf_url()
                localctx.el = localctx._idtf_url.el
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Idtf_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.items = None
            self.first = None # Idtf_commonContext
            self.second = None # Idtf_commonContext

        def idtf_common(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(scsParser.Idtf_commonContext)
            else:
                return self.getTypedRuleContext(scsParser.Idtf_commonContext,i)


        def internal_sentence_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(scsParser.Internal_sentence_listContext)
            else:
                return self.getTypedRuleContext(scsParser.Internal_sentence_listContext,i)


        def getRuleIndex(self):
            return scsParser.RULE_idtf_list




    def idtf_list(self):

        localctx = scsParser.Idtf_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_idtf_list)
        localctx.items = []
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            localctx.first = self.idtf_common()
            localctx.items.append(localctx.first.el)
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==scsParser.T__50:
                self.state = 172
                self.internal_sentence_list(localctx.first.el)


            self.state = 183
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 175
                    self.match(scsParser.T__48)
                    self.state = 176
                    localctx.second = self.idtf_common()
                    localctx.items.append(localctx.second.el)
                    self.state = 179
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==scsParser.T__50:
                        self.state = 178
                        self.internal_sentence_list(localctx.first.el)

             
                self.state = 185
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Internal_sentenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, src:Element=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.src = None
            self.c = None # ConnectorContext
            self.attr = None # Attr_listContext
            self.target = None # Idtf_listContext
            self.src = src

        def connector(self):
            return self.getTypedRuleContext(scsParser.ConnectorContext,0)


        def idtf_list(self):
            return self.getTypedRuleContext(scsParser.Idtf_listContext,0)


        def attr_list(self):
            return self.getTypedRuleContext(scsParser.Attr_listContext,0)


        def getRuleIndex(self):
            return scsParser.RULE_internal_sentence




    def internal_sentence(self, src:Element):

        localctx = scsParser.Internal_sentenceContext(self, self._ctx, self.state, src)
        self.enterRule(localctx, 38, self.RULE_internal_sentence)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            localctx.c = self.connector()
            self.state = 188
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 187
                localctx.attr = self.attr_list()


            self.state = 190
            localctx.target = self.idtf_list()

            for t in localctx.target.items:
            	edge = None
            	if isinstance(localctx.c.el, Edge):
            		edge = self._impl.create_edge(localctx.c.el.ctx, localctx.c.el.connector)
            	else:
            		edge = self._impl.create_arc(localctx.c.el.ctx, localctx.c.el.connector)
            	self._impl.append_triple(localctx.src.el, edge, t)
            	if localctx.attr is not None:
            		for a, e in localctx.attr.items:
            			self._impl.append_triple(a, e, edge)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Internal_sentence_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, src:Element=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.src = None
            self.src = src

        def internal_sentence(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(scsParser.Internal_sentenceContext)
            else:
                return self.getTypedRuleContext(scsParser.Internal_sentenceContext,i)


        def SENTENCE_SEP(self, i:int=None):
            if i is None:
                return self.getTokens(scsParser.SENTENCE_SEP)
            else:
                return self.getToken(scsParser.SENTENCE_SEP, i)

        def getRuleIndex(self):
            return scsParser.RULE_internal_sentence_list




    def internal_sentence_list(self, src:Element):

        localctx = scsParser.Internal_sentence_listContext(self, self._ctx, self.state, src)
        self.enterRule(localctx, 40, self.RULE_internal_sentence_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.match(scsParser.T__50)
            self.state = 197 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 194
                self.internal_sentence(src)
                self.state = 195
                self.match(scsParser.SENTENCE_SEP)
                self.state = 199 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << scsParser.T__1) | (1 << scsParser.T__2) | (1 << scsParser.T__3) | (1 << scsParser.T__4) | (1 << scsParser.T__5) | (1 << scsParser.T__6) | (1 << scsParser.T__7) | (1 << scsParser.T__8) | (1 << scsParser.T__9) | (1 << scsParser.T__10) | (1 << scsParser.T__11) | (1 << scsParser.T__12) | (1 << scsParser.T__13) | (1 << scsParser.T__14) | (1 << scsParser.T__15) | (1 << scsParser.T__16) | (1 << scsParser.T__17) | (1 << scsParser.T__18) | (1 << scsParser.T__19) | (1 << scsParser.T__20) | (1 << scsParser.T__21) | (1 << scsParser.T__22) | (1 << scsParser.T__23) | (1 << scsParser.T__24) | (1 << scsParser.T__25) | (1 << scsParser.T__26) | (1 << scsParser.T__27) | (1 << scsParser.T__28) | (1 << scsParser.T__29) | (1 << scsParser.T__30) | (1 << scsParser.T__31) | (1 << scsParser.T__32) | (1 << scsParser.T__33) | (1 << scsParser.T__34) | (1 << scsParser.T__35) | (1 << scsParser.T__36) | (1 << scsParser.T__37) | (1 << scsParser.T__38))) != 0)):
                    break

            self.state = 201
            self.match(scsParser.T__51)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sentence_lvl1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.src = None # Idtf_lvl1Context
            self.edge = None # Idtf_lvl1Context
            self.trg = None # Idtf_lvl1Context

        def LVL1_ITEM_SEP(self, i:int=None):
            if i is None:
                return self.getTokens(scsParser.LVL1_ITEM_SEP)
            else:
                return self.getToken(scsParser.LVL1_ITEM_SEP, i)

        def idtf_lvl1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(scsParser.Idtf_lvl1Context)
            else:
                return self.getTypedRuleContext(scsParser.Idtf_lvl1Context,i)


        def getRuleIndex(self):
            return scsParser.RULE_sentence_lvl1




    def sentence_lvl1(self):

        localctx = scsParser.Sentence_lvl1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_sentence_lvl1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            localctx.src = self.idtf_lvl1()
            self.state = 204
            self.match(scsParser.LVL1_ITEM_SEP)
            self.state = 205
            localctx.edge = self.idtf_lvl1()
            self.state = 206
            self.match(scsParser.LVL1_ITEM_SEP)
            self.state = 207
            localctx.trg = self.idtf_lvl1()

            self._impl.append_triple(localctx.src.el, localctx.edge.el, localctx.trg.el)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sentence_lvl_4_list_itemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, src:Element=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.src = None
            self.c = None # ConnectorContext
            self.attr = None # Attr_listContext
            self.target = None # Idtf_listContext
            self.src = src

        def connector(self):
            return self.getTypedRuleContext(scsParser.ConnectorContext,0)


        def idtf_list(self):
            return self.getTypedRuleContext(scsParser.Idtf_listContext,0)


        def attr_list(self):
            return self.getTypedRuleContext(scsParser.Attr_listContext,0)


        def getRuleIndex(self):
            return scsParser.RULE_sentence_lvl_4_list_item




    def sentence_lvl_4_list_item(self, src:Element):

        localctx = scsParser.Sentence_lvl_4_list_itemContext(self, self._ctx, self.state, src)
        self.enterRule(localctx, 44, self.RULE_sentence_lvl_4_list_item)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            localctx.c = self.connector()
            self.state = 212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 211
                localctx.attr = self.attr_list()


            self.state = 214
            localctx.target = self.idtf_list()

            for t in localctx.target.items:
            	edge = None
            	if isinstance(localctx.c.el, Edge):
            		edge = self._impl.create_edge(localctx.c.el.ctx, localctx.c.el.connector)
            	else:
            		edge = self._impl.create_arc(localctx.c.el.ctx, localctx.c.el.connector)

            	self._impl.append_triple(localctx.src, edge, t)
            	if localctx.attr is not None:
            		for a, e in localctx.attr.items:
            			self._impl.append_triple(a, e, edge)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sentence_lvl_commonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._idtf_common = None # Idtf_commonContext

        def idtf_common(self):
            return self.getTypedRuleContext(scsParser.Idtf_commonContext,0)


        def sentence_lvl_4_list_item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(scsParser.Sentence_lvl_4_list_itemContext)
            else:
                return self.getTypedRuleContext(scsParser.Sentence_lvl_4_list_itemContext,i)


        def getRuleIndex(self):
            return scsParser.RULE_sentence_lvl_common




    def sentence_lvl_common(self):

        localctx = scsParser.Sentence_lvl_commonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_sentence_lvl_common)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            localctx._idtf_common = self.idtf_common()
            self.state = 219
            self.sentence_lvl_4_list_item(localctx._idtf_common.el)
            self.state = 224
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==scsParser.T__48:
                self.state = 220
                self.match(scsParser.T__48)
                self.state = 221
                self.sentence_lvl_4_list_item(localctx._idtf_common.el)
                self.state = 226
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.items = None
            self._ID_SYSTEM = None # Token
            self._EDGE_ATTR = None # Token

        def ID_SYSTEM(self, i:int=None):
            if i is None:
                return self.getTokens(scsParser.ID_SYSTEM)
            else:
                return self.getToken(scsParser.ID_SYSTEM, i)

        def EDGE_ATTR(self, i:int=None):
            if i is None:
                return self.getTokens(scsParser.EDGE_ATTR)
            else:
                return self.getToken(scsParser.EDGE_ATTR, i)

        def getRuleIndex(self):
            return scsParser.RULE_attr_list




    def attr_list(self):

        localctx = scsParser.Attr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_attr_list)
        localctx.items = []
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 227
                    localctx._ID_SYSTEM = self.match(scsParser.ID_SYSTEM)
                    self.state = 228
                    localctx._EDGE_ATTR = self.match(scsParser.EDGE_ATTR)

                    node = self._impl.create_node(create_token_context(localctx._ID_SYSTEM))
                    edge = None
                    connector = "->" if (None if localctx._EDGE_ATTR is None else localctx._EDGE_ATTR.text) == ":" else "_->"
                    edge = self._impl.create_arc(create_token_context(localctx._EDGE_ATTR), connector)

                    localctx.items.append((node, edge))


                else:
                    raise NoViableAltException(self)
                self.state = 232 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.contour_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def contour_sempred(self, localctx:ContourContext, predIndex:int):
            if predIndex == 0:
                return count > 0
         




