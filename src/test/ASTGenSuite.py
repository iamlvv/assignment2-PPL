import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test300(self):
        input = """x: integer;"""
        expect = str(Program([VarDecl("x", IntegerType())]))
        self.assertTrue(TestAST.test(input, expect, 300))

    def test301(self):
        input = """x, y, z: integer = 1, 2, 3;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 301))

    def test302(self):
        input = """x, y, z: integer = 1, 2, 3;
        a, b: float;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
])"""
        self.assertTrue(TestAST.test(input, expect, 302))

    def test303(self):
        """Simple program"""
        input = """main: function void () {
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test304(self):
        """More complex program"""
        input = """
foo: function void (inherit a: integer, inherit out b: float) inherit bar {}

main: function void () {
     printInteger(4);
}"""
        expect = """Program([
\tFuncDecl(foo, VoidType, [InheritParam(a, IntegerType), InheritOutParam(b, FloatType)], bar, BlockStmt([]))
\tFuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 304))
    
    def test305(self):
        input = """
foo: function void (inherit a: integer, inherit out b: float) inherit bar {
    return "hello";
}

main: function void () {
     printInteger(4);
}"""
        expect = """Program([
	FuncDecl(foo, VoidType, [InheritParam(a, IntegerType), InheritOutParam(b, FloatType)], bar, BlockStmt([ReturnStmt(StringLit(hello))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 305))
    
    def test306(self):
        input = """
        x: integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            delta: integer = fact(3);
            x: integer;
            y: integer = 43;
            inc(x, delta);
            printInteger(x);
        }
        """
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(65))
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, IntegerType, FuncCall(fact, [IntegerLit(3)])), VarDecl(x, IntegerType), VarDecl(y, IntegerType, IntegerLit(43)), CallStmt(inc, Id(x), Id(delta)), CallStmt(printInteger, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 306))
    
    def test307(self):
        input = """main: function void () {}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 307))
    
    def test308(self):
        input = """main: function void () {
                while (true) {
                    x: integer;
                    x = x + 1;
                    return x;
                }
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BooleanLit(True), BlockStmt([VarDecl(x, IntegerType), AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1))), ReturnStmt(Id(x))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 308))
    
    def test309(self):
        input = """ //a
        b, T: string = "chau", str::str; """
        expected = """Program([
	VarDecl(b, StringType, StringLit(chau))
	VarDecl(T, StringType, BinExpr(::, Id(str), Id(str)))
])"""
        self.assertTrue(TestAST.test(input, expected, 309))
    
    def test310(self):
        input = """ /*
        a
        */
        b, T: string = "chau", str::str; """
        expect = """Program([
	VarDecl(b, StringType, StringLit(chau))
	VarDecl(T, StringType, BinExpr(::, Id(str), Id(str)))
])"""
        self.assertTrue(TestAST.test(input, expect, 310))
    
    def test311(self):
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
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, IntegerType, FuncCall(fact, [IntegerLit(3)])), CallStmt(inc, Id(x), Id(delta)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(writeLn, Id(i))])), CallStmt(printInteger, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 311))
        
    def test312(self):
        input = """fact: function integer (n: integer) {
            while (i < 1) {
                for (i = 0, i < 10, i+1) {
                    break;
                    continue;
                    return i == 1;
                }
            }
            }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([WhileStmt(BinExpr(<, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([BreakStmt(), ContinueStmt(), ReturnStmt(BinExpr(==, Id(i), IntegerLit(1)))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 312))
    
    def test313(self):
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
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([DoWhileStmt(BinExpr(==, Id(n), IntegerLit(10)), BlockStmt([WhileStmt(BinExpr(<, BinExpr(+, Id(i), BinExpr(+, IntegerLit(2), IntegerLit(3))), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), BinExpr(+, IntegerLit(10), IntegerLit(1))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(print, StringLit(Hello World))]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 313))
    
    def test314(self):
        input = """fact: function integer (n: integer) {
            foo(2+x, 4.0/y);
            goo();
            super(2 * x, (2+3) /2 % 3 == 21);
            }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([CallStmt(foo, BinExpr(+, IntegerLit(2), Id(x)), BinExpr(/, FloatLit(4.0), Id(y))), CallStmt(goo, ), CallStmt(super, BinExpr(*, IntegerLit(2), Id(x)), BinExpr(==, BinExpr(%, BinExpr(/, BinExpr(+, IntegerLit(2), IntegerLit(3)), IntegerLit(2)), IntegerLit(3)), IntegerLit(21)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 314))
    
    def test315(self):
        input = """_45_0: function auto () {
                return arr[5_6,1.];
                }"""
        expect = """Program([
	FuncDecl(_45_0, AutoType, [], None, BlockStmt([ReturnStmt(ArrayCell(arr, [IntegerLit(56), FloatLit(1.0)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 315))
    
    def test316(self):
        input = """_45_0: function auto () {
                return arr[5_6,1.];
                if (n == 0) return 1;
                else return (n - 1) + fact(n + 2);
                }"""
        expect = """Program([
	FuncDecl(_45_0, AutoType, [], None, BlockStmt([ReturnStmt(ArrayCell(arr, [IntegerLit(56), FloatLit(1.0)])), IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(+, BinExpr(-, Id(n), IntegerLit(1)), FuncCall(fact, [BinExpr(+, Id(n), IntegerLit(2))]))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 316))
    
    def test317(self):
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
        expect = """Program([
	FuncDecl(_45_0, AutoType, [], None, BlockStmt([ReturnStmt(ArrayCell(arr, [IntegerLit(56), FloatLit(1.0), StringLit(helloChau)])), DoWhileStmt(BinExpr(==, BinExpr(*, Id(n), IntegerLit(2)), IntegerLit(1)), BlockStmt([CallStmt(helloworld, IntegerLit(2))])), WhileStmt(BinExpr(>, Id(x), IntegerLit(1)), BlockStmt([CallStmt(print, Id(x))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 317))
    
    def test318(self):
        input = """ a, b, c: auto = 4., 1+2, x; """
        expect = """Program([
	VarDecl(a, AutoType, FloatLit(4.0))
	VarDecl(b, AutoType, BinExpr(+, IntegerLit(1), IntegerLit(2)))
	VarDecl(c, AutoType, Id(x))
])"""
        self.assertTrue(TestAST.test(input, expect, 318))
        
    def test319(self):
        input = """x:array[3_6,0] of integer = {1,2,4};"""
        expect = """Program([
	VarDecl(x, ArrayType([36, 0], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(4)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 319))
    
    def test320(self):
        input = """_12:array[3_6,12] of float = {};"""
        expect = """Program([
	VarDecl(_12, ArrayType([36, 12], FloatType), ArrayLit([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 320))
    
    def test321(self):
        input = """avg: float = (a + b + c2)/3;"""
        expect = """Program([
	VarDecl(avg, FloatType, BinExpr(/, BinExpr(+, BinExpr(+, Id(a), Id(b)), Id(c2)), IntegerLit(3)))
])"""
        self.assertTrue(TestAST.test(input, expect, 321))
    
    def test322(self):
        input = """getName: function string (inherit out x:array[2_1,8] of float) {
                return;
                }"""
        expect = """Program([
	FuncDecl(getName, StringType, [InheritOutParam(x, ArrayType([21, 8], FloatType))], None, BlockStmt([ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 322))
    
    def test323(self):
        input = """ a, b, c: auto = 4., 1+2, x; """
        expect = """Program([
	VarDecl(a, AutoType, FloatLit(4.0))
	VarDecl(b, AutoType, BinExpr(+, IntegerLit(1), IntegerLit(2)))
	VarDecl(c, AutoType, Id(x))
])"""
        self.assertTrue(TestAST.test(input, expect, 323))
    
    def test324(self):
        input = """a, b, c: integer = 3, 4, "hello";"""
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(3))
	VarDecl(b, IntegerType, IntegerLit(4))
	VarDecl(c, IntegerType, StringLit(hello))
])"""
        self.assertTrue(TestAST.test(input, expect, 324))
    
    def test325(self):
        input = """name: string = "helloguys"::WorldwideWeb[5,1_7];"""
        expect = """Program([
	VarDecl(name, StringType, BinExpr(::, StringLit(helloguys), ArrayCell(WorldwideWeb, [IntegerLit(5), IntegerLit(17)])))
])"""
        self.assertTrue(TestAST.test(input, expect, 325))
    
    def test326(self):
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
        expect = """Program([
	FuncDecl(main, VoidType, [Param(x, IntegerType), Param(a_123, StringType)], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), BlockStmt([BlockStmt([AssignStmt(ArrayCell(a, [BinExpr(+, IntegerLit(1), FuncCall(foo, [IntegerLit(2)]))]), BinExpr(+, BinExpr(+, IntegerLit(5), IntegerLit(3)), BinExpr(*, IntegerLit(2), IntegerLit(2))))])])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 326))
    
    def test327(self):
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
        expect = """Program([
	FuncDecl(main, VoidType, [Param(x, IntegerType), Param(a_123, StringType)], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), BlockStmt([BlockStmt([AssignStmt(ArrayCell(a, [BinExpr(+, IntegerLit(1), FuncCall(foo, [IntegerLit(2)]))]), BinExpr(+, BinExpr(+, IntegerLit(5), IntegerLit(3)), BinExpr(*, IntegerLit(2), IntegerLit(2))))])])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 327))
    
    def test328(self):
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
        expect = """Program([
	FuncDecl(main, VoidType, [Param(x, IntegerType), Param(a_123, StringType)], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), BlockStmt([BlockStmt([AssignStmt(ArrayCell(a, [BinExpr(+, IntegerLit(1), FuncCall(foo, [IntegerLit(2)]))]), BinExpr(+, BinExpr(+, IntegerLit(5), IntegerLit(3)), BinExpr(*, IntegerLit(2), IntegerLit(2)))), WhileStmt(BinExpr(>, Id(x), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(1)), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))))]))])])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 328))
    
    def test329(self):
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
        expect = """Program([
	FuncDecl(main, VoidType, [Param(x, IntegerType), Param(a_123, StringType)], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), BlockStmt([BlockStmt([AssignStmt(ArrayCell(a, [BinExpr(+, IntegerLit(1), FuncCall(foo, [IntegerLit(2)]))]), BinExpr(+, BinExpr(+, IntegerLit(5), IntegerLit(3)), BinExpr(*, IntegerLit(2), IntegerLit(2)))), WhileStmt(BinExpr(>, Id(x), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(1)), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))), BreakStmt(), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<=, Id(i), IntegerLit(10)), BinExpr(+, Id(i), FloatLit(10001.03)), BlockStmt([CallStmt(writeln, )]))]))])])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 329))
    
    def test330(self):
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
        expect = """Program([
	FuncDecl(main, VoidType, [Param(x, IntegerType), Param(a_123, StringType)], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), BlockStmt([BlockStmt([AssignStmt(ArrayCell(a, [BinExpr(+, IntegerLit(1), FuncCall(foo, [IntegerLit(2)]))]), BinExpr(+, BinExpr(+, IntegerLit(5), IntegerLit(3)), BinExpr(*, IntegerLit(2), IntegerLit(2)))), WhileStmt(BinExpr(>, Id(x), IntegerLit(1)), BlockStmt([DoWhileStmt(BinExpr(>, Id(x), IntegerLit(1)), BlockStmt([WhileStmt(BinExpr(<, Id(n), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(i), FloatLit(3.0)), BinExpr(>=, Id(i), BinExpr(+, BinExpr(+, IntegerLit(10), IntegerLit(1)), IntegerLit(2))), BinExpr(+, Id(i), IntegerLit(2)), BlockStmt([ReturnStmt()]))]))])), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))]))])])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 330))
    
    def test331(self):
        input = """ //a string \n b :string = 1;"""
        expected = """Program([
	VarDecl(b, StringType, IntegerLit(1))
])"""
        self.assertTrue(TestAST.test(input, expected, 331))
        
    def test332(self):
        input = """main: function float(x: array[7] of float) {
                if (2<3) return a[x[y]];
                }"""
        expected = """Program([
	FuncDecl(main, FloatType, [Param(x, ArrayType([7], FloatType))], None, BlockStmt([IfStmt(BinExpr(<, IntegerLit(2), IntegerLit(3)), ReturnStmt(ArrayCell(a, [ArrayCell(x, [Id(y)])])))]))
])"""
        self.assertTrue(TestAST.test(input, expected, 332))
    
    def test333(self):
        input = """main: function integer (arr: array [100] of float, n: integer){
                    res: integer;
                    res = arr[0];
                    for (i = 1, i < n, 1){}  
                         if (arr[i] > res)
                            res = arr[i];
                    }
                """
        expected = """Program([
	FuncDecl(main, IntegerType, [Param(arr, ArrayType([100], FloatType)), Param(n, IntegerType)], None, BlockStmt([VarDecl(res, IntegerType), AssignStmt(Id(res), ArrayCell(arr, [IntegerLit(0)])), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), Id(n)), IntegerLit(1), BlockStmt([])), IfStmt(BinExpr(>, ArrayCell(arr, [Id(i)]), Id(res)), AssignStmt(Id(res), ArrayCell(arr, [Id(i)])))]))
])"""
        self.assertTrue(TestAST.test(input, expected, 333))
    
    def test334(self):
        input = """main: function integer (arr: array [2550] of float, n: integer){
                res: integer;
                    res = arr[0];
                    for (i = 1, i < n, 1)
                        if (arr[i] > res)
                            res = arr[i];
                    return res;
                }
                """
        expected = """Program([
	FuncDecl(main, IntegerType, [Param(arr, ArrayType([2550], FloatType)), Param(n, IntegerType)], None, BlockStmt([VarDecl(res, IntegerType), AssignStmt(Id(res), ArrayCell(arr, [IntegerLit(0)])), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), Id(n)), IntegerLit(1), IfStmt(BinExpr(>, ArrayCell(arr, [Id(i)]), Id(res)), AssignStmt(Id(res), ArrayCell(arr, [Id(i)])))), ReturnStmt(Id(res))]))
])"""
        self.assertTrue(TestAST.test(input, expected, 334))
    
    def test335(self):
        input = """main: function array [20,20] of integer (a: array [110,110] of integer, out b: array [10,10] of integer, r: integer, c: integer ) {
                    for (i = 0, i < r, 1) 
                        for (j = 0, j < c, 1)
                            b[j,i] = a[i,j];
                    return b;
                    /*This is the comment*/
                }
                """
        expected = """Program([
	FuncDecl(main, ArrayType([20, 20], IntegerType), [Param(a, ArrayType([110, 110], IntegerType)), OutParam(b, ArrayType([10, 10], IntegerType)), Param(r, IntegerType), Param(c, IntegerType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(r)), IntegerLit(1), ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), Id(c)), IntegerLit(1), AssignStmt(ArrayCell(b, [Id(j), Id(i)]), ArrayCell(a, [Id(i), Id(j)])))), ReturnStmt(Id(b))]))
])"""
        self.assertTrue(TestAST.test(input, expected, 335))
    
    def test336(self):
        input = """main: function string (x: float,y: integer) {
                x=1;
                y= x + x * y;
                }"""
        expected = """Program([
	FuncDecl(main, StringType, [Param(x, FloatType), Param(y, IntegerType)], None, BlockStmt([AssignStmt(Id(x), IntegerLit(1)), AssignStmt(Id(y), BinExpr(+, Id(x), BinExpr(*, Id(x), Id(y))))]))
])"""
        self.assertTrue(TestAST.test(input, expected, 336))

    def test337(self):
        input = """x,y: integer;
        main: function void (x: integer, a_123: string) {
            i: integer =0;
            a[1+foo(2)] = a[b[3,4]]+5;
        }
        """
        expected = """Program([
	VarDecl(x, IntegerType)
	VarDecl(y, IntegerType)
	FuncDecl(main, VoidType, [Param(x, IntegerType), Param(a_123, StringType)], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), AssignStmt(ArrayCell(a, [BinExpr(+, IntegerLit(1), FuncCall(foo, [IntegerLit(2)]))]), BinExpr(+, ArrayCell(a, [ArrayCell(b, [IntegerLit(3), IntegerLit(4)])]), IntegerLit(5)))]))
])"""
        self.assertTrue(TestAST.test(input, expected, 337))
    
    def test338(self):
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
        expected = """Program([
	FuncDecl(main, VoidType, [Param(x, IntegerType), Param(a_123, StringType)], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), BlockStmt([BlockStmt([AssignStmt(ArrayCell(a, [BinExpr(+, IntegerLit(1), FuncCall(foo, [IntegerLit(2)]))]), BinExpr(+, ArrayCell(a, [ArrayCell(b, [IntegerLit(3), IntegerLit(4)])]), IntegerLit(5)))])])]))
])"""
        self.assertTrue(TestAST.test(input, expected, 338))
    
    def test339(self):
        input = """a: array [3] of string = {{}};"""
        expected = """Program([
	VarDecl(a, ArrayType([3], StringType), ArrayLit([ArrayLit([])]))
])"""
        self.assertTrue(TestAST.test(input, expected, 339))
        
    def test340(self):
        input = """a: array [3] of string = {"abc", "def", "ghi"};"""
        expected = """Program([
	VarDecl(a, ArrayType([3], StringType), ArrayLit([StringLit(abc), StringLit(def), StringLit(ghi)]))
])"""
        self.assertTrue(TestAST.test(input, expected, 340))
        
    def test341(self):
        input = """a: function integer (abc: integer,cba:string,_12_3:float) {} b: function void () {}
                _C: function float () {}"""
        expected = """Program([
	FuncDecl(a, IntegerType, [Param(abc, IntegerType), Param(cba, StringType), Param(_12_3, FloatType)], None, BlockStmt([]))
	FuncDecl(b, VoidType, [], None, BlockStmt([]))
	FuncDecl(_C, FloatType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expected, 341))
        
    def test342(self):
        input = """a,b,c: integer = 11,11+2,11+0+4;"""
        expected = """Program([
	VarDecl(a, IntegerType, IntegerLit(11))
	VarDecl(b, IntegerType, BinExpr(+, IntegerLit(11), IntegerLit(2)))
	VarDecl(c, IntegerType, BinExpr(+, BinExpr(+, IntegerLit(11), IntegerLit(0)), IntegerLit(4)))
])"""
        self.assertTrue(TestAST.test(input, expected, 342))
    
    def test343(self):
        input = """a: float = .12E+3;"""
        expected = """Program([
	VarDecl(a, FloatType, FloatLit(120.0))
])"""
        self.assertTrue(TestAST.test(input, expected, 343))
    
    def test344(self):
        input = """a,a__1,a__2 : float = 123.0e4, 123.E+0, 1_2_3;"""
        expected = """Program([
	VarDecl(a, FloatType, FloatLit(1230000.0))
	VarDecl(a__1, FloatType, FloatLit(123.0))
	VarDecl(a__2, FloatType, IntegerLit(123))
])"""
        self.assertTrue(TestAST.test(input, expected, 344))
    
    def test345(self):
        input = """a: array [2,3] of integer = {1,2,{},{2,3,4},{4,5,6},1,2};"""
        expected = """Program([
	VarDecl(a, ArrayType([2, 3], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), ArrayLit([]), ArrayLit([IntegerLit(2), IntegerLit(3), IntegerLit(4)]), ArrayLit([IntegerLit(4), IntegerLit(5), IntegerLit(6)]), IntegerLit(1), IntegerLit(2)]))
])"""
        self.assertTrue(TestAST.test(input, expected, 345))
    
    def test346(self):
        input = """a: array [3] of string = {{}};"""
        expected = """Program([
	VarDecl(a, ArrayType([3], StringType), ArrayLit([ArrayLit([])]))
])"""
        self.assertTrue(TestAST.test(input, expected, 346))
    
    def test347(self):
        input= """a,b,c,d : auto;"""
        expected = """Program([
	VarDecl(a, AutoType)
	VarDecl(b, AutoType)
	VarDecl(c, AutoType)
	VarDecl(d, AutoType)
])"""
        self.assertTrue(TestAST.test(input, expected, 347))
    
    def test348(self):
        input = """a: integer =1 ;
        b: array [2] of integer = {{2,3,4},{4,5,6}};
        a,b : float;
        a, b : array [2] of integer= {1,2},{   2   ,   3   };
                """
        expected = """Program([
	VarDecl(a, IntegerType, IntegerLit(1))
	VarDecl(b, ArrayType([2], IntegerType), ArrayLit([ArrayLit([IntegerLit(2), IntegerLit(3), IntegerLit(4)]), ArrayLit([IntegerLit(4), IntegerLit(5), IntegerLit(6)])]))
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
	VarDecl(a, ArrayType([2], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2)]))
	VarDecl(b, ArrayType([2], IntegerType), ArrayLit([IntegerLit(2), IntegerLit(3)]))
])"""
        self.assertTrue(TestAST.test(input, expected, 348))
    
    def test349(self):
        input = """ x: float = -12E3;"""
        expected = """Program([
	VarDecl(x, FloatType, UnExpr(-, FloatLit(12000.0)))
])"""
        self.assertTrue(TestAST.test(input, expected, 349))
    
    def test350(self):
        input = """
        x: array [2] of float;
        a: function integer (inherit out abc: integer) {
            x = 11;
            b[c[2==2]]=4;
            foo(x);
        }"""
        expected = """Program([
	VarDecl(x, ArrayType([2], FloatType))
	FuncDecl(a, IntegerType, [InheritOutParam(abc, IntegerType)], None, BlockStmt([AssignStmt(Id(x), IntegerLit(11)), AssignStmt(ArrayCell(b, [ArrayCell(c, [BinExpr(==, IntegerLit(2), IntegerLit(2))])]), IntegerLit(4)), CallStmt(foo, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expected, 350))
    
    def test351(self):
        input = """
        x: auto;
        a: function integer (inherit out n: integer){
           if (n == 0) return 1;
            else return n * a(n - 1); 
        }
        main: function void (x: integer)
        {
            x=11;
            foo(x);
        }"""
        expected = """Program([
	VarDecl(x, AutoType)
	FuncDecl(a, IntegerType, [InheritOutParam(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(a, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	FuncDecl(main, VoidType, [Param(x, IntegerType)], None, BlockStmt([AssignStmt(Id(x), IntegerLit(11)), CallStmt(foo, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expected, 351))
    
    def test352(self):
        input = """
        main: function void (x: integer, a_123: string) {
            i: integer =0;
            a[1+foo(2)] = a[b[3,4]]+5;
            x[1_2_3] = {1,2,{1,2}};
        }
        """
        expected = """Program([
	FuncDecl(main, VoidType, [Param(x, IntegerType), Param(a_123, StringType)], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), AssignStmt(ArrayCell(a, [BinExpr(+, IntegerLit(1), FuncCall(foo, [IntegerLit(2)]))]), BinExpr(+, ArrayCell(a, [ArrayCell(b, [IntegerLit(3), IntegerLit(4)])]), IntegerLit(5))), AssignStmt(ArrayCell(x, [IntegerLit(123)]), ArrayLit([IntegerLit(1), IntegerLit(2), ArrayLit([IntegerLit(1), IntegerLit(2)])]))]))
])"""
        self.assertTrue(TestAST.test(input, expected, 352))
    
    def test353(self):
        input = """
        main: function void (x: integer, a_123: string) {
            i: integer =0;
            x[1+2*3] = {1,2,{1,2}};
            y= z[foo(1)*foo[2]%foo(2)];

        }
        """
        expected = """Program([
	FuncDecl(main, VoidType, [Param(x, IntegerType), Param(a_123, StringType)], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), AssignStmt(ArrayCell(x, [BinExpr(+, IntegerLit(1), BinExpr(*, IntegerLit(2), IntegerLit(3)))]), ArrayLit([IntegerLit(1), IntegerLit(2), ArrayLit([IntegerLit(1), IntegerLit(2)])])), AssignStmt(Id(y), ArrayCell(z, [BinExpr(%, BinExpr(*, FuncCall(foo, [IntegerLit(1)]), ArrayCell(foo, [IntegerLit(2)])), FuncCall(foo, [IntegerLit(2)]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expected, 353))
        
    def test354(self):
        input = """
        main: function void (a: string, b: string) {
            printString(a::b);
        }
        """
        expected = """Program([
	FuncDecl(main, VoidType, [Param(a, StringType), Param(b, StringType)], None, BlockStmt([CallStmt(printString, BinExpr(::, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expected, 354))
    
    def test355(self):
        input = """
        main: function void (x: integer, a_123: string) {
            i: integer =0;
            a[3+foo(2)] = a[b[2/3]]+4;
            x[1_2_3] = {1,2,{1,2}};
            d= e[foo(2)+a[5]*foo(2)];
        }"""
        expected = """Program([
	FuncDecl(main, VoidType, [Param(x, IntegerType), Param(a_123, StringType)], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), AssignStmt(ArrayCell(a, [BinExpr(+, IntegerLit(3), FuncCall(foo, [IntegerLit(2)]))]), BinExpr(+, ArrayCell(a, [ArrayCell(b, [BinExpr(/, IntegerLit(2), IntegerLit(3))])]), IntegerLit(4))), AssignStmt(ArrayCell(x, [IntegerLit(123)]), ArrayLit([IntegerLit(1), IntegerLit(2), ArrayLit([IntegerLit(1), IntegerLit(2)])])), AssignStmt(Id(d), ArrayCell(e, [BinExpr(+, FuncCall(foo, [IntegerLit(2)]), BinExpr(*, ArrayCell(a, [IntegerLit(5)]), FuncCall(foo, [IntegerLit(2)])))]))]))
])"""
        self.assertTrue(TestAST.test(input, expected, 355))
    
    def test356(self):
        input = r"""foo: /*comment*/function void (a: integer, b: float) {
                    i: float = .0E1;
                    while (true)
                    {
                        a[i] = b + 1.0;
                        i=i+1;
                    }
                }"""
        expected = """Program([
	FuncDecl(foo, VoidType, [Param(a, IntegerType), Param(b, FloatType)], None, BlockStmt([VarDecl(i, FloatType, FloatLit(0.0)), WhileStmt(BooleanLit(True), BlockStmt([AssignStmt(ArrayCell(a, [Id(i)]), BinExpr(+, Id(b), FloatLit(1.0))), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expected, 356))
    
    def test357(self):
        input = r"""foo: /*comment*/function void (a: integer, b: float) {
                    i: float = .0E1;
                    while (i<=5)
                    {
                        a[i] = b + 1.0;
                        i=i+1;
                    }
                }"""
        expected = """Program([
	FuncDecl(foo, VoidType, [Param(a, IntegerType), Param(b, FloatType)], None, BlockStmt([VarDecl(i, FloatType, FloatLit(0.0)), WhileStmt(BinExpr(<=, Id(i), IntegerLit(5)), BlockStmt([AssignStmt(ArrayCell(a, [Id(i)]), BinExpr(+, Id(b), FloatLit(1.0))), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expected, 357))
    
    def test358(self):
        input = r"""foo: /*comment*/function void (a: integer, b: float) {
                    i: float = .0E2;
                    do {
                        a[i] = b + 1.0;
                        i=i+1;
                    }
                    while (false);
                }"""
        expected = """Program([
	FuncDecl(foo, VoidType, [Param(a, IntegerType), Param(b, FloatType)], None, BlockStmt([VarDecl(i, FloatType, FloatLit(0.0)), DoWhileStmt(BooleanLit(False), BlockStmt([AssignStmt(ArrayCell(a, [Id(i)]), BinExpr(+, Id(b), FloatLit(1.0))), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expected, 358))
    
    def test359(self):
        input = """fact: function boolean (x: integer) {
            return x==10;}"""
        expected = """Program([
	FuncDecl(fact, BooleanType, [Param(x, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(==, Id(x), IntegerLit(10)))]))
])"""
        self.assertTrue(TestAST.test(input, expected, 359))
    
    def test360(self):
        input = """fact: function integer (x: integer, y: float, z: auto) {
                if (1+1)
                {
                x=1;
                y= 1_2_3.45;
                }
                break;}"""
        expected = """Program([
	FuncDecl(fact, IntegerType, [Param(x, IntegerType), Param(y, FloatType), Param(z, AutoType)], None, BlockStmt([IfStmt(BinExpr(+, IntegerLit(1), IntegerLit(1)), BlockStmt([AssignStmt(Id(x), IntegerLit(1)), AssignStmt(Id(y), FloatLit(123.45))])), BreakStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expected, 360))
        
    def test361(self):
        input = """main: function string (x: array [100] of integer,n: integer, exp: float) {
                    output: array [100] of integer;
                    count: array [10] of integer = {0};
                    i: integer;
                    for (i = 0, i < n, i+1)
                        count[(arr[i] / exp) % 10] = count[(arr[i] / exp) % 10] + 1;
                    for (i = 1, i < 10, i+1)
                        count[i] = count[i] + count[i-1];
                    for (i = n-1, i >= 0, i-1)
                    {
                        output[count[(arr[i] / exp)%10] - 1] = arr[i];
                        count[(arr[i] / exp) % 10] = count[(arr[i] / exp) % 10] - 1;
                    }
                }
                """
        expected = """Program([
	FuncDecl(main, StringType, [Param(x, ArrayType([100], IntegerType)), Param(n, IntegerType), Param(exp, FloatType)], None, BlockStmt([VarDecl(output, ArrayType([100], IntegerType)), VarDecl(count, ArrayType([10], IntegerType), ArrayLit([IntegerLit(0)])), VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(ArrayCell(count, [BinExpr(%, BinExpr(/, ArrayCell(arr, [Id(i)]), Id(exp)), IntegerLit(10))]), BinExpr(+, ArrayCell(count, [BinExpr(%, BinExpr(/, ArrayCell(arr, [Id(i)]), Id(exp)), IntegerLit(10))]), IntegerLit(1)))), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(ArrayCell(count, [Id(i)]), BinExpr(+, ArrayCell(count, [Id(i)]), ArrayCell(count, [BinExpr(-, Id(i), IntegerLit(1))])))), ForStmt(AssignStmt(Id(i), BinExpr(-, Id(n), IntegerLit(1))), BinExpr(>=, Id(i), IntegerLit(0)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(output, [BinExpr(-, ArrayCell(count, [BinExpr(%, BinExpr(/, ArrayCell(arr, [Id(i)]), Id(exp)), IntegerLit(10))]), IntegerLit(1))]), ArrayCell(arr, [Id(i)])), AssignStmt(ArrayCell(count, [BinExpr(%, BinExpr(/, ArrayCell(arr, [Id(i)]), Id(exp)), IntegerLit(10))]), BinExpr(-, ArrayCell(count, [BinExpr(%, BinExpr(/, ArrayCell(arr, [Id(i)]), Id(exp)), IntegerLit(10))]), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expected, 361))
    
    def test362(self):
        input = """main: function string (start: array [10] of integer, end: integer) {
                    size, i, j,p : integer;
                    size = end - start;
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
                    }
                    swap(start[0], start[j]);
                    return start[j];
                }
                """
        expected = """Program([
	FuncDecl(main, StringType, [Param(start, ArrayType([10], IntegerType)), Param(end, IntegerType)], None, BlockStmt([VarDecl(size, IntegerType), VarDecl(i, IntegerType), VarDecl(j, IntegerType), VarDecl(p, IntegerType), AssignStmt(Id(size), BinExpr(-, Id(end), Id(start))), AssignStmt(Id(i), IntegerLit(1)), AssignStmt(Id(j), BinExpr(-, Id(size), IntegerLit(1))), AssignStmt(Id(p), ArrayCell(start, [IntegerLit(0)])), WhileStmt(BooleanLit(True), BlockStmt([WhileStmt(BinExpr(<, ArrayCell(start, [Id(i)]), Id(p)), IfStmt(BinExpr(==, Id(i), BinExpr(-, Id(size), IntegerLit(1))), BreakStmt())), WhileStmt(BinExpr(>, ArrayCell(start, [Id(j)]), Id(p)), IfStmt(BinExpr(==, Id(j), IntegerLit(0)), BreakStmt())), IfStmt(BinExpr(>=, Id(i), Id(j)), BreakStmt()), CallStmt(swap, ArrayCell(start, [Id(i)]), ArrayCell(start, [Id(j)]))])), CallStmt(swap, ArrayCell(start, [IntegerLit(0)]), ArrayCell(start, [Id(j)])), ReturnStmt(ArrayCell(start, [Id(j)]))]))
])"""
        self.assertTrue(TestAST.test(input, expected, 362))
    
    def test363(self):
        input = """swap: function array [10,10] of integer (a: array [10,10] of integer, out b: array [10,10] of integer, r: integer, c: integer ) {
                    for (i = 0, i < r, 1) 
                        for (j = 0, j < c, 1)
                            b[j,i] = a[i,j];
                    return b;
                }
                """
        expected = """Program([
	FuncDecl(swap, ArrayType([10, 10], IntegerType), [Param(a, ArrayType([10, 10], IntegerType)), OutParam(b, ArrayType([10, 10], IntegerType)), Param(r, IntegerType), Param(c, IntegerType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(r)), IntegerLit(1), ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), Id(c)), IntegerLit(1), AssignStmt(ArrayCell(b, [Id(j), Id(i)]), ArrayCell(a, [Id(i), Id(j)])))), ReturnStmt(Id(b))]))
])"""
        self.assertTrue(TestAST.test(input, expected, 363))
    
    def test364(self):
        input = """main: function integer (arr: array [100] of integer, n: integer){
                res: integer;
                    res = arr[0];
                    for (i = 1, i < n, 1)
                        if (arr[i] > res)
                            res = arr[i];
                    return res;
                }
                """
        expected = """Program([
	FuncDecl(main, IntegerType, [Param(arr, ArrayType([100], IntegerType)), Param(n, IntegerType)], None, BlockStmt([VarDecl(res, IntegerType), AssignStmt(Id(res), ArrayCell(arr, [IntegerLit(0)])), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), Id(n)), IntegerLit(1), IfStmt(BinExpr(>, ArrayCell(arr, [Id(i)]), Id(res)), AssignStmt(Id(res), ArrayCell(arr, [Id(i)])))), ReturnStmt(Id(res))]))
])"""
        self.assertTrue(TestAST.test(input, expected, 364))
    
    def test365(self):
        input = """main: function integer (arr: array [100] of integer, n: integer){
                    res: integer;
                    res = arr[0];
                    for (i = 1, i < n, 1){}  
                         if (arr[i] > res)
                            res = arr[i];
                    }
                """
        expected = """Program([
	FuncDecl(main, IntegerType, [Param(arr, ArrayType([100], IntegerType)), Param(n, IntegerType)], None, BlockStmt([VarDecl(res, IntegerType), AssignStmt(Id(res), ArrayCell(arr, [IntegerLit(0)])), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), Id(n)), IntegerLit(1), BlockStmt([])), IfStmt(BinExpr(>, ArrayCell(arr, [Id(i)]), Id(res)), AssignStmt(Id(res), ArrayCell(arr, [Id(i)])))]))
])"""
        self.assertTrue(TestAST.test(input, expected, 365))
    
    def test366(self):
        input = """x: integer;
        fact: function integer (n: integer)
        {
            if(n==0)
                return 1;
            else
                return n* fact(n-1);
        }
        /*
        comment
        */
        main: function integer (x: integer)
        {
            x = 10;
            fact(x);
        }
        """
        expected = """Program([
	VarDecl(x, IntegerType)
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	FuncDecl(main, IntegerType, [Param(x, IntegerType)], None, BlockStmt([AssignStmt(Id(x), IntegerLit(10)), CallStmt(fact, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expected, 366))
    
    def test367(self):
        input = """main: function integer (a: array [2] of integer, b: integer)
        {
            i: integer =0;
            while (a[i] > b)
            {
                writeln(a[i]);
                i = i + 1;
            }
                    
        }
                """
        expected = """Program([
	FuncDecl(main, IntegerType, [Param(a, ArrayType([2], IntegerType)), Param(b, IntegerType)], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), WhileStmt(BinExpr(>, ArrayCell(a, [Id(i)]), Id(b)), BlockStmt([CallStmt(writeln, ArrayCell(a, [Id(i)])), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expected, 367))
    
    def test368(self):
        input = """fact: function float(x: array[7] of string) {
                if (2<3) return a[x[y]];
                }"""
        expected = """Program([
	FuncDecl(fact, FloatType, [Param(x, ArrayType([7], StringType))], None, BlockStmt([IfStmt(BinExpr(<, IntegerLit(2), IntegerLit(3)), ReturnStmt(ArrayCell(a, [ArrayCell(x, [Id(y)])])))]))
])"""
        self.assertTrue(TestAST.test(input, expected, 368))
    
    def test369(self):
        input = """a: integer = a*1.2E-9;"""
        expected = """Program([
	VarDecl(a, IntegerType, BinExpr(*, Id(a), FloatLit(1.2e-09)))
])"""
        self.assertTrue(TestAST.test(input, expected, 369))
    
    def test370(self):
        input = """abcd,_12_3 : boolean = abcd(),true&&false;"""
        expected = """Program([
	VarDecl(abcd, BooleanType, FuncCall(abcd, []))
	VarDecl(_12_3, BooleanType, BinExpr(&&, BooleanLit(True), BooleanLit(False)))
])"""
        self.assertTrue(TestAST.test(input, expected, 370))
    
    def test371(self):
        input = """dope : array[3,10_2] of string = {1,{5.6e-34},4};"""
        expected = """Program([
	VarDecl(dope, ArrayType([3, 102], StringType), ArrayLit([IntegerLit(1), ArrayLit([FloatLit(5.6e-34)]), IntegerLit(4)]))
])"""
        self.assertTrue(TestAST.test(input, expected, 371))
        
    def test372(self):
        input = """non_Assoc1st: function string(inherit out x:array[2] of string) {
                x[1,2] = (""::concat)::foo("haizz"); 
                }"""
        expected = """Program([
	FuncDecl(non_Assoc1st, StringType, [InheritOutParam(x, ArrayType([2], StringType))], None, BlockStmt([AssignStmt(ArrayCell(x, [IntegerLit(1), IntegerLit(2)]), BinExpr(::, BinExpr(::, StringLit(), Id(concat)), FuncCall(foo, [StringLit(haizz)])))]))
])"""
        self.assertTrue(TestAST.test(input, expected, 372))
    
    def test373(self):
        input = """fact: function integer(n: auto) {
                fact = n * fact(n-!-1);
                return fact;
                }"""
        expected = """Program([
	FuncDecl(fact, IntegerType, [Param(n, AutoType)], None, BlockStmt([AssignStmt(Id(fact), BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), UnExpr(!, UnExpr(-, IntegerLit(1))))]))), ReturnStmt(Id(fact))]))
])"""
        self.assertTrue(TestAST.test(input, expected, 373))
    
    def test374(self):
        input = """__C__: array[7] of float = germanyTOM(jK[""::{""}]);"""
        expected = """Program([
	VarDecl(__C__, ArrayType([7], FloatType), FuncCall(germanyTOM, [ArrayCell(jK, [BinExpr(::, StringLit(), ArrayLit([StringLit()]))])]))
])"""
        self.assertTrue(TestAST.test(input, expected, 374))
    
    def test375(self):
        input = """func: function void() {
                for (idx[1]=2_1,7==(4>5),--i) {
                    arr:array[3_1,0] of string;
                    arr[idx[i]] = arr[idx[i]]::"jdk";
                    }
                }"""
        expected = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(ArrayCell(idx, [IntegerLit(1)]), IntegerLit(21)), BinExpr(==, IntegerLit(7), BinExpr(>, IntegerLit(4), IntegerLit(5))), UnExpr(-, UnExpr(-, Id(i))), BlockStmt([VarDecl(arr, ArrayType([31, 0], StringType)), AssignStmt(ArrayCell(arr, [ArrayCell(idx, [Id(i)])]), BinExpr(::, ArrayCell(arr, [ArrayCell(idx, [Id(i)])]), StringLit(jdk)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expected, 375))
    
    def test376(self):
        input = """JER: function void(X: integer) {
                {}
                emotion = "haizz"::"hihi" + "huhu";
                }"""
        expected = """Program([
	FuncDecl(JER, VoidType, [Param(X, IntegerType)], None, BlockStmt([BlockStmt([]), AssignStmt(Id(emotion), BinExpr(::, StringLit(haizz), BinExpr(+, StringLit(hihi), StringLit(huhu))))]))
])"""
        self.assertTrue(TestAST.test(input, expected, 376))
    
    def test377(self):
        input = """F: function auto() {
                dict[pair[1]+pair[0]] = 7.e-9/3;
                return dict[2.];
                }"""
        expected = """Program([
	FuncDecl(F, AutoType, [], None, BlockStmt([AssignStmt(ArrayCell(dict, [BinExpr(+, ArrayCell(pair, [IntegerLit(1)]), ArrayCell(pair, [IntegerLit(0)]))]), BinExpr(/, FloatLit(7e-09), IntegerLit(3))), ReturnStmt(ArrayCell(dict, [FloatLit(2.0)]))]))
])"""
        self.assertTrue(TestAST.test(input, expected, 377))
    
    def test378(self):
        input = """lexer: function void() {
                parser, x: integer = getAge(), getName();
                age = getAge();
                return age;
                }"""
        expected = """Program([
	FuncDecl(lexer, VoidType, [], None, BlockStmt([VarDecl(parser, IntegerType, FuncCall(getAge, [])), VarDecl(x, IntegerType, FuncCall(getName, [])), AssignStmt(Id(age), FuncCall(getAge, [])), ReturnStmt(Id(age))]))
])"""
        self.assertTrue(TestAST.test(input, expected, 378))
    
    def test379(self):
        input = """main: function void(arr: array[1,2] of string) {
                if (str::str) if (7 - 4 ==-3) return; else break;
                }"""
        expected = """Program([
	FuncDecl(main, VoidType, [Param(arr, ArrayType([1, 2], StringType))], None, BlockStmt([IfStmt(BinExpr(::, Id(str), Id(str)), IfStmt(BinExpr(==, BinExpr(-, IntegerLit(7), IntegerLit(4)), UnExpr(-, IntegerLit(3))), ReturnStmt(), BreakStmt()))]))
])"""
        self.assertTrue(TestAST.test(input, expected, 379))
    
    def test380(self):
        input = """main: function void(x: boolean) {
                if (true || ""::{"" + str}) continue;
                }"""
        expected = """Program([
	FuncDecl(main, VoidType, [Param(x, BooleanType)], None, BlockStmt([IfStmt(BinExpr(::, BinExpr(||, BooleanLit(True), StringLit()), ArrayLit([BinExpr(+, StringLit(), Id(str))])), ContinueStmt())]))
])"""
        self.assertTrue(TestAST.test(input, expected, 380))
    
    def test381(self):
        input = """nestedIf: function boolean(bool: boolean) {
                if (true) 
                    if (10 == 4 + 5) UwU = U::U;
                    else print(UwU);
                else {}
                }"""
        expected = """Program([
	FuncDecl(nestedIf, BooleanType, [Param(bool, BooleanType)], None, BlockStmt([IfStmt(BooleanLit(True), IfStmt(BinExpr(==, IntegerLit(10), BinExpr(+, IntegerLit(4), IntegerLit(5))), AssignStmt(Id(UwU), BinExpr(::, Id(U), Id(U))), CallStmt(print, Id(UwU))), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expected, 381))
    
    def test382(self):
        input = """fact: function integer(n: integer) {
                for (idx[id[1_4]] = 2 % 2, true, --i)
                    return n * fact(n-1);
                }"""
        expected = """Program([
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([ForStmt(AssignStmt(ArrayCell(idx, [ArrayCell(id, [IntegerLit(14)])]), BinExpr(%, IntegerLit(2), IntegerLit(2))), BooleanLit(True), UnExpr(-, UnExpr(-, Id(i))), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
])"""
        self.assertTrue(TestAST.test(input, expected, 382))
    
    def test383(self):
        input = """main: function void() {
                for (id = 7., 0.3, --1)
                    for (min = 0, min && 9 > 2, false)
                        break;
                }"""
        expected = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(id), FloatLit(7.0)), FloatLit(0.3), UnExpr(-, UnExpr(-, IntegerLit(1))), ForStmt(AssignStmt(Id(min), IntegerLit(0)), BinExpr(>, BinExpr(&&, Id(min), IntegerLit(9)), IntegerLit(2)), BooleanLit(False), BreakStmt()))]))
])"""
        self.assertTrue(TestAST.test(input, expected, 383))
    
    def test384(self):
        input = """main: function void(args: array[2] of string) {
                if ("jerry"::{"n","tom"})
                    for (i = 0, i < length, i + 1)
                        print(letter[i]);
                }"""
        expected = """Program([
	FuncDecl(main, VoidType, [Param(args, ArrayType([2], StringType))], None, BlockStmt([IfStmt(BinExpr(::, StringLit(jerry), ArrayLit([StringLit(n), StringLit(tom)])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(length)), BinExpr(+, Id(i), IntegerLit(1)), CallStmt(print, ArrayCell(letter, [Id(i)]))))]))
])"""
        self.assertTrue(TestAST.test(input, expected, 384))
    
    def test385(self):
        input = """VANVY: function auto() {
                while(id[x]::str == 7)
                    return id[x];
                }"""
        expect = """Program([
	FuncDecl(VANVY, AutoType, [], None, BlockStmt([WhileStmt(BinExpr(::, ArrayCell(id, [Id(x)]), BinExpr(==, Id(str), IntegerLit(7))), ReturnStmt(ArrayCell(id, [Id(x)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 385))
    
    def test386(self):
        input = """main: function void() {
                while(x+1) {}
                }"""
        expected = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(+, Id(x), IntegerLit(1)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expected, 386))
    
    def test387(self):
        input = """nestedLoop: function array[2,3] of string(n: integer) {
                while(y%3 == 0) {
                    for (i = 3, i < 1_2, i) {
                        while(true) n = false;
                    }
                }
                }"""
        expected = """Program([
	FuncDecl(nestedLoop, ArrayType([2, 3], StringType), [Param(n, IntegerType)], None, BlockStmt([WhileStmt(BinExpr(==, BinExpr(%, Id(y), IntegerLit(3)), IntegerLit(0)), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(3)), BinExpr(<, Id(i), IntegerLit(12)), Id(i), BlockStmt([WhileStmt(BooleanLit(True), AssignStmt(Id(n), BooleanLit(False)))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expected, 387))
        
    def test388(self):
        input = """UwU: function string(s: float) {
                i: integer = 0;
                do {
                    i = i + 1;
                    print(i);
                } while(--i < s);
                }"""
        expected = """Program([
	FuncDecl(UwU, StringType, [Param(s, FloatType)], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), DoWhileStmt(BinExpr(<, UnExpr(-, UnExpr(-, Id(i))), Id(s)), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))), CallStmt(print, Id(i))]))]))
])"""
        self.assertTrue(TestAST.test(input, expected, 388))
    
    def test389(self):
        input = """control: function void() inherit Mixi{
                break;
                continue;
                return;
                }"""
        expected = """Program([
	FuncDecl(control, VoidType, [], Mixi, BlockStmt([BreakStmt(), ContinueStmt(), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expected, 389))
    
    def test390(self):
        input = """sum: integer = 0;
                avg: float = 0.0;
                grade: array[1] of integer = {8.e3, 9, 0, -6};
                """
        expected = """Program([
	VarDecl(sum, IntegerType, IntegerLit(0))
	VarDecl(avg, FloatType, FloatLit(0.0))
	VarDecl(grade, ArrayType([1], IntegerType), ArrayLit([FloatLit(8000.0), IntegerLit(9), IntegerLit(0), UnExpr(-, IntegerLit(6))]))
])"""
        self.assertTrue(TestAST.test(input, expected, 390))
    
    def test391(self):
        input = """ x, y: integer = 10, 25;
                    sum: function integer(x: integer, y: integer){
                            z: integer = x+y;
                            print ("sum of x+y =", z);
                            return z;
                        }"""
        expected = """Program([
	VarDecl(x, IntegerType, IntegerLit(10))
	VarDecl(y, IntegerType, IntegerLit(25))
	FuncDecl(sum, IntegerType, [Param(x, IntegerType), Param(y, IntegerType)], None, BlockStmt([VarDecl(z, IntegerType, BinExpr(+, Id(x), Id(y))), CallStmt(print, StringLit(sum of x+y =), Id(z)), ReturnStmt(Id(z))]))
])"""
        
        self.assertTrue(TestAST.test(input, expected, 391))
    
    def test392(self):
        input = """ sendFile: function void(file: string, path: string) {
                sendFile(path::("//"::file));
                return path::("//"::file);
                } """
        expected = """Program([
	FuncDecl(sendFile, VoidType, [Param(file, StringType), Param(path, StringType)], None, BlockStmt([CallStmt(sendFile, BinExpr(::, Id(path), BinExpr(::, StringLit(//), Id(file)))), ReturnStmt(BinExpr(::, Id(path), BinExpr(::, StringLit(//), Id(file))))]))
])"""
        self.assertTrue(TestAST.test(input, expected, 392))
    
    def test393(self):
        input = """ main: function void() {
                        if (a == b) {
                            
                        }
                        else {
                            if (10 == 5) {}
                        }
                    } """
        expected = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), Id(b)), BlockStmt([]), BlockStmt([IfStmt(BinExpr(==, IntegerLit(10), IntegerLit(5)), BlockStmt([]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expected, 393))
    
    def test394(self):
        input = """func: function void() {
                while(true + false / bool) {
                    x: boolean;
                }
                }"""
        expected = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(+, BooleanLit(True), BinExpr(/, BooleanLit(False), Id(bool))), BlockStmt([VarDecl(x, BooleanType)]))]))
])"""
        self.assertTrue(TestAST.test(input, expected, 394))
    
    def test395(self):
        input = """aizza: function boolean(bool: boolean) {
                do {
                    getGirlFr("jenny"::firstName+" \\n");
                } while (false % true);
                }"""       
        expected = """Program([
	FuncDecl(aizza, BooleanType, [Param(bool, BooleanType)], None, BlockStmt([DoWhileStmt(BinExpr(%, BooleanLit(False), BooleanLit(True)), BlockStmt([CallStmt(getGirlFr, BinExpr(::, StringLit(jenny), BinExpr(+, Id(firstName), StringLit( \\n))))]))]))
])"""
        self.assertTrue(TestAST.test(input, expected, 395))
    
    def test396(self):
        input = """fact: function integer (n: integer) {
            while ((n || 4) && (n == 3)) {
                    delta: integer = fact(3);
                    inc(x, delta, alpha);
                    do {printHello();}
                    while (1 + 4 == 2);
                }
            }"""
        expected = """Program([
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([WhileStmt(BinExpr(&&, BinExpr(||, Id(n), IntegerLit(4)), BinExpr(==, Id(n), IntegerLit(3))), BlockStmt([VarDecl(delta, IntegerType, FuncCall(fact, [IntegerLit(3)])), CallStmt(inc, Id(x), Id(delta), Id(alpha)), DoWhileStmt(BinExpr(==, BinExpr(+, IntegerLit(1), IntegerLit(4)), IntegerLit(2)), BlockStmt([CallStmt(printHello, )]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expected, 396))
    
    def test397(self):
        input = """fact: function integer (n: integer) {
            {
                /* x: string; */
                func: integer = /*0*/123;
            }
            }"""
        expected = """Program([
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([BlockStmt([VarDecl(func, IntegerType, IntegerLit(123))])]))
])"""
        self.assertTrue(TestAST.test(input, expected, 397))
    
    def test398(self):
        input = """
        main: function void (x: integer, a_123: string) {
            if (1 < (2 < 3)) 
            {
                return 1;
            }
        }
        """
        expected = """Program([
	FuncDecl(main, VoidType, [Param(x, IntegerType), Param(a_123, StringType)], None, BlockStmt([IfStmt(BinExpr(<, IntegerLit(1), BinExpr(<, IntegerLit(2), IntegerLit(3))), BlockStmt([ReturnStmt(IntegerLit(1))]))]))
])"""
        self.assertTrue(TestAST.test(input, expected, 398))
    
    def test399(self):
        input = """fact: function integer (n: integer) {
            if (n == 0) return 1;
            // else return 1.3e-4 * fact(n - 1);
            else return;
        }"""
        expected = """Program([
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt())]))
])"""
        self.assertTrue(TestAST.test(input, expected, 399))
    
    def test400(self):
        input = """fact: function integer (n: integer) {
            while (true) {
                    delta: integer = fact(3);
                    inc(x, delta, alpha);
                    do {printHello();}
                    while (1 + 4 == 2);
                }
            }"""
        expected = """Program([
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([WhileStmt(BooleanLit(True), BlockStmt([VarDecl(delta, IntegerType, FuncCall(fact, [IntegerLit(3)])), CallStmt(inc, Id(x), Id(delta), Id(alpha)), DoWhileStmt(BinExpr(==, BinExpr(+, IntegerLit(1), IntegerLit(4)), IntegerLit(2)), BlockStmt([CallStmt(printHello, )]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expected, 400))

