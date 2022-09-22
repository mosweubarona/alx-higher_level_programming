#!/usr/bin/python3
"""find-peak function"""


def find_peak(TheList):
    """Finds a peak in TheList"""

    if TheList is None or TheList == []:
        return None
    x = 0
    z = len(TheList)
    Y = ((z - x) // 2) + x
    Y = int(Y)
    if z == 1:
        return TheList[0]
    if z == 2:
        return max(TheList)
    if TheList[Y] >= TheList[Y - 1] and\
            TheList[Y] >= TheList[Y + 1]:
        return TheList[Y]
    if Y > 0 and TheList[Y] < TheList[Y + 1]:
        return find_peak(TheList[Y:])
    if Y > 0 and TheList[Y] < TheList[Y - 1]:
        return find_peak(TheList[:Y])
