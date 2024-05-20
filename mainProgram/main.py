from antlr4 import *
from antlr4.tree.Tree import *
import graphviz

from Compiler.GrammarLexer import GrammarLexer
from Compiler.GrammarParser import GrammarParser
from EmojiHandler.EmojiReader import EmojiReader
from TreePrinterListener import TreePrinterListener
from mainProgram.MyListener import MyListener


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
    with open('./Results/tokens.txt', 'w', encoding='utf-8') as file:
        file.write(tokens_string)



def main():

    #Tu wpisz ścieżkę do pliku, który chcesz przetworzyć
    # albo wykorzystaj jeden z przykładowych plików z przedrostkiem original
    input_file = 'Examples/4/originalExample.txt'

    # Tu wpisz ścieżkę do pliku, do którego chcesz zapisać emotikonowo przetworzony język
    # albo wykorzystaj jeden z przykładowych plików
    output_file = 'Examples/4/example.txt'

    # Tu wpisz ścieżkę do pliku, do którego chcesz zapisać przetłumaczony na kod język
    # albo wykorzystaj jeden z przykładowych plików
    result_file = 'Examples/4/result.py'

    EmojiReader(input_file).convertToFile(output_file)

    input_stream = FileStream(output_file, encoding='utf-8')
    lexer = GrammarLexer(input_stream)
    print_tokens(lexer)
    stream = CommonTokenStream(lexer)
    parser = GrammarParser(stream)
    tree = parser.start()

    #Konstrukcja drzewa

    printer = TreePrinterListener(parser.ruleNames)

    listener = MyListener(result_file)
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    walker.walk(printer, tree)
    formatted_tree = printer.getFormattedTree()
    with open('Results/parsing_tree.txt', 'w', encoding='utf-8') as file:
        file.write(formatted_tree)
    printer.saveGraph('Examples/4/dot_parsing_tree')

    #Listener
    listener.save_output()


if __name__ == '__main__':
    main()