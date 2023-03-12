# Generated from c:\Users\levan\OneDrive\Documents\GitHub\assignment2-PPL\src\main\mt22\parser\MT22.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3<")
        buf.write("\u017b\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\3\2\3\2\3\2\3\3\3\3\3\3\3")
        buf.write("\3\5\3\\\n\3\3\4\3\4\5\4`\n\4\3\5\3\5\3\5\5\5e\n\5\3\6")
        buf.write("\3\6\3\6\3\6\3\6\5\6l\n\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\5\7w\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t")
        buf.write("\3\t\5\t\u0083\n\t\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u008b\n")
        buf.write("\n\3\13\3\13\3\13\3\13\3\13\5\13\u0092\n\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\5\13\u0099\n\13\3\13\3\13\5\13\u009d\n")
        buf.write("\13\3\f\3\f\3\f\3\r\5\r\u00a3\n\r\3\r\5\r\u00a6\n\r\3")
        buf.write("\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u00b2")
        buf.write("\n\16\3\17\3\17\3\17\3\17\3\20\3\20\5\20\u00ba\n\20\3")
        buf.write("\20\3\20\3\20\5\20\u00bf\n\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\5\21\u00cb\n\21\3\22\3\22\5")
        buf.write("\22\u00cf\n\22\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\5\25\u00df\n\25\3\26\3")
        buf.write("\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\5\33\u0104\n\33\3\33\3\33\3\34\3\34\3\34\3\34\3")
        buf.write("\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\36\5\36\u0119\n\36\3\37\3\37\3 \3 \3 \3 \3 \5")
        buf.write(" \u0122\n \3!\3!\3!\3!\3!\5!\u0129\n!\3\"\3\"\3\"\3\"")
        buf.write("\3\"\5\"\u0130\n\"\3#\3#\3#\3#\3#\3#\7#\u0138\n#\f#\16")
        buf.write("#\u013b\13#\3$\3$\3$\3$\3$\3$\7$\u0143\n$\f$\16$\u0146")
        buf.write("\13$\3%\3%\3%\3%\3%\3%\7%\u014e\n%\f%\16%\u0151\13%\3")
        buf.write("&\3&\3&\5&\u0156\n&\3\'\3\'\3\'\5\'\u015b\n\'\3(\3(\3")
        buf.write("(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\5(\u016d\n(\3")
        buf.write(")\3)\3)\3)\3)\3*\3*\3*\5*\u0177\n*\3*\3*\3*\2\5DFH+\2")
        buf.write("\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64")
        buf.write("\668:<>@BDFHJLNPR\2\7\6\2%%((--\60\60\3\2\13\20\3\2\21")
        buf.write("\22\3\2\6\7\3\2\b\n\2\u0184\2T\3\2\2\2\4[\3\2\2\2\6_\3")
        buf.write("\2\2\2\bd\3\2\2\2\nk\3\2\2\2\fv\3\2\2\2\16x\3\2\2\2\20")
        buf.write("\u0082\3\2\2\2\22\u008a\3\2\2\2\24\u008c\3\2\2\2\26\u009e")
        buf.write("\3\2\2\2\30\u00a2\3\2\2\2\32\u00b1\3\2\2\2\34\u00b3\3")
        buf.write("\2\2\2\36\u00be\3\2\2\2 \u00ca\3\2\2\2\"\u00ce\3\2\2\2")
        buf.write("$\u00d0\3\2\2\2&\u00d2\3\2\2\2(\u00d7\3\2\2\2*\u00e0\3")
        buf.write("\2\2\2,\u00e6\3\2\2\2.\u00ee\3\2\2\2\60\u00fa\3\2\2\2")
        buf.write("\62\u00fd\3\2\2\2\64\u0100\3\2\2\2\66\u0107\3\2\2\28\u010d")
        buf.write("\3\2\2\2:\u0118\3\2\2\2<\u011a\3\2\2\2>\u0121\3\2\2\2")
        buf.write("@\u0128\3\2\2\2B\u012f\3\2\2\2D\u0131\3\2\2\2F\u013c\3")
        buf.write("\2\2\2H\u0147\3\2\2\2J\u0155\3\2\2\2L\u015a\3\2\2\2N\u016c")
        buf.write("\3\2\2\2P\u016e\3\2\2\2R\u0173\3\2\2\2TU\5\4\3\2UV\7\2")
        buf.write("\2\3V\3\3\2\2\2WX\5\6\4\2XY\5\4\3\2Y\\\3\2\2\2Z\\\5\6")
        buf.write("\4\2[W\3\2\2\2[Z\3\2\2\2\\\5\3\2\2\2]`\5\n\6\2^`\5\24")
        buf.write("\13\2_]\3\2\2\2_^\3\2\2\2`\7\3\2\2\2ae\5<\37\2be\58\35")
        buf.write("\2ce\7#\2\2da\3\2\2\2db\3\2\2\2dc\3\2\2\2e\t\3\2\2\2f")
        buf.write("g\5\20\t\2gh\7\36\2\2hi\5\b\5\2il\3\2\2\2jl\5\f\7\2kf")
        buf.write("\3\2\2\2kj\3\2\2\2lm\3\2\2\2mn\7\33\2\2n\13\3\2\2\2op")
        buf.write("\78\2\2pq\7\34\2\2qr\5\f\7\2rs\7\34\2\2st\5@!\2tw\3\2")
        buf.write("\2\2uw\5\16\b\2vo\3\2\2\2vu\3\2\2\2w\r\3\2\2\2xy\78\2")
        buf.write("\2yz\7\36\2\2z{\5\b\5\2{|\7\5\2\2|}\5@!\2}\17\3\2\2\2")
        buf.write("~\177\78\2\2\177\u0080\7\34\2\2\u0080\u0083\5\20\t\2\u0081")
        buf.write("\u0083\78\2\2\u0082~\3\2\2\2\u0082\u0081\3\2\2\2\u0083")
        buf.write("\21\3\2\2\2\u0084\u0085\5@!\2\u0085\u0086\7\34\2\2\u0086")
        buf.write("\u0087\5\22\n\2\u0087\u008b\3\2\2\2\u0088\u008b\5@!\2")
        buf.write("\u0089\u008b\3\2\2\2\u008a\u0084\3\2\2\2\u008a\u0088\3")
        buf.write("\2\2\2\u008a\u0089\3\2\2\2\u008b\23\3\2\2\2\u008c\u008d")
        buf.write("\78\2\2\u008d\u008e\7\36\2\2\u008e\u0091\7*\2\2\u008f")
        buf.write("\u0092\5\b\5\2\u0090\u0092\7\61\2\2\u0091\u008f\3\2\2")
        buf.write("\2\u0091\u0090\3\2\2\2\u0092\u0093\3\2\2\2\u0093\u0094")
        buf.write("\7\25\2\2\u0094\u0095\5\32\16\2\u0095\u0098\7\26\2\2\u0096")
        buf.write("\u0097\7,\2\2\u0097\u0099\78\2\2\u0098\u0096\3\2\2\2\u0098")
        buf.write("\u0099\3\2\2\2\u0099\u009c\3\2\2\2\u009a\u009d\5\34\17")
        buf.write("\2\u009b\u009d\5\26\f\2\u009c\u009a\3\2\2\2\u009c\u009b")
        buf.write("\3\2\2\2\u009d\25\3\2\2\2\u009e\u009f\7\27\2\2\u009f\u00a0")
        buf.write("\7\30\2\2\u00a0\27\3\2\2\2\u00a1\u00a3\7,\2\2\u00a2\u00a1")
        buf.write("\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3\u00a5\3\2\2\2\u00a4")
        buf.write("\u00a6\7.\2\2\u00a5\u00a4\3\2\2\2\u00a5\u00a6\3\2\2\2")
        buf.write("\u00a6\u00a7\3\2\2\2\u00a7\u00a8\78\2\2\u00a8\u00a9\7")
        buf.write("\36\2\2\u00a9\u00aa\5\b\5\2\u00aa\31\3\2\2\2\u00ab\u00ac")
        buf.write("\5\30\r\2\u00ac\u00ad\7\34\2\2\u00ad\u00ae\5\32\16\2\u00ae")
        buf.write("\u00b2\3\2\2\2\u00af\u00b2\5\30\r\2\u00b0\u00b2\3\2\2")
        buf.write("\2\u00b1\u00ab\3\2\2\2\u00b1\u00af\3\2\2\2\u00b1\u00b0")
        buf.write("\3\2\2\2\u00b2\33\3\2\2\2\u00b3\u00b4\7\27\2\2\u00b4\u00b5")
        buf.write("\5\36\20\2\u00b5\u00b6\7\30\2\2\u00b6\35\3\2\2\2\u00b7")
        buf.write("\u00ba\5 \21\2\u00b8\u00ba\5\n\6\2\u00b9\u00b7\3\2\2\2")
        buf.write("\u00b9\u00b8\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00bc\5")
        buf.write("\36\20\2\u00bc\u00bf\3\2\2\2\u00bd\u00bf\3\2\2\2\u00be")
        buf.write("\u00b9\3\2\2\2\u00be\u00bd\3\2\2\2\u00bf\37\3\2\2\2\u00c0")
        buf.write("\u00cb\5&\24\2\u00c1\u00cb\5(\25\2\u00c2\u00cb\5*\26\2")
        buf.write("\u00c3\u00cb\5.\30\2\u00c4\u00cb\5\60\31\2\u00c5\u00cb")
        buf.write("\5\62\32\2\u00c6\u00cb\5\64\33\2\u00c7\u00cb\5\66\34\2")
        buf.write("\u00c8\u00cb\5\34\17\2\u00c9\u00cb\5,\27\2\u00ca\u00c0")
        buf.write("\3\2\2\2\u00ca\u00c1\3\2\2\2\u00ca\u00c2\3\2\2\2\u00ca")
        buf.write("\u00c3\3\2\2\2\u00ca\u00c4\3\2\2\2\u00ca\u00c5\3\2\2\2")
        buf.write("\u00ca\u00c6\3\2\2\2\u00ca\u00c7\3\2\2\2\u00ca\u00c8\3")
        buf.write("\2\2\2\u00ca\u00c9\3\2\2\2\u00cb!\3\2\2\2\u00cc\u00cf")
        buf.write("\5$\23\2\u00cd\u00cf\5P)\2\u00ce\u00cc\3\2\2\2\u00ce\u00cd")
        buf.write("\3\2\2\2\u00cf#\3\2\2\2\u00d0\u00d1\78\2\2\u00d1%\3\2")
        buf.write("\2\2\u00d2\u00d3\5\"\22\2\u00d3\u00d4\7\5\2\2\u00d4\u00d5")
        buf.write("\5@!\2\u00d5\u00d6\7\33\2\2\u00d6\'\3\2\2\2\u00d7\u00d8")
        buf.write("\7+\2\2\u00d8\u00d9\7\25\2\2\u00d9\u00da\5@!\2\u00da\u00db")
        buf.write("\7\26\2\2\u00db\u00de\5 \21\2\u00dc\u00dd\7\'\2\2\u00dd")
        buf.write("\u00df\5 \21\2\u00de\u00dc\3\2\2\2\u00de\u00df\3\2\2\2")
        buf.write("\u00df)\3\2\2\2\u00e0\u00e1\7\62\2\2\u00e1\u00e2\7\25")
        buf.write("\2\2\u00e2\u00e3\5@!\2\u00e3\u00e4\7\26\2\2\u00e4\u00e5")
        buf.write("\5 \21\2\u00e5+\3\2\2\2\u00e6\u00e7\7\65\2\2\u00e7\u00e8")
        buf.write("\5\34\17\2\u00e8\u00e9\7\62\2\2\u00e9\u00ea\7\25\2\2\u00ea")
        buf.write("\u00eb\5@!\2\u00eb\u00ec\7\26\2\2\u00ec\u00ed\7\33\2\2")
        buf.write("\u00ed-\3\2\2\2\u00ee\u00ef\7)\2\2\u00ef\u00f0\7\25\2")
        buf.write("\2\u00f0\u00f1\5\"\22\2\u00f1\u00f2\7\5\2\2\u00f2\u00f3")
        buf.write("\5@!\2\u00f3\u00f4\7\34\2\2\u00f4\u00f5\5@!\2\u00f5\u00f6")
        buf.write("\7\34\2\2\u00f6\u00f7\5@!\2\u00f7\u00f8\7\26\2\2\u00f8")
        buf.write("\u00f9\5 \21\2\u00f9/\3\2\2\2\u00fa\u00fb\7$\2\2\u00fb")
        buf.write("\u00fc\7\33\2\2\u00fc\61\3\2\2\2\u00fd\u00fe\7&\2\2\u00fe")
        buf.write("\u00ff\7\33\2\2\u00ff\63\3\2\2\2\u0100\u0103\7/\2\2\u0101")
        buf.write("\u0104\5@!\2\u0102\u0104\3\2\2\2\u0103\u0101\3\2\2\2\u0103")
        buf.write("\u0102\3\2\2\2\u0104\u0105\3\2\2\2\u0105\u0106\7\33\2")
        buf.write("\2\u0106\65\3\2\2\2\u0107\u0108\78\2\2\u0108\u0109\7\25")
        buf.write("\2\2\u0109\u010a\5\22\n\2\u010a\u010b\7\26\2\2\u010b\u010c")
        buf.write("\7\33\2\2\u010c\67\3\2\2\2\u010d\u010e\7\67\2\2\u010e")
        buf.write("\u010f\7\31\2\2\u010f\u0110\5:\36\2\u0110\u0111\7\32\2")
        buf.write("\2\u0111\u0112\7\66\2\2\u0112\u0113\5<\37\2\u01139\3\2")
        buf.write("\2\2\u0114\u0115\7\37\2\2\u0115\u0116\7\34\2\2\u0116\u0119")
        buf.write("\5:\36\2\u0117\u0119\7\37\2\2\u0118\u0114\3\2\2\2\u0118")
        buf.write("\u0117\3\2\2\2\u0119;\3\2\2\2\u011a\u011b\t\2\2\2\u011b")
        buf.write("=\3\2\2\2\u011c\u0122\7\37\2\2\u011d\u0122\7 \2\2\u011e")
        buf.write("\u0122\7\"\2\2\u011f\u0122\7!\2\2\u0120\u0122\5R*\2\u0121")
        buf.write("\u011c\3\2\2\2\u0121\u011d\3\2\2\2\u0121\u011e\3\2\2\2")
        buf.write("\u0121\u011f\3\2\2\2\u0121\u0120\3\2\2\2\u0122?\3\2\2")
        buf.write("\2\u0123\u0124\5B\"\2\u0124\u0125\7\23\2\2\u0125\u0126")
        buf.write("\5B\"\2\u0126\u0129\3\2\2\2\u0127\u0129\5B\"\2\u0128\u0123")
        buf.write("\3\2\2\2\u0128\u0127\3\2\2\2\u0129A\3\2\2\2\u012a\u012b")
        buf.write("\5D#\2\u012b\u012c\t\3\2\2\u012c\u012d\5D#\2\u012d\u0130")
        buf.write("\3\2\2\2\u012e\u0130\5D#\2\u012f\u012a\3\2\2\2\u012f\u012e")
        buf.write("\3\2\2\2\u0130C\3\2\2\2\u0131\u0132\b#\1\2\u0132\u0133")
        buf.write("\5F$\2\u0133\u0139\3\2\2\2\u0134\u0135\f\4\2\2\u0135\u0136")
        buf.write("\t\4\2\2\u0136\u0138\5F$\2\u0137\u0134\3\2\2\2\u0138\u013b")
        buf.write("\3\2\2\2\u0139\u0137\3\2\2\2\u0139\u013a\3\2\2\2\u013a")
        buf.write("E\3\2\2\2\u013b\u0139\3\2\2\2\u013c\u013d\b$\1\2\u013d")
        buf.write("\u013e\5H%\2\u013e\u0144\3\2\2\2\u013f\u0140\f\4\2\2\u0140")
        buf.write("\u0141\t\5\2\2\u0141\u0143\5H%\2\u0142\u013f\3\2\2\2\u0143")
        buf.write("\u0146\3\2\2\2\u0144\u0142\3\2\2\2\u0144\u0145\3\2\2\2")
        buf.write("\u0145G\3\2\2\2\u0146\u0144\3\2\2\2\u0147\u0148\b%\1\2")
        buf.write("\u0148\u0149\5J&\2\u0149\u014f\3\2\2\2\u014a\u014b\f\4")
        buf.write("\2\2\u014b\u014c\t\6\2\2\u014c\u014e\5J&\2\u014d\u014a")
        buf.write("\3\2\2\2\u014e\u0151\3\2\2\2\u014f\u014d\3\2\2\2\u014f")
        buf.write("\u0150\3\2\2\2\u0150I\3\2\2\2\u0151\u014f\3\2\2\2\u0152")
        buf.write("\u0153\7\24\2\2\u0153\u0156\5J&\2\u0154\u0156\5L\'\2\u0155")
        buf.write("\u0152\3\2\2\2\u0155\u0154\3\2\2\2\u0156K\3\2\2\2\u0157")
        buf.write("\u0158\7\7\2\2\u0158\u015b\5L\'\2\u0159\u015b\5N(\2\u015a")
        buf.write("\u0157\3\2\2\2\u015a\u0159\3\2\2\2\u015bM\3\2\2\2\u015c")
        buf.write("\u016d\7\37\2\2\u015d\u016d\7!\2\2\u015e\u016d\7 \2\2")
        buf.write("\u015f\u016d\7\"\2\2\u0160\u016d\78\2\2\u0161\u016d\5")
        buf.write("P)\2\u0162\u0163\78\2\2\u0163\u0164\7\25\2\2\u0164\u0165")
        buf.write("\5\22\n\2\u0165\u0166\7\26\2\2\u0166\u016d\3\2\2\2\u0167")
        buf.write("\u0168\7\25\2\2\u0168\u0169\5@!\2\u0169\u016a\7\26\2\2")
        buf.write("\u016a\u016d\3\2\2\2\u016b\u016d\5R*\2\u016c\u015c\3\2")
        buf.write("\2\2\u016c\u015d\3\2\2\2\u016c\u015e\3\2\2\2\u016c\u015f")
        buf.write("\3\2\2\2\u016c\u0160\3\2\2\2\u016c\u0161\3\2\2\2\u016c")
        buf.write("\u0162\3\2\2\2\u016c\u0167\3\2\2\2\u016c\u016b\3\2\2\2")
        buf.write("\u016dO\3\2\2\2\u016e\u016f\78\2\2\u016f\u0170\7\31\2")
        buf.write("\2\u0170\u0171\5\22\n\2\u0171\u0172\7\32\2\2\u0172Q\3")
        buf.write("\2\2\2\u0173\u0176\7\27\2\2\u0174\u0177\5\22\n\2\u0175")
        buf.write("\u0177\5\26\f\2\u0176\u0174\3\2\2\2\u0176\u0175\3\2\2")
        buf.write("\2\u0177\u0178\3\2\2\2\u0178\u0179\7\30\2\2\u0179S\3\2")
        buf.write("\2\2 [_dkv\u0082\u008a\u0091\u0098\u009c\u00a2\u00a5\u00b1")
        buf.write("\u00b9\u00be\u00ca\u00ce\u00de\u0103\u0118\u0121\u0128")
        buf.write("\u012f\u0139\u0144\u014f\u0155\u015a\u016c\u0176")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'='", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'=='", "'!='", "'>'", 
                     "'<'", "'>='", "'<='", "'&&'", "'||'", "'::'", "'!'", 
                     "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", "','", 
                     "'.'", "':'" ]

    symbolicNames = [ "<INVALID>", "SL_COMMENT", "ML_COMMENT", "ASSIGNOP", 
                      "ADDOP", "SUBOP", "MULOP", "DIVOP", "MODOP", "EQOP", 
                      "NEOP", "GTOP", "LTOP", "GTEOP", "LTEOP", "ANDOP", 
                      "OROP", "STRINGOP", "NOTOP", "LP", "RP", "LC", "RC", 
                      "LS", "RS", "SEMICOLON", "COMMA", "DOT", "COLON", 
                      "INTLIT", "BOOLLIT", "FLOATLIT", "STRINGLIT", "AUTO", 
                      "BREAK", "BOOLEAN", "CONTINUE", "ELSE", "FLOAT", "FOR", 
                      "FUNCTION", "IF", "INHERIT", "INTEGER", "OUT", "RETURN", 
                      "STRING", "VOID", "WHILE", "TRUE", "FALSE", "DO", 
                      "OF", "ARRAY", "IDENTIFIER", "WS", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decllist = 1
    RULE_declaration = 2
    RULE_typ = 3
    RULE_vardec = 4
    RULE_subvardec = 5
    RULE_expand = 6
    RULE_idlist = 7
    RULE_exprlist = 8
    RULE_funcdec = 9
    RULE_emptycurl = 10
    RULE_parameter = 11
    RULE_parameterlist = 12
    RULE_blockstate = 13
    RULE_blockstatemin = 14
    RULE_statement = 15
    RULE_lhs = 16
    RULE_scalarvar = 17
    RULE_assignstate = 18
    RULE_ifstate = 19
    RULE_whilestate = 20
    RULE_dowhilestate = 21
    RULE_forstate = 22
    RULE_breakstate = 23
    RULE_continuestate = 24
    RULE_returnstate = 25
    RULE_funcall = 26
    RULE_arraytype = 27
    RULE_dimensions = 28
    RULE_atomictype = 29
    RULE_literal = 30
    RULE_expr = 31
    RULE_expr1 = 32
    RULE_expr2 = 33
    RULE_expr3 = 34
    RULE_expr4 = 35
    RULE_expr5 = 36
    RULE_expr6 = 37
    RULE_expr7 = 38
    RULE_exprindex = 39
    RULE_arraylit = 40

    ruleNames =  [ "program", "decllist", "declaration", "typ", "vardec", 
                   "subvardec", "expand", "idlist", "exprlist", "funcdec", 
                   "emptycurl", "parameter", "parameterlist", "blockstate", 
                   "blockstatemin", "statement", "lhs", "scalarvar", "assignstate", 
                   "ifstate", "whilestate", "dowhilestate", "forstate", 
                   "breakstate", "continuestate", "returnstate", "funcall", 
                   "arraytype", "dimensions", "atomictype", "literal", "expr", 
                   "expr1", "expr2", "expr3", "expr4", "expr5", "expr6", 
                   "expr7", "exprindex", "arraylit" ]

    EOF = Token.EOF
    SL_COMMENT=1
    ML_COMMENT=2
    ASSIGNOP=3
    ADDOP=4
    SUBOP=5
    MULOP=6
    DIVOP=7
    MODOP=8
    EQOP=9
    NEOP=10
    GTOP=11
    LTOP=12
    GTEOP=13
    LTEOP=14
    ANDOP=15
    OROP=16
    STRINGOP=17
    NOTOP=18
    LP=19
    RP=20
    LC=21
    RC=22
    LS=23
    RS=24
    SEMICOLON=25
    COMMA=26
    DOT=27
    COLON=28
    INTLIT=29
    BOOLLIT=30
    FLOATLIT=31
    STRINGLIT=32
    AUTO=33
    BREAK=34
    BOOLEAN=35
    CONTINUE=36
    ELSE=37
    FLOAT=38
    FOR=39
    FUNCTION=40
    IF=41
    INHERIT=42
    INTEGER=43
    OUT=44
    RETURN=45
    STRING=46
    VOID=47
    WHILE=48
    TRUE=49
    FALSE=50
    DO=51
    OF=52
    ARRAY=53
    IDENTIFIER=54
    WS=55
    UNCLOSE_STRING=56
    ILLEGAL_ESCAPE=57
    ERROR_CHAR=58

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decllist(self):
            return self.getTypedRuleContext(MT22Parser.DecllistContext,0)


        def EOF(self):
            return self.getToken(MT22Parser.EOF, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_program




    def program(self):

        localctx = MT22Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.decllist()
            self.state = 83
            self.match(MT22Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecllistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(MT22Parser.DeclarationContext,0)


        def decllist(self):
            return self.getTypedRuleContext(MT22Parser.DecllistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_decllist




    def decllist(self):

        localctx = MT22Parser.DecllistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decllist)
        try:
            self.state = 89
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 85
                self.declaration()
                self.state = 86
                self.decllist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 88
                self.declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardec(self):
            return self.getTypedRuleContext(MT22Parser.VardecContext,0)


        def funcdec(self):
            return self.getTypedRuleContext(MT22Parser.FuncdecContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_declaration




    def declaration(self):

        localctx = MT22Parser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaration)
        try:
            self.state = 93
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 91
                self.vardec()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 92
                self.funcdec()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atomictype(self):
            return self.getTypedRuleContext(MT22Parser.AtomictypeContext,0)


        def arraytype(self):
            return self.getTypedRuleContext(MT22Parser.ArraytypeContext,0)


        def AUTO(self):
            return self.getToken(MT22Parser.AUTO, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_typ




    def typ(self):

        localctx = MT22Parser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_typ)
        try:
            self.state = 98
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.BOOLEAN, MT22Parser.FLOAT, MT22Parser.INTEGER, MT22Parser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.atomictype()
                pass
            elif token in [MT22Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.arraytype()
                pass
            elif token in [MT22Parser.AUTO]:
                self.enterOuterAlt(localctx, 3)
                self.state = 97
                self.match(MT22Parser.AUTO)
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


    class VardecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(MT22Parser.SEMICOLON, 0)

        def subvardec(self):
            return self.getTypedRuleContext(MT22Parser.SubvardecContext,0)


        def idlist(self):
            return self.getTypedRuleContext(MT22Parser.IdlistContext,0)


        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def typ(self):
            return self.getTypedRuleContext(MT22Parser.TypContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_vardec




    def vardec(self):

        localctx = MT22Parser.VardecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_vardec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 100
                self.idlist()
                self.state = 101
                self.match(MT22Parser.COLON)
                self.state = 102
                self.typ()
                pass

            elif la_ == 2:
                self.state = 104
                self.subvardec()
                pass


            self.state = 107
            self.match(MT22Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubvardecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMA)
            else:
                return self.getToken(MT22Parser.COMMA, i)

        def subvardec(self):
            return self.getTypedRuleContext(MT22Parser.SubvardecContext,0)


        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def expand(self):
            return self.getTypedRuleContext(MT22Parser.ExpandContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_subvardec




    def subvardec(self):

        localctx = MT22Parser.SubvardecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_subvardec)
        try:
            self.state = 116
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self.match(MT22Parser.IDENTIFIER)
                self.state = 110
                self.match(MT22Parser.COMMA)
                self.state = 111
                self.subvardec()
                self.state = 112
                self.match(MT22Parser.COMMA)
                self.state = 113
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 115
                self.expand()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def typ(self):
            return self.getTypedRuleContext(MT22Parser.TypContext,0)


        def ASSIGNOP(self):
            return self.getToken(MT22Parser.ASSIGNOP, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expand




    def expand(self):

        localctx = MT22Parser.ExpandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_expand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(MT22Parser.IDENTIFIER)
            self.state = 119
            self.match(MT22Parser.COLON)
            self.state = 120
            self.typ()
            self.state = 121
            self.match(MT22Parser.ASSIGNOP)
            self.state = 122
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def idlist(self):
            return self.getTypedRuleContext(MT22Parser.IdlistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_idlist




    def idlist(self):

        localctx = MT22Parser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_idlist)
        try:
            self.state = 128
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.match(MT22Parser.IDENTIFIER)
                self.state = 125
                self.match(MT22Parser.COMMA)
                self.state = 126
                self.idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 127
                self.match(MT22Parser.IDENTIFIER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def exprlist(self):
            return self.getTypedRuleContext(MT22Parser.ExprlistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_exprlist




    def exprlist(self):

        localctx = MT22Parser.ExprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_exprlist)
        try:
            self.state = 136
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.expr()
                self.state = 131
                self.match(MT22Parser.COMMA)
                self.state = 132
                self.exprlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                self.expr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.IDENTIFIER)
            else:
                return self.getToken(MT22Parser.IDENTIFIER, i)

        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def FUNCTION(self):
            return self.getToken(MT22Parser.FUNCTION, 0)

        def LP(self):
            return self.getToken(MT22Parser.LP, 0)

        def parameterlist(self):
            return self.getTypedRuleContext(MT22Parser.ParameterlistContext,0)


        def RP(self):
            return self.getToken(MT22Parser.RP, 0)

        def typ(self):
            return self.getTypedRuleContext(MT22Parser.TypContext,0)


        def VOID(self):
            return self.getToken(MT22Parser.VOID, 0)

        def blockstate(self):
            return self.getTypedRuleContext(MT22Parser.BlockstateContext,0)


        def emptycurl(self):
            return self.getTypedRuleContext(MT22Parser.EmptycurlContext,0)


        def INHERIT(self):
            return self.getToken(MT22Parser.INHERIT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_funcdec




    def funcdec(self):

        localctx = MT22Parser.FuncdecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_funcdec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.match(MT22Parser.IDENTIFIER)
            self.state = 139
            self.match(MT22Parser.COLON)
            self.state = 140
            self.match(MT22Parser.FUNCTION)
            self.state = 143
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.AUTO, MT22Parser.BOOLEAN, MT22Parser.FLOAT, MT22Parser.INTEGER, MT22Parser.STRING, MT22Parser.ARRAY]:
                self.state = 141
                self.typ()
                pass
            elif token in [MT22Parser.VOID]:
                self.state = 142
                self.match(MT22Parser.VOID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 145
            self.match(MT22Parser.LP)
            self.state = 146
            self.parameterlist()
            self.state = 147
            self.match(MT22Parser.RP)
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.INHERIT:
                self.state = 148
                self.match(MT22Parser.INHERIT)
                self.state = 149
                self.match(MT22Parser.IDENTIFIER)


            self.state = 154
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 152
                self.blockstate()
                pass

            elif la_ == 2:
                self.state = 153
                self.emptycurl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EmptycurlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LC(self):
            return self.getToken(MT22Parser.LC, 0)

        def RC(self):
            return self.getToken(MT22Parser.RC, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_emptycurl




    def emptycurl(self):

        localctx = MT22Parser.EmptycurlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_emptycurl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(MT22Parser.LC)
            self.state = 157
            self.match(MT22Parser.RC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def typ(self):
            return self.getTypedRuleContext(MT22Parser.TypContext,0)


        def INHERIT(self):
            return self.getToken(MT22Parser.INHERIT, 0)

        def OUT(self):
            return self.getToken(MT22Parser.OUT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_parameter




    def parameter(self):

        localctx = MT22Parser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.INHERIT:
                self.state = 159
                self.match(MT22Parser.INHERIT)


            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.OUT:
                self.state = 162
                self.match(MT22Parser.OUT)


            self.state = 165
            self.match(MT22Parser.IDENTIFIER)
            self.state = 166
            self.match(MT22Parser.COLON)
            self.state = 167
            self.typ()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self):
            return self.getTypedRuleContext(MT22Parser.ParameterContext,0)


        def parameterlist(self):
            return self.getTypedRuleContext(MT22Parser.ParameterlistContext,0)


        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_parameterlist




    def parameterlist(self):

        localctx = MT22Parser.ParameterlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_parameterlist)
        try:
            self.state = 175
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 169
                self.parameter()

                self.state = 170
                self.match(MT22Parser.COMMA)
                self.state = 171
                self.parameterlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 173
                self.parameter()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockstateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LC(self):
            return self.getToken(MT22Parser.LC, 0)

        def RC(self):
            return self.getToken(MT22Parser.RC, 0)

        def blockstatemin(self):
            return self.getTypedRuleContext(MT22Parser.BlockstateminContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_blockstate




    def blockstate(self):

        localctx = MT22Parser.BlockstateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_blockstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.match(MT22Parser.LC)

            self.state = 178
            self.blockstatemin()
            self.state = 179
            self.match(MT22Parser.RC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockstateminContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blockstatemin(self):
            return self.getTypedRuleContext(MT22Parser.BlockstateminContext,0)


        def statement(self):
            return self.getTypedRuleContext(MT22Parser.StatementContext,0)


        def vardec(self):
            return self.getTypedRuleContext(MT22Parser.VardecContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_blockstatemin




    def blockstatemin(self):

        localctx = MT22Parser.BlockstateminContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_blockstatemin)
        try:
            self.state = 188
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.LC, MT22Parser.BREAK, MT22Parser.CONTINUE, MT22Parser.FOR, MT22Parser.IF, MT22Parser.RETURN, MT22Parser.WHILE, MT22Parser.DO, MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                if la_ == 1:
                    self.state = 181
                    self.statement()
                    pass

                elif la_ == 2:
                    self.state = 182
                    self.vardec()
                    pass


                self.state = 185
                self.blockstatemin()
                pass
            elif token in [MT22Parser.RC]:
                self.enterOuterAlt(localctx, 2)

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


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignstate(self):
            return self.getTypedRuleContext(MT22Parser.AssignstateContext,0)


        def ifstate(self):
            return self.getTypedRuleContext(MT22Parser.IfstateContext,0)


        def whilestate(self):
            return self.getTypedRuleContext(MT22Parser.WhilestateContext,0)


        def forstate(self):
            return self.getTypedRuleContext(MT22Parser.ForstateContext,0)


        def breakstate(self):
            return self.getTypedRuleContext(MT22Parser.BreakstateContext,0)


        def continuestate(self):
            return self.getTypedRuleContext(MT22Parser.ContinuestateContext,0)


        def returnstate(self):
            return self.getTypedRuleContext(MT22Parser.ReturnstateContext,0)


        def funcall(self):
            return self.getTypedRuleContext(MT22Parser.FuncallContext,0)


        def blockstate(self):
            return self.getTypedRuleContext(MT22Parser.BlockstateContext,0)


        def dowhilestate(self):
            return self.getTypedRuleContext(MT22Parser.DowhilestateContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_statement




    def statement(self):

        localctx = MT22Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_statement)
        try:
            self.state = 200
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 190
                self.assignstate()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 191
                self.ifstate()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 192
                self.whilestate()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 193
                self.forstate()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 194
                self.breakstate()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 195
                self.continuestate()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 196
                self.returnstate()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 197
                self.funcall()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 198
                self.blockstate()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 199
                self.dowhilestate()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalarvar(self):
            return self.getTypedRuleContext(MT22Parser.ScalarvarContext,0)


        def exprindex(self):
            return self.getTypedRuleContext(MT22Parser.ExprindexContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_lhs




    def lhs(self):

        localctx = MT22Parser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_lhs)
        try:
            self.state = 204
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                self.scalarvar()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
                self.exprindex()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScalarvarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_scalarvar




    def scalarvar(self):

        localctx = MT22Parser.ScalarvarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_scalarvar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(MT22Parser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignstateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(MT22Parser.LhsContext,0)


        def ASSIGNOP(self):
            return self.getToken(MT22Parser.ASSIGNOP, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def SEMICOLON(self):
            return self.getToken(MT22Parser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_assignstate




    def assignstate(self):

        localctx = MT22Parser.AssignstateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_assignstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.lhs()
            self.state = 209
            self.match(MT22Parser.ASSIGNOP)
            self.state = 210
            self.expr()
            self.state = 211
            self.match(MT22Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MT22Parser.IF, 0)

        def LP(self):
            return self.getToken(MT22Parser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def RP(self):
            return self.getToken(MT22Parser.RP, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.StatementContext)
            else:
                return self.getTypedRuleContext(MT22Parser.StatementContext,i)


        def ELSE(self):
            return self.getToken(MT22Parser.ELSE, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_ifstate




    def ifstate(self):

        localctx = MT22Parser.IfstateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_ifstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(MT22Parser.IF)
            self.state = 214
            self.match(MT22Parser.LP)
            self.state = 215
            self.expr()
            self.state = 216
            self.match(MT22Parser.RP)
            self.state = 217
            self.statement()
            self.state = 220
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 218
                self.match(MT22Parser.ELSE)
                self.state = 219
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhilestateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(MT22Parser.WHILE, 0)

        def LP(self):
            return self.getToken(MT22Parser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def RP(self):
            return self.getToken(MT22Parser.RP, 0)

        def statement(self):
            return self.getTypedRuleContext(MT22Parser.StatementContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_whilestate




    def whilestate(self):

        localctx = MT22Parser.WhilestateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_whilestate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(MT22Parser.WHILE)
            self.state = 223
            self.match(MT22Parser.LP)
            self.state = 224
            self.expr()
            self.state = 225
            self.match(MT22Parser.RP)
            self.state = 226
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DowhilestateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(MT22Parser.DO, 0)

        def blockstate(self):
            return self.getTypedRuleContext(MT22Parser.BlockstateContext,0)


        def WHILE(self):
            return self.getToken(MT22Parser.WHILE, 0)

        def LP(self):
            return self.getToken(MT22Parser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def RP(self):
            return self.getToken(MT22Parser.RP, 0)

        def SEMICOLON(self):
            return self.getToken(MT22Parser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_dowhilestate




    def dowhilestate(self):

        localctx = MT22Parser.DowhilestateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_dowhilestate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.match(MT22Parser.DO)
            self.state = 229
            self.blockstate()
            self.state = 230
            self.match(MT22Parser.WHILE)
            self.state = 231
            self.match(MT22Parser.LP)
            self.state = 232
            self.expr()
            self.state = 233
            self.match(MT22Parser.RP)
            self.state = 234
            self.match(MT22Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MT22Parser.FOR, 0)

        def LP(self):
            return self.getToken(MT22Parser.LP, 0)

        def lhs(self):
            return self.getTypedRuleContext(MT22Parser.LhsContext,0)


        def ASSIGNOP(self):
            return self.getToken(MT22Parser.ASSIGNOP, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.ExprContext)
            else:
                return self.getTypedRuleContext(MT22Parser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMA)
            else:
                return self.getToken(MT22Parser.COMMA, i)

        def RP(self):
            return self.getToken(MT22Parser.RP, 0)

        def statement(self):
            return self.getTypedRuleContext(MT22Parser.StatementContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_forstate




    def forstate(self):

        localctx = MT22Parser.ForstateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_forstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.match(MT22Parser.FOR)
            self.state = 237
            self.match(MT22Parser.LP)
            self.state = 238
            self.lhs()
            self.state = 239
            self.match(MT22Parser.ASSIGNOP)
            self.state = 240
            self.expr()
            self.state = 241
            self.match(MT22Parser.COMMA)
            self.state = 242
            self.expr()
            self.state = 243
            self.match(MT22Parser.COMMA)
            self.state = 244
            self.expr()
            self.state = 245
            self.match(MT22Parser.RP)
            self.state = 246
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakstateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MT22Parser.BREAK, 0)

        def SEMICOLON(self):
            return self.getToken(MT22Parser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_breakstate




    def breakstate(self):

        localctx = MT22Parser.BreakstateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_breakstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.match(MT22Parser.BREAK)
            self.state = 249
            self.match(MT22Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinuestateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MT22Parser.CONTINUE, 0)

        def SEMICOLON(self):
            return self.getToken(MT22Parser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_continuestate




    def continuestate(self):

        localctx = MT22Parser.ContinuestateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_continuestate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.match(MT22Parser.CONTINUE)
            self.state = 252
            self.match(MT22Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MT22Parser.RETURN, 0)

        def SEMICOLON(self):
            return self.getToken(MT22Parser.SEMICOLON, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_returnstate




    def returnstate(self):

        localctx = MT22Parser.ReturnstateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_returnstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.match(MT22Parser.RETURN)
            self.state = 257
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.SUBOP, MT22Parser.NOTOP, MT22Parser.LP, MT22Parser.LC, MT22Parser.INTLIT, MT22Parser.BOOLLIT, MT22Parser.FLOATLIT, MT22Parser.STRINGLIT, MT22Parser.IDENTIFIER]:
                self.state = 255
                self.expr()
                pass
            elif token in [MT22Parser.SEMICOLON]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 259
            self.match(MT22Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(MT22Parser.LP, 0)

        def exprlist(self):
            return self.getTypedRuleContext(MT22Parser.ExprlistContext,0)


        def RP(self):
            return self.getToken(MT22Parser.RP, 0)

        def SEMICOLON(self):
            return self.getToken(MT22Parser.SEMICOLON, 0)

        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_funcall




    def funcall(self):

        localctx = MT22Parser.FuncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_funcall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.match(MT22Parser.IDENTIFIER)
            self.state = 262
            self.match(MT22Parser.LP)
            self.state = 263
            self.exprlist()
            self.state = 264
            self.match(MT22Parser.RP)
            self.state = 265
            self.match(MT22Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraytypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(MT22Parser.ARRAY, 0)

        def LS(self):
            return self.getToken(MT22Parser.LS, 0)

        def dimensions(self):
            return self.getTypedRuleContext(MT22Parser.DimensionsContext,0)


        def RS(self):
            return self.getToken(MT22Parser.RS, 0)

        def OF(self):
            return self.getToken(MT22Parser.OF, 0)

        def atomictype(self):
            return self.getTypedRuleContext(MT22Parser.AtomictypeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_arraytype




    def arraytype(self):

        localctx = MT22Parser.ArraytypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_arraytype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.match(MT22Parser.ARRAY)
            self.state = 268
            self.match(MT22Parser.LS)
            self.state = 269
            self.dimensions()
            self.state = 270
            self.match(MT22Parser.RS)
            self.state = 271
            self.match(MT22Parser.OF)
            self.state = 272
            self.atomictype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimensionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(MT22Parser.INTLIT, 0)

        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def dimensions(self):
            return self.getTypedRuleContext(MT22Parser.DimensionsContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_dimensions




    def dimensions(self):

        localctx = MT22Parser.DimensionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_dimensions)
        try:
            self.state = 278
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 274
                self.match(MT22Parser.INTLIT)
                self.state = 275
                self.match(MT22Parser.COMMA)
                self.state = 276
                self.dimensions()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 277
                self.match(MT22Parser.INTLIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomictypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(MT22Parser.INTEGER, 0)

        def BOOLEAN(self):
            return self.getToken(MT22Parser.BOOLEAN, 0)

        def FLOAT(self):
            return self.getToken(MT22Parser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MT22Parser.STRING, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_atomictype




    def atomictype(self):

        localctx = MT22Parser.AtomictypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_atomictype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.BOOLEAN) | (1 << MT22Parser.FLOAT) | (1 << MT22Parser.INTEGER) | (1 << MT22Parser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(MT22Parser.INTLIT, 0)

        def BOOLLIT(self):
            return self.getToken(MT22Parser.BOOLLIT, 0)

        def STRINGLIT(self):
            return self.getToken(MT22Parser.STRINGLIT, 0)

        def FLOATLIT(self):
            return self.getToken(MT22Parser.FLOATLIT, 0)

        def arraylit(self):
            return self.getTypedRuleContext(MT22Parser.ArraylitContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_literal




    def literal(self):

        localctx = MT22Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_literal)
        try:
            self.state = 287
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 282
                self.match(MT22Parser.INTLIT)
                pass
            elif token in [MT22Parser.BOOLLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 283
                self.match(MT22Parser.BOOLLIT)
                pass
            elif token in [MT22Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 284
                self.match(MT22Parser.STRINGLIT)
                pass
            elif token in [MT22Parser.FLOATLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 285
                self.match(MT22Parser.FLOATLIT)
                pass
            elif token in [MT22Parser.LC]:
                self.enterOuterAlt(localctx, 5)
                self.state = 286
                self.arraylit()
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


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Expr1Context)
            else:
                return self.getTypedRuleContext(MT22Parser.Expr1Context,i)


        def STRINGOP(self):
            return self.getToken(MT22Parser.STRINGOP, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr




    def expr(self):

        localctx = MT22Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_expr)
        try:
            self.state = 294
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 289
                self.expr1()

                self.state = 290
                self.match(MT22Parser.STRINGOP)
                self.state = 291
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 293
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Expr2Context)
            else:
                return self.getTypedRuleContext(MT22Parser.Expr2Context,i)


        def GTOP(self):
            return self.getToken(MT22Parser.GTOP, 0)

        def LTOP(self):
            return self.getToken(MT22Parser.LTOP, 0)

        def GTEOP(self):
            return self.getToken(MT22Parser.GTEOP, 0)

        def LTEOP(self):
            return self.getToken(MT22Parser.LTEOP, 0)

        def EQOP(self):
            return self.getToken(MT22Parser.EQOP, 0)

        def NEOP(self):
            return self.getToken(MT22Parser.NEOP, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr1




    def expr1(self):

        localctx = MT22Parser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 301
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 296
                self.expr2(0)
                self.state = 297
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.EQOP) | (1 << MT22Parser.NEOP) | (1 << MT22Parser.GTOP) | (1 << MT22Parser.LTOP) | (1 << MT22Parser.GTEOP) | (1 << MT22Parser.LTEOP))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 298
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 300
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(MT22Parser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(MT22Parser.Expr2Context,0)


        def ANDOP(self):
            return self.getToken(MT22Parser.ANDOP, 0)

        def OROP(self):
            return self.getToken(MT22Parser.OROP, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr2



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 311
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 306
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 307
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.ANDOP or _la==MT22Parser.OROP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 308
                    self.expr3(0) 
                self.state = 313
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(MT22Parser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(MT22Parser.Expr3Context,0)


        def ADDOP(self):
            return self.getToken(MT22Parser.ADDOP, 0)

        def SUBOP(self):
            return self.getToken(MT22Parser.SUBOP, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr3



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 322
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 317
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 318
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.ADDOP or _la==MT22Parser.SUBOP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 319
                    self.expr4(0) 
                self.state = 324
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(MT22Parser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(MT22Parser.Expr4Context,0)


        def MULOP(self):
            return self.getToken(MT22Parser.MULOP, 0)

        def DIVOP(self):
            return self.getToken(MT22Parser.DIVOP, 0)

        def MODOP(self):
            return self.getToken(MT22Parser.MODOP, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr4



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 333
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 328
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 329
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.MULOP) | (1 << MT22Parser.DIVOP) | (1 << MT22Parser.MODOP))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 330
                    self.expr5() 
                self.state = 335
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(MT22Parser.Expr5Context,0)


        def NOTOP(self):
            return self.getToken(MT22Parser.NOTOP, 0)

        def expr6(self):
            return self.getTypedRuleContext(MT22Parser.Expr6Context,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expr5




    def expr5(self):

        localctx = MT22Parser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_expr5)
        try:
            self.state = 339
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.NOTOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 336
                self.match(MT22Parser.NOTOP)
                self.state = 337
                self.expr5()
                pass
            elif token in [MT22Parser.SUBOP, MT22Parser.LP, MT22Parser.LC, MT22Parser.INTLIT, MT22Parser.BOOLLIT, MT22Parser.FLOATLIT, MT22Parser.STRINGLIT, MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 338
                self.expr6()
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


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr6(self):
            return self.getTypedRuleContext(MT22Parser.Expr6Context,0)


        def SUBOP(self):
            return self.getToken(MT22Parser.SUBOP, 0)

        def expr7(self):
            return self.getTypedRuleContext(MT22Parser.Expr7Context,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expr6




    def expr6(self):

        localctx = MT22Parser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_expr6)
        try:
            self.state = 344
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.SUBOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 341
                self.match(MT22Parser.SUBOP)
                self.state = 342
                self.expr6()
                pass
            elif token in [MT22Parser.LP, MT22Parser.LC, MT22Parser.INTLIT, MT22Parser.BOOLLIT, MT22Parser.FLOATLIT, MT22Parser.STRINGLIT, MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 343
                self.expr7()
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


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(MT22Parser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(MT22Parser.FLOATLIT, 0)

        def BOOLLIT(self):
            return self.getToken(MT22Parser.BOOLLIT, 0)

        def STRINGLIT(self):
            return self.getToken(MT22Parser.STRINGLIT, 0)

        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def exprindex(self):
            return self.getTypedRuleContext(MT22Parser.ExprindexContext,0)


        def LP(self):
            return self.getToken(MT22Parser.LP, 0)

        def exprlist(self):
            return self.getTypedRuleContext(MT22Parser.ExprlistContext,0)


        def RP(self):
            return self.getToken(MT22Parser.RP, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def arraylit(self):
            return self.getTypedRuleContext(MT22Parser.ArraylitContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expr7




    def expr7(self):

        localctx = MT22Parser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_expr7)
        try:
            self.state = 362
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 346
                self.match(MT22Parser.INTLIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 347
                self.match(MT22Parser.FLOATLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 348
                self.match(MT22Parser.BOOLLIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 349
                self.match(MT22Parser.STRINGLIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 350
                self.match(MT22Parser.IDENTIFIER)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 351
                self.exprindex()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 352
                self.match(MT22Parser.IDENTIFIER)
                self.state = 353
                self.match(MT22Parser.LP)
                self.state = 354
                self.exprlist()
                self.state = 355
                self.match(MT22Parser.RP)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 357
                self.match(MT22Parser.LP)
                self.state = 358
                self.expr()
                self.state = 359
                self.match(MT22Parser.RP)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 361
                self.arraylit()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprindexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def LS(self):
            return self.getToken(MT22Parser.LS, 0)

        def exprlist(self):
            return self.getTypedRuleContext(MT22Parser.ExprlistContext,0)


        def RS(self):
            return self.getToken(MT22Parser.RS, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_exprindex




    def exprindex(self):

        localctx = MT22Parser.ExprindexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_exprindex)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self.match(MT22Parser.IDENTIFIER)
            self.state = 365
            self.match(MT22Parser.LS)
            self.state = 366
            self.exprlist()
            self.state = 367
            self.match(MT22Parser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraylitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LC(self):
            return self.getToken(MT22Parser.LC, 0)

        def RC(self):
            return self.getToken(MT22Parser.RC, 0)

        def exprlist(self):
            return self.getTypedRuleContext(MT22Parser.ExprlistContext,0)


        def emptycurl(self):
            return self.getTypedRuleContext(MT22Parser.EmptycurlContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_arraylit




    def arraylit(self):

        localctx = MT22Parser.ArraylitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_arraylit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            self.match(MT22Parser.LC)
            self.state = 372
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 370
                self.exprlist()
                pass

            elif la_ == 2:
                self.state = 371
                self.emptycurl()
                pass


            self.state = 374
            self.match(MT22Parser.RC)
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
        self._predicates[33] = self.expr2_sempred
        self._predicates[34] = self.expr3_sempred
        self._predicates[35] = self.expr4_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




