// Generated from Grammar.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link GrammarParser}.
 */
public interface GrammarListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link GrammarParser#start}.
	 * @param ctx the parse tree
	 */
	void enterStart(GrammarParser.StartContext ctx);
	/**
	 * Exit a parse tree produced by {@link GrammarParser#start}.
	 * @param ctx the parse tree
	 */
	void exitStart(GrammarParser.StartContext ctx);
	/**
	 * Enter a parse tree produced by {@link GrammarParser#stmt}.
	 * @param ctx the parse tree
	 */
	void enterStmt(GrammarParser.StmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link GrammarParser#stmt}.
	 * @param ctx the parse tree
	 */
	void exitStmt(GrammarParser.StmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link GrammarParser#simple_stmt}.
	 * @param ctx the parse tree
	 */
	void enterSimple_stmt(GrammarParser.Simple_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link GrammarParser#simple_stmt}.
	 * @param ctx the parse tree
	 */
	void exitSimple_stmt(GrammarParser.Simple_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link GrammarParser#assignment_stmt}.
	 * @param ctx the parse tree
	 */
	void enterAssignment_stmt(GrammarParser.Assignment_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link GrammarParser#assignment_stmt}.
	 * @param ctx the parse tree
	 */
	void exitAssignment_stmt(GrammarParser.Assignment_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link GrammarParser#declare_stmt}.
	 * @param ctx the parse tree
	 */
	void enterDeclare_stmt(GrammarParser.Declare_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link GrammarParser#declare_stmt}.
	 * @param ctx the parse tree
	 */
	void exitDeclare_stmt(GrammarParser.Declare_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link GrammarParser#single_declaration}.
	 * @param ctx the parse tree
	 */
	void enterSingle_declaration(GrammarParser.Single_declarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link GrammarParser#single_declaration}.
	 * @param ctx the parse tree
	 */
	void exitSingle_declaration(GrammarParser.Single_declarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link GrammarParser#import_stmt}.
	 * @param ctx the parse tree
	 */
	void enterImport_stmt(GrammarParser.Import_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link GrammarParser#import_stmt}.
	 * @param ctx the parse tree
	 */
	void exitImport_stmt(GrammarParser.Import_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link GrammarParser#from_stmt}.
	 * @param ctx the parse tree
	 */
	void enterFrom_stmt(GrammarParser.From_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link GrammarParser#from_stmt}.
	 * @param ctx the parse tree
	 */
	void exitFrom_stmt(GrammarParser.From_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link GrammarParser#module_name}.
	 * @param ctx the parse tree
	 */
	void enterModule_name(GrammarParser.Module_nameContext ctx);
	/**
	 * Exit a parse tree produced by {@link GrammarParser#module_name}.
	 * @param ctx the parse tree
	 */
	void exitModule_name(GrammarParser.Module_nameContext ctx);
	/**
	 * Enter a parse tree produced by {@link GrammarParser#import_list}.
	 * @param ctx the parse tree
	 */
	void enterImport_list(GrammarParser.Import_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link GrammarParser#import_list}.
	 * @param ctx the parse tree
	 */
	void exitImport_list(GrammarParser.Import_listContext ctx);
	/**
	 * Enter a parse tree produced by {@link GrammarParser#import_name}.
	 * @param ctx the parse tree
	 */
	void enterImport_name(GrammarParser.Import_nameContext ctx);
	/**
	 * Exit a parse tree produced by {@link GrammarParser#import_name}.
	 * @param ctx the parse tree
	 */
	void exitImport_name(GrammarParser.Import_nameContext ctx);
	/**
	 * Enter a parse tree produced by {@link GrammarParser#try_stmt}.
	 * @param ctx the parse tree
	 */
	void enterTry_stmt(GrammarParser.Try_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link GrammarParser#try_stmt}.
	 * @param ctx the parse tree
	 */
	void exitTry_stmt(GrammarParser.Try_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link GrammarParser#except_clause}.
	 * @param ctx the parse tree
	 */
	void enterExcept_clause(GrammarParser.Except_clauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link GrammarParser#except_clause}.
	 * @param ctx the parse tree
	 */
	void exitExcept_clause(GrammarParser.Except_clauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link GrammarParser#print_stmt}.
	 * @param ctx the parse tree
	 */
	void enterPrint_stmt(GrammarParser.Print_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link GrammarParser#print_stmt}.
	 * @param ctx the parse tree
	 */
	void exitPrint_stmt(GrammarParser.Print_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link GrammarParser#multiple_assignment_stmt}.
	 * @param ctx the parse tree
	 */
	void enterMultiple_assignment_stmt(GrammarParser.Multiple_assignment_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link GrammarParser#multiple_assignment_stmt}.
	 * @param ctx the parse tree
	 */
	void exitMultiple_assignment_stmt(GrammarParser.Multiple_assignment_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link GrammarParser#raise_stmt}.
	 * @param ctx the parse tree
	 */
	void enterRaise_stmt(GrammarParser.Raise_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link GrammarParser#raise_stmt}.
	 * @param ctx the parse tree
	 */
	void exitRaise_stmt(GrammarParser.Raise_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link GrammarParser#exception_expr}.
	 * @param ctx the parse tree
	 */
	void enterException_expr(GrammarParser.Exception_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link GrammarParser#exception_expr}.
	 * @param ctx the parse tree
	 */
	void exitException_expr(GrammarParser.Exception_exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link GrammarParser#exception_name}.
	 * @param ctx the parse tree
	 */
	void enterException_name(GrammarParser.Exception_nameContext ctx);
	/**
	 * Exit a parse tree produced by {@link GrammarParser#exception_name}.
	 * @param ctx the parse tree
	 */
	void exitException_name(GrammarParser.Exception_nameContext ctx);
	/**
	 * Enter a parse tree produced by {@link GrammarParser#compound_stmt}.
	 * @param ctx the parse tree
	 */
	void enterCompound_stmt(GrammarParser.Compound_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link GrammarParser#compound_stmt}.
	 * @param ctx the parse tree
	 */
	void exitCompound_stmt(GrammarParser.Compound_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link GrammarParser#if_stmt}.
	 * @param ctx the parse tree
	 */
	void enterIf_stmt(GrammarParser.If_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link GrammarParser#if_stmt}.
	 * @param ctx the parse tree
	 */
	void exitIf_stmt(GrammarParser.If_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link GrammarParser#while_stmt}.
	 * @param ctx the parse tree
	 */
	void enterWhile_stmt(GrammarParser.While_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link GrammarParser#while_stmt}.
	 * @param ctx the parse tree
	 */
	void exitWhile_stmt(GrammarParser.While_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link GrammarParser#for_stmt}.
	 * @param ctx the parse tree
	 */
	void enterFor_stmt(GrammarParser.For_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link GrammarParser#for_stmt}.
	 * @param ctx the parse tree
	 */
	void exitFor_stmt(GrammarParser.For_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link GrammarParser#function_def}.
	 * @param ctx the parse tree
	 */
	void enterFunction_def(GrammarParser.Function_defContext ctx);
	/**
	 * Exit a parse tree produced by {@link GrammarParser#function_def}.
	 * @param ctx the parse tree
	 */
	void exitFunction_def(GrammarParser.Function_defContext ctx);
	/**
	 * Enter a parse tree produced by {@link GrammarParser#parameters}.
	 * @param ctx the parse tree
	 */
	void enterParameters(GrammarParser.ParametersContext ctx);
	/**
	 * Exit a parse tree produced by {@link GrammarParser#parameters}.
	 * @param ctx the parse tree
	 */
	void exitParameters(GrammarParser.ParametersContext ctx);
	/**
	 * Enter a parse tree produced by {@link GrammarParser#typed_par}.
	 * @param ctx the parse tree
	 */
	void enterTyped_par(GrammarParser.Typed_parContext ctx);
	/**
	 * Exit a parse tree produced by {@link GrammarParser#typed_par}.
	 * @param ctx the parse tree
	 */
	void exitTyped_par(GrammarParser.Typed_parContext ctx);
	/**
	 * Enter a parse tree produced by {@link GrammarParser#loop_stmt}.
	 * @param ctx the parse tree
	 */
	void enterLoop_stmt(GrammarParser.Loop_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link GrammarParser#loop_stmt}.
	 * @param ctx the parse tree
	 */
	void exitLoop_stmt(GrammarParser.Loop_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link GrammarParser#func_body}.
	 * @param ctx the parse tree
	 */
	void enterFunc_body(GrammarParser.Func_bodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link GrammarParser#func_body}.
	 * @param ctx the parse tree
	 */
	void exitFunc_body(GrammarParser.Func_bodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link GrammarParser#flow_stmt}.
	 * @param ctx the parse tree
	 */
	void enterFlow_stmt(GrammarParser.Flow_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link GrammarParser#flow_stmt}.
	 * @param ctx the parse tree
	 */
	void exitFlow_stmt(GrammarParser.Flow_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link GrammarParser#return_stmt}.
	 * @param ctx the parse tree
	 */
	void enterReturn_stmt(GrammarParser.Return_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link GrammarParser#return_stmt}.
	 * @param ctx the parse tree
	 */
	void exitReturn_stmt(GrammarParser.Return_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link GrammarParser#explist}.
	 * @param ctx the parse tree
	 */
	void enterExplist(GrammarParser.ExplistContext ctx);
	/**
	 * Exit a parse tree produced by {@link GrammarParser#explist}.
	 * @param ctx the parse tree
	 */
	void exitExplist(GrammarParser.ExplistContext ctx);
	/**
	 * Enter a parse tree produced by {@link GrammarParser#exp}.
	 * @param ctx the parse tree
	 */
	void enterExp(GrammarParser.ExpContext ctx);
	/**
	 * Exit a parse tree produced by {@link GrammarParser#exp}.
	 * @param ctx the parse tree
	 */
	void exitExp(GrammarParser.ExpContext ctx);
	/**
	 * Enter a parse tree produced by {@link GrammarParser#arithmeticOperation}.
	 * @param ctx the parse tree
	 */
	void enterArithmeticOperation(GrammarParser.ArithmeticOperationContext ctx);
	/**
	 * Exit a parse tree produced by {@link GrammarParser#arithmeticOperation}.
	 * @param ctx the parse tree
	 */
	void exitArithmeticOperation(GrammarParser.ArithmeticOperationContext ctx);
	/**
	 * Enter a parse tree produced by {@link GrammarParser#term}.
	 * @param ctx the parse tree
	 */
	void enterTerm(GrammarParser.TermContext ctx);
	/**
	 * Exit a parse tree produced by {@link GrammarParser#term}.
	 * @param ctx the parse tree
	 */
	void exitTerm(GrammarParser.TermContext ctx);
	/**
	 * Enter a parse tree produced by {@link GrammarParser#factor}.
	 * @param ctx the parse tree
	 */
	void enterFactor(GrammarParser.FactorContext ctx);
	/**
	 * Exit a parse tree produced by {@link GrammarParser#factor}.
	 * @param ctx the parse tree
	 */
	void exitFactor(GrammarParser.FactorContext ctx);
	/**
	 * Enter a parse tree produced by {@link GrammarParser#printOperation}.
	 * @param ctx the parse tree
	 */
	void enterPrintOperation(GrammarParser.PrintOperationContext ctx);
	/**
	 * Exit a parse tree produced by {@link GrammarParser#printOperation}.
	 * @param ctx the parse tree
	 */
	void exitPrintOperation(GrammarParser.PrintOperationContext ctx);
	/**
	 * Enter a parse tree produced by {@link GrammarParser#conditionalOperation}.
	 * @param ctx the parse tree
	 */
	void enterConditionalOperation(GrammarParser.ConditionalOperationContext ctx);
	/**
	 * Exit a parse tree produced by {@link GrammarParser#conditionalOperation}.
	 * @param ctx the parse tree
	 */
	void exitConditionalOperation(GrammarParser.ConditionalOperationContext ctx);
	/**
	 * Enter a parse tree produced by {@link GrammarParser#logicalTerm}.
	 * @param ctx the parse tree
	 */
	void enterLogicalTerm(GrammarParser.LogicalTermContext ctx);
	/**
	 * Exit a parse tree produced by {@link GrammarParser#logicalTerm}.
	 * @param ctx the parse tree
	 */
	void exitLogicalTerm(GrammarParser.LogicalTermContext ctx);
	/**
	 * Enter a parse tree produced by {@link GrammarParser#logicalFactor}.
	 * @param ctx the parse tree
	 */
	void enterLogicalFactor(GrammarParser.LogicalFactorContext ctx);
	/**
	 * Exit a parse tree produced by {@link GrammarParser#logicalFactor}.
	 * @param ctx the parse tree
	 */
	void exitLogicalFactor(GrammarParser.LogicalFactorContext ctx);
	/**
	 * Enter a parse tree produced by {@link GrammarParser#logicalPrimary}.
	 * @param ctx the parse tree
	 */
	void enterLogicalPrimary(GrammarParser.LogicalPrimaryContext ctx);
	/**
	 * Exit a parse tree produced by {@link GrammarParser#logicalPrimary}.
	 * @param ctx the parse tree
	 */
	void exitLogicalPrimary(GrammarParser.LogicalPrimaryContext ctx);
	/**
	 * Enter a parse tree produced by {@link GrammarParser#value}.
	 * @param ctx the parse tree
	 */
	void enterValue(GrammarParser.ValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link GrammarParser#value}.
	 * @param ctx the parse tree
	 */
	void exitValue(GrammarParser.ValueContext ctx);
}