#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.


# triangle(a, b, c) analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    # DELETE 'PASS' AND WRITE THIS CODE
    sides = [a, b, c]
    for side in sides:
        if side <= 0:
            raise TriangleError

    num_sides_equal = len(set(sides))
    if num_sides_equal == 1:
        return 'equilateral'
    elif num_sides_equal == 2:
        side_a = None
        side_b = None
        for side in set(sides):
            if sides.count(side) == 2:
                side_a = side
            else:
                side_b = side
        if side_a and side_b and side_a < side_b:
            raise TriangleError
        
        return 'isosceles'
    else:
        return 'scalene'


# Error class used in part 2.  No need to change this code.
class TriangleError(StandardError):
    pass
