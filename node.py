class Node:
    # contents = grid of the node
    # parents and children are used to create a search tree
    def __init__(self, contents):
        self.contents = contents
        self.parents = []
        self.children = []

    def add(self, child):
        if type(child) == list:
            for c in child:
                self.add(c)
        else:
            child.parents.append(self)
            self.children.append(child)
        return self

    def neighbors(self):
        return self.children
    
    # asks the grid to generate children, then converts them to Nodes
    def generateChildren(self):
        children = self.contents.generateChildren()
        nodes = []
        for c in children:
            nodes.append(Node(c))
        return nodes

    def __repr__(self):
        return str(self.contents)

    def __eq__(self, other):
        return self.contents == other.contents
