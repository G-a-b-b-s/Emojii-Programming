from tkinter import *
from tkinter import scrolledtext, messagebox
from antlr4 import *
from Compiler import GrammarLexer, GrammarParser
import MyErrorListener
from EmojiHandler.EmojiReader import EmojiReader
from MyListener import MyListener
import tempfile
import subprocess
import re


class EmojiTranslatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("✨ Emoji Coding Language ✨")
        self.root.configure(bg="#eed9c4")
        self.create_widgets()

    def create_widgets(self):
            # Configure grid layout to make it responsive
            self.root.grid_columnconfigure(0, weight=1)
            self.root.grid_columnconfigure(1, weight=1)
            self.root.grid_columnconfigure(2, weight=1)
            self.root.grid_rowconfigure(1, weight=1)
            self.root.grid_rowconfigure(4, weight=1)

            self.input_label = Label(self.root, text="📝 Input-Emoji Code", bg="#eed9c4", fg="#000000",
                                     font=("Helvetica", 14, "bold"))
            self.input_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

            self.input_text = scrolledtext.ScrolledText(self.root, width=50, height=20, wrap=WORD, bg="#1e1e1e",
                                                        fg="#dcdcdc", insertbackground="#dcdcdc", font=("Consolas", 12))
            self.input_text.grid(row=1, column=0, padx=10, pady=10)

            self.translate_button = Button(self.root, text="✨ Make magic happen! ✨", command=self.translate_code,
                                           bg="#d9b99b", fg="#000000", font=("Helvetica", 12, "bold"))
            self.translate_button.grid(row=2, column=0, columnspan=3, padx=30, pady=10)

            self.translated_label = Label(self.root, text="💻 Translated Python Code", bg="#eed9c4", fg="#000000",
                                          font=("Helvetica", 14, "bold"))
            self.translated_label.grid(row=0, column=1, padx=10, pady=10, sticky="w")

            self.translated_text = scrolledtext.ScrolledText(self.root, width=50, height=20, wrap=WORD, bg="#1e1e1e",
                                                             fg="#dcdcdc", insertbackground="#dcdcdc",
                                                             font=("Consolas", 12))
            self.translated_text.grid(row=1, column=1, padx=10, pady=10)

            self.execution_label = Label(self.root, text="🔧 Execution Output", bg="#eed9c4", fg="#000000",
                                         font=("Helvetica", 14, "bold"))
            self.execution_label.grid(row=0, column=2, padx=10, pady=10, sticky="w")

            self.execution_text = scrolledtext.ScrolledText(self.root, width=50, height=20, wrap=WORD, bg="#1e1e1e",
                                                            fg="#dcdcdc", insertbackground="#dcdcdc",
                                                            font=("Consolas", 12))
            self.execution_text.grid(row=1, column=2, padx=10, pady=10)

    def translate_code(self):
        input_code = self.input_text.get("1.0", END)
        try:
            translated_code, errors = self.translate_emoji_code(input_code)
            if errors:
                self.translated_text.delete("1.0", END)
                self.execution_text.delete("1.0", END)
                self.signalize_errors(errors)
            else:
                self.translated_text.delete("1.0", END)
                self.translated_text.insert("1.0", translated_code)
                self.execution_text.delete("1.0", END)
                self.execute_code(translated_code)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def translate_emoji_code(self, code):
        emo = EmojiReader()
        code_translated = emo.replace_words_with_dict_values(code)
        print(code_translated)
        input_stream = InputStream(code_translated)

        lexer = GrammarLexer.GrammarLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = GrammarParser.GrammarParser(stream)
        error_listener = MyErrorListener.MyErrorListener(self.input_text)
        parser._listeners = [error_listener]
        tree = parser.start()

        errors = error_listener.get_errors()

        if errors:
            return "", errors
        else:
            listener = MyListener()
            walker = ParseTreeWalker()
            walker.walk(listener, tree)

            formatted_code = listener.code()

            return formatted_code, []

    def remove_parentheses_from_conditions(self, code):
        pattern = re.compile(r'(if|elif)\s*\((.*?)\)\s*:')
        return pattern.sub(r'\1 \2:', code)

    def execute_code(self, code):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as temp_file:
            print(code.encode())
            temp_file.write(code.encode())
            temp_file_path = temp_file.name

        try:
            result = subprocess.run(['python', temp_file_path], capture_output=True, text=True)
            self.execution_text.insert("1.0", result.stdout)
            if result.stderr:
                self.execution_text.insert("1.0", result.stderr)
        except Exception as e:
            self.execution_text.insert("1.0", str(e))
        finally:
            print(f"Tymczasowy plik został zapisany pod ścieżką: {temp_file_path}")

    def signalize_errors(self, errors):
        self.input_text.tag_configure("error", background="yellow")
        for line, column, msg in errors:
            start_pos = f"{line}.{column - 1}"
            end_pos = f"{line}.{column}"
            self.input_text.tag_add("error", start_pos, end_pos)


if __name__ == "__main__":
    root = Tk()
    app = EmojiTranslatorGUI(root)
    root.mainloop()
