class Stack:
    @staticmethod
    def pop(items):
        return items.pop(0)
    
    @staticmethod
    def push(items, add, f):
        items.append(add)

class Queue:
    @staticmethod
    def pop(items):
        return items.pop()

    @staticmethod
    def push(items, add, f):
        items.append(add)

class PriorityQueue(Stack):
    @staticmethod
    def push(items, add, f):
        addCost = len(add)
        index = 0
        for i in items:
            if len(i) >= addCost:
                break
            index += 1
        items.insert(index, add)

class AStar(PriorityQueue):
    @staticmethod
    def push(items, add, f):
        addCost = len(add) + f(add)
        index = 0
        for i in items:
            if (len(i) + f(i)) >= addCost:
                break
            index += 1
        items.insert(index, add)
