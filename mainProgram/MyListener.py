from Compiler import GrammarParser
from Compiler.GrammarListener import GrammarListener


class MyListener(GrammarListener):
    def __init__(self, output_file=None):
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

    def enterFor_stmt(self, ctx: GrammarParser.GrammarParser.For_stmtContext):
        identifier = ctx.IDENTIFIER().getText()
        range_value = ctx.NUMBER().getText()
        self.output_buffer.append(f"for {identifier} in range({range_value}):\n\t")

    def enterPrint_stmt(self, ctx:GrammarParser.GrammarParser.Print_stmtContext):
        print("print_stmt")
        self.output_buffer.append("print(")

    def enterPrintOperation(self, ctx: GrammarParser.GrammarParser.PrintOperationContext):
        print("W princie")
        if ctx.STRING() and ctx.exp():
            string = ctx.STRING().getText()
            expression = ctx.exp().getText()
            self.output_buffer.append(f"{string}, {expression}")
        elif ctx.STRING() and not ctx.exp():
            string = ctx.STRING().getText()
            self.output_buffer.append(f"{string}")
    def exitPrint_stmt(self, ctx: GrammarParser.GrammarParser.Print_stmtContext):
        print("Po princie")
        self.output_buffer.append(")\n")

    def enterArithmeticOperation(self, ctx: GrammarParser.GrammarParser.ArithmeticOperationContext):
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
            print(f"{left} {operator_mapping.get(operator, operator)} {right}")
            self.output_buffer.append(f"{left} {operator_mapping.get(operator, operator)} {right}")

    def enterWhile_stmt(self, ctx: GrammarParser.GrammarParser.While_stmtContext):
        print("while stmst")
        condition = ctx.getChild(2).getText()  # Pobierz warunek z 3. dziecka kontekstu (conditionalOperation)
        self.output_buffer.append(f"while {condition}:\n\t")

    def enterIf_stmt(self, ctx: GrammarParser.GrammarParser.If_stmtContext):
        print("W ifie")
        self.output_buffer.append("if ")

    def enterExp(self, ctx: GrammarParser.GrammarParser.ExpContext):
        if ctx.children is not None and len(ctx.children) > 0:
            if not isinstance(ctx.getChild(0), GrammarParser.GrammarParser.PrintOperationContext) and not isinstance(
                    ctx.getChild(0), GrammarParser.GrammarParser.ArithmeticOperationContext) and not isinstance(
                    ctx.getChild(0), GrammarParser.GrammarParser.ConditionalOperationContext)and not isinstance(
                    ctx.getChild(0), GrammarParser.GrammarParser.ValueContext):
                self.output_buffer.append(ctx.getText())
    def exitIf_stmt(self, ctx: GrammarParser.GrammarParser.If_stmtContext):
        self.output_buffer.append("\n")

    def enterElif_stmt(self, ctx: GrammarParser.GrammarParser.Elif_stmtContext):
        print("elif stmst:")
        self.output_buffer.append("elif ")

    def exitElif_stmt(self, ctx: GrammarParser.GrammarParser.Elif_stmtContext):
        print("w exit elif")
        self.output_buffer.append("\n")

    def enterElse_stmt(self, ctx: GrammarParser.GrammarParser.Else_stmtContext):
        print('else stmt')
        self.output_buffer.append("else:\n\t")
    def enterConditionalOperation(self, ctx: GrammarParser.GrammarParser.ConditionalOperationContext):
        print("conditional op")
        text = ctx.getText().split(":")
        output = ""
        print(text)
        for v in text:
            token = ":" + v + ":"
            print(token)
            if token in self.tokens_map.keys():
                output += self.tokens_map[token]
            else:
                output += v
        print("dodaje: ", output)
        self.output_buffer.append(output+":\n\t")

    def enterFunction_def(self, ctx):
        print("w def ")
        func_name = ctx.getChild(1).getText()
        params = self.params(ctx,3)
        self.output_buffer.append(f"def {func_name}({params}):\n\t")

    def enterFunction_call(self, ctx: GrammarParser.GrammarParser.Function_callContext):
        function_name = ctx.IDENTIFIER().getText()
        arguments = [arg.getText() for arg in ctx.exp()]
        mapped_args = ", ".join(arguments)  # Łączy argumenty funkcji jako stringi
        print(mapped_args)
        self.output_buffer.append(f"{function_name}({mapped_args})\n")
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
    def enterValue(self, ctx: GrammarParser.GrammarParser.ValueContext):
         print("w value: ")
         parent_ctx_type = type(ctx.parentCtx).__name__
         print(f"Rodzaj kontekstu nadrzędnego: {parent_ctx_type}")
         if not isinstance(ctx.parentCtx, GrammarParser.GrammarParser.FactorContext) and not isinstance(ctx.parentCtx, GrammarParser.GrammarParser.LogicalPrimaryContext):
             value_token = ctx.getText()
             self.output_buffer.append(value_token)


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
