from node import Node
from algorithms import Stack, Queue, PriorityQueue, AStar

# no hashtable
class TreeSearch:
    def solve(self, board, algorithm):
        solution = None
        start = Node(board)
        
        # paths is the frontier (a list of lists)
        paths = [[start]]

        # while the frontier has not been exhausted...
        while(len(paths) > 0):
            # take out the first path
            path = algorithm.pop(paths)

            # the node to examine is the last node in the path
            node = path[len(path) - 1]
            
            if node.contents.isSolution():
                # if it's a solution, we're done!
                solution = path
                break

            # add all its generated neighbors to the node
            node.add(node.generateChildren())

            for n in node.neighbors():
                # cycle checking
                if not n in path:
                    # create a new path containing the current path
                    newPath = list(path)

                    # add the new neighbor to it
                    newPath.append(n)

                    # add it to the frontier according to the specified algorithm
                    algorithm.push(paths, newPath, self.heuristic)

        # remove the first item from the path (which is just "start," not a real move)
        solution.pop(0)

        # return the solution (defaults to None)
        return solution

    # print out a list of steps
    def out(self, solution):
        for s in solution:
            print(s)

    def heuristic(self, item):
        grid = item[1].contents

        # check how far A is from the goal
        a = grid.findCar("A")
        cost = (5 - a.position["x"])

        # add one for each car in its way
        for c in grid.cars:
            if c.designation != "A" and ((c.position["y"] + c.length) > 2):
                cost += 1

        return cost

# search with a hashtable
class GraphSearch:
    def __init__(self):
        self.hashTable = {}

    # this solution algorithm works essentially the same, except
    # instead of storing Nodes directly, they are looked up in a hashtable
    # through Grid's identity() hash method
    # note that each item in a given path is a list of a Node's hash as well as
    # its action - this is different from before and changes how the
    # heuristic and output code are written (but not how they work)
    def solve(self, board, algorithm):
        solution = None
        start = Node(board)
        self.hashTable[start.contents.identity()] = start
        paths = [[[start.contents.identity(), start.contents.action]]]

        while(len(paths) > 0):
            print(len(paths))
            path = algorithm.pop(paths)
            print(len(path))
            print("")
            node = path[len(path) - 1]
            node = self.hashTable[node[0]]
            if node.contents.isSolution():
                solution = path
                break
            node.add(node.generateChildren())
            for n in node.neighbors():
                identity = n.contents.identity()
                if not identity in self.hashTable:
                    newPath = list(path)
                    newPath.append([identity, n.contents.action])
                    self.hashTable[identity] = n
                    algorithm.push(paths, newPath, self.heuristic)
        solution.pop(0)
        return solution
    
    def out(self, solution):
        for s in solution:
            print(s[1])

    def heuristic(self, item):
        grid = self.hashTable[item[len(item) - 1][0]].contents
        a = grid.findCar("A")
        cost = (5 - a.position["x"])
        for c in grid.cars:
            if c.designation != "A" and ((c.position["y"] + c.length) > 2):
                cost += 1
        return cost
