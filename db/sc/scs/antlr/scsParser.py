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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3>")
        buf.write("\u00e2\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\3\2\5\2\64\n\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\7\3=")
        buf.write("\n\3\f\3\16\3@\13\3\3\3\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\6\3\6\3\6\3\6\3\6\3\6\5\6Q\n\6\3\7\7\7T\n\7\f\7\16")
        buf.write("\7W\13\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\5\t`\n\t\3\n\3\n")
        buf.write("\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3")
        buf.write("\r\5\rq\n\r\3\r\3\r\3\r\3\r\3\16\5\16x\n\16\3\16\3\16")
        buf.write("\3\16\3\17\3\17\3\17\7\17\u0080\n\17\f\17\16\17\u0083")
        buf.write("\13\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3")
        buf.write("\21\3\21\5\21\u0090\n\21\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\5\23\u00a7\n\23\3\24\3\24\3\24\5")
        buf.write("\24\u00ac\n\24\3\24\3\24\3\24\3\24\5\24\u00b2\n\24\7\24")
        buf.write("\u00b4\n\24\f\24\16\24\u00b7\13\24\3\25\3\25\5\25\u00bb")
        buf.write("\n\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\6\26\u00c4\n")
        buf.write("\26\r\26\16\26\u00c5\3\26\3\26\3\27\3\27\5\27\u00cc\n")
        buf.write("\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\7\30\u00d6")
        buf.write("\n\30\f\30\16\30\u00d9\13\30\3\31\3\31\3\31\6\31\u00de")
        buf.write("\n\31\r\31\16\31\u00df\3\31\2\2\32\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"$&(*,.\60\2\5\3\2\4\r\3\2\16)\4\2")
        buf.write("**\63\63\2\u00df\2\63\3\2\2\2\48\3\2\2\2\6D\3\2\2\2\b")
        buf.write("G\3\2\2\2\nP\3\2\2\2\fU\3\2\2\2\16Z\3\2\2\2\20_\3\2\2")
        buf.write("\2\22a\3\2\2\2\24d\3\2\2\2\26g\3\2\2\2\30l\3\2\2\2\32")
        buf.write("w\3\2\2\2\34|\3\2\2\2\36\u0084\3\2\2\2 \u008f\3\2\2\2")
        buf.write("\"\u0091\3\2\2\2$\u00a6\3\2\2\2&\u00a8\3\2\2\2(\u00b8")
        buf.write("\3\2\2\2*\u00bf\3\2\2\2,\u00c9\3\2\2\2.\u00d1\3\2\2\2")
        buf.write("\60\u00dd\3\2\2\2\62\64\7\3\2\2\63\62\3\2\2\2\63\64\3")
        buf.write("\2\2\2\64\65\3\2\2\2\65\66\7\67\2\2\66\67\b\2\1\2\67\3")
        buf.write("\3\2\2\289\7\65\2\29:\6\3\2\2:>\b\3\1\2;=\5\16\b\2<;\3")
        buf.write("\2\2\2=@\3\2\2\2><\3\2\2\2>?\3\2\2\2?A\3\2\2\2@>\3\2\2")
        buf.write("\2AB\7\66\2\2BC\b\3\1\2C\5\3\2\2\2DE\t\2\2\2EF\b\4\1\2")
        buf.write("F\7\3\2\2\2GH\t\3\2\2HI\b\5\1\2I\t\3\2\2\2JK\5\6\4\2K")
        buf.write("L\b\6\1\2LQ\3\2\2\2MN\5\b\5\2NO\b\6\1\2OQ\3\2\2\2PJ\3")
        buf.write("\2\2\2PM\3\2\2\2Q\13\3\2\2\2RT\5\16\b\2SR\3\2\2\2TW\3")
        buf.write("\2\2\2US\3\2\2\2UV\3\2\2\2VX\3\2\2\2WU\3\2\2\2XY\7\2\2")
        buf.write("\3Y\r\3\2\2\2Z[\5\20\t\2[\\\7>\2\2\\\17\3\2\2\2]`\5\26")
        buf.write("\f\2^`\5.\30\2_]\3\2\2\2_^\3\2\2\2`\21\3\2\2\2ab\7\64")
        buf.write("\2\2bc\b\n\1\2c\23\3\2\2\2de\t\4\2\2ef\b\13\1\2f\25\3")
        buf.write("\2\2\2gh\7\64\2\2hi\7+\2\2ij\5$\23\2jk\b\f\1\2k\27\3\2")
        buf.write("\2\2lm\7,\2\2mn\5 \21\2np\5\n\6\2oq\5\60\31\2po\3\2\2")
        buf.write("\2pq\3\2\2\2qr\3\2\2\2rs\5 \21\2st\7-\2\2tu\b\r\1\2u\31")
        buf.write("\3\2\2\2vx\5\60\31\2wv\3\2\2\2wx\3\2\2\2xy\3\2\2\2yz\5")
        buf.write("$\23\2z{\b\16\1\2{\33\3\2\2\2|\u0081\5\32\16\2}~\7.\2")
        buf.write("\2~\u0080\5\32\16\2\177}\3\2\2\2\u0080\u0083\3\2\2\2\u0081")
        buf.write("\177\3\2\2\2\u0081\u0082\3\2\2\2\u0082\35\3\2\2\2\u0083")
        buf.write("\u0081\3\2\2\2\u0084\u0085\7/\2\2\u0085\u0086\b\20\1\2")
        buf.write("\u0086\u0087\5\34\17\2\u0087\u0088\7\60\2\2\u0088\37\3")
        buf.write("\2\2\2\u0089\u008a\5\22\n\2\u008a\u008b\b\21\1\2\u008b")
        buf.write("\u0090\3\2\2\2\u008c\u008d\5\24\13\2\u008d\u008e\b\21")
        buf.write("\1\2\u008e\u0090\3\2\2\2\u008f\u0089\3\2\2\2\u008f\u008c")
        buf.write("\3\2\2\2\u0090!\3\2\2\2\u0091\u0092\78\2\2\u0092\u0093")
        buf.write("\b\22\1\2\u0093#\3\2\2\2\u0094\u0095\5 \21\2\u0095\u0096")
        buf.write("\b\23\1\2\u0096\u00a7\3\2\2\2\u0097\u0098\5\30\r\2\u0098")
        buf.write("\u0099\b\23\1\2\u0099\u00a7\3\2\2\2\u009a\u009b\5\36\20")
        buf.write("\2\u009b\u009c\b\23\1\2\u009c\u00a7\3\2\2\2\u009d\u009e")
        buf.write("\5\4\3\2\u009e\u009f\b\23\1\2\u009f\u00a7\3\2\2\2\u00a0")
        buf.write("\u00a1\5\2\2\2\u00a1\u00a2\b\23\1\2\u00a2\u00a7\3\2\2")
        buf.write("\2\u00a3\u00a4\5\"\22\2\u00a4\u00a5\b\23\1\2\u00a5\u00a7")
        buf.write("\3\2\2\2\u00a6\u0094\3\2\2\2\u00a6\u0097\3\2\2\2\u00a6")
        buf.write("\u009a\3\2\2\2\u00a6\u009d\3\2\2\2\u00a6\u00a0\3\2\2\2")
        buf.write("\u00a6\u00a3\3\2\2\2\u00a7%\3\2\2\2\u00a8\u00a9\5$\23")
        buf.write("\2\u00a9\u00ab\b\24\1\2\u00aa\u00ac\5*\26\2\u00ab\u00aa")
        buf.write("\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\u00b5\3\2\2\2\u00ad")
        buf.write("\u00ae\7.\2\2\u00ae\u00af\5$\23\2\u00af\u00b1\b\24\1\2")
        buf.write("\u00b0\u00b2\5*\26\2\u00b1\u00b0\3\2\2\2\u00b1\u00b2\3")
        buf.write("\2\2\2\u00b2\u00b4\3\2\2\2\u00b3\u00ad\3\2\2\2\u00b4\u00b7")
        buf.write("\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6")
        buf.write("\'\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b8\u00ba\5\n\6\2\u00b9")
        buf.write("\u00bb\5\60\31\2\u00ba\u00b9\3\2\2\2\u00ba\u00bb\3\2\2")
        buf.write("\2\u00bb\u00bc\3\2\2\2\u00bc\u00bd\5&\24\2\u00bd\u00be")
        buf.write("\b\25\1\2\u00be)\3\2\2\2\u00bf\u00c3\7\61\2\2\u00c0\u00c1")
        buf.write("\5(\25\2\u00c1\u00c2\7>\2\2\u00c2\u00c4\3\2\2\2\u00c3")
        buf.write("\u00c0\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\u00c3\3\2\2\2")
        buf.write("\u00c5\u00c6\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7\u00c8\7")
        buf.write("\62\2\2\u00c8+\3\2\2\2\u00c9\u00cb\5\n\6\2\u00ca\u00cc")
        buf.write("\5\60\31\2\u00cb\u00ca\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc")
        buf.write("\u00cd\3\2\2\2\u00cd\u00ce\5&\24\2\u00ce\u00cf\3\2\2\2")
        buf.write("\u00cf\u00d0\b\27\1\2\u00d0-\3\2\2\2\u00d1\u00d2\5$\23")
        buf.write("\2\u00d2\u00d7\5,\27\2\u00d3\u00d4\7.\2\2\u00d4\u00d6")
        buf.write("\5,\27\2\u00d5\u00d3\3\2\2\2\u00d6\u00d9\3\2\2\2\u00d7")
        buf.write("\u00d5\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8/\3\2\2\2\u00d9")
        buf.write("\u00d7\3\2\2\2\u00da\u00db\7\63\2\2\u00db\u00dc\79\2\2")
        buf.write("\u00dc\u00de\b\31\1\2\u00dd\u00da\3\2\2\2\u00de\u00df")
        buf.write("\3\2\2\2\u00df\u00dd\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0")
        buf.write("\61\3\2\2\2\24\63>PU_pw\u0081\u008f\u00a6\u00ab\u00b1")
        buf.write("\u00b5\u00ba\u00c5\u00cb\u00d7\u00df")
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
                     "'_<|~'", "'_~/>'", "'_</~'", "'...'", "'='", "'('", 
                     "')'", "';'", "'{'", "'}'", "'(*'", "'*)'", "<INVALID>", 
                     "<INVALID>", "'[*'", "'*]'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "';;'" ]

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
                      "<INVALID>", "ID_SYSTEM", "ALIAS_SYMBOLS", "CONTOUR_BEGIN", 
                      "CONTOUR_END", "CONTENT_BODY", "LINK", "EDGE_ATTR", 
                      "LINE_TERMINATOR", "LINE_COMMENT", "MULTINE_COMMENT", 
                      "WS", "SENTENCE_SEP" ]

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
    RULE_idtf_edge = 11
    RULE_idtf_set_item = 12
    RULE_idtf_set_item_list = 13
    RULE_idtf_set = 14
    RULE_idtf_atomic = 15
    RULE_idtf_url = 16
    RULE_idtf_common = 17
    RULE_idtf_list = 18
    RULE_internal_sentence = 19
    RULE_internal_sentence_list = 20
    RULE_sentence_lvl_4_list_item = 21
    RULE_sentence_lvl_common = 22
    RULE_attr_list = 23

    ruleNames =  [ "content", "contour", "connector_edge", "connector_arc", 
                   "connector", "syntax", "sentence_wrap", "sentence", "ifdf_alias", 
                   "idtf_system", "sentence_assign", "idtf_edge", "idtf_set_item", 
                   "idtf_set_item_list", "idtf_set", "idtf_atomic", "idtf_url", 
                   "idtf_common", "idtf_list", "internal_sentence", "internal_sentence_list", 
                   "sentence_lvl_4_list_item", "sentence_lvl_common", "attr_list" ]

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
    ID_SYSTEM=49
    ALIAS_SYMBOLS=50
    CONTOUR_BEGIN=51
    CONTOUR_END=52
    CONTENT_BODY=53
    LINK=54
    EDGE_ATTR=55
    LINE_TERMINATOR=56
    LINE_COMMENT=57
    MULTINE_COMMENT=58
    WS=59
    SENTENCE_SEP=60

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
            self.v = None # Token
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
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==scsParser.T__0:
                self.state = 48
                localctx.v = self.match(scsParser.T__0)


            self.state = 51
            localctx._CONTENT_BODY = self.match(scsParser.CONTENT_BODY)

            token_context = create_token_context(localctx._CONTENT_BODY)
            localctx.el = self._impl.create_link(token_context, (None if localctx._CONTENT_BODY is None else localctx._CONTENT_BODY.text)[1:-1], Link.Type.STRING, localctx.v is not None)

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
            self.el = None
            self._CONTOUR_BEGIN = None # Token

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
            self.state = 54
            localctx._CONTOUR_BEGIN = self.match(scsParser.CONTOUR_BEGIN)
            self.state = 55
            if not count > 0:
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "count > 0")
            self._impl.start_contour()

            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << scsParser.T__0) | (1 << scsParser.T__39) | (1 << scsParser.T__41) | (1 << scsParser.T__44) | (1 << scsParser.ID_SYSTEM) | (1 << scsParser.ALIAS_SYMBOLS) | (1 << scsParser.CONTOUR_BEGIN) | (1 << scsParser.CONTENT_BODY) | (1 << scsParser.LINK))) != 0):
                self.state = 57
                self.sentence_wrap()
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 63
            self.match(scsParser.CONTOUR_END)

            count -= 1
            if count == 0:
            	contour = self._impl.create_node(create_token_context(localctx._CONTOUR_BEGIN))
            	self._impl.end_contour(contour)
            	localctx.el = contour

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
            self.state = 66
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
            self.state = 69
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
            self.state = 78
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [scsParser.T__1, scsParser.T__2, scsParser.T__3, scsParser.T__4, scsParser.T__5, scsParser.T__6, scsParser.T__7, scsParser.T__8, scsParser.T__9, scsParser.T__10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                localctx._connector_edge = self.connector_edge()
                localctx.el = localctx._connector_edge.el
                pass
            elif token in [scsParser.T__11, scsParser.T__12, scsParser.T__13, scsParser.T__14, scsParser.T__15, scsParser.T__16, scsParser.T__17, scsParser.T__18, scsParser.T__19, scsParser.T__20, scsParser.T__21, scsParser.T__22, scsParser.T__23, scsParser.T__24, scsParser.T__25, scsParser.T__26, scsParser.T__27, scsParser.T__28, scsParser.T__29, scsParser.T__30, scsParser.T__31, scsParser.T__32, scsParser.T__33, scsParser.T__34, scsParser.T__35, scsParser.T__36, scsParser.T__37, scsParser.T__38]:
                self.enterOuterAlt(localctx, 2)
                self.state = 75
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
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << scsParser.T__0) | (1 << scsParser.T__39) | (1 << scsParser.T__41) | (1 << scsParser.T__44) | (1 << scsParser.ID_SYSTEM) | (1 << scsParser.ALIAS_SYMBOLS) | (1 << scsParser.CONTOUR_BEGIN) | (1 << scsParser.CONTENT_BODY) | (1 << scsParser.LINK))) != 0):
                self.state = 80
                self.sentence_wrap()
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 86
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
            self.state = 88
            self.sentence()
            self.state = 89
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
            self.state = 93
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 91
                self.sentence_assign()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 92
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
            self.state = 95
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
            self.state = 98
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
            self.state = 101
            localctx._ALIAS_SYMBOLS = self.match(scsParser.ALIAS_SYMBOLS)
            self.state = 102
            self.match(scsParser.T__40)
            self.state = 103
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
        self.enterRule(localctx, 22, self.RULE_idtf_edge)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(scsParser.T__41)
            self.state = 107
            localctx.src = self.idtf_atomic()
            self.state = 108
            localctx._connector = self.connector()
            self.state = 110
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 109
                localctx.attr = self.attr_list()


            self.state = 112
            localctx.trg = self.idtf_atomic()
            self.state = 113
            self.match(scsParser.T__42)

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


    class Idtf_set_itemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, set:Element=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.set = None
            self.attr = None # Attr_listContext
            self.idtf = None # Idtf_commonContext
            self.set = set

        def idtf_common(self):
            return self.getTypedRuleContext(scsParser.Idtf_commonContext,0)


        def attr_list(self):
            return self.getTypedRuleContext(scsParser.Attr_listContext,0)


        def getRuleIndex(self):
            return scsParser.RULE_idtf_set_item




    def idtf_set_item(self, set:Element):

        localctx = scsParser.Idtf_set_itemContext(self, self._ctx, self.state, set)
        self.enterRule(localctx, 24, self.RULE_idtf_set_item)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 116
                localctx.attr = self.attr_list()


            self.state = 119
            localctx.idtf = self.idtf_common()

            edge = self._impl.create_arc(localctx.idtf.el.ctx.clone(), '->')
            self._impl.append_triple(localctx.set, edge, localctx.idtf.el)
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


    class Idtf_set_item_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, set:Element=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.set = None
            self.set = set

        def idtf_set_item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(scsParser.Idtf_set_itemContext)
            else:
                return self.getTypedRuleContext(scsParser.Idtf_set_itemContext,i)


        def getRuleIndex(self):
            return scsParser.RULE_idtf_set_item_list




    def idtf_set_item_list(self, set:Element):

        localctx = scsParser.Idtf_set_item_listContext(self, self._ctx, self.state, set)
        self.enterRule(localctx, 26, self.RULE_idtf_set_item_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.idtf_set_item(set)
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==scsParser.T__43:
                self.state = 123
                self.match(scsParser.T__43)
                self.state = 124
                self.idtf_set_item(set)
                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            self.el = None
            self.t = None # Token

        def idtf_set_item_list(self):
            return self.getTypedRuleContext(scsParser.Idtf_set_item_listContext,0)


        def getRuleIndex(self):
            return scsParser.RULE_idtf_set




    def idtf_set(self):

        localctx = scsParser.Idtf_setContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_idtf_set)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            localctx.t = self.match(scsParser.T__44)

            context = create_token_context(localctx.t)
            localctx.el = self._impl.create_node(context)
            	
            self.state = 132
            self.idtf_set_item_list(localctx.el)
            self.state = 133
            self.match(scsParser.T__45)
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
            self.state = 141
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [scsParser.ALIAS_SYMBOLS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                localctx._ifdf_alias = self.ifdf_alias()
                localctx.el = localctx._ifdf_alias.el
                pass
            elif token in [scsParser.T__39, scsParser.ID_SYSTEM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
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
            self.state = 143
            localctx._LINK = self.match(scsParser.LINK)

            context = create_token_context(localctx._LINK)
            localctx.el = self._impl.create_link(context, (None if localctx._LINK is None else localctx._LINK.text)[1:-1], Link.Type.URL, False)

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
            self._idtf_set = None # Idtf_setContext
            self._contour = None # ContourContext
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
            self.state = 164
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [scsParser.T__39, scsParser.ID_SYSTEM, scsParser.ALIAS_SYMBOLS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                localctx._idtf_atomic = self.idtf_atomic()
                localctx.el = localctx._idtf_atomic.el
                pass
            elif token in [scsParser.T__41]:
                self.enterOuterAlt(localctx, 2)
                self.state = 149
                localctx._idtf_edge = self.idtf_edge()
                localctx.el = localctx._idtf_edge.el
                pass
            elif token in [scsParser.T__44]:
                self.enterOuterAlt(localctx, 3)
                self.state = 152
                localctx._idtf_set = self.idtf_set()
                localctx.el = localctx._idtf_set.el
                pass
            elif token in [scsParser.CONTOUR_BEGIN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 155
                localctx._contour = self.contour()
                localctx.el = localctx._contour.el
                pass
            elif token in [scsParser.T__0, scsParser.CONTENT_BODY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 158
                localctx._content = self.content()
                localctx.el = localctx._content.el
                pass
            elif token in [scsParser.LINK]:
                self.enterOuterAlt(localctx, 6)
                self.state = 161
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
            self.state = 166
            localctx.first = self.idtf_common()
            localctx.items.append(localctx.first.el)
            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==scsParser.T__46:
                self.state = 168
                self.internal_sentence_list(localctx.first.el)


            self.state = 179
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 171
                    self.match(scsParser.T__43)
                    self.state = 172
                    localctx.second = self.idtf_common()
                    localctx.items.append(localctx.second.el)
                    self.state = 175
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==scsParser.T__46:
                        self.state = 174
                        self.internal_sentence_list(localctx.first.el)

             
                self.state = 181
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

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
            self.state = 182
            localctx.c = self.connector()
            self.state = 184
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 183
                localctx.attr = self.attr_list()


            self.state = 186
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
            self.state = 189
            self.match(scsParser.T__46)
            self.state = 193 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 190
                self.internal_sentence(src)
                self.state = 191
                self.match(scsParser.SENTENCE_SEP)
                self.state = 195 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << scsParser.T__1) | (1 << scsParser.T__2) | (1 << scsParser.T__3) | (1 << scsParser.T__4) | (1 << scsParser.T__5) | (1 << scsParser.T__6) | (1 << scsParser.T__7) | (1 << scsParser.T__8) | (1 << scsParser.T__9) | (1 << scsParser.T__10) | (1 << scsParser.T__11) | (1 << scsParser.T__12) | (1 << scsParser.T__13) | (1 << scsParser.T__14) | (1 << scsParser.T__15) | (1 << scsParser.T__16) | (1 << scsParser.T__17) | (1 << scsParser.T__18) | (1 << scsParser.T__19) | (1 << scsParser.T__20) | (1 << scsParser.T__21) | (1 << scsParser.T__22) | (1 << scsParser.T__23) | (1 << scsParser.T__24) | (1 << scsParser.T__25) | (1 << scsParser.T__26) | (1 << scsParser.T__27) | (1 << scsParser.T__28) | (1 << scsParser.T__29) | (1 << scsParser.T__30) | (1 << scsParser.T__31) | (1 << scsParser.T__32) | (1 << scsParser.T__33) | (1 << scsParser.T__34) | (1 << scsParser.T__35) | (1 << scsParser.T__36) | (1 << scsParser.T__37) | (1 << scsParser.T__38))) != 0)):
                    break

            self.state = 197
            self.match(scsParser.T__47)
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
        self.enterRule(localctx, 42, self.RULE_sentence_lvl_4_list_item)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            localctx.c = self.connector()
            self.state = 201
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 200
                localctx.attr = self.attr_list()


            self.state = 203
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
        self.enterRule(localctx, 44, self.RULE_sentence_lvl_common)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            localctx._idtf_common = self.idtf_common()
            self.state = 208
            self.sentence_lvl_4_list_item(localctx._idtf_common.el)
            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==scsParser.T__43:
                self.state = 209
                self.match(scsParser.T__43)
                self.state = 210
                self.sentence_lvl_4_list_item(localctx._idtf_common.el)
                self.state = 215
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
        self.enterRule(localctx, 46, self.RULE_attr_list)
        localctx.items = []
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 216
                    localctx._ID_SYSTEM = self.match(scsParser.ID_SYSTEM)
                    self.state = 217
                    localctx._EDGE_ATTR = self.match(scsParser.EDGE_ATTR)

                    node = self._impl.create_node(create_token_context(localctx._ID_SYSTEM))
                    edge = None
                    connector = "->" if (None if localctx._EDGE_ATTR is None else localctx._EDGE_ATTR.text) == ":" else "_->"
                    edge = self._impl.create_arc(create_token_context(localctx._EDGE_ATTR), connector)

                    localctx.items.append((node, edge))


                else:
                    raise NoViableAltException(self)
                self.state = 221 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

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
         




