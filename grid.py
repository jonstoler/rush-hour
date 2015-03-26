from car import Car, Orientation
import copy

class Grid:
    # each grid is given an action representing how it was reached
    # from the previous grid
    def __init__(self, action):
        self.cars = []
        self.action = action
    
    # returns a specific car, if it exists
    def findCar(self, car):
        for c in self.cars:
            if c.designation == car:
                return c
        return None

    # checks whether a space is occupied by a car or if it's empty
    def occupied(self, x, y):
        if x < 0 or x > 5: return "out of bounds"
        if y < 0 or y > 5: return "out of bounds"
        for c in self.cars:
            if c.orientation == Orientation.HORZ:
                if (x >= c.position["x"] and x < (c.position["x"] + c.length) and y == c.position["y"]): return c.designation
            elif c.orientation == Orientation.VERT:
                if (y >= c.position["y"] and y < (c.position["y"] + c.length) and x == c.position["x"]): return c.designation
        return False

    # hashes the board
    # hashes are each car, followed by its coordinates in a string
    # for instance:
    # A22B33C10
    def identity(self):
        identifier = ""
        for c in self.cars:
            identifier += c.designation + str(c.position["x"]) + str(c.position["y"])
        return identifier

    # places a car on the grid
    def addCar(self, car):
        self.cars.append(car)

    # checks for solutions
    def isSolution(self):
        # determine whether car A is at the goal
        for c in self.cars:
            if c.designation == "A":
                return ((c.position["x"] + c.length) == 6 and c.position["y"] == 2)
        return False

    # moves a car by a specific number of spaces
    def move(self, car, dx, dy):
        for c in self.cars:
            if c.designation == car:
                c.position["x"] += dx
                c.position["y"] += dy

    # generates all possible moves
    def generateChildren(self):
        children = []

        # go through each car...
        for c in self.cars:
            # if it's horizontal, check its x coordinates, left and right
            if c.orientation == Orientation.HORZ:
                if not self.occupied(c.position["x"] - 1, c.position["y"]):
                    # create a copy of the grid, then modify it
                    g = copy.deepcopy(self)
                    # set its action
                    g.action = "move " + c.designation + " to the left"
                    # move the car
                    g.move(c.designation, -1, 0)
                    # add it to the list of possible moves
                    children.append(g)
                if not self.occupied(c.position["x"] + c.length, c.position["y"]):
                    g = copy.deepcopy(self)
                    g.action = "move " + c.designation + " to the right"
                    g.move(c.designation, 1, 0)
                    children.append(g)
            # otherwise, check vertically
            else:
                if not self.occupied(c.position["x"], c.position["y"] - 1):
                    g = copy.deepcopy(self)
                    g.action = "move " + c.designation + " up"
                    g.move(c.designation, 0, -1)
                    children.append(g)
                if not self.occupied(c.position["x"], c.position["y"] + c.length):
                    g = copy.deepcopy(self)
                    g.action = "move " + c.designation + " down"
                    g.move(c.designation, 0, 1)
                    children.append(g)

        return children
    
    # allows printing grids to show their actions
    def __repr__(self):
        return self.action

    def __eq__(self, other):
        return (self.identity() == other.identity())
