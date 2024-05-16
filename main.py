from antlr4 import *
from graphviz import dot

from Compiler.GrammarLexer import GrammarLexer
from Compiler.GrammarParser import GrammarParser
from Compiler.GrammarListener import GrammarListener
from antlr4.tree.Tree import *
from antlr4 import ParserRuleContext
import graphviz

import spacy


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
    # tu możesz wybrać inny plik do testowania z folderu algorithms lub przesłać swój plik do folderu, a następnie wpisać jesgo nazwę
    input_stream = FileStream('Examples/example.txt', encoding='utf-8')
    lexer = GrammarLexer(input_stream)
    print_tokens(lexer)
    stream = CommonTokenStream(lexer)
    parser = GrammarParser(stream)
    tree = parser.start()


    printer = TreePrinterListener(parser.ruleNames)
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    formatted_tree = printer.getFormattedTree()
    print(formatted_tree)
    with open('Results/parsing_tree.txt', 'w', encoding='utf-8') as file:
        file.write(formatted_tree)
    printer.saveGraph('Results/dot_parsing_tree')


if __name__ == '__main__':
    main()