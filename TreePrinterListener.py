import graphviz
from antlr4 import ParseTreeListener


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

