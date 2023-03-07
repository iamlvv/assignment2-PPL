# Generated from c:\Users\levan\OneDrive\Documents\GitHub\assignment2-PPL\src\main\mt22\parser\MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2<")
        buf.write("\u0240\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\3\2\3\2\3\2\3\2\7\2\u00b8\n")
        buf.write("\2\f\2\16\2\u00bb\13\2\3\2\5\2\u00be\n\2\3\2\3\2\3\3\3")
        buf.write("\3\3\3\3\3\7\3\u00c6\n\3\f\3\16\3\u00c9\13\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t")
        buf.write("\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17")
        buf.write("\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24")
        buf.write("\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32")
        buf.write("\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37")
        buf.write("\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3\'")
        buf.write("\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3,\3-\3")
        buf.write("-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63")
        buf.write("\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\38\78\u0142")
        buf.write("\n8\f8\168\u0145\138\38\38\68\u0149\n8\r8\168\u014a\7")
        buf.write("8\u014d\n8\f8\168\u0150\138\38\58\u0153\n8\39\39\39\3")
        buf.write("9\39\39\39\39\39\59\u015e\n9\3:\3:\3:\7:\u0163\n:\f:\16")
        buf.write(":\u0166\13:\5:\u0168\n:\3:\3:\5:\u016c\n:\3:\6:\u016f")
        buf.write("\n:\r:\16:\u0170\5:\u0173\n:\3:\3:\3:\3:\7:\u0179\n:\f")
        buf.write(":\16:\u017c\13:\3:\3:\5:\u0180\n:\3:\6:\u0183\n:\r:\16")
        buf.write(":\u0184\5:\u0187\n:\3;\3;\3;\3;\7;\u018d\n;\f;\16;\u0190")
        buf.write("\13;\3;\3;\3;\3<\3<\3<\3=\3=\3>\3>\3>\3>\3>\3?\3?\3?\3")
        buf.write("?\3?\3?\3@\3@\3@\3@\3@\3@\3@\3@\3A\3A\3A\3A\3A\3A\3A\3")
        buf.write("A\3A\3B\3B\3B\3B\3B\3C\3C\3C\3C\3C\3C\3D\3D\3D\3D\3E\3")
        buf.write("E\3E\3E\3E\3E\3E\3E\3E\3F\3F\3F\3G\3G\3G\3G\3G\3G\3G\3")
        buf.write("G\3H\3H\3H\3H\3H\3H\3H\3H\3I\3I\3I\3I\3J\3J\3J\3J\3J\3")
        buf.write("J\3J\3K\3K\3K\3K\3K\3K\3K\3L\3L\3L\3L\3L\3M\3M\3M\3M\3")
        buf.write("M\3M\3N\3N\3N\3N\3N\3O\3O\3O\3O\3O\3O\3P\3P\3P\3Q\3Q\3")
        buf.write("Q\3R\3R\3R\3R\3R\3R\3S\3S\7S\u0217\nS\fS\16S\u021a\13")
        buf.write("S\3T\6T\u021d\nT\rT\16T\u021e\3T\3T\3U\3U\5U\u0225\nU")
        buf.write("\3V\3V\3V\3W\3W\7W\u022c\nW\fW\16W\u022f\13W\3W\3W\3X")
        buf.write("\3X\7X\u0235\nX\fX\16X\u0238\13X\3X\3X\3X\3X\3Y\3Y\3Y")
        buf.write("\3\u00c7\2Z\3\3\5\4\7\2\t\2\13\2\r\2\17\2\21\2\23\2\25")
        buf.write("\2\27\2\31\2\33\2\35\2\37\2!\2#\2%\2\'\2)\2+\2-\2/\2\61")
        buf.write("\2\63\2\65\2\67\29\2;\5=\6?\7A\bC\tE\nG\13I\fK\rM\16O")
        buf.write("\17Q\20S\21U\22W\23Y\24[\25]\26_\27a\30c\31e\32g\33i\34")
        buf.write("k\35m\36o\37q s!u\"w\2y\2{#}$\177%\u0081&\u0083\'\u0085")
        buf.write("(\u0087)\u0089*\u008b+\u008d,\u008f-\u0091.\u0093/\u0095")
        buf.write("\60\u0097\61\u0099\62\u009b\63\u009d\64\u009f\65\u00a1")
        buf.write("\66\u00a3\67\u00a58\u00a79\u00a9\2\u00ab\2\u00ad:\u00af")
        buf.write(";\u00b1<\3\2+\3\2\f\f\3\3\f\f\4\2CCcc\4\2DDdd\4\2EEee")
        buf.write("\4\2FFff\4\2GGgg\4\2HHhh\4\2IIii\4\2JJjj\4\2KKkk\4\2L")
        buf.write("Lll\4\2MMmm\4\2NNnn\4\2OOoo\4\2PPpp\4\2QQqq\4\2RRrr\4")
        buf.write("\2SSss\4\2TTtt\4\2UUuu\4\2VVvv\4\2WWww\4\2XXxx\4\2YYy")
        buf.write("y\4\2ZZzz\4\2[[{{\4\2\\\\||\3\2\62\62\3\2\63;\3\2\62;")
        buf.write("\3\2aa\3\2\60\60\4\2--//\n\2$$))^^ddhhppttvv\6\2\f\f\17")
        buf.write("\17$$^^\n\2$$\61\61^^ddhhppttvv\5\2\2!$$^^\5\2C\\aac|")
        buf.write("\6\2\62;C\\aac|\5\2\n\f\16\17\"\"\2\u0238\2\3\3\2\2\2")
        buf.write("\2\5\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2")
        buf.write("\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2")
        buf.write("\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3")
        buf.write("\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_")
        buf.write("\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2")
        buf.write("i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2")
        buf.write("\2s\3\2\2\2\2u\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2")
        buf.write("\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2")
        buf.write("\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d")
        buf.write("\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2")
        buf.write("\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b")
        buf.write("\3\2\2\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\2\u00a1\3\2\2")
        buf.write("\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7\3\2\2\2\2\u00ad")
        buf.write("\3\2\2\2\2\u00af\3\2\2\2\2\u00b1\3\2\2\2\3\u00b3\3\2\2")
        buf.write("\2\5\u00c1\3\2\2\2\7\u00cf\3\2\2\2\t\u00d1\3\2\2\2\13")
        buf.write("\u00d3\3\2\2\2\r\u00d5\3\2\2\2\17\u00d7\3\2\2\2\21\u00d9")
        buf.write("\3\2\2\2\23\u00db\3\2\2\2\25\u00dd\3\2\2\2\27\u00df\3")
        buf.write("\2\2\2\31\u00e1\3\2\2\2\33\u00e3\3\2\2\2\35\u00e5\3\2")
        buf.write("\2\2\37\u00e7\3\2\2\2!\u00e9\3\2\2\2#\u00eb\3\2\2\2%\u00ed")
        buf.write("\3\2\2\2\'\u00ef\3\2\2\2)\u00f1\3\2\2\2+\u00f3\3\2\2\2")
        buf.write("-\u00f5\3\2\2\2/\u00f7\3\2\2\2\61\u00f9\3\2\2\2\63\u00fb")
        buf.write("\3\2\2\2\65\u00fd\3\2\2\2\67\u00ff\3\2\2\29\u0101\3\2")
        buf.write("\2\2;\u0103\3\2\2\2=\u0105\3\2\2\2?\u0107\3\2\2\2A\u0109")
        buf.write("\3\2\2\2C\u010b\3\2\2\2E\u010d\3\2\2\2G\u010f\3\2\2\2")
        buf.write("I\u0112\3\2\2\2K\u0115\3\2\2\2M\u0117\3\2\2\2O\u0119\3")
        buf.write("\2\2\2Q\u011c\3\2\2\2S\u011f\3\2\2\2U\u0122\3\2\2\2W\u0125")
        buf.write("\3\2\2\2Y\u0128\3\2\2\2[\u012a\3\2\2\2]\u012c\3\2\2\2")
        buf.write("_\u012e\3\2\2\2a\u0130\3\2\2\2c\u0132\3\2\2\2e\u0134\3")
        buf.write("\2\2\2g\u0136\3\2\2\2i\u0138\3\2\2\2k\u013a\3\2\2\2m\u013c")
        buf.write("\3\2\2\2o\u0152\3\2\2\2q\u015d\3\2\2\2s\u0186\3\2\2\2")
        buf.write("u\u0188\3\2\2\2w\u0194\3\2\2\2y\u0197\3\2\2\2{\u0199\3")
        buf.write("\2\2\2}\u019e\3\2\2\2\177\u01a4\3\2\2\2\u0081\u01ac\3")
        buf.write("\2\2\2\u0083\u01b5\3\2\2\2\u0085\u01ba\3\2\2\2\u0087\u01c0")
        buf.write("\3\2\2\2\u0089\u01c4\3\2\2\2\u008b\u01cd\3\2\2\2\u008d")
        buf.write("\u01d0\3\2\2\2\u008f\u01d8\3\2\2\2\u0091\u01e0\3\2\2\2")
        buf.write("\u0093\u01e4\3\2\2\2\u0095\u01eb\3\2\2\2\u0097\u01f2\3")
        buf.write("\2\2\2\u0099\u01f7\3\2\2\2\u009b\u01fd\3\2\2\2\u009d\u0202")
        buf.write("\3\2\2\2\u009f\u0208\3\2\2\2\u00a1\u020b\3\2\2\2\u00a3")
        buf.write("\u020e\3\2\2\2\u00a5\u0214\3\2\2\2\u00a7\u021c\3\2\2\2")
        buf.write("\u00a9\u0224\3\2\2\2\u00ab\u0226\3\2\2\2\u00ad\u0229\3")
        buf.write("\2\2\2\u00af\u0232\3\2\2\2\u00b1\u023d\3\2\2\2\u00b3\u00b4")
        buf.write("\7\61\2\2\u00b4\u00b5\7\61\2\2\u00b5\u00b9\3\2\2\2\u00b6")
        buf.write("\u00b8\n\2\2\2\u00b7\u00b6\3\2\2\2\u00b8\u00bb\3\2\2\2")
        buf.write("\u00b9\u00b7\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00bd\3")
        buf.write("\2\2\2\u00bb\u00b9\3\2\2\2\u00bc\u00be\t\3\2\2\u00bd\u00bc")
        buf.write("\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf\u00c0\b\2\2\2\u00c0")
        buf.write("\4\3\2\2\2\u00c1\u00c2\7\61\2\2\u00c2\u00c3\7,\2\2\u00c3")
        buf.write("\u00c7\3\2\2\2\u00c4\u00c6\13\2\2\2\u00c5\u00c4\3\2\2")
        buf.write("\2\u00c6\u00c9\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c7\u00c5")
        buf.write("\3\2\2\2\u00c8\u00ca\3\2\2\2\u00c9\u00c7\3\2\2\2\u00ca")
        buf.write("\u00cb\7,\2\2\u00cb\u00cc\7\61\2\2\u00cc\u00cd\3\2\2\2")
        buf.write("\u00cd\u00ce\b\3\2\2\u00ce\6\3\2\2\2\u00cf\u00d0\t\4\2")
        buf.write("\2\u00d0\b\3\2\2\2\u00d1\u00d2\t\5\2\2\u00d2\n\3\2\2\2")
        buf.write("\u00d3\u00d4\t\6\2\2\u00d4\f\3\2\2\2\u00d5\u00d6\t\7\2")
        buf.write("\2\u00d6\16\3\2\2\2\u00d7\u00d8\t\b\2\2\u00d8\20\3\2\2")
        buf.write("\2\u00d9\u00da\t\t\2\2\u00da\22\3\2\2\2\u00db\u00dc\t")
        buf.write("\n\2\2\u00dc\24\3\2\2\2\u00dd\u00de\t\13\2\2\u00de\26")
        buf.write("\3\2\2\2\u00df\u00e0\t\f\2\2\u00e0\30\3\2\2\2\u00e1\u00e2")
        buf.write("\t\r\2\2\u00e2\32\3\2\2\2\u00e3\u00e4\t\16\2\2\u00e4\34")
        buf.write("\3\2\2\2\u00e5\u00e6\t\17\2\2\u00e6\36\3\2\2\2\u00e7\u00e8")
        buf.write("\t\20\2\2\u00e8 \3\2\2\2\u00e9\u00ea\t\21\2\2\u00ea\"")
        buf.write("\3\2\2\2\u00eb\u00ec\t\22\2\2\u00ec$\3\2\2\2\u00ed\u00ee")
        buf.write("\t\23\2\2\u00ee&\3\2\2\2\u00ef\u00f0\t\24\2\2\u00f0(\3")
        buf.write("\2\2\2\u00f1\u00f2\t\25\2\2\u00f2*\3\2\2\2\u00f3\u00f4")
        buf.write("\t\26\2\2\u00f4,\3\2\2\2\u00f5\u00f6\t\27\2\2\u00f6.\3")
        buf.write("\2\2\2\u00f7\u00f8\t\30\2\2\u00f8\60\3\2\2\2\u00f9\u00fa")
        buf.write("\t\31\2\2\u00fa\62\3\2\2\2\u00fb\u00fc\t\32\2\2\u00fc")
        buf.write("\64\3\2\2\2\u00fd\u00fe\t\33\2\2\u00fe\66\3\2\2\2\u00ff")
        buf.write("\u0100\t\34\2\2\u01008\3\2\2\2\u0101\u0102\t\35\2\2\u0102")
        buf.write(":\3\2\2\2\u0103\u0104\7?\2\2\u0104<\3\2\2\2\u0105\u0106")
        buf.write("\7-\2\2\u0106>\3\2\2\2\u0107\u0108\7/\2\2\u0108@\3\2\2")
        buf.write("\2\u0109\u010a\7,\2\2\u010aB\3\2\2\2\u010b\u010c\7\61")
        buf.write("\2\2\u010cD\3\2\2\2\u010d\u010e\7\'\2\2\u010eF\3\2\2\2")
        buf.write("\u010f\u0110\7?\2\2\u0110\u0111\7?\2\2\u0111H\3\2\2\2")
        buf.write("\u0112\u0113\7#\2\2\u0113\u0114\7?\2\2\u0114J\3\2\2\2")
        buf.write("\u0115\u0116\7@\2\2\u0116L\3\2\2\2\u0117\u0118\7>\2\2")
        buf.write("\u0118N\3\2\2\2\u0119\u011a\7@\2\2\u011a\u011b\7?\2\2")
        buf.write("\u011bP\3\2\2\2\u011c\u011d\7>\2\2\u011d\u011e\7?\2\2")
        buf.write("\u011eR\3\2\2\2\u011f\u0120\7(\2\2\u0120\u0121\7(\2\2")
        buf.write("\u0121T\3\2\2\2\u0122\u0123\7~\2\2\u0123\u0124\7~\2\2")
        buf.write("\u0124V\3\2\2\2\u0125\u0126\7<\2\2\u0126\u0127\7<\2\2")
        buf.write("\u0127X\3\2\2\2\u0128\u0129\7#\2\2\u0129Z\3\2\2\2\u012a")
        buf.write("\u012b\7*\2\2\u012b\\\3\2\2\2\u012c\u012d\7+\2\2\u012d")
        buf.write("^\3\2\2\2\u012e\u012f\7}\2\2\u012f`\3\2\2\2\u0130\u0131")
        buf.write("\7\177\2\2\u0131b\3\2\2\2\u0132\u0133\7]\2\2\u0133d\3")
        buf.write("\2\2\2\u0134\u0135\7_\2\2\u0135f\3\2\2\2\u0136\u0137\7")
        buf.write("=\2\2\u0137h\3\2\2\2\u0138\u0139\7.\2\2\u0139j\3\2\2\2")
        buf.write("\u013a\u013b\7\60\2\2\u013bl\3\2\2\2\u013c\u013d\7<\2")
        buf.write("\2\u013dn\3\2\2\2\u013e\u0153\t\36\2\2\u013f\u0143\t\37")
        buf.write("\2\2\u0140\u0142\t \2\2\u0141\u0140\3\2\2\2\u0142\u0145")
        buf.write("\3\2\2\2\u0143\u0141\3\2\2\2\u0143\u0144\3\2\2\2\u0144")
        buf.write("\u014e\3\2\2\2\u0145\u0143\3\2\2\2\u0146\u0148\t!\2\2")
        buf.write("\u0147\u0149\t \2\2\u0148\u0147\3\2\2\2\u0149\u014a\3")
        buf.write("\2\2\2\u014a\u0148\3\2\2\2\u014a\u014b\3\2\2\2\u014b\u014d")
        buf.write("\3\2\2\2\u014c\u0146\3\2\2\2\u014d\u0150\3\2\2\2\u014e")
        buf.write("\u014c\3\2\2\2\u014e\u014f\3\2\2\2\u014f\u0151\3\2\2\2")
        buf.write("\u0150\u014e\3\2\2\2\u0151\u0153\b8\3\2\u0152\u013e\3")
        buf.write("\2\2\2\u0152\u013f\3\2\2\2\u0153p\3\2\2\2\u0154\u0155")
        buf.write("\7v\2\2\u0155\u0156\7t\2\2\u0156\u0157\7w\2\2\u0157\u015e")
        buf.write("\7g\2\2\u0158\u0159\7h\2\2\u0159\u015a\7c\2\2\u015a\u015b")
        buf.write("\7n\2\2\u015b\u015c\7u\2\2\u015c\u015e\7g\2\2\u015d\u0154")
        buf.write("\3\2\2\2\u015d\u0158\3\2\2\2\u015er\3\2\2\2\u015f\u0167")
        buf.write("\5o8\2\u0160\u0164\t\"\2\2\u0161\u0163\t \2\2\u0162\u0161")
        buf.write("\3\2\2\2\u0163\u0166\3\2\2\2\u0164\u0162\3\2\2\2\u0164")
        buf.write("\u0165\3\2\2\2\u0165\u0168\3\2\2\2\u0166\u0164\3\2\2\2")
        buf.write("\u0167\u0160\3\2\2\2\u0167\u0168\3\2\2\2\u0168\u0172\3")
        buf.write("\2\2\2\u0169\u016b\t\b\2\2\u016a\u016c\t#\2\2\u016b\u016a")
        buf.write("\3\2\2\2\u016b\u016c\3\2\2\2\u016c\u016e\3\2\2\2\u016d")
        buf.write("\u016f\t \2\2\u016e\u016d\3\2\2\2\u016f\u0170\3\2\2\2")
        buf.write("\u0170\u016e\3\2\2\2\u0170\u0171\3\2\2\2\u0171\u0173\3")
        buf.write("\2\2\2\u0172\u0169\3\2\2\2\u0172\u0173\3\2\2\2\u0173\u0174")
        buf.write("\3\2\2\2\u0174\u0175\b:\4\2\u0175\u0187\3\2\2\2\u0176")
        buf.write("\u017a\t\"\2\2\u0177\u0179\t \2\2\u0178\u0177\3\2\2\2")
        buf.write("\u0179\u017c\3\2\2\2\u017a\u0178\3\2\2\2\u017a\u017b\3")
        buf.write("\2\2\2\u017b\u017d\3\2\2\2\u017c\u017a\3\2\2\2\u017d\u017f")
        buf.write("\t\b\2\2\u017e\u0180\t#\2\2\u017f\u017e\3\2\2\2\u017f")
        buf.write("\u0180\3\2\2\2\u0180\u0182\3\2\2\2\u0181\u0183\t \2\2")
        buf.write("\u0182\u0181\3\2\2\2\u0183\u0184\3\2\2\2\u0184\u0182\3")
        buf.write("\2\2\2\u0184\u0185\3\2\2\2\u0185\u0187\3\2\2\2\u0186\u015f")
        buf.write("\3\2\2\2\u0186\u0176\3\2\2\2\u0187t\3\2\2\2\u0188\u018e")
        buf.write("\7$\2\2\u0189\u018a\7^\2\2\u018a\u018d\t$\2\2\u018b\u018d")
        buf.write("\n%\2\2\u018c\u0189\3\2\2\2\u018c\u018b\3\2\2\2\u018d")
        buf.write("\u0190\3\2\2\2\u018e\u018c\3\2\2\2\u018e\u018f\3\2\2\2")
        buf.write("\u018f\u0191\3\2\2\2\u0190\u018e\3\2\2\2\u0191\u0192\7")
        buf.write("$\2\2\u0192\u0193\b;\5\2\u0193v\3\2\2\2\u0194\u0195\7")
        buf.write("^\2\2\u0195\u0196\t&\2\2\u0196x\3\2\2\2\u0197\u0198\n")
        buf.write("\'\2\2\u0198z\3\2\2\2\u0199\u019a\5\7\4\2\u019a\u019b")
        buf.write("\5/\30\2\u019b\u019c\5-\27\2\u019c\u019d\5#\22\2\u019d")
        buf.write("|\3\2\2\2\u019e\u019f\5\t\5\2\u019f\u01a0\5)\25\2\u01a0")
        buf.write("\u01a1\5\17\b\2\u01a1\u01a2\5\7\4\2\u01a2\u01a3\5\33\16")
        buf.write("\2\u01a3~\3\2\2\2\u01a4\u01a5\5\t\5\2\u01a5\u01a6\5#\22")
        buf.write("\2\u01a6\u01a7\5#\22\2\u01a7\u01a8\5\35\17\2\u01a8\u01a9")
        buf.write("\5\17\b\2\u01a9\u01aa\5\7\4\2\u01aa\u01ab\5!\21\2\u01ab")
        buf.write("\u0080\3\2\2\2\u01ac\u01ad\5\13\6\2\u01ad\u01ae\5#\22")
        buf.write("\2\u01ae\u01af\5!\21\2\u01af\u01b0\5-\27\2\u01b0\u01b1")
        buf.write("\5\27\f\2\u01b1\u01b2\5!\21\2\u01b2\u01b3\5/\30\2\u01b3")
        buf.write("\u01b4\5\17\b\2\u01b4\u0082\3\2\2\2\u01b5\u01b6\5\17\b")
        buf.write("\2\u01b6\u01b7\5\35\17\2\u01b7\u01b8\5+\26\2\u01b8\u01b9")
        buf.write("\5\17\b\2\u01b9\u0084\3\2\2\2\u01ba\u01bb\5\21\t\2\u01bb")
        buf.write("\u01bc\5\35\17\2\u01bc\u01bd\5#\22\2\u01bd\u01be\5\7\4")
        buf.write("\2\u01be\u01bf\5-\27\2\u01bf\u0086\3\2\2\2\u01c0\u01c1")
        buf.write("\5\21\t\2\u01c1\u01c2\5#\22\2\u01c2\u01c3\5)\25\2\u01c3")
        buf.write("\u0088\3\2\2\2\u01c4\u01c5\5\21\t\2\u01c5\u01c6\5/\30")
        buf.write("\2\u01c6\u01c7\5!\21\2\u01c7\u01c8\5\13\6\2\u01c8\u01c9")
        buf.write("\5-\27\2\u01c9\u01ca\5\27\f\2\u01ca\u01cb\5#\22\2\u01cb")
        buf.write("\u01cc\5!\21\2\u01cc\u008a\3\2\2\2\u01cd\u01ce\5\27\f")
        buf.write("\2\u01ce\u01cf\5\21\t\2\u01cf\u008c\3\2\2\2\u01d0\u01d1")
        buf.write("\5\27\f\2\u01d1\u01d2\5!\21\2\u01d2\u01d3\5\25\13\2\u01d3")
        buf.write("\u01d4\5\17\b\2\u01d4\u01d5\5)\25\2\u01d5\u01d6\5\27\f")
        buf.write("\2\u01d6\u01d7\5-\27\2\u01d7\u008e\3\2\2\2\u01d8\u01d9")
        buf.write("\5\27\f\2\u01d9\u01da\5!\21\2\u01da\u01db\5-\27\2\u01db")
        buf.write("\u01dc\5\17\b\2\u01dc\u01dd\5\23\n\2\u01dd\u01de\5\17")
        buf.write("\b\2\u01de\u01df\5)\25\2\u01df\u0090\3\2\2\2\u01e0\u01e1")
        buf.write("\5#\22\2\u01e1\u01e2\5/\30\2\u01e2\u01e3\5-\27\2\u01e3")
        buf.write("\u0092\3\2\2\2\u01e4\u01e5\5)\25\2\u01e5\u01e6\5\17\b")
        buf.write("\2\u01e6\u01e7\5-\27\2\u01e7\u01e8\5/\30\2\u01e8\u01e9")
        buf.write("\5)\25\2\u01e9\u01ea\5!\21\2\u01ea\u0094\3\2\2\2\u01eb")
        buf.write("\u01ec\5+\26\2\u01ec\u01ed\5-\27\2\u01ed\u01ee\5)\25\2")
        buf.write("\u01ee\u01ef\5\27\f\2\u01ef\u01f0\5!\21\2\u01f0\u01f1")
        buf.write("\5\23\n\2\u01f1\u0096\3\2\2\2\u01f2\u01f3\5\61\31\2\u01f3")
        buf.write("\u01f4\5#\22\2\u01f4\u01f5\5\27\f\2\u01f5\u01f6\5\r\7")
        buf.write("\2\u01f6\u0098\3\2\2\2\u01f7\u01f8\5\63\32\2\u01f8\u01f9")
        buf.write("\5\25\13\2\u01f9\u01fa\5\27\f\2\u01fa\u01fb\5\35\17\2")
        buf.write("\u01fb\u01fc\5\17\b\2\u01fc\u009a\3\2\2\2\u01fd\u01fe")
        buf.write("\5-\27\2\u01fe\u01ff\5)\25\2\u01ff\u0200\5/\30\2\u0200")
        buf.write("\u0201\5\17\b\2\u0201\u009c\3\2\2\2\u0202\u0203\5\21\t")
        buf.write("\2\u0203\u0204\5\7\4\2\u0204\u0205\5\35\17\2\u0205\u0206")
        buf.write("\5+\26\2\u0206\u0207\5\17\b\2\u0207\u009e\3\2\2\2\u0208")
        buf.write("\u0209\5\r\7\2\u0209\u020a\5#\22\2\u020a\u00a0\3\2\2\2")
        buf.write("\u020b\u020c\5#\22\2\u020c\u020d\5\21\t\2\u020d\u00a2")
        buf.write("\3\2\2\2\u020e\u020f\5\7\4\2\u020f\u0210\5)\25\2\u0210")
        buf.write("\u0211\5)\25\2\u0211\u0212\5\7\4\2\u0212\u0213\5\67\34")
        buf.write("\2\u0213\u00a4\3\2\2\2\u0214\u0218\t(\2\2\u0215\u0217")
        buf.write("\t)\2\2\u0216\u0215\3\2\2\2\u0217\u021a\3\2\2\2\u0218")
        buf.write("\u0216\3\2\2\2\u0218\u0219\3\2\2\2\u0219\u00a6\3\2\2\2")
        buf.write("\u021a\u0218\3\2\2\2\u021b\u021d\t*\2\2\u021c\u021b\3")
        buf.write("\2\2\2\u021d\u021e\3\2\2\2\u021e\u021c\3\2\2\2\u021e\u021f")
        buf.write("\3\2\2\2\u021f\u0220\3\2\2\2\u0220\u0221\bT\2\2\u0221")
        buf.write("\u00a8\3\2\2\2\u0222\u0225\n%\2\2\u0223\u0225\5\u00ab")
        buf.write("V\2\u0224\u0222\3\2\2\2\u0224\u0223\3\2\2\2\u0225\u00aa")
        buf.write("\3\2\2\2\u0226\u0227\7^\2\2\u0227\u0228\t$\2\2\u0228\u00ac")
        buf.write("\3\2\2\2\u0229\u022d\7$\2\2\u022a\u022c\5\u00a9U\2\u022b")
        buf.write("\u022a\3\2\2\2\u022c\u022f\3\2\2\2\u022d\u022b\3\2\2\2")
        buf.write("\u022d\u022e\3\2\2\2\u022e\u0230\3\2\2\2\u022f\u022d\3")
        buf.write("\2\2\2\u0230\u0231\bW\6\2\u0231\u00ae\3\2\2\2\u0232\u0236")
        buf.write("\7$\2\2\u0233\u0235\5\u00a9U\2\u0234\u0233\3\2\2\2\u0235")
        buf.write("\u0238\3\2\2\2\u0236\u0234\3\2\2\2\u0236\u0237\3\2\2\2")
        buf.write("\u0237\u0239\3\2\2\2\u0238\u0236\3\2\2\2\u0239\u023a\7")
        buf.write("^\2\2\u023a\u023b\n$\2\2\u023b\u023c\bX\7\2\u023c\u00b0")
        buf.write("\3\2\2\2\u023d\u023e\13\2\2\2\u023e\u023f\bY\b\2\u023f")
        buf.write("\u00b2\3\2\2\2\33\2\u00b9\u00bd\u00c7\u0143\u014a\u014e")
        buf.write("\u0152\u015d\u0164\u0167\u016b\u0170\u0172\u017a\u017f")
        buf.write("\u0184\u0186\u018c\u018e\u0218\u021e\u0224\u022d\u0236")
        buf.write("\t\b\2\2\38\2\3:\3\3;\4\3W\5\3X\6\3Y\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    SL_COMMENT = 1
    ML_COMMENT = 2
    ASSIGNOP = 3
    ADDOP = 4
    SUBOP = 5
    MULOP = 6
    DIVOP = 7
    MODOP = 8
    EQOP = 9
    NEOP = 10
    GTOP = 11
    LTOP = 12
    GTEOP = 13
    LTEOP = 14
    ANDOP = 15
    OROP = 16
    STRINGOP = 17
    NOTOP = 18
    LP = 19
    RP = 20
    LC = 21
    RC = 22
    LS = 23
    RS = 24
    SEMICOLON = 25
    COMMA = 26
    DOT = 27
    COLON = 28
    INTLIT = 29
    BOOLLIT = 30
    FLOATLIT = 31
    STRINGLIT = 32
    AUTO = 33
    BREAK = 34
    BOOLEAN = 35
    CONTINUE = 36
    ELSE = 37
    FLOAT = 38
    FOR = 39
    FUNCTION = 40
    IF = 41
    INHERIT = 42
    INTEGER = 43
    OUT = 44
    RETURN = 45
    STRING = 46
    VOID = 47
    WHILE = 48
    TRUE = 49
    FALSE = 50
    DO = 51
    OF = 52
    ARRAY = 53
    IDENTIFIER = 54
    WS = 55
    UNCLOSE_STRING = 56
    ILLEGAL_ESCAPE = 57
    ERROR_CHAR = 58

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", "'!='", "'>'", 
            "'<'", "'>='", "'<='", "'&&'", "'||'", "'::'", "'!'", "'('", 
            "')'", "'{'", "'}'", "'['", "']'", "';'", "','", "'.'", "':'" ]

    symbolicNames = [ "<INVALID>",
            "SL_COMMENT", "ML_COMMENT", "ASSIGNOP", "ADDOP", "SUBOP", "MULOP", 
            "DIVOP", "MODOP", "EQOP", "NEOP", "GTOP", "LTOP", "GTEOP", "LTEOP", 
            "ANDOP", "OROP", "STRINGOP", "NOTOP", "LP", "RP", "LC", "RC", 
            "LS", "RS", "SEMICOLON", "COMMA", "DOT", "COLON", "INTLIT", 
            "BOOLLIT", "FLOATLIT", "STRINGLIT", "AUTO", "BREAK", "BOOLEAN", 
            "CONTINUE", "ELSE", "FLOAT", "FOR", "FUNCTION", "IF", "INHERIT", 
            "INTEGER", "OUT", "RETURN", "STRING", "VOID", "WHILE", "TRUE", 
            "FALSE", "DO", "OF", "ARRAY", "IDENTIFIER", "WS", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "SL_COMMENT", "ML_COMMENT", "A", "B", "C", "D", "E", "F", 
                  "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", 
                  "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "ASSIGNOP", 
                  "ADDOP", "SUBOP", "MULOP", "DIVOP", "MODOP", "EQOP", "NEOP", 
                  "GTOP", "LTOP", "GTEOP", "LTEOP", "ANDOP", "OROP", "STRINGOP", 
                  "NOTOP", "LP", "RP", "LC", "RC", "LS", "RS", "SEMICOLON", 
                  "COMMA", "DOT", "COLON", "INTLIT", "BOOLLIT", "FLOATLIT", 
                  "STRINGLIT", "ESC", "SAFECODEPOINT", "AUTO", "BREAK", 
                  "BOOLEAN", "CONTINUE", "ELSE", "FLOAT", "FOR", "FUNCTION", 
                  "IF", "INHERIT", "INTEGER", "OUT", "RETURN", "STRING", 
                  "VOID", "WHILE", "TRUE", "FALSE", "DO", "OF", "ARRAY", 
                  "IDENTIFIER", "WS", "STRINGCHAR", "EscapeSequence", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[54] = self.INTLIT_action 
            actions[56] = self.FLOATLIT_action 
            actions[57] = self.STRINGLIT_action 
            actions[85] = self.UNCLOSE_STRING_action 
            actions[86] = self.ILLEGAL_ESCAPE_action 
            actions[87] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace("_", "")
     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace("_", "")
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text[1:-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            	raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            	raise IllegalEscape(self.text[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise ErrorToken(self.text)
     


