from algorithms import Stack, Queue, PriorityQueue, AStar
from search import TreeSearch, GraphSearch
from board import Board
import sys
import time

# puzzles should be entered through stdin
# empty spaces are represented by +'s
# cars are given letter designations
# each row is on its own line
# spaces are ignored

# for example:
"""
+ + + + B +
+ + + + B +
+ + + + B +
+ + A A B +
+ + + C + +
+ + + C D D
+ + + + + +
"""

# what type of seach do you want?
# GraphSearch or TreeSearch
searchType = TreeSearch

# how do you want the frontier to be managed?
# Stack, Queue, PriorityQueue, or AStar
manager = Queue

# read the puzzle and make a board out of it
puzzle = sys.stdin.read()
board = Board.parse(puzzle)

times = []
trials = 1

for i in range(0, trials):
    start = time.time()

    search = searchType()
    solution = search.solve(board, manager)
    board.generateChildren()

    done = time.time()
    times.append(done - start)

print(sum(times) / trials)

print("INPUT")
print("===========")
print(puzzle)
print("SOLUTION")
print("===================")
search.out(solution)
print("")
print("=== %d steps ===" % (len(solution) + 1))
print("=== %.4f seconds ===" % (done - start))
