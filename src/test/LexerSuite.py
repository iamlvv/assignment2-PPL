import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test101(self):
        """test all"""
        self.assertTrue(TestLexer.test("abc?vn", "abc,Error Token ?", 101))
    def test102(self):
        self.assertTrue(TestLexer.test("1_2_3_4.5_6_7", "1234.5,_6_7,<EOF>", 102))
    def test103(self):
        self.assertTrue(TestLexer.test(""" "abc?vn" """ , "abc?vn,<EOF>", 103))
    def test104(self):
        self.assertTrue(TestLexer.test("This is ! John" , "This,is,!,John,<EOF>", 104))
    def test105(self):
        self.assertTrue(TestLexer.test("123__3_4", "123,__3_4,<EOF>", 105))
    def test106(self):
        self.assertTrue(TestLexer.test("123..456", "123.,.,456,<EOF>", 106))
    def test107(self):
        self.assertTrue(TestLexer.test("123.456", "123.456,<EOF>", 107))
    def test108(self):
        self.assertTrue(TestLexer.test("1__23.456e-7", "1,__23,.456e-7,<EOF>", 108))
    def test109(self):
        self.assertTrue(TestLexer.test("1__23.456E-7", "1,__23,.456E-7,<EOF>", 109))
    def test110(self):
        self.assertTrue(TestLexer.test("-123", "-,123,<EOF>", 110))
    def test111(self):
        self.assertTrue(TestLexer.test("-123e-7", "-,123e-7,<EOF>", 111))
    def test112(self):
        self.assertTrue(TestLexer.test(""" "Hi \\This is Bi" """, "Illegal Escape In String: Hi \T", 112))
    def test113(self):
        self.assertTrue(TestLexer.test(""" "Hi \nThis is Bi" """, "Unclosed String: Hi ", 113))
    def test114(self):
        self.assertTrue(TestLexer.test("abc\nXuey", "abc,Xuey,<EOF>", 114))
    def test115(self):
        self.assertTrue(TestLexer.test("abc\\\n\f\tXuey", "abc,Error Token \\", 115))
    def test116(self):
        self.assertTrue(TestLexer.test("\nA-SS", "A,-,SS,<EOF>", 116))
    def test117(self):
        self.assertTrue(TestLexer.test("A-SS~~~`", "A,-,SS,Error Token ~", 117))
    def test118(self):
        self.assertTrue(TestLexer.test("aW23weuut_qn___sns", "aW23weuut_qn___sns,<EOF>", 118))
    def test119(self):
        self.assertTrue(TestLexer.test("aW23weuut_qn___sns`abc", "aW23weuut_qn___sns,Error Token `", 119))
    def test120(self):
        self.assertTrue(TestLexer.test("aW23weuut_qn_234__snsabc", "aW23weuut_qn_234__snsabc,<EOF>", 120))
    def test121(self):
        self.assertTrue(TestLexer.test("123.343weuut_qn_234__snsabc", "123.343,weuut_qn_234__snsabc,<EOF>", 121))
    def test122(self):
        self.assertTrue(TestLexer.test("123.343+123.343AAAbsb", "123.343,+,123.343,AAAbsb,<EOF>", 122))
    def test123(self):
        self.assertTrue(TestLexer.test("123.343+123.343_23\n\t22.23", "123.343,+,123.343,_23,22.23,<EOF>", 123))
    def test124(self):
        self.assertTrue(TestLexer.test("123.343+123.343_23E-22.23", "123.343,+,123.343,_23E,-,22.23,<EOF>", 124))
    def test125(self):
        self.assertTrue(TestLexer.test("Pu\\\\s\\s\n~y", "Pu,Error Token \\", 125))
    def test126(self):
        self.assertTrue(TestLexer.test("true", "true,<EOF>", 126))
    def test127(self):
        self.assertTrue(TestLexer.test("{1, 5, 7, 12}", "{,1,,,5,,,7,,,12,},<EOF>", 127))
    def test128(self):
        self.assertTrue(TestLexer.test("&&abs_123_123.53_43", "&&,abs_123_123,.,5343,<EOF>", 128))
    def test129(self):
        self.assertTrue(TestLexer.test("a.aa.12_1`.34", "a,.,aa,.,121,Error Token `", 129))
    def test130(self):
        self.assertTrue(TestLexer.test("\nabc_12E-10E+10", "abc_12E,-,10E+10,<EOF>", 130))
    def test131(self):
        self.assertTrue(TestLexer.test("12_a_3.E-120+111,", "12,_a_3,.E-120,+,111,,,<EOF>", 131))
    def test132(self):
        self.assertTrue(TestLexer.test(""" "\\?vn" """ , "Illegal Escape In String: \?", 132))
    def test133(self):
        self.assertTrue(TestLexer.test(""" "\\\t?vn" """ , "Illegal Escape In String: \	", 133))
    def test134(self):
        self.assertTrue(TestLexer.test(""" "Escape tam bay \g thi sao" """, "Illegal Escape In String: Escape tam bay \g", 134))
    def test135(self):
        self.assertTrue(TestLexer.test(""" "Toi co mot string \\g bi khum" """, "Illegal Escape In String: Toi co mot string \g", 135))
    def test136(self):
        self.assertTrue(TestLexer.test(""" "What about \ v" """, "Illegal Escape In String: What about \ ", 136))
    def test137(self):
        self.assertTrue(TestLexer.test(""" "What about \n" """, "Unclosed String: What about ", 137))
    def test138(self):
        self.assertTrue(TestLexer.test(""" "What about \\" """ , "Unclosed String: What about \\\" ", 138))
    def test139(self):
        self.assertTrue(TestLexer.test("hai##" , "hai,Error Token #", 139))
    def test140(self):
        self.assertTrue(TestLexer.test("hai*&^$()" , "hai,*,Error Token &", 140))
    def test141(self):
        self.assertTrue(TestLexer.test("hai*(){}[]", "hai,*,(,),{,},[,],<EOF>", 141))
    def test142(self):
        self.assertTrue(TestLexer.test("hai:integer=234", "hai,:,integer,=,234,<EOF>", 142))
    def test143(self):
        self.assertTrue(TestLexer.test("*&?!-32E10", "*,Error Token &", 143))
    def test144(self):
        self.assertTrue(TestLexer.test("12345>12,.23434.54", "12345,>,12,,,.,23434.54,<EOF>", 144))
    def test145(self):
        self.assertTrue(TestLexer.test("12345\"dskds\"", "12345,dskds,<EOF>", 145))
    def test146(self):
        self.assertTrue(TestLexer.test("12345\"dskds\"'''", "12345,dskds,Error Token '", 146))
    def test147(self):
        self.assertTrue(TestLexer.test("12345\"dskds\"\"\"", "12345,dskds,,<EOF>", 147))
    def test148(self):
        self.assertTrue(TestLexer.test("12345\"dskds\"\"", "12345,dskds,Unclosed String: ", 148))
    def test149(self):
        self.assertTrue(TestLexer.test("12345\"dskds\"\n\"", "12345,dskds,Unclosed String: ", 149))
    def test150(self):
        self.assertTrue(TestLexer.test("12345\"dskds\"\\\"", "12345,dskds,Error Token \\", 150))
    def test151(self):
        self.assertTrue(TestLexer.test(" 0", "0,<EOF>", 151))
    def test152(self):
        self.assertTrue(TestLexer.test("[0].34", "[,0,],.,34,<EOF>", 152))
    def test153(self):
        self.assertTrue(TestLexer.test("0.34_342", "0.34,_342,<EOF>", 153))
    def test154(self):
        self.assertTrue(TestLexer.test("0.34_342E-10", "0.34,_342E,-,10,<EOF>", 154))
    def test155(self):
        self.assertTrue(TestLexer.test("0.34_342E-10+123", "0.34,_342E,-,10,+,123,<EOF>", 155))
    def test156(self):
        self.assertTrue(TestLexer.test(""" "0.34_342E-10+123.123?`~~~~" """, "0.34_342E-10+123.123?`~~~~,<EOF>", 156))
    def test157(self):
        self.assertTrue(TestLexer.test(""" "0.34_342E-10+123.123?`~~~~"\\n\\" """, "0.34_342E-10+123.123?`~~~~,Error Token \\", 157))
    def test158(self):
        self.assertTrue(TestLexer.test(""" "0.34_342E-10+123.123?`"~~~~"\\n\\" """, "0.34_342E-10+123.123?`,Error Token ~", 158))
    def test159(self):
        self.assertTrue(TestLexer.test("23x2*32", "23,x2,*,32,<EOF>", 159))
    def test160(self):
        self.assertTrue(TestLexer.test("23x2*32+=23.34_23", "23,x2,*,32,+,=,23.34,_23,<EOF>", 160))
    def test161(self):
        self.assertTrue(TestLexer.test("23x2*32+=23.34_23E-10", "23,x2,*,32,+,=,23.34,_23E,-,10,<EOF>", 161))
    def test162(self):
        self.assertTrue(TestLexer.test("23x2*32+=23.34_23E-10+123", "23,x2,*,32,+,=,23.34,_23E,-,10,+,123,<EOF>", 162))
    def test163(self):
        self.assertTrue(TestLexer.test("23x2*32==23.34_23E-10+123", "23,x2,*,32,==,23.34,_23E,-,10,+,123,<EOF>", 163))
    def test164(self):
        self.assertTrue(TestLexer.test("23x2*32==23.34_23eEEEEe-10+123", "23,x2,*,32,==,23.34,_23eEEEEe,-,10,+,123,<EOF>", 164))
    def test165(self):
        self.assertTrue(TestLexer.test("23x2+23abcd_!@*32==23.34_23eEEEEe-10+123.123", "23,x2,+,23,abcd_,!,Error Token @", 165))
    def test166(self):
        self.assertTrue(TestLexer.test("23x2+23abcd_\"!@*32==23.34_23eEEEEe-10+123.123", "23,x2,+,23,abcd_,Unclosed String: !@*32==23.34_23eEEEEe-10+123.123", 166))
    def test167(self):
        self.assertTrue(TestLexer.test("23x2+23abcd_\"\"!@*32==23.34_23eEEEEe-10+123.123", "23,x2,+,23,abcd_,,!,Error Token @", 167))
    def test168(self):
        self.assertTrue(TestLexer.test("23x2+23abcd_\"\n\\\"!@*32==23.34_23eEEEEe-10+123.123", "23,x2,+,23,abcd_,Unclosed String: ", 168))
    def test169(self):
        self.assertTrue(TestLexer.test("3\"!@\"*32==23.34_23eEEEEe-10+123.123", "3,!@,*,32,==,23.34,_23eEEEEe,-,10,+,123.123,<EOF>", 169))
    def test170(self):
        self.assertTrue(TestLexer.test("PX[aajX(eC+ex9*{)!UY!MijZ3zP}T", "PX,[,aajX,(,eC,+,ex9,*,{,),!,UY,!,MijZ3zP,},T,<EOF>", 170))
    def test171(self):
        self.assertTrue(TestLexer.test("NMgNRSMt+W9.p)&t3_uJge!=P9}=G4", "NMgNRSMt,+,W9,.,p,),Error Token &", 171))
    def test172(self):
        self.assertTrue(TestLexer.test("JBEZvEmW3C&ZQLbE-{d!f(*q", "JBEZvEmW3C,Error Token &", 172))
    def test173(self):
        self.assertTrue(TestLexer.test("abc___123.12", "abc___123,.,12,<EOF>", 173))
    def test174(self):
        self.assertTrue(TestLexer.test("abc___123.12e-10EE1", "abc___123,.12e-10,EE1,<EOF>", 174))
    def test175(self):
        self.assertTrue(TestLexer.test("abc_??a", "abc_,Error Token ?", 175))
    def test176(self):
        self.assertTrue(TestLexer.test("abc_\\fa", "abc_,Error Token \\", 176))
    def test177(self):
        self.assertTrue(TestLexer.test("abc_\tfa", "abc_,fa,<EOF>", 177))
    def test178(self):
        self.assertTrue(TestLexer.test("abc_\nfa", "abc_,fa,<EOF>", 178))
    def test179(self):
        self.assertTrue(TestLexer.test("abc_xx.sfa", "abc_xx,.,sfa,<EOF>", 179))
    def test180(self):
        self.assertTrue(TestLexer.test("abc___xx.sfa", "abc___xx,.,sfa,<EOF>", 180))
    def test181(self):
        self.assertTrue(TestLexer.test("{a}", "{,a,},<EOF>", 181))
    def test182(self):
        self.assertTrue(TestLexer.test("{a}+{b}", "{,a,},+,{,b,},<EOF>", 182))
    def test183(self):
        self.assertTrue(TestLexer.test("{a}+{b}+c()}", "{,a,},+,{,b,},+,c,(,),},<EOF>", 183))
    def test184(self):
        self.assertTrue(TestLexer.test("{a}+{b}+c()}}PO{S}", "{,a,},+,{,b,},+,c,(,),},},PO,{,S,},<EOF>", 184))
    def test185(self):
        self.assertTrue(TestLexer.test("{a}+{b}+c()][s11!]", "{,a,},+,{,b,},+,c,(,),],[,s11,!,],<EOF>", 185))
    def test186(self):
        self.assertTrue(TestLexer.test("!", "!,<EOF>", 186))
    def test187(self):
        self.assertTrue(TestLexer.test("!@", "!,Error Token @", 187))
    def test188(self):
        self.assertTrue(TestLexer.test("[{()}]", "[,{,(,),},],<EOF>", 188))
    def test189(self):
        self.assertTrue(TestLexer.test("[{()}]!45.34", "[,{,(,),},],!,45.34,<EOF>", 189))
    def test190(self):
        self.assertTrue(TestLexer.test(""" hoa co chu \b?vn """, "hoa,co,chu,Error Token ?", 190))
    def test191(self):
        self.assertTrue(TestLexer.test(" 12223.12_2_1 ", "12223.12,_2_1,<EOF>", 191))
    def test192(self):
        self.assertTrue(TestLexer.test(""" Higuie_12223.12e-10 """, "Higuie_12223,.12e-10,<EOF>", 192))
    def test193(self):
        self.assertTrue(TestLexer.test(""" Higuie_12223.12e-10e{} """, "Higuie_12223,.12e-10,e,{,},<EOF>", 193))
    def test194(self):
        self.assertTrue(TestLexer.test(""" Higuie_12223.12e-10e{[}](8.23_122) """, "Higuie_12223,.12e-10,e,{,[,},],(,8.23,_122,),<EOF>", 194))
    def test195(self):
        self.assertTrue(TestLexer.test(""" Higuie_12223.12e-10e{[}](8.23_122a,bcv) """, "Higuie_12223,.12e-10,e,{,[,},],(,8.23,_122a,,,bcv,),<EOF>", 195))
    def test196(self):
        self.assertTrue(TestLexer.test(""" Higuie_12223.12e-10e{[}](8.23_122a,bcv//) """, "Higuie_12223,.12e-10,e,{,[,},],(,8.23,_122a,,,bcv,<EOF>", 196))
    def test197(self):
        self.assertTrue(TestLexer.test(""" Higuie_12223.12e-10e{[}](8.23_122a,bcv/*ds*/) """, "Higuie_12223,.12e-10,e,{,[,},],(,8.23,_122a,,,bcv,),<EOF>", 197))
    def test198(self):
        self.assertTrue(TestLexer.test(""" Higuie_12223.12e-10e{[}](8.23_122a,bcv/*ds*/\\a) """, "Higuie_12223,.12e-10,e,{,[,},],(,8.23,_122a,,,bcv,Error Token \\", 198))
    def test199(self):
        self.assertTrue(TestLexer.test(""" Higuie_12223".123_122a,bcv/*ds*/a) """, "Higuie_12223,Unclosed String: .123_122a,bcv/*ds*/a) ", 199))
    def test200(self):
        self.assertTrue(TestLexer.test("001+2", "0,0,1,+,2,<EOF>", 200))
        
