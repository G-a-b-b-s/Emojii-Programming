from tkinter.ttk import Progressbar
import sys
import os

# Dodaj katalog główny projektu do sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)
from antlr4.error.ErrorListener import ErrorListener
from tkinter import *
from tkinter import scrolledtext, messagebox
from antlr4 import *
from Compiler import GrammarLexer, GrammarParser, GrammarListener
import MyErrorListener
import EmojiHandler.EmojiReader
from mainProgram.MyListener import MyListener
from mainProgram.TreePrinterListener import TreePrinterListener
from mainProgram.main import print_tokens


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
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(4, weight=1)

        self.input_label = Label(self.root, text="📝 Input-Emoji Code", bg="#eed9c4", fg="#000000",
                                 font=("Helvetica", 14, "bold"))
        self.input_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.input_text = scrolledtext.ScrolledText(self.root, width=70, height=20, wrap=WORD, bg="#1e1e1e",
                                                    fg="#dcdcdc", insertbackground="#dcdcdc", font=("Consolas", 12))
        self.input_text.grid(row=1, column=0, padx=10, pady=10)

        self.translate_button = Button(self.root, text="✨ Make magic happen! ✨", command=self.translate_code,
                                       bg="#d9b99b", fg="#000000", font=("Helvetica", 12, "bold"))
        self.translate_button.grid(row=2, column=0,columnspan=2, padx=30, pady=10)

        self.output_label = Label(self.root, text="💻 Your code", bg="#eed9c4", fg="#000000",
                                  font=("Helvetica", 14, "bold"))
        self.output_label.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.output_text = scrolledtext.ScrolledText(self.root, width=70, height=20, wrap=WORD, bg="#1e1e1e",
                                                     fg="#dcdcdc", insertbackground="#dcdcdc", font=("Consolas", 12))
        self.output_text.grid(row=1, column=1, padx=10, pady=10)


    def translate_code(self):
        input_code = self.input_text.get("1.0", END)
        try:
            translated_code, errors = self.translate_emoji_code(input_code)

            if errors:
                self.output_text.delete("1.0", END)
            for elem in translated_code:
                self.output_text.insert("1.0", elem)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def translate_emoji_code(self, code):
        emo = EmojiHandler.EmojiReader.EmojiReader()
        code_translated = emo.replace_words_with_dict_values(code)
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

            return listener.output_buffer, []

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
