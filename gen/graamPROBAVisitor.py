# Generated from C:/Users/martyna/PycharmProjects/teoriaKompilatorow/Emojii-Programming/Grammars/graamPROBA.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .graamPROBAParser import graamPROBAParser
else:
    from graamPROBAParser import graamPROBAParser

# This class defines a complete generic visitor for a parse tree produced by graamPROBAParser.

class graamPROBAVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by graamPROBAParser#start.
    def visitStart(self, ctx:graamPROBAParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by graamPROBAParser#stmt.
    def visitStmt(self, ctx:graamPROBAParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by graamPROBAParser#simple_stmt.
    def visitSimple_stmt(self, ctx:graamPROBAParser.Simple_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by graamPROBAParser#assignment_stmt.
    def visitAssignment_stmt(self, ctx:graamPROBAParser.Assignment_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by graamPROBAParser#declare_stmt.
    def visitDeclare_stmt(self, ctx:graamPROBAParser.Declare_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by graamPROBAParser#single_declaration.
    def visitSingle_declaration(self, ctx:graamPROBAParser.Single_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by graamPROBAParser#import_stmt.
    def visitImport_stmt(self, ctx:graamPROBAParser.Import_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by graamPROBAParser#from_stmt.
    def visitFrom_stmt(self, ctx:graamPROBAParser.From_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by graamPROBAParser#module_name.
    def visitModule_name(self, ctx:graamPROBAParser.Module_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by graamPROBAParser#import_list.
    def visitImport_list(self, ctx:graamPROBAParser.Import_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by graamPROBAParser#import_name.
    def visitImport_name(self, ctx:graamPROBAParser.Import_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by graamPROBAParser#try_stmt.
    def visitTry_stmt(self, ctx:graamPROBAParser.Try_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by graamPROBAParser#except_clause.
    def visitExcept_clause(self, ctx:graamPROBAParser.Except_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by graamPROBAParser#print_stmt.
    def visitPrint_stmt(self, ctx:graamPROBAParser.Print_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by graamPROBAParser#multiple_assignment_stmt.
    def visitMultiple_assignment_stmt(self, ctx:graamPROBAParser.Multiple_assignment_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by graamPROBAParser#raise_stmt.
    def visitRaise_stmt(self, ctx:graamPROBAParser.Raise_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by graamPROBAParser#exception_expr.
    def visitException_expr(self, ctx:graamPROBAParser.Exception_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by graamPROBAParser#exception_name.
    def visitException_name(self, ctx:graamPROBAParser.Exception_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by graamPROBAParser#compound_stmt.
    def visitCompound_stmt(self, ctx:graamPROBAParser.Compound_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by graamPROBAParser#if_stmt.
    def visitIf_stmt(self, ctx:graamPROBAParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by graamPROBAParser#while_stmt.
    def visitWhile_stmt(self, ctx:graamPROBAParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by graamPROBAParser#for_stmt.
    def visitFor_stmt(self, ctx:graamPROBAParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by graamPROBAParser#function_def.
    def visitFunction_def(self, ctx:graamPROBAParser.Function_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by graamPROBAParser#parameters.
    def visitParameters(self, ctx:graamPROBAParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by graamPROBAParser#typed_par.
    def visitTyped_par(self, ctx:graamPROBAParser.Typed_parContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by graamPROBAParser#loop_stmt.
    def visitLoop_stmt(self, ctx:graamPROBAParser.Loop_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by graamPROBAParser#func_body.
    def visitFunc_body(self, ctx:graamPROBAParser.Func_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by graamPROBAParser#flow_stmt.
    def visitFlow_stmt(self, ctx:graamPROBAParser.Flow_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by graamPROBAParser#return_stmt.
    def visitReturn_stmt(self, ctx:graamPROBAParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by graamPROBAParser#explist.
    def visitExplist(self, ctx:graamPROBAParser.ExplistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by graamPROBAParser#exp.
    def visitExp(self, ctx:graamPROBAParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by graamPROBAParser#arithmeticOperation.
    def visitArithmeticOperation(self, ctx:graamPROBAParser.ArithmeticOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by graamPROBAParser#term.
    def visitTerm(self, ctx:graamPROBAParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by graamPROBAParser#factor.
    def visitFactor(self, ctx:graamPROBAParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by graamPROBAParser#printOperation.
    def visitPrintOperation(self, ctx:graamPROBAParser.PrintOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by graamPROBAParser#conditionalOperation.
    def visitConditionalOperation(self, ctx:graamPROBAParser.ConditionalOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by graamPROBAParser#logicalTerm.
    def visitLogicalTerm(self, ctx:graamPROBAParser.LogicalTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by graamPROBAParser#logicalFactor.
    def visitLogicalFactor(self, ctx:graamPROBAParser.LogicalFactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by graamPROBAParser#logicalPrimary.
    def visitLogicalPrimary(self, ctx:graamPROBAParser.LogicalPrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by graamPROBAParser#value.
    def visitValue(self, ctx:graamPROBAParser.ValueContext):
        return self.visitChildren(ctx)



del graamPROBAParser