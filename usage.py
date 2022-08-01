#!/usr/bin/env python3

def usage():
        print("USAGE")
        print("   ./104intersection opt xp yp zp xv yv zv p\n")
        print("DESCRIPTION")
        print("\topt\t\tsurface option: 1 for a sphere, 2 for a cylainder, 3 for a cone")
        print("\t(xp, yp, zp)\tcoordinates of a point by with the light ray passes throught")
        print("\t(xv, yx, zv)\tcoordinates of a vecteur parallel of the light ray")
        print("\tp\t\tparameter: radius of the sphere, radius of the cylainder or")
        print("\t\t\tangle formed by the cone and the Z-axis")
