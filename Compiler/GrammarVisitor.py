# Generated from C:/Users/martyna/PycharmProjects/teoriaKompilatorow/Emojii-Programming/Grammars/Grammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete generic visitor for a parse tree produced by GrammarParser.

class GrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GrammarParser#start.
    def visitStart(self, ctx:GrammarParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#stmt.
    def visitStmt(self, ctx:GrammarParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#simple_stmt.
    def visitSimple_stmt(self, ctx:GrammarParser.Simple_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#assignment_stmt.
    def visitAssignment_stmt(self, ctx:GrammarParser.Assignment_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#declare_stmt.
    def visitDeclare_stmt(self, ctx:GrammarParser.Declare_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#single_declaration.
    def visitSingle_declaration(self, ctx:GrammarParser.Single_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#import_stmt.
    def visitImport_stmt(self, ctx:GrammarParser.Import_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#from_stmt.
    def visitFrom_stmt(self, ctx:GrammarParser.From_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#module_name.
    def visitModule_name(self, ctx:GrammarParser.Module_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#import_list.
    def visitImport_list(self, ctx:GrammarParser.Import_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#import_name.
    def visitImport_name(self, ctx:GrammarParser.Import_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#try_stmt.
    def visitTry_stmt(self, ctx:GrammarParser.Try_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#except_clause.
    def visitExcept_clause(self, ctx:GrammarParser.Except_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#print_stmt.
    def visitPrint_stmt(self, ctx:GrammarParser.Print_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#multiple_assignment_stmt.
    def visitMultiple_assignment_stmt(self, ctx:GrammarParser.Multiple_assignment_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#raise_stmt.
    def visitRaise_stmt(self, ctx:GrammarParser.Raise_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#exception_expr.
    def visitException_expr(self, ctx:GrammarParser.Exception_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#exception_name.
    def visitException_name(self, ctx:GrammarParser.Exception_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#compound_stmt.
    def visitCompound_stmt(self, ctx:GrammarParser.Compound_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#if_stmt.
    def visitIf_stmt(self, ctx:GrammarParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#elif_stmt.
    def visitElif_stmt(self, ctx:GrammarParser.Elif_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#else_stmt.
    def visitElse_stmt(self, ctx:GrammarParser.Else_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#while_stmt.
    def visitWhile_stmt(self, ctx:GrammarParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#for_stmt.
    def visitFor_stmt(self, ctx:GrammarParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#function_def.
    def visitFunction_def(self, ctx:GrammarParser.Function_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#parameters.
    def visitParameters(self, ctx:GrammarParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#typed_par.
    def visitTyped_par(self, ctx:GrammarParser.Typed_parContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#function_call.
    def visitFunction_call(self, ctx:GrammarParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#exp_list.
    def visitExp_list(self, ctx:GrammarParser.Exp_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#loop_stmt.
    def visitLoop_stmt(self, ctx:GrammarParser.Loop_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#func_body.
    def visitFunc_body(self, ctx:GrammarParser.Func_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#flow_stmt.
    def visitFlow_stmt(self, ctx:GrammarParser.Flow_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#return_stmt.
    def visitReturn_stmt(self, ctx:GrammarParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#explist.
    def visitExplist(self, ctx:GrammarParser.ExplistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#exp.
    def visitExp(self, ctx:GrammarParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#arithmeticOperation.
    def visitArithmeticOperation(self, ctx:GrammarParser.ArithmeticOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#term.
    def visitTerm(self, ctx:GrammarParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#factor.
    def visitFactor(self, ctx:GrammarParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#printOperation.
    def visitPrintOperation(self, ctx:GrammarParser.PrintOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#conditionalOperation.
    def visitConditionalOperation(self, ctx:GrammarParser.ConditionalOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#logicalTerm.
    def visitLogicalTerm(self, ctx:GrammarParser.LogicalTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#logicalFactor.
    def visitLogicalFactor(self, ctx:GrammarParser.LogicalFactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#logicalPrimary.
    def visitLogicalPrimary(self, ctx:GrammarParser.LogicalPrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#value.
    def visitValue(self, ctx:GrammarParser.ValueContext):
        return self.visitChildren(ctx)



del GrammarParser