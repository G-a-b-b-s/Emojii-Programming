from antlr4.error.ErrorListener import ErrorListener


class MyErrorListener(ErrorListener):
    def __init__(self, input_text):
        super().__init__()
        self.input_text = input_text
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append((line, column, msg))

    def get_errors(self):
        return self.errors

