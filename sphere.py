#!/usr/bin/env python3
import sys
import tool

def sphere():
    if (float(sys.argv[8]) == 0):
        sys.exit(84)
    a = (float(sys.argv[5])*float(sys.argv[5]) + float(sys.argv[6])*float(sys.argv[6]) + float(sys.argv[7])*float(sys.argv[7]))
    b = (2 * (float(sys.argv[2])*float(sys.argv[5]) + float(sys.argv[3])*float(sys.argv[6]) + float(sys.argv[4])*float(sys.argv[7])))
    c = (float(sys.argv[2])*float(sys.argv[2]) + float(sys.argv[3])*float(sys.argv[3]) + float(sys.argv[4])*float(sys.argv[4])) - (float(sys.argv[8]) * float(sys.argv[8]))
    if (a == 0):
        sys.exit(84)
    delta = ((b * b) - (4 * a * c))
    x = tool.coordinates
    x1  = tool.coordinates
    x2 = tool.coordinates

    print("Sphere of radius", sys.argv[8])
    print("Line passing through the point ({}, {}, {})" .format(sys.argv[2], sys.argv[3], sys.argv[4]), end= ' ')
    print("and parallel to the vector ({}, {}, {})" .format(sys.argv[5], sys.argv[6], sys.argv[7]))

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
