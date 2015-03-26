class Orientation:
    VERT = 1
    HORZ = 0

class Car:
    # designation is how to represent the car (A is the "goal car")
    # x and y are its current board coordinates
    # orientation is either VERT (1) or HORZ (0)
    # length is how long it is
    def __init__(self, designation, x, y, orientation, length):
        self.designation = designation
        self.position = {"x": x, "y": y}
        self.orientation = orientation
        self.length = length
