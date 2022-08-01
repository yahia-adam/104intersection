#!/usr/bin/env python3
import math
import sys

class coordinates:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_z(self):
        return self.z

def equation(t):
    point = coordinates(float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]))
    vector = coordinates(float(sys.argv[5]), float(sys.argv[6]), float(sys.argv[7]))
    xl = point.x + t * vector.x
    yl = point.y + t * vector.y
    zl = point.z + t * vector.z
    l = coordinates(xl, yl, zl)
    return(l)

def one_sol(a, b):
    return (-b / (2*a))

def sol_1(a, b, delta):
    x1 = ((-b + math.sqrt(delta)) /  (2 * a))
    return(x1)

def sol_2(a, b, delta):
    x2 = ((-b - math.sqrt(delta)) /  (2 * a))
    return(x2)

