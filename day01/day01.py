"""
Solve day 1 of Advent of Code.
http://adventofcode.com/day/1
"""

instruction = {'(': 1, ')': -1 }
#right = 3537
#left = 3463

def floor_frominstructions(instructions):
    return sum([instruction.get(x, 0) for x in instructions])
def position_of_basement(instructions):
    if i in + 1:
        return -1
    else floor_frominstructions(instructions) == -1:
        return i
