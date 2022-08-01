#!/usr/bin/env python3
import math
import sys
import tool

def cylinder():
    xp = float(sys.argv[2])
    yp = float(sys.argv[3])
    zp = float(sys.argv[4])
    xv = float(sys.argv[5])
    yv = float(sys.argv[6])
    zv = float(sys.argv[7])
    p = float(sys.argv[8])

    a = math.pow(xv,2) + math.pow(yv,2)
    b = 2 * xp * xv + 2 * yp * yv
    c = math.pow(xp,2) + math.pow(yp,2) - math.pow(p,2)
    if (a == 0 and zv == 0):
        sys.exit(84)
    delta = ((b * b) - (4 * a * c))
    x = tool.coordinates
    x1  = tool.coordinates
    x2 = tool.coordinates

    print("Cylinder of radius", sys.argv[8])
    print("Line passing through the point ({}, {}, {})" .format(sys.argv[2], sys.argv[3], sys.argv[4]), end= ' ')
    print("and parallel to the vector ({}, {}, {})" .format(sys.argv[5], sys.argv[6], sys.argv[7]))
    
    if (c == 0):
        print("There is an infinite number of intersection points.")
        sys.exit(0)
    if (delta < 0):
        print("No intersection point.")
    if (delta == 0):
        print("1 intersection point:")
        x = tool.equation(tool.one_sol(a, b))
        print("({:.3f}, {:.3f}, {:.3f})" .format(x.x, x.y, x.z))
    if (delta > 0):
        print("2 intersection points:")
        x1 = tool.equation(tool.sol_1(a, b, delta))
        x2 = tool.equation(tool.sol_2(a, b, delta))
        print("({:.3f}, {:.3f}, {:.3f})" .format(x1.x, x1.y, x1.z))
        print("({:.3f}, {:.3f}, {:.3f})" .format(x2.x, x2.y, x2.z))
