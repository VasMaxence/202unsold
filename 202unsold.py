#!/usr/bin/env python3

import os, sys
from math import *


def usage():
    print("USAGE")
    print("    ./202unsold a b\n")
    print("DESCRIPTION")
    print("    a    constant computed from the past results")
    print("    b    constant computed from the past results")


def calculForTab(x, y):
    dividend = (a - x) * (b - y)
    divider = ((5 * a) - 150) * ((5 * b) - 150)
    return dividend / divider


def calculRow(Y):
    X = 10
    tuple = []
    calc = 0.000

    while X < a:
        tuple.append(calculForTab(X, Y))
        X += 10
    for i in range(len(tuple)):
        calc += tuple[i]
    tuple.append(calc)
    return tuple


def printRow(tuple):
    for i in range(len(tuple)):
        print("%.3f\t" % tuple[i], end='')


def calculLawByArrayTuple(tabTuple):
    tuple = []

    for i in range(len(tabTuple)):
        result = tabTuple[0][i] + tabTuple[1][i] + tabTuple[2][i] + tabTuple[3][i] + tabTuple[4][i]
        tuple.append(result)
    return tuple


def manageTab():
    print("\tX=10\tX=20\tX=30\tX=40\tX=50\tY law")
    tabTuple = [calculRow(10), calculRow(20), calculRow(30), calculRow(40), calculRow(50)]
    X_law = calculLawByArrayTuple(tabTuple)
    print("Y=10", end='\t')
    printRow(tabTuple[0])
    print("\nY=20", end='\t')
    printRow(tabTuple[1])
    print("\nY=30", end='\t')
    printRow(tabTuple[2])
    print("\nY=40", end='\t')
    printRow(tabTuple[3])
    print("\nY=50", end='\t')
    printRow(tabTuple[4])
    print("\nX law", end='\t')
    printRow(X_law)
    return tabTuple


def manageZ(tuple):
    total = 0.00
    result = [tuple[0][0],
              tuple[1][0] + tuple[0][1],
              tuple[2][0] + tuple[0][2] + tuple[1][1],
              tuple[3][0] + tuple[0][3] + tuple[1][2] + tuple[2][1],
              tuple[4][0] + tuple[0][4] + tuple[1][3] + tuple[3][1] + tuple[2][2],
              tuple[4][1] + tuple[1][4] + tuple[2][3] + tuple[3][2],
              tuple[4][2] + tuple[2][4] + tuple[3][3],
              tuple[4][3] + tuple[3][4],
              tuple[4][4]]
    for i in range(len(result)):
        total += result[i]

    print("z\t20\t30\t40\t50\t60\t70\t80\t90\t100\ttotal")
    print("p(Z=z)", end='\t')
    printRow(result)
    print("%d" % total)


def manageEsperance():
    print("expected value of X:\t%0.1f" % total)
    print("variance of X:\t\t%0.1f" % varX)
    print("expected value of Y:\t%0.1f" % total2)
    print("variance of Y:\t\t%0.1f" % varY)
    print("expected value of Z:\t%0.1f" % (total + total2))
    print("variance of Z:\t\t%0.1f" % (varX + varY))


def main():
    print("------------------------------------------------------")
    tuple = manageTab()
    print("\n------------------------------------------------------")
    manageZ(tuple)
    print("------------------------------------------------------")
    manageEsperance()
    print("------------------------------------------------------")


def errorManagement():
    assert (ac == 2 or ac == 3), "Number of argument aren't valid"
    if ac == 2:
        assert (av[1] == "-h"), "Try : ./202unsold -h"
        usage()
    else:
        assert (0 <= int(av[1]) <= 100), "A must be between 0 and 100"
        assert (0 <= int(av[2]) <= 100), "B must be between 0 and 100"
        assert (int(av[1]) < int(av[2])), "A must be inferior than B"


if __name__ == '__main__':
    try:
        ac = len(sys.argv)
        av = sys.argv
        errorManagement()
        a = float(av[1])
        b = float(av[2])
        main()
        sys.exit(0)
    except AssertionError as error:
        sys.stderr.write(str(error))
        sys.exit(84)
