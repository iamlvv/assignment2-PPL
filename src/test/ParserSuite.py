import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test201(self):
        """Simple program: int main() {} """
        input = """fact: function void() {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
    def test202(self):
        """Simple program: int main() {} """
        input = """x: integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            delta: integer = fact(3);
            inc(x, delta);
            printInteger(x);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))
    def test203(self):
        """Simple program: int main() {} """
        input = """x, y, z, abc_23: integer = 65, 1;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            delta: integer = fact(3);
            inc(x, delta);
            printInteger(x);
        }
        """
        expect = "Error on line 1 col 32: ;"
        self.assertTrue(TestParser.test(input, expect, 203))
    def test204(self):
        input = """x, y, z, abc_23: integer = 65, 1;
        """
        expect = "Error on line 1 col 32: ;"
        self.assertTrue(TestParser.test(input, expect, 204))
    def test205(self):
        
        input = """//var declare
        x12, _04, T: string = "chau \t", str::str;"""
        expect = "Error on line 2 col 48: ;"
        self.assertTrue(TestParser.test(input, expect, 205))
    def test206(self):
        input = """x, y, z, abc_23: integer = 65, 1;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            delta: integer = fact(3);
            inc(x, delta);
            printInteger(x);
        }
        """
        expect = "Error on line 1 col 32: ;"
        self.assertTrue(TestParser.test(input, expect, 206))
    def test207(self):
        
        input = """//a
        x12"""
        expect = "Error on line 2 col 11: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 207))
    def test208(self):
        input = """ /////////////abs/////////***/ """
        expect = "Error on line 1 col 31: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 208))
    def test209(self):
        input = """//a"""
        expect = "Error on line 1 col 3: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 209))
    def test210(self):
        input = """ //a
        b, T: string = "chau", str::str; """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))
    def test211(self):
        input = """ /*
        a
        */
        b, T: string = "chau", str::str; """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 211))
    def test212(self):
        input = """fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            delta: integer = fact(3);
            inc(x, delta);
            for (i = 0, i < 10, i+1) {
                writeLn(i);
            }
            printInteger(x);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))
    def test213(self):
        input = """fact: function integer (n: integer) {
            """
        expect = "Error on line 2 col 12: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 213))
    def test214(self):
        input = """fact: function integer (n: integer) {
            """
        expect = "Error on line 2 col 12: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 214))
    def test215(self):
        input = """fact: float integer (n: integer) {
            }"""
        expect = "Error on line 1 col 12: integer"
        self.assertTrue(TestParser.test(input, expect, 215))
    def test216(self):
        input = """fact: function integer (n: integer) {
            while (i < 1) {
                for (i = 0, i < 10, i+1) {
                    break;
                    continue;
                    return i == 1;
                }
            }
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))
    def test217(self):
        input = """fact: function integer (n: integer) {
            continue;
            printInteger(3__12);
            goo(1, 2, 3);
            {
                r,s: integer;
                r = 2.0;
                a,b: array [5] of integer;
                s = r * r * a;
                a[0] = s;
            }
            }"""
        expect = "Error on line 3 col 26: __12"
        self.assertTrue(TestParser.test(input, expect, 217))
    def test218(self):
        input = """fact: function integer (n: integer) {
            do {
                while (i + (2 + 3) < 1) {
                        for (i = 1, i < (10 + 1), i+1) {
                            print("Hello World");
                        }
                    }
            }
            while (n == 10);
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))
    def test219(self):
        input = """fact: function integer (n: integer) {
            foo(2+x, 4.0/y);
            goo();
            super(2 * x, (2+3) /2 % 3 == 21);
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))
    def test220(self):
        input = """fact: function integer (n: integer) {
            while (n == 10 || n == 20 && n == 30) {
                    delta: integer = fact(3);
                    inc(x, delta, alpha);
                    do printHello();
                    while (1 + 4 == 2);
                }
            }"""
        expect = "Error on line 2 col 32: =="
        self.assertTrue(TestParser.test(input, expect, 220))
    def test221(self):
        
        input = """_45_0: function auto () {
                return arr[5_6,1.];
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221))
    def test222(self):
        input = """_45_0: function auto () {
                return arr[5_6,1.];
                if (n == 0) return 1;
                else return (n - 1) + fact(n + 2);
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))
    def test223(self):
        input = """_45_0: function auto () {
                return arr[5_6,1.];
                do helloworld(2);
                while (23 == 1)
                }"""
        expect = "Error on line 3 col 19: helloworld"
        self.assertTrue(TestParser.test(input, expect, 223))
    def test224(self):
        input = """_45_0: function auto () {
                return arr[5_6,1.];
                do {
                    helloworld(2);
                }
                while (n * 2 == 1)
                }"""
        expect = "Error on line 7 col 16: }"
        self.assertTrue(TestParser.test(input, expect, 224))
    def test225(self):
        input = """_45_0: function auto () {
                return arr[5_6,1., "helloBK"];
                do {
                    helloworld(2);
                }
                while (n * 2 == 1)
                }"""
        expect = "Error on line 7 col 16: }"
        self.assertTrue(TestParser.test(input, expect, 225))
    def test226(self):
        input = """_45_0: function auto () {
                return arr[5_6,1."helloChau"];
                do {
                    helloworld(2);
                }
                while (n * 2 == 1);
                }"""
        expect = "Error on line 2 col 33: helloChau"
        self.assertTrue(TestParser.test(input, expect, 226))
    def test227(self):
        input = """_45_0: function auto () {
                return arr[5_6,1.,"helloChau"];
                do {
                    helloworld(2);
                }
                while (n * 2 == 1);
                while (x > 1) {
                    print(x);
                }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 227))
    def test228(self):
        input = """_45_0: function auto () {
                return arr[5_6,1.];
                do {
                    helloworld(2);
                }
                while (n * 2 == 1)
                }"""
        expect = "Error on line 7 col 16: }"
        self.assertTrue(TestParser.test(input, expect, 228))
    def test229(self):
        input = """_45_0: function auto () {
                return arr[5_6,1.];
                do {
                    helloworld(2);
                }
                while (n * 2 == 1) if (n == 0) return 1 else return (n - 1) + fact(n + 2);
                }"""
        expect = "Error on line 6 col 35: if"
        self.assertTrue(TestParser.test(input, expect, 229))
    def test230(self):
        input = """_45_0: function auto () {
                return arr[5_6,1.];
                do {
                    helloworld(2);
                }
                while (n * 2 == 1);
                while (1) if (x == 0) else break;
                }"""
        expect = "Error on line 7 col 38: else"
        self.assertTrue(TestParser.test(input, expect, 230))
    def test231(self):
        input = """if ((1 < 2) < 3) return 1;"""
        expect = "Error on line 1 col 0: if"
        self.assertTrue(TestParser.test(input, expect, 231))
    def test232(self):
        input = """
        main: function void (x: integer, a_123: string) {
            i: integer =0;
            {
                {
                    a[1+foo(2)] = a[b[3][4]]+5;
                }
            }
        }
        """
        expect = """Error on line 6 col 40: ["""
        self.assertTrue(TestParser.test(input,expect,232))
    def test233(self):
        
        input = """ a, b, c: auto = 4., 1+2, x; """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233))
    def test234(self):
        
        input = """a, b, c: auto = 4., 1+2, __12"""
        expect = "Error on line 1 col 29: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 234))
    def test235(self):
        
        input = """a, b, c: integer = 3, 4, 5, 6;"""
        expect = "Error on line 1 col 26: ,"
        self.assertTrue(TestParser.test(input, expect, 235))
    def test236(self):
        
        input = """count,_12_5 = count(),true&&false;"""
        expect = "Error on line 1 col 12: ="
        self.assertTrue(TestParser.test(input, expect, 236))
    def test237(self):
        
        input = """x:array[3_6,0] of auto = {1,2,4};"""
        expect = "Error on line 1 col 18: auto"
        self.assertTrue(TestParser.test(input, expect, 237))
    def test238(self):
        
        input = """x:array[3_6,0] of integer = {1,2,4};"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 238))
    def test239(self):
        
        input = """hkt:array[3_6,d12] of float = {1,{5.6e-34},4};"""
        expect = "Error on line 1 col 14: d12"
        self.assertTrue(TestParser.test(input, expect, 239))
    def test240(self):
        
        input = """_12:array[3_6,12] of float = {};"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 240))
    def test241(self):
        
        input = """avg: float = (a + b + c2)/3;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))
    def test242(self):
        
        input = """random_num: integer = ();"""
        expect = "Error on line 1 col 23: )"
        self.assertTrue(TestParser.test(input, expect, 242))
    def test243(self):
        
        input = """getName: function string (inherit out x:array[2_1,8] of float) {
                return;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 243))
    def test244(self):
        
        input = """arr[4_5,0]: function void () inherit getName {
                return {};
                }"""
        expect = "Error on line 1 col 3: ["
        self.assertTrue(TestParser.test(input, expect, 244))
    def test245(self):
        
        input = """d5: function void();
                }"""
        expect = "Error on line 1 col 19: ;"
        self.assertTrue(TestParser.test(input, expect, 245))
    def test246(self):
        
        input = """Tdk__9:auto = __6H[2,3_09] + foo() / 3.4e-9+7__0;"""
        expect = "Error on line 1 col 45: __0"
        self.assertTrue(TestParser.test(input, expect, 246))
    def test247(self):
        
        input = """ a, b, c: auto = 4., 1+2, x; """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 247))
    def test248(self):
        
        input = """a, b, c: auto = 4., 1+2, __12"""
        expect = "Error on line 1 col 29: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 248))
    def test249(self):
        
        input = """a, b, c, d, e: float = 3, 4, 5, 6, array [12] of integer;"""
        expect = "Error on line 1 col 35: array"
        self.assertTrue(TestParser.test(input, expect, 249))
    def test250(self):
        input = """a, b, c: integer = 3, 4, "hello";"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 250))
    def test251(self):
        input = """a, b, c: integer = 3, 4, 5, 6;"""
        expect = "Error on line 1 col 26: ,"
        self.assertTrue(TestParser.test(input, expect, 251))
    def test252(self):
        
        input = """name: string = "helloguys"::WorldwideWeb[5,1_7];"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 252))
    def test253(self):
        input = """name: string = "helloguys"::WorldwideWeb[5,1_7], 34._23;"""
        expect = "Error on line 1 col 47: ,"
        self.assertTrue(TestParser.test(input, expect, 253))
    def test254(self):
        input="""
        main: function void (x: integer, a_123: string) {
            i: integer = 150;
            {
                {
                    while () {
                        return -1;
                        for (,,) {
                            writeln();
                        }
                    }
                }
            }
        }
        """
        expect = "Error on line 6 col 27: )"
        self.assertTrue(TestParser.test(input,expect,254))
    def test255(self):
        input="""
        main: function void (x: integer, a_123: string) {
            i: integer =0;
            {
                {
                    a[1+foo(2)] = 5 + 3 + 2 * 2;
                }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,255))
    def test256(self):
        input="""
        main: function void (x: integer, a_123: string) {
            i: integer =0;
            {
                {
                    a[1+foo(2)] = 5 + 3 + 2 * 2;
                }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,256))
    def test257(self):
        input="""
        main: function void (x: integer, a_123: string) {
            i: integer =0;
            {
                {
                    a[1+foo(2)] = while (x > 1) return -1;
                }
            }
        }
        """
        expect = "Error on line 6 col 34: while"
        self.assertTrue(TestParser.test(input,expect,257))
    def test258(self):
        input="""
        main: function void (x: integer, a_123: string) {
            i: integer =0;
            {
                {
                    a[1+foo(2)] = 5 + 3 + 2 * 2;
                    while (x > 1) {
                        do {
                            while (n < 1) {
                                for (i = 3._20, i < 10, i+2) {
                                    return;
                                }
                            }
                        }
                        i = i + 1;
                    }
                }
            }
        }
        """
        expect = "Error on line 10 col 43: _20"
        self.assertTrue(TestParser.test(input,expect,258))
    def test259(self):
        input="""
        main: function void (x: integer, a_123: string) {
            i: integer =0;
            {
                {
                    a[1+foo(2)] = 5 + 3 + 2 * 2;
                    while (x > 1) {
                        do {
                            while (n < 1) {
                                for (i = 3.2_0_2, i < 10, i+2) {
                                    return;
                                }
                            }
                        }
                        i = i + 1;
                    }
                }
            }
        }
        """
        expect = "Error on line 10 col 44: _0_2"
        self.assertTrue(TestParser.test(input,expect,259))
    def test260(self):
        input="""
        main: function void (x: integer, a_123: string) {
            i: integer =0;
            {
                {
                    a[1+foo(2)] = 5 + 3 + 2 * 2;
                    while (x > 1) {
                        do {
                            while (n < 1) {
                                for (i = 3.2_0_2, i < 10, i+2) {
                                    return;
                                }
                            }
                        }
                        while (x > 1);
                        i = i + 1;
                    }
                }
            }
        }
        """
        expect = "Error on line 10 col 44: _0_2"
        self.assertTrue(TestParser.test(input,expect,260))
    def test261(self):
        input="""
        main: function void (x: integer, a_123: string) {
            i: integer =0;
            {
                {
                    a[1+foo(2)] = 5 + 3 + 2 * 2;
                    while (x > 1) {
                        do {
                            while (n < 1) {
                                for (i = 3.2_0_2, i < 10, i+2) {
                                    return;
                                }
                            }
                        }
                        while (x > 1);
                        i = i + 1;
                    }
                }
            }
        }
        """
        expect = "Error on line 10 col 44: _0_2"
        self.assertTrue(TestParser.test(input,expect,261))
    def test262(self):
        input="""
        main: function void (x: integer, a_123: string) {
            i: integer =0;
            {
                {
                    a[1+foo(2)] = 5 + 3 + 2 * 2;
                    while (x > 1) {
                        for (i = 3.2_0_2,,) {
                            a[0] = 23;
                            i = i + 1;
                            return;
                        }
                    }
                }
            }
        }
        """
        expect = "Error on line 8 col 36: _0_2"
        self.assertTrue(TestParser.test(input,expect,262))
    def test263(self):
        input="""
        main: function void (x: integer, a_123: string) {
            i: integer =0;
            {
                {
                    a[1+foo(2)] = 5 + 3 + 2 * 2;
                    while (x > 1) {
                        if (x == 1)
                        i = i + 1;
                    }
                }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,263))
    def test264(self):
        input="""
        main: function void (x: integer, a_123: string) {
            i: integer =0;
            {
                {
                    a[1+foo(2)] = 5 + 3 + 2 * 2;
                    while (x > 1) {
                        if (x == 1)
                        i = i + 1;
                        else
                        return;
                    }
                }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,264))
    def test265(self):
        input="""
        main: function void (x: integer, a_123: string) {
            i: integer =0;
            {
                {
                    a[1+foo(2)] = 5 + 3 + 2 * 2;
                    while (x > 1) {
                        if (x == 1)
                        i = i + 1;
                        break;
                        for (i = 0, i <= 10, i =  i + 1) {
                            writeln();
                        }
                    }
                }
            }
        }
        """
        expect = "Error on line 11 col 47: ="
        self.assertTrue(TestParser.test(input,expect,265))
    def test266(self):
        input="""
        main: function void (x: integer, a_123: string) {
            i: integer =0;
            {
                {
                    a[1+foo(2)] = 5 + 3 + 2 * 2;
                     while (x > 1) {
                        if (x == 1)
                        i = i + 1;
                        break;
                        for (i = 0, i <= 10, i + 1.0_1__2) {
                            writeln();
                        }
                    }
                }
            }
        }
        """
        expect = "Error on line 11 col 52: _1__2"
        self.assertTrue(TestParser.test(input,expect,266))
    def test267(self):
        input="""
        main: function void (x: integer, a_123: string) {
            i: integer =0;
            {
                {
                    a[1+foo(2)] = 5 + 3 + 2 * 2;
                     while (x > 1) {
                        if (x == 1)
                        i = i + 1;
                        break;
                        for (i = 0, i <= 10, i + (1_000_1.03)) {
                            writeln();
                        }
                    }
                }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,267))
    def test268(self):
        input="""
        main: function void (x: integer, a_123: string) {
            i: integer =0;
            {
                {
                    a[1+foo(2)] = 5 + 3 + 2 * 2;
                    while (x > 1) {
                        do {
                            while (n < 1) {
                                for (i = 3.2_0_2, i < 10, i+2) {
                                    return;
                                }
                            }
                        }
                        while (x > 1);
                        i = i + 1;
                    }
                }
            }
        }
        """
        expect = "Error on line 10 col 44: _0_2"
        self.assertTrue(TestParser.test(input,expect,268))
    def test269(self):
        input="""
        main: function void (x: integer, a_123: string) {
            i: integer =0;
            {
                {
                    a[1+foo(2)] = 5 + 3 + 2 * 2;
                    while (x > 1) {
                        do {
                            while (n < 1) {
                                for (i = 3.0, i >= 10 + 1 + 2, i+2) {
                                    return;
                                }
                            }
                        }
                        while (x > 1);
                        i = i + 1;
                    }
                }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,269))
    def test270(self):
        input="""
        main: function void (x: integer, a_123: string) {
            i: integer =0;
            {
                {
                    a[1+foo(2)] = 5 + 3 + 2 * 2;
                    while (x > 1) {
                        do {
                            while (n < 1) {
                                for (i = 3, i < 10 < 15, i+2) {
                                    return;
                                }
                            }
                        }
                        while (x > 1);
                        i = i + 1;
                    }
                }
            }
        }
        """
        expect = "Error on line 10 col 51: <"
        self.assertTrue(TestParser.test(input,expect,270))
    def test271(self):
        input="""
        main: function void (x: integer, a_123: string) {
            i: integer =0;
            {
                {
                    a[1+foo(2)] = 5 + 3 + 2 * 2;
                    while (x > 1) {
                        do {
                            while (n < 1) {
                                for (i = 3.2_0_2, i < 10, i+2) {
                                    return;
                                }
                            }
                        }
                        while (x > 1);
                        i = i + 1;
                    }
                }
            }
        }
        """
        expect = "Error on line 10 col 44: _0_2"
        self.assertTrue(TestParser.test(input,expect,271))
    def test272(self):
        input = """lp: function void (auto/**/x: integer);"""
        expect = "Error on line 1 col 19: auto"
        self.assertTrue(TestParser.test(input, expect, 272))
    def test273(self):
        input = """ //a string \n b :string = 1;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect , 273))
        
    def test274(self):
        input = """ //"string\n" b " """
        expect = "Error on line 2 col 0:  b "
        self.assertTrue(TestParser.test(input, expect, 274))
        
    def test275(self):
        input = """ //string\n """
        expect = "Error on line 2 col 1: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 275))
        
    def test276(self):
        input = """ /* //string\n */ """
        expect = "Error on line 2 col 4: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 276))
        
    def test277(self):
        input = """ /* /* //\n\\t string **/ """
        expect = "Error on line 2 col 14: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 277))
        
    def test278(self):
        input = """ delta: string = "//this is a \n comment"; """
        expect = "//this is a "
        self.assertTrue(TestParser.test(input, expect, 278))

    def test279(self):
        input = """ //12__34:/aa/*\n*/ """
        expect = "Error on line 2 col 0: *"
        self.assertTrue(TestParser.test(input, expect, 279))
        
    def test280(self):
        input = """ //delta: integer = 1; """
        expect = "Error on line 1 col 23: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 280))
        
    def test281(self):
        input = """ /*delta: float = function () {} */ """
        expect = "Error on line 1 col 36: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 281))
        
    def test282(self):
        input = """ /////////////abs/////////***/ """
        expect = "Error on line 1 col 31: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 282))
        
    def test283(self):
        input = """ abc*/ """
        expect = "Error on line 1 col 4: *"
        self.assertTrue(TestParser.test(input, expect, 283))
    def test284(self):
        
        input = """main: function float(x: array[] of integer) {
                if (2<3) return a[x[y]];
                }"""
        expect = "Error on line 1 col 30: ]"
        self.assertTrue(TestParser.test(input, expect, 284))
    def test285(self):
        
        input = """main: function float(x: array[7] of float) {
                if (2<3) return a[x[y]];
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 285))
    def test286(self):
        
        input = """adj_Idnex: function auto(x: array[0] of string) {
                break;
                foo(t[a][_8] / 5);
                }"""
        expect = "Error on line 3 col 24: ["
        self.assertTrue(TestParser.test(input, expect, 286))
    def test287(self):
        input = """ fact: function integer (b: integer, a: array [5] of integer)
            {
                for( (i==0) , i<10, 2 + i)
                {
                writeln(a[i] + 124 + 12);
                }
            }
            main: function integer (x: integer)
            {
            x = 10;
            fact(x);
            """
        expect = """Error on line 3 col 21: ("""    
        self.assertTrue(TestParser.test(input,expect,287))
    def test288(self):
        input = """x: integer;
        fact: function integer (n: string)
        {
            if(n==0)
                return 1;
            else
                return n * fact(n-1);
        }
        t: integer;
        
        main: function integer (x: float)
        {
            x = 10;
            printString(x::"Hello"::"World");
            fact(x);
        }
                """
        expect = """Error on line 14 col 34: ::"""    
        self.assertTrue(TestParser.test(input,expect,288))
    def test289(self):
        input = """main: function integer (arr: array [100] of float, n: integer){
                    res: integer;
                    res = arr[0];
                    for (i = 1, i < n, 1){}  
                         if (arr[i] > res)
                            res = arr[i];
                    }
                """
        expect = """successful"""    
        self.assertTrue(TestParser.test(input,expect,289))
    def test290(self):
        input = """main: function integer (arr: array [2550] of float, n: integer){
                res: integer;
                    res = arr[0];
                    for (i = 1, i < n, 1)
                        if (arr[i] > res)
                            res = arr[i];
                    return res;
                }
                """
        expect = """successful"""    
        self.assertTrue(TestParser.test(input,expect,290))
    def test291(self):
        input = """main: function string (new: array [10] of integer, old: integer) {
                    size, i, j,p : integer;
                    size = new - old;
                    i = 1;
                    j = size - 1;
                    p = start[0];
                    while (true)
                    {
                        while (start[i] < p)
                            if (i == size - 1)
                                break;
                        while (start[j] > p)
                            if (j == 0)
                                break;
                        if (i >= j) 
                            break;
                        swap(start[i], start[j]);
                        //THis is the comment 
                    }
                    swap(start[0], start[j]);
                    return start[j];
                };
                """
        expect = """Error on line 22 col 17: ;"""    
        self.assertTrue(TestParser.test(input,expect,291))
    def test292(self):
        input = """main: function array [20,20] of integer (a: array [110,110] of integer, out b: array [10,10] of integer, r: integer, c: integer ) {
                    for (i = 0, i < r, 1) 
                        for (j = 0, j < c, 1)
                            b[j,i] = a[i,j];
                    return b;
                    /*This is the comment*/
                }
                """
        expect = """successful"""   
        self.assertTrue(TestParser.test(input,expect,292))
    def test293(self):
        input = """main: function integer (x: integer, y: float, z: auto) {
                if (y ==  34)
                {
                x = 1*2!4;
                a: array [5,1] of integer;
                }
                else return y; 
                }"""
        expect = """Error on line 4 col 23: !"""    
        self.assertTrue(TestParser.test(input,expect,293))
    def test294(self):
        input = """main: function integer (x: integer, y: float, z: auto) {}
                a_a= !(5>x) && (z!=y);
                """
        expect = """Error on line 2 col 19: ="""    
        self.assertTrue(TestParser.test(input,expect,294))
    def test295(self):
        input = """main: function string (10+1) {
                return "Hello" :: "World"; 
                }"""
        expect = """Error on line 1 col 23: 10"""    
        self.assertTrue(TestParser.test(input,expect,295))
    def test296(self):
        input = """main: function string (x: float,y: integer) {
                x=1;
                y= x + x * y;
                }"""
        expect = """successful"""    
        self.assertTrue(TestParser.test(input,expect,296))
    def test297(self):
        input = """x,y: integer;
        main: function void (x: integer, a_123: string) {
            i: integer =0;
            a[1+foo(2)] = a[b[3,4]]+5;
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,297))
    def test298(self):
        input = """
        main: function void (x: integer, a_123: string) {
            i: integer =0;
            {
                {
                    a[1+foo(2)] = a[b[3,4]]+5;
                }
            } 
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,298))
    def test299(self):
        input = """a: array [3] of string = {{}};"""
        expect = "successful"
        self.assertTrue(TestParser.test( input,expect,299))
    
    def test300(self):
        input = """getStr: function auto() {
                str[1_2] = ""::concatenate::foo("haizz"); 
                }"""
        expect = "Error on line 2 col 42: ::"
        self.assertTrue(TestParser.test( input,expect,300))
    