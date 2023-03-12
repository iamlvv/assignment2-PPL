from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *


class ASTGeneration(MT22Visitor):
    #program: decclist EOF;
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        result = []
        for decllist in ctx.decllist():
            result.append(self.visit(decllist))
        return Program(result)
    
    #decllist: declaration decllist | declaration;
    def visitDecllist(self, ctx: MT22Parser.DecllistContext):
        if ctx.getChildCount() == 0: return []
        elif ctx.declaration(): return [self.visit(ctx.declaration())]
        return [self.visit(ctx.declaration()) + self.visit(ctx.decllist())]
    
    #declaration: vardec | funcdec;
    def visitDeclaration(self, ctx: MT22Parser.DeclarationContext):
        if ctx.vardec(): return self.visit(ctx.vardec())
        elif ctx.funcdec(): return self.visit(ctx.funcdec())
    
    #typ: AUTO | atomictype | arraytype;
    def visitTyp(self, ctx: MT22Parser.TypContext):
        if ctx.AUTO(): return AutoType()
        elif ctx.atomictype(): return self.visit(ctx.atomictype())
        elif ctx.arraytype(): return self.visit(ctx.arraytype())
    
    #vardec: ((idlist COLON typ) | subvardec) SEMICOLON;
    def visitVardec(self, ctx: MT22Parser.VardecContext):
        if ctx.idlist(): return VarDecl(Id(ctx.idlist().getText()), self.visit(ctx.typ()))
        elif ctx.subvardec(): return self.visit(ctx.subvardec())
    
    #subvardec: IDENTIFIER COMMA subvardec COMMA expr | expand;
    def visitSubvardec(self, ctx: MT22Parser.SubvardecContext):
        if ctx.getChildCount() == 5:
            return self.visit(ctx.subvardec()) + self.visit(ctx.expr())
        return self.visit(ctx.expand())
    
    #expand: IDENTIFIER COLON typ ASSIGNOP expr;
    def visitExpand(self, ctx: MT22Parser.ExpandContext):
        return self.visit(ctx.typ()) + self.visit(ctx.expr())

    #idlist: IDENTIFIER COMMA idlist | IDENTIFIER;
    def visitIdlist(self, ctx: MT22Parser.IdlistContext):
        if ctx.getChildCount() == 1: return Id(ctx.IDENTIFIER().getText())
        return Id(ctx.IDENTIFIER().getText()) + self.visit(ctx.idlist())
    
    #exprlist: expr COMMA exprlist | expr |;
    def visitExprlist(self, ctx: MT22Parser.ExprlistContext):
        if ctx.getChildCount() == 0: return []
        elif ctx.getChildCount() == 1: return [self.visit(ctx.expr())]
        return [self.visit(ctx.expr())] + self.visit(ctx.exprlist())
    
    #funcdec: IDENTIFIER COLON FUNCTION (typ | VOID) LP parameterlist RP (INHERIT IDENTIFIER)? (blockstate | emptycurl);
    def visitFuncdec(self, ctx: MT22Parser.FuncdecContext):
        if ctx.typ(): return FuncDecl(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.typ()), self.visit(ctx.parameterlist()), self.visit(ctx.IDENTIFIER()), self.visit(ctx.blockstate()))
        elif ctx.VOID(): return FuncDecl(Id(ctx.IDENTIFIER().getText()), VoidType(), self.visit(ctx.parameterlist()), self.visit(ctx.IDENTIFIER()), self.visit(ctx.blockstate()))
        
    #emptycurl: LC RC;
    def visitEmptycurl(self, ctx: MT22Parser.EmptycurlContext):
        return []
    
    #parameter: (INHERIT)? (OUT)? IDENTIFIER COLON typ;
    def visitParameter(self, ctx: MT22Parser.ParameterContext):
        if ctx.INHERIT():
            if ctx.OUT():
                return [ParamDecl(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.typ()), True, True)]
            else: return [ParamDecl(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.typ()), True, False)]
        else:
            if ctx.OUT():
                return [ParamDecl(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.typ()), False, True)]
            else: return [ParamDecl(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.typ()), False, False)]
    
    #parameterlist: parameter COMMA parameterlist | parameter |;
    def visitParameterlist(self, ctx: MT22Parser.ParameterlistContext):
        if ctx.getChildCount() == 0: return []
        elif ctx.getChildCount() == 1: return self.visit(ctx.parameter())
        return self.visit(ctx.parameter()) + self.visit(ctx.parameterlist())
    
    #blockstate: LC blockstatemin RC;
    def visitBlockstate(self, ctx: MT22Parser.BlockstateContext):
        return self.visit(ctx.blockstatemin())
    
    #blockstatemin: (statement | vardec) blockstatemin |;
    def visitBlockstatemin(self, ctx: MT22Parser.BlockstateminContext):
        if ctx.getChildCount() == 0: return []
        elif ctx.vardec(): return [self.visit(ctx.vardec())] + self.visit(ctx.blockstatemin())
        elif ctx.statement(): return [self.visit(ctx.statement())] + self.visit(ctx.blockstatemin())
        
    #statement: ifstate | forstate | dowhilestate | whilestate | breakstate | continuestate | returnstate | funcall | assignstate | blockstate;
    def visitStatement(self, ctx: MT22Parser.StatementContext):
        if ctx.ifstate(): return self.visit(ctx.ifstate())
        elif ctx.forstate(): return self.visit(ctx.forstate())
        elif ctx.dowhilestate(): return self.visit(ctx.dowhilestate())
        elif ctx.whilestate(): return self.visit(ctx.whilestate())
        elif ctx.breakstate(): return self.visit(ctx.breakstate())
        elif ctx.continuestate(): return self.visit(ctx.continuestate())
        elif ctx.returnstate(): return self.visit(ctx.returnstate())
        elif ctx.funcall(): return self.visit(ctx.funcall())
        elif ctx.assignstate(): return self.visit(ctx.assignstate())
        elif ctx.blockstate(): return self.visit(ctx.blockstate())
        
    #lhs: scalarvar | exprindex;
    def visitLhs(self, ctx: MT22Parser.LhsContext):
        if ctx.scalarvar(): return self.visit(ctx.scalarvar())
        elif ctx.exprindex(): return self.visit(ctx.exprindex())
    
    #scalarvar: IDENTIFIER;
    def visitScalar(self, ctx: MT22Parser.ScalarContext):
        return Id(ctx.IDENTIFIER().getText())
    
    #assignstate: lhs ASSIGNOP expr SEMICOLON;
    def visitAssignstate(self, ctx: MT22Parser.AssignstateContext):
        return AssignStmt(self.visit(ctx.lhs()), self.visit(ctx.expr()))
    
    #ifstate: IF LP expr RP statement (ELSE statement)?;
    def visitIfstate(self, ctx: MT22Parser.IfstateContext):
        if ctx.statement(1):
            return IfStmt(self.visit(ctx.expr()), self.visit(ctx.statement(0)), self.visit(ctx.statement(1)))
        else: return IfStmt(self.visit(ctx.expr()), self.visit(ctx.statement(0)), [])
    
    #forstate: FOR LP lhs ASSIGNOP expr COMMA expr COMMA expr RP statement;
    def visitForstate(self, ctx: MT22Parser.ForstateContext):
        return ForStmt(self.visit(ctx.lhs()), self.visit(ctx.expr(0)), self.visit(ctx.expr(1)), self.visit(ctx.expr(2)), self.visit(ctx.statement()))
    
    #whilestate: WHILE LP expr RP statement;
    def visitWhilestate(self, ctx: MT22Parser.WhilestateContext):
        return WhileStmt(self.visit(ctx.expr()), self.visit(ctx.statement()))
    
    #dowhilestate: DO blockstate WHILE LP expr RP SEMICOLON;
    def visitDowhilestate(self, ctx: MT22Parser.DowhilestateContext):
        return DowhileStmt(self.visit(ctx.expr()), self.visit(ctx.blockstate()))
    
    #breakstate: BREAK SEMICOLON;
    def visitBreakState(self, ctx: MT22Parser.BreakStateContext):
        return BreakStmt()
    
    #continuestate: CONTINUE SEMICOLON;
    def visitContinueState(self, ctx: MT22Parser.ContinueStateContext):
        return ContinueStmt()
    
    #returnstate: RETURN expr? SEMICOLON;
    def visitReturnState(self, ctx: MT22Parser.ReturnStateContext):
        if ctx.expr(): return ReturnStmt(self.visit(ctx.expr()))
        else: return ReturnStmt(None)
        
    #funcall: IDENTIFIER LP exprlist RP SEMICOLON;
    def visitFunctioncall(self, ctx: MT22Parser.FunctioncallContext):
        return CallStmt(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.exprlist()))
    
    #arraytype: ARRAY LS dimensions RS OF atomictype;
    def visitArraytype(self, ctx: MT22Parser.ArraytypeContext):
        return ArrayType(self.visit(ctx.dimensions()), self.visit(ctx.atomictype()))
    
    #dimensions: INTLIT COMMA dimensions | INTLIT;
    def visitDimensions(self, ctx: MT22Parser.DimensionsContext):
        if ctx.getChildCount() == 1: return [int(ctx.INTLIT().getText())]
        return [int(ctx.INTLIT().getText())] + self.visit(ctx.dimensions())
    
    #atomictype: INTEGER | BOOLEAN | FLOAT | STRING;
    def visitAtomictype(self, ctx: MT22Parser.AtomictypeContext):
        if ctx.INTEGER(): return IntType()
        elif ctx.BOOLEAN(): return BooleanType()
        elif ctx.FLOAT(): return FloatType()
        elif ctx.STRING(): return StringType()
    
    #literal: INTLIT | BOOLLIT | STRINGLIT | FLOATLIT | arraylit;
    def visitLiterals(self, ctx: MT22Parser.LiteralsContext):
        if ctx.INTLIT(): return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.BOOLLIT(): return BooleanLiteral(ctx.BOOLLIT().getText() == "true")
        elif ctx.STRINGLIT(): return StringLiteral(ctx.STRINGLIT().getText())
        elif ctx.FLOATLIT(): return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.arraylit(): return self.visit(ctx.arraylit())
    
    #arraylit: '{' (exprlist | emptycurl) '}';
    def visitArraylit(self, ctx: MT22Parser.ArraylitContext):
        if ctx.exprlist(): return ArrayLit(self.visit(ctx.exprlist()))
        else: return ArrayLit([])
        
    #expr: expr1 (STRINGOP) expr1 | expr1;
    def visitExpr(self, ctx: MT22Parser.ExprContext):
        if ctx.getChildCount() == 1: return self.visit(ctx.expr1(0))
        return BinExp(ctx.STRINGOP().getText(), self.visit(ctx.expr1(0)), self.visit(ctx.expr1(1)))
    
    #expr1: expr2 (GTOP | LTOP | GTEOP | LTEOP | EQOP | NEOP) expr2 | expr2;
    def visitExpr1(self, ctx: MT22Parser.Expr1Context):
        if ctx.getChildCount() == 1: return self.visit(ctx.expr2(0))
        return BinExp(ctx.getChild(1).getText(), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))
    
    #expr2: expr2 (ANDOP | OROP) expr3 | expr3;
    def visitExpr2(self, ctx: MT22Parser.Expr2Context):
        if ctx.getChildCount() == 1: return self.visit(ctx.expr3(0))
        return BinExp(ctx.getChild(1).getText(), self.visit(ctx.expr2(0)), self.visit(ctx.expr3(1)))
    
    #expr3: expr3 (ADDOP | SUBOP) expr4 | expr4;
    def visitExpr3(self, ctx: MT22Parser.Expr3Context):
        if ctx.getChildCount() == 1: return self.visit(ctx.expr4(0))
        return BinExp(ctx.getChild(1).getText(), self.visit(ctx.expr3(0)), self.visit(ctx.expr4(1)))
    
    #expr4: expr4 (MULOP | DIVOP | MODOP) expr5 | expr5;
    def visitExpr4(self, ctx: MT22Parser.Expr4Context):
        if ctx.getChildCount() == 1: return self.visit(ctx.expr5(0))
        return BinExp(ctx.getChild(1).getText(), self.visit(ctx.expr4(0)), self.visit(ctx.expr5(1)))
    
    #expr5: (NOTOP) expr5 | expr6;
    def visitExpr5(self, ctx: MT22Parser.Expr5Context):
        if ctx.getChildCount() == 1: return self.visit(ctx.expr6())
        return UnExp(ctx.NOTOP().getText(), self.visit(ctx.expr5()))
    
    #expr6: (SUBOP) expr6 | expr7;
    def visitExpr6(self, ctx: MT22Parser.Expr6Context):
        if ctx.getChildCount() == 1: return self.visit(ctx.expr7())
        return UnExp(ctx.SUBOP().getText(), self.visit(ctx.expr6()))
    
    #expr7: NTLIT | FLOATLIT | BOOLLIT | STRINGLIT | IDENTIFIER | exprindex | (IDENTIFIER LP exprlist RP) | (LP expr RP) | arraylit;
    def visitExpr7(self, ctx: MT22Parser.Expr7Context):
        if ctx.NTLIT(): return IntLiteral(int(ctx.NTLIT().getText()))
        elif ctx.FLOATLIT(): return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.BOOLLIT(): return BooleanLiteral(ctx.BOOLLIT().getText() == "true")
        elif ctx.STRINGLIT(): return StringLiteral(ctx.STRINGLIT().getText())
        elif ctx.IDENTIFIER(): return Id(ctx.IDENTIFIER().getText())
        elif ctx.exprindex(): return self.visit(ctx.exprindex())
        elif ctx.getChildCount() == 4: return CallExpr(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.exprlist()))
        elif ctx.getChildCount() == 3: return self.visit(ctx.expr())
        elif ctx.arraylit(): return self.visit(ctx.arraylit())
        
    #exprindex: IDENTIFIER LS exprlist RS;
    def visitExprindex(self, ctx: MT22Parser.ExprindexContext):
        return ArrayCell(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.exprlist()))