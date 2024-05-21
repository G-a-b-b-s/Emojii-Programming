# Generated from C:/Users/martyna/PycharmProjects/teoriaKompilatorow/Emojii-Programming/Grammars/Grammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete listener for a parse tree produced by GrammarParser.
class GrammarListener(ParseTreeListener):

    # Enter a parse tree produced by GrammarParser#start.
    def enterStart(self, ctx:GrammarParser.StartContext):
        pass

    # Exit a parse tree produced by GrammarParser#start.
    def exitStart(self, ctx:GrammarParser.StartContext):
        pass


    # Enter a parse tree produced by GrammarParser#stmt.
    def enterStmt(self, ctx:GrammarParser.StmtContext):
        pass

    # Exit a parse tree produced by GrammarParser#stmt.
    def exitStmt(self, ctx:GrammarParser.StmtContext):
        pass


    # Enter a parse tree produced by GrammarParser#simple_stmt.
    def enterSimple_stmt(self, ctx:GrammarParser.Simple_stmtContext):
        pass

    # Exit a parse tree produced by GrammarParser#simple_stmt.
    def exitSimple_stmt(self, ctx:GrammarParser.Simple_stmtContext):
        pass


    # Enter a parse tree produced by GrammarParser#assignment_stmt.
    def enterAssignment_stmt(self, ctx:GrammarParser.Assignment_stmtContext):
        pass

    # Exit a parse tree produced by GrammarParser#assignment_stmt.
    def exitAssignment_stmt(self, ctx:GrammarParser.Assignment_stmtContext):
        pass


    # Enter a parse tree produced by GrammarParser#declare_stmt.
    def enterDeclare_stmt(self, ctx:GrammarParser.Declare_stmtContext):
        pass

    # Exit a parse tree produced by GrammarParser#declare_stmt.
    def exitDeclare_stmt(self, ctx:GrammarParser.Declare_stmtContext):
        pass


    # Enter a parse tree produced by GrammarParser#single_declaration.
    def enterSingle_declaration(self, ctx:GrammarParser.Single_declarationContext):
        pass

    # Exit a parse tree produced by GrammarParser#single_declaration.
    def exitSingle_declaration(self, ctx:GrammarParser.Single_declarationContext):
        pass


    # Enter a parse tree produced by GrammarParser#import_stmt.
    def enterImport_stmt(self, ctx:GrammarParser.Import_stmtContext):
        pass

    # Exit a parse tree produced by GrammarParser#import_stmt.
    def exitImport_stmt(self, ctx:GrammarParser.Import_stmtContext):
        pass


    # Enter a parse tree produced by GrammarParser#from_stmt.
    def enterFrom_stmt(self, ctx:GrammarParser.From_stmtContext):
        pass

    # Exit a parse tree produced by GrammarParser#from_stmt.
    def exitFrom_stmt(self, ctx:GrammarParser.From_stmtContext):
        pass


    # Enter a parse tree produced by GrammarParser#module_name.
    def enterModule_name(self, ctx:GrammarParser.Module_nameContext):
        pass

    # Exit a parse tree produced by GrammarParser#module_name.
    def exitModule_name(self, ctx:GrammarParser.Module_nameContext):
        pass


    # Enter a parse tree produced by GrammarParser#import_list.
    def enterImport_list(self, ctx:GrammarParser.Import_listContext):
        pass

    # Exit a parse tree produced by GrammarParser#import_list.
    def exitImport_list(self, ctx:GrammarParser.Import_listContext):
        pass


    # Enter a parse tree produced by GrammarParser#import_name.
    def enterImport_name(self, ctx:GrammarParser.Import_nameContext):
        pass

    # Exit a parse tree produced by GrammarParser#import_name.
    def exitImport_name(self, ctx:GrammarParser.Import_nameContext):
        pass


    # Enter a parse tree produced by GrammarParser#try_stmt.
    def enterTry_stmt(self, ctx:GrammarParser.Try_stmtContext):
        pass

    # Exit a parse tree produced by GrammarParser#try_stmt.
    def exitTry_stmt(self, ctx:GrammarParser.Try_stmtContext):
        pass


    # Enter a parse tree produced by GrammarParser#except_clause.
    def enterExcept_clause(self, ctx:GrammarParser.Except_clauseContext):
        pass

    # Exit a parse tree produced by GrammarParser#except_clause.
    def exitExcept_clause(self, ctx:GrammarParser.Except_clauseContext):
        pass


    # Enter a parse tree produced by GrammarParser#print_stmt.
    def enterPrint_stmt(self, ctx:GrammarParser.Print_stmtContext):
        pass

    # Exit a parse tree produced by GrammarParser#print_stmt.
    def exitPrint_stmt(self, ctx:GrammarParser.Print_stmtContext):
        pass


    # Enter a parse tree produced by GrammarParser#multiple_assignment_stmt.
    def enterMultiple_assignment_stmt(self, ctx:GrammarParser.Multiple_assignment_stmtContext):
        pass

    # Exit a parse tree produced by GrammarParser#multiple_assignment_stmt.
    def exitMultiple_assignment_stmt(self, ctx:GrammarParser.Multiple_assignment_stmtContext):
        pass


    # Enter a parse tree produced by GrammarParser#raise_stmt.
    def enterRaise_stmt(self, ctx:GrammarParser.Raise_stmtContext):
        pass

    # Exit a parse tree produced by GrammarParser#raise_stmt.
    def exitRaise_stmt(self, ctx:GrammarParser.Raise_stmtContext):
        pass


    # Enter a parse tree produced by GrammarParser#exception_expr.
    def enterException_expr(self, ctx:GrammarParser.Exception_exprContext):
        pass

    # Exit a parse tree produced by GrammarParser#exception_expr.
    def exitException_expr(self, ctx:GrammarParser.Exception_exprContext):
        pass


    # Enter a parse tree produced by GrammarParser#exception_name.
    def enterException_name(self, ctx:GrammarParser.Exception_nameContext):
        pass

    # Exit a parse tree produced by GrammarParser#exception_name.
    def exitException_name(self, ctx:GrammarParser.Exception_nameContext):
        pass


    # Enter a parse tree produced by GrammarParser#compound_stmt.
    def enterCompound_stmt(self, ctx:GrammarParser.Compound_stmtContext):
        pass

    # Exit a parse tree produced by GrammarParser#compound_stmt.
    def exitCompound_stmt(self, ctx:GrammarParser.Compound_stmtContext):
        pass


    # Enter a parse tree produced by GrammarParser#if_stmt.
    def enterIf_stmt(self, ctx:GrammarParser.If_stmtContext):
        pass

    # Exit a parse tree produced by GrammarParser#if_stmt.
    def exitIf_stmt(self, ctx:GrammarParser.If_stmtContext):
        pass


    # Enter a parse tree produced by GrammarParser#elif_stmt.
    def enterElif_stmt(self, ctx:GrammarParser.Elif_stmtContext):
        pass

    # Exit a parse tree produced by GrammarParser#elif_stmt.
    def exitElif_stmt(self, ctx:GrammarParser.Elif_stmtContext):
        pass


    # Enter a parse tree produced by GrammarParser#else_stmt.
    def enterElse_stmt(self, ctx:GrammarParser.Else_stmtContext):
        pass

    # Exit a parse tree produced by GrammarParser#else_stmt.
    def exitElse_stmt(self, ctx:GrammarParser.Else_stmtContext):
        pass


    # Enter a parse tree produced by GrammarParser#while_stmt.
    def enterWhile_stmt(self, ctx:GrammarParser.While_stmtContext):
        pass

    # Exit a parse tree produced by GrammarParser#while_stmt.
    def exitWhile_stmt(self, ctx:GrammarParser.While_stmtContext):
        pass


    # Enter a parse tree produced by GrammarParser#for_stmt.
    def enterFor_stmt(self, ctx:GrammarParser.For_stmtContext):
        pass

    # Exit a parse tree produced by GrammarParser#for_stmt.
    def exitFor_stmt(self, ctx:GrammarParser.For_stmtContext):
        pass


    # Enter a parse tree produced by GrammarParser#function_def.
    def enterFunction_def(self, ctx:GrammarParser.Function_defContext):
        pass

    # Exit a parse tree produced by GrammarParser#function_def.
    def exitFunction_def(self, ctx:GrammarParser.Function_defContext):
        pass


    # Enter a parse tree produced by GrammarParser#parameters.
    def enterParameters(self, ctx:GrammarParser.ParametersContext):
        pass

    # Exit a parse tree produced by GrammarParser#parameters.
    def exitParameters(self, ctx:GrammarParser.ParametersContext):
        pass


    # Enter a parse tree produced by GrammarParser#typed_par.
    def enterTyped_par(self, ctx:GrammarParser.Typed_parContext):
        pass

    # Exit a parse tree produced by GrammarParser#typed_par.
    def exitTyped_par(self, ctx:GrammarParser.Typed_parContext):
        pass


    # Enter a parse tree produced by GrammarParser#function_call.
    def enterFunction_call(self, ctx:GrammarParser.Function_callContext):
        pass

    # Exit a parse tree produced by GrammarParser#function_call.
    def exitFunction_call(self, ctx:GrammarParser.Function_callContext):
        pass


    # Enter a parse tree produced by GrammarParser#loop_stmt.
    def enterLoop_stmt(self, ctx:GrammarParser.Loop_stmtContext):
        pass

    # Exit a parse tree produced by GrammarParser#loop_stmt.
    def exitLoop_stmt(self, ctx:GrammarParser.Loop_stmtContext):
        pass


    # Enter a parse tree produced by GrammarParser#func_body.
    def enterFunc_body(self, ctx:GrammarParser.Func_bodyContext):
        pass

    # Exit a parse tree produced by GrammarParser#func_body.
    def exitFunc_body(self, ctx:GrammarParser.Func_bodyContext):
        pass


    # Enter a parse tree produced by GrammarParser#flow_stmt.
    def enterFlow_stmt(self, ctx:GrammarParser.Flow_stmtContext):
        pass

    # Exit a parse tree produced by GrammarParser#flow_stmt.
    def exitFlow_stmt(self, ctx:GrammarParser.Flow_stmtContext):
        pass


    # Enter a parse tree produced by GrammarParser#return_stmt.
    def enterReturn_stmt(self, ctx:GrammarParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by GrammarParser#return_stmt.
    def exitReturn_stmt(self, ctx:GrammarParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by GrammarParser#explist.
    def enterExplist(self, ctx:GrammarParser.ExplistContext):
        pass

    # Exit a parse tree produced by GrammarParser#explist.
    def exitExplist(self, ctx:GrammarParser.ExplistContext):
        pass


    # Enter a parse tree produced by GrammarParser#exp.
    def enterExp(self, ctx:GrammarParser.ExpContext):
        pass

    # Exit a parse tree produced by GrammarParser#exp.
    def exitExp(self, ctx:GrammarParser.ExpContext):
        pass


    # Enter a parse tree produced by GrammarParser#arithmeticOperation.
    def enterArithmeticOperation(self, ctx:GrammarParser.ArithmeticOperationContext):
        pass

    # Exit a parse tree produced by GrammarParser#arithmeticOperation.
    def exitArithmeticOperation(self, ctx:GrammarParser.ArithmeticOperationContext):
        pass


    # Enter a parse tree produced by GrammarParser#term.
    def enterTerm(self, ctx:GrammarParser.TermContext):
        pass

    # Exit a parse tree produced by GrammarParser#term.
    def exitTerm(self, ctx:GrammarParser.TermContext):
        pass


    # Enter a parse tree produced by GrammarParser#factor.
    def enterFactor(self, ctx:GrammarParser.FactorContext):
        pass

    # Exit a parse tree produced by GrammarParser#factor.
    def exitFactor(self, ctx:GrammarParser.FactorContext):
        pass


    # Enter a parse tree produced by GrammarParser#printOperation.
    def enterPrintOperation(self, ctx:GrammarParser.PrintOperationContext):
        pass

    # Exit a parse tree produced by GrammarParser#printOperation.
    def exitPrintOperation(self, ctx:GrammarParser.PrintOperationContext):
        pass


    # Enter a parse tree produced by GrammarParser#conditionalOperation.
    def enterConditionalOperation(self, ctx:GrammarParser.ConditionalOperationContext):
        pass

    # Exit a parse tree produced by GrammarParser#conditionalOperation.
    def exitConditionalOperation(self, ctx:GrammarParser.ConditionalOperationContext):
        pass


    # Enter a parse tree produced by GrammarParser#logicalTerm.
    def enterLogicalTerm(self, ctx:GrammarParser.LogicalTermContext):
        pass

    # Exit a parse tree produced by GrammarParser#logicalTerm.
    def exitLogicalTerm(self, ctx:GrammarParser.LogicalTermContext):
        pass


    # Enter a parse tree produced by GrammarParser#logicalFactor.
    def enterLogicalFactor(self, ctx:GrammarParser.LogicalFactorContext):
        pass

    # Exit a parse tree produced by GrammarParser#logicalFactor.
    def exitLogicalFactor(self, ctx:GrammarParser.LogicalFactorContext):
        pass


    # Enter a parse tree produced by GrammarParser#logicalPrimary.
    def enterLogicalPrimary(self, ctx:GrammarParser.LogicalPrimaryContext):
        pass

    # Exit a parse tree produced by GrammarParser#logicalPrimary.
    def exitLogicalPrimary(self, ctx:GrammarParser.LogicalPrimaryContext):
        pass


    # Enter a parse tree produced by GrammarParser#value.
    def enterValue(self, ctx:GrammarParser.ValueContext):
        pass

    # Exit a parse tree produced by GrammarParser#value.
    def exitValue(self, ctx:GrammarParser.ValueContext):
        pass



del GrammarParser