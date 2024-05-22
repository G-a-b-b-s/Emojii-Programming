from Compiler import GrammarParser
from Compiler.GrammarListener import GrammarListener


class MyListener(GrammarListener):
    def __init__(self, output_file=None):
        self.output_file = output_file
        self.output_buffer = []
        self.indent_level = 0
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
        range_values = ctx.exp_list().exp()  # Pobieramy listę wszystkich numerów w zakresie

        # Sprawdzamy, czy drugi numer istnieje
        if len(range_values) == 2:
            start = range_values[0].getText()  # Pierwszy numer to początek zakresu
            end = range_values[1].getText()  # Drugi numer to koniec zakresu
            range_str = f"{start}, {end}"
        else:
            start = range_values[0].getText()  # Pierwszy numer to początek zakresu
            range_str = start
        indent = '\t' * self.indent_level
        self.output_buffer.append(f"{indent}for {identifier} in range({range_str}):\n")
        self.indent_level += 1
    def exitFor_stmt(self, ctx:GrammarParser.GrammarParser.For_stmtContext):
        self.indent_level-=1
    def enterPrint_stmt(self, ctx:GrammarParser.GrammarParser.Print_stmtContext):
        print("print_stmt")
        indent = '\t' * self.indent_level
        self.output_buffer.append(f"{indent}print(")

    def enterPrintOperation(self, ctx: GrammarParser.GrammarParser.PrintOperationContext):
        print("W princie")
        print(self.output_buffer)
        if ctx.STRING() and ctx.exp():
            string = ctx.STRING().getText()
            expression = ctx.exp().getText()
            print(f"DODAJE: {string}, {expression}")
            self.output_buffer.append(f"{string}, ")
        elif ctx.STRING() and not ctx.exp():
            string = ctx.STRING().getText()
            print(f"DODAJE: {string}")
            self.output_buffer.append(f"{string}")

    def enterAssignment_stmt(self, ctx: GrammarParser.GrammarParser.Assignment_stmtContext):
        identifier = ctx.IDENTIFIER().getText()
        expression = ctx.exp().getText()
        indent = '\t' * self.indent_level
        # Check if the previous token was also '='
        self.output_buffer.append(f"{indent}{identifier} = ")

    def exitAssignment_stmt(self, ctx: GrammarParser.GrammarParser.Assignment_stmtContext):
        self.output_buffer.append("\n")
    def exitPrint_stmt(self, ctx: GrammarParser.GrammarParser.Print_stmtContext):
        print("Po princie")
        self.output_buffer.append(")\n")
        # print("3")

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
            # print("lewy ", left)
            # print("srodek ", {operator_mapping.get(operator, operator)} )
            # print("prawy: ",right)
            # print(f"{left} {operator_mapping.get(operator, operator)} {right}")
            print(f"DODAJE: {left} {operator_mapping.get(operator, operator)} {right}")
            indent = '\t' * self.indent_level
            self.output_buffer.append(f"{left} {operator_mapping.get(operator, operator)} {right}")

    def enterWhile_stmt(self, ctx: GrammarParser.GrammarParser.While_stmtContext):
        print("while stmst")
        condition = ctx.getChild(2).getText()  # Pobierz warunek z 3. dziecka kontekstu (conditionalOperation)
        self.output_buffer.append(f"while {condition}:\n\t")
        indent = '\t' * self.indent_level
        print(f"DODAJE: {indent} while {condition}:\n\t")
        self.indent_level += 1
    def exitWhile_stmt(self, ctx:GrammarParser.GrammarParser.While_stmtContext):
        self.indent_level-=1
    def enterIf_stmt(self, ctx: GrammarParser.GrammarParser.If_stmtContext):
        print("W ifie")
        indent = '\t' * self.indent_level
        self.output_buffer.append(f"{indent}if ")
        self.indent_level += 1

    def enterExp(self, ctx: GrammarParser.GrammarParser.ExpContext):
        print("w expression")
        if ctx.children is not None and len(ctx.children) > 0:
            if not isinstance(ctx.getChild(0), GrammarParser.GrammarParser.PrintOperationContext) and not isinstance(
                    ctx.getChild(0), GrammarParser.GrammarParser.ArithmeticOperationContext) and not isinstance(
                    ctx.getChild(0), GrammarParser.GrammarParser.ConditionalOperationContext) and not isinstance(
                    ctx.getChild(0), GrammarParser.GrammarParser.ValueContext):
                print(f"DODAJE: {ctx.getText()}")
                self.output_buffer.append(f"{ctx.getText()}")
                print(self.output_buffer)
    def exitIf_stmt(self, ctx: GrammarParser.GrammarParser.If_stmtContext):
        self.indent_level -= 1
        print("po ifie")
        self.output_buffer.append("\n")

    def enterElif_stmt(self, ctx: GrammarParser.GrammarParser.Elif_stmtContext):
        self.indent_level -= 1
        indent= '\t' * self.indent_level
        print("elif stmst:")
        self.output_buffer.append(f"{indent}elif ")
        self.indent_level += 1

    def exitElif_stmt(self, ctx: GrammarParser.GrammarParser.Elif_stmtContext):
        self.indent_level -= 1
        print("w exit elif")
        self.output_buffer.append("\n")

    def enterElse_stmt(self, ctx: GrammarParser.GrammarParser.Else_stmtContext):
        print('else stmt')
        self.indent_level -= 1
        indent = '\t' * self.indent_level
        self.output_buffer.append(f"{indent}else:\n")
        self.indent_level += 1
    def exitElse_stmt(self, ctx:GrammarParser.GrammarParser.Else_stmtContext):
        self.indent_level-=1
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
        if '= =' in output:
            output = output.replace('= =', '==')
        print(f"DODAJE: {output}:\n\t")
        self.output_buffer.append(f"{output} :\n")

    def enterFunction_def(self, ctx):
        print("w def ")
        func_name = ctx.getChild(1).getText()
        params = self.params(ctx,3)
        indent = '\t' * self.indent_level
        self.output_buffer.append(f"{indent}def {func_name}({params}):\n")
        self.indent_level += 1
    def exitFunction_def(self, ctx):
        self.indent_level -= 1
    def enterFunction_call(self, ctx: GrammarParser.GrammarParser.Function_callContext):
        print("funcion call")
        function_name = ctx.IDENTIFIER().getText()
        # Sprawdzamy, czy parametry istnieją
        if ctx.parameters():
            # Uzyskujemy wszystkie 'typed_par' w ramach 'parameters'
            parameters_ctx = ctx.parameters()
            typed_pars = parameters_ctx.typed_par()
            arguments = [arg.getText() for arg in typed_pars]
        else:
            arguments = []

        mapped_args = ", ".join(arguments)  # Łączy argumenty funkcji jako stringi
        print(f"DODAJE: {function_name}({mapped_args})\n")
        indent = '\t' * self.indent_level
        self.output_buffer.append(f"{indent}{function_name}({mapped_args})\n")

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
         if not isinstance(ctx.parentCtx, GrammarParser.GrammarParser.FactorContext) and not isinstance(ctx.parentCtx, GrammarParser.GrammarParser.LogicalPrimaryContext) and not isinstance(ctx.parentCtx, GrammarParser.GrammarParser.PrintOperationContext)\
                 and self.output_buffer[-1][-2]!=':':
             value_token = ctx.getText()
             print(f"DODAJE: {value_token}")
             self.output_buffer.append(value_token)

    def enterReturn_stmt(self, ctx: GrammarParser.GrammarParser.Return_stmtContext):
        print("w returnie")
        indent = '\t' * self.indent_level  # Calculate current indentation
        self.output_buffer.append(f"{indent}return\n")
    def save_output(self):
        with open(self.output_file, "w") as file:
            file.write("".join(self.output_buffer))