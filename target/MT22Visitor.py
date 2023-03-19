# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decllist.
    def visitDecllist(self, ctx:MT22Parser.DecllistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#declaration.
    def visitDeclaration(self, ctx:MT22Parser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#typ.
    def visitTyp(self, ctx:MT22Parser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardec.
    def visitVardec(self, ctx:MT22Parser.VardecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#subvardec.
    def visitSubvardec(self, ctx:MT22Parser.SubvardecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expand.
    def visitExpand(self, ctx:MT22Parser.ExpandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#idlist.
    def visitIdlist(self, ctx:MT22Parser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exprlist.
    def visitExprlist(self, ctx:MT22Parser.ExprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#subexprlist.
    def visitSubexprlist(self, ctx:MT22Parser.SubexprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcdec.
    def visitFuncdec(self, ctx:MT22Parser.FuncdecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#emptycurl.
    def visitEmptycurl(self, ctx:MT22Parser.EmptycurlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#parameter.
    def visitParameter(self, ctx:MT22Parser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#parameterlist.
    def visitParameterlist(self, ctx:MT22Parser.ParameterlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#blockstate.
    def visitBlockstate(self, ctx:MT22Parser.BlockstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#blockstatemin.
    def visitBlockstatemin(self, ctx:MT22Parser.BlockstateminContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#statement.
    def visitStatement(self, ctx:MT22Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#lhs.
    def visitLhs(self, ctx:MT22Parser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#scalarvar.
    def visitScalarvar(self, ctx:MT22Parser.ScalarvarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assignstate.
    def visitAssignstate(self, ctx:MT22Parser.AssignstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#ifstate.
    def visitIfstate(self, ctx:MT22Parser.IfstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#whilestate.
    def visitWhilestate(self, ctx:MT22Parser.WhilestateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dowhilestate.
    def visitDowhilestate(self, ctx:MT22Parser.DowhilestateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#forstate.
    def visitForstate(self, ctx:MT22Parser.ForstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#breakstate.
    def visitBreakstate(self, ctx:MT22Parser.BreakstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#continuestate.
    def visitContinuestate(self, ctx:MT22Parser.ContinuestateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#returnstate.
    def visitReturnstate(self, ctx:MT22Parser.ReturnstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcall.
    def visitFuncall(self, ctx:MT22Parser.FuncallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arraytype.
    def visitArraytype(self, ctx:MT22Parser.ArraytypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dimensions.
    def visitDimensions(self, ctx:MT22Parser.DimensionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#atomictype.
    def visitAtomictype(self, ctx:MT22Parser.AtomictypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#literal.
    def visitLiteral(self, ctx:MT22Parser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr.
    def visitExpr(self, ctx:MT22Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr1.
    def visitExpr1(self, ctx:MT22Parser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr2.
    def visitExpr2(self, ctx:MT22Parser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr3.
    def visitExpr3(self, ctx:MT22Parser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr4.
    def visitExpr4(self, ctx:MT22Parser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr5.
    def visitExpr5(self, ctx:MT22Parser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr6.
    def visitExpr6(self, ctx:MT22Parser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr7.
    def visitExpr7(self, ctx:MT22Parser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exprindex.
    def visitExprindex(self, ctx:MT22Parser.ExprindexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arraylit.
    def visitArraylit(self, ctx:MT22Parser.ArraylitContext):
        return self.visitChildren(ctx)



del MT22Parser