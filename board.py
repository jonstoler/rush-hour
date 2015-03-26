from car import Car, Orientation
from grid import Grid

class Board:
    @staticmethod
    # converts a string representation to an actual starting grid
    def parse(str):
        # break the string into lines
        chars = str.split("\n")

        # and remove trailing newline
        chars.pop()

        for i in range(0, len(chars)):
            # create a new list, removing spaces
            chars[i] = list(chars[i].replace(" ", ""))

        cars = {}
        for x in range(0, len(chars)):
            for y in range(0, len(chars[x])):
                # if the current cell ins't empty...
                if chars[x][y] != "+":
                    # check to see if this car is already listed
                    if not chars[x][y] in cars:
                        cars[chars[x][y]] = {"x": y, "y": x, "orientation": None, "length": 1}
                    else:
                        # otherwise make the car longer
                        cars[chars[x][y]]["length"] += 1
                        # and determine its orientation
                        if x > 0 and chars[x - 1][y] == chars[x][y]:
                            cars[chars[x][y]]["orientation"] = Orientation.VERT
                        elif y > 0 and chars[x][y - 1] == chars[x][y]:
                            cars[chars[x][y]]["orientation"] = Orientation.HORZ

        # then create the grid
        grid = Grid("start")
        for c in cars:
            grid.addCar(Car(c, cars[c]["x"], cars[c]["y"], cars[c]["orientation"], cars[c]["length"]))
        return grid
