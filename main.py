from antlr4 import *
from antlr4.tree.Tree import *
import graphviz
import translator
from Supplier.GrammarLexer import GrammarLexer
from Supplier.GrammarParser import GrammarParser
from EmojiHandler.EmojiReader import EmojiReader
from gen.kolejnaProbaLexer import kolejnaProbaLexer
from gen.kolejnaProbaParser import  kolejnaProbaParser
from gen.kolejnaProbaListener import kolejnaProbaListener

def print_tokens(lexer):
    lexer.reset()
    tokens = []
    used_token_types = []
    for token in lexer.getAllTokens():
        token_description = f"{token.text} ({lexer.symbolicNames[token.type]})"
        tokens.append(token_description)
        used_token_types.append(lexer.symbolicNames[token.type])
    lexer.reset()
    tokens_string = '\n'.join(tokens)
    with open('tokens.txt', 'w', encoding='utf-8') as file:
        file.write(tokens_string)



class MyListener(kolejnaProbaListener):
    def __init__(self, output_file):
        self.output_file = output_file
        self.output_buffer = []
        self.tokens_map ={

            ':heavy_plus_sign:': '+',
            ':heavy_minus_sign:': '-',
            ':heavy_multiplication_x:': '*',
            ':heavy_division_sign:': '/',
            ':heavy_equals_sign:': '=',
            ':dragon:': '>',
            ':mouse2:': '<',
            ':leopard:': '>=',
            ':chipmunk:': '<=',
            ':last_quarter_moon_with_face:': '(',
            ':first_quarter_moon_with_face:': ')',
            ':leftwards_hand:': '{',
            ':rightwards_hand:': '}',
            ':paperclip:': ',',
            ':paperclips:': ':',
            ':pushpin:': ';',
            #QUOTE       : ':clapper:';
            ':female_detective:': 'or',
            ':two_women_holding_hands:': 'and',
            ':champagne:': '%',
            #COMMENT     : '/*' .*? '*/' -> skip;
            ':printer:': 'print',
            ':heavy_exclamation_mark:': 'not',
            ':question:': 'if',
            ':heavy_exclamation_mark::heavy_exclamation_mark:': 'else',
            ':question::heavy_exclamation_mark:': 'elif',
            ':gift:': 'for',
            ':mailbox_with_no_mail:': 'in',
            ':mountain_snow:': 'range',
            ':radio:': 'enumerate',
            ':tornado:': 'while',
            ':clipboard:': 'switch',
            ':white_check_mark:': 'case',
            ':vertical_traffic_light:': 'break',
            ':massage:': 'continue',
            ':boomerang:': 'return',
            ':bulb:': 'def',
            ':thumbsup:': 'true',
            ':thumbsdown:': 'false',
            ':crystal_ball:': 'try',
            ':fishing_pole_and_fish:': 'except',
            ':hourglass:': 'finally',
            ':sunrise:': 'raise',
            ':skull:': 'const',
            ':earth_americas:': 'import',
            ':articulated_lorry:': 'from',
            ':rainbow:': 'lambda',
            ':wastebasket:': 'None',
            'as': 'as'
        }

    def enterFor_stmt(self, ctx: kolejnaProbaParser.For_stmtContext):
        identifier = ctx.IDENTIFIER().getText()
        range_value = ctx.NUMBER().getText()
        self.output_buffer.append(f"for {identifier} in range({range_value}):\n\t")

    def enterPrint_stmt(self, ctx: kolejnaProbaParser.Print_stmtContext):
        print("print_stmt")
        self.output_buffer.append("print(")

    def enterPrintOperation(self, ctx: kolejnaProbaParser.PrintOperationContext):
        if ctx.getChildCount() == 3:  # STRING COMMA exp
            print("tekst w print op: ", ctx.getText())
            string = ctx.STRING().getText()
            expression = ctx.exp().getText()
            self.output_buffer.append(f"{string}, ")
        elif ctx.getChildCount() == 3:  # '(' STRING ')'
            string = ctx.STRING().getText()
            self.output_buffer.append(f"{string}")
    def exitPrint_stmt(self, ctx: kolejnaProbaParser.Print_stmtContext):
        self.output_buffer.append(")\n")

    def enterArithmeticOperation(self, ctx: kolejnaProbaParser.ArithmeticOperationContext):
         print("artimh op")
         if ctx.getChild(1) is not None:

            left = ctx.getChild(0).getText()
            operator = ctx.getChild(1).getText()
            right = ctx.getChild(2).getText()
            operator_mapping = {
                ':heavy_plus_sign:': '+',
                ':heavy_minus_sign:': '-',
                ':heavy_multiplication_x:': '*',
                ':heavy_division_sign:': '/',
            }
            print("lewy ", left)
            print("srodek ", {operator_mapping.get(operator, operator)} )
            print("prawy: ",right)
            self.output_buffer.append(f"{left} {operator_mapping.get(operator, operator)} {right}")

    def enterWhile_stmt(self, ctx: kolejnaProbaParser.While_stmtContext):
        print("while stmst")
        condition = ctx.getChild(2).getText()  # Pobierz warunek z 3. dziecka kontekstu (conditionalOperation)
        self.output_buffer.append(f"while {condition}:\n\t")

    def enterIf_stmt(self, ctx: kolejnaProbaParser.If_stmtContext):
        print("if_stmst")
        #print(ctx.getChild().getText())
        val = self.tokens_map[ctx.getChild(0).getText()]

        self.output_buffer.append(val+" ")

    def enterExp(self, ctx: kolejnaProbaParser.ExpContext):
        if not isinstance(ctx.getChild(0), kolejnaProbaParser.PrintOperationContext):
            self.output_buffer.append(ctx.getText())
    def exitIf_stmt(self, ctx: kolejnaProbaParser.If_stmtContext):
        self.output_buffer.append("\n")

    def enterElif_stmt(self, ctx: kolejnaProbaParser.Elif_stmtContext):
        print("elif stmst:")
        print(ctx.getText())
        self.output_buffer.append("elif ")

    def exitElif_stmt(self, ctx: kolejnaProbaParser.Elif_stmtContext):
        print("w exit elif")
        self.output_buffer.append("")

    def enterElse_stmt(self, ctx: kolejnaProbaParser.Else_stmtContext):
        print('else stmt')
        #print(ctx.getText())
        self.output_buffer.append("else:\n\t")
    def enterConditionalOperation(self, ctx: kolejnaProbaParser.ConditionalOperationContext):
        print("conditional op")
        text = ctx.getText().split(":")
        output = ""
        #print(text)
        for v in text:
            token = ":" + v + ":"
            # print(token)
            if token in self.tokens_map.keys():
                output += self.tokens_map[token]
            else:
                output += v
        #print("output: ", output)
        self.output_buffer.append(output+":\n\t")

    def enterFunction_def(self, ctx):
        print("w def ")
        func_name = ctx.getChild(1).getText()
        params = self.params(ctx,3)
        self.output_buffer.append(f"def {func_name}({params}):\n\t")
    def params(self,ctx, number):
        #print("w params")
        params = ctx.getChild(number).getText().split(':')
        output=""
        #print(params)
        for v in params:
            token =":"+v+":"

            if token in self.tokens_map.keys():
                output+=self.tokens_map[token]
            else:
                output+=v
        #print(output)
        return output
    def enterValue(self, ctx: kolejnaProbaParser.ValueContext):
         value_token = ctx.getText()
         print("w value: ",value_token)
         if value_token in self.tokens_map.keys():
            mapped_value = self.tokens_map.get(value_token, value_token)
            self.output_buffer.append(mapped_value)


    # def enterEveryRule(self, ctx: ParserRuleContext):
    #     for i in range(ctx.getChildCount()):
    #         child = ctx.getChild(i)
    #         if isinstance(child, TerminalNodeImpl):
    #             token_text = child.getText()
    #             mapped_value = self.tokens_map.get(token_text, token_text)
    #             self.output_buffer.append(mapped_value)

    def save_output(self):
        with open(self.output_file, "w") as file:
            file.write("".join(self.output_buffer))


class TreePrinterListener(ParseTreeListener):
    def __init__(self, rule_names):
        self.rule_names = rule_names
        self.lines = []
        self.level = 0
        self.graph = graphviz.Digraph()
        self.node_count = 0

    def enterEveryRule(self, ctx):
        rule_index = ctx.getRuleIndex()
        rule_name = self.rule_names[rule_index] if self.rule_names else "Unknown rule"
        self.lines.append(' ' * 2 * self.level + rule_name)

        current_node_id = f"node{self.node_count}"
        self.node_count += 1
        self.graph.node(current_node_id, rule_name)

        if self.level > 0:
            parent_node_id = f"node{self.node_count - 2}"
            self.graph.edge(parent_node_id, current_node_id)

        ctx.node_id = current_node_id
        self.level += 1

    def exitEveryRule(self, ctx):
        self.level -= 1

    def visitTerminal(self, node):
        parent_node_id = node.parentCtx.node_id
        terminal_node_id = f"node{self.node_count}"
        self.node_count += 1
        terminal_name = node.getText()
        self.graph.node(terminal_node_id, terminal_name, shape='box')
        self.graph.edge(parent_node_id, terminal_node_id)

    def getFormattedTree(self):
        return "\n".join(self.lines)

    def saveGraph(self, filename):
        self.graph.render(filename, format='png', cleanup=True)


def main():
    #Tu wpisz ścieżkę do pliku, który chcesz przetworzyć albo wykorzystaj jeden z przykładowych plików
    input_file = 'Examples/3/originalExample.txt'
    output_file = 'Examples/3/example.txt'
    result_file = 'Examples/3/result.py'

    #Preprocessing
    translator.translator(input_file, output_file)
    input_stream = FileStream(output_file, encoding='utf-8')
    lexer = kolejnaProbaLexer(input_stream)
    print_tokens(lexer)
    stream = CommonTokenStream(lexer)
    parser = kolejnaProbaParser(stream)
    tree = parser.start()

    # #Konstrukcja drzewa

    printer = TreePrinterListener(parser.ruleNames)

    walker = ParseTreeWalker()
    walker.walk(printer, tree)

    formatted_tree = printer.getFormattedTree()
    with open('Results/parsing_tree.txt', 'w', encoding='utf-8') as file:
        file.write(formatted_tree)
    printer.saveGraph('Results/dot_parsing_tree')

    listener = MyListener(result_file)
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    listener.save_output()


if __name__ == '__main__':
    main()