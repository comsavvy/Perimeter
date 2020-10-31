#!/usr/bin/env python
import sys
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int

    def distance(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5


def read(arg):
    points = []
    with open(arg, 'r') as data:
        for i in data:
            point = tuple(int(a) for a in i.strip().split(','))
            points.append(point)
    return points


def total_perim(data):
    side = []
    a = [Point(*d) for d in data]
    total = 0
    i = 0
    while i < len(a)-1:
        perimeter = a[i].distance(a[i+1])
        side.append(perimeter)
        total += perimeter
        i += 1
    last = a[0].distance(a[-1])
    total += last
    side.append(last)
    return round(total, 2), side


def outcome(data):
    val = total_perim(data)
    print(f'Sides: {val[1]}'
          f'\nTotal perimeter: {val[0]}'
          f'\nMaximum length: {round(max(val[1]), 2)}'
          f'\nAverage length: {round(val[0]/len(val[1]), 2)}')


if __name__ == '__main__':
    argument = sys.argv[1:]
    dt = (read(arg) for arg in argument)
    mover = 0  # This will allow the display of file name
    for i in dt:
        print("-"*10, argument[mover], "*"*10)  # Displaying the name of the file
        print('Points:', i)
        outcome(i)
        print(end='\n')
        mover += 1
