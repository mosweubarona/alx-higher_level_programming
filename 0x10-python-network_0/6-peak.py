#!/usr/bin/python3
"""find-peak function"""


def find_peak(list_of_integers):
    """find a peak in a list of unsorted integers."""
    TheList = list_of_integers
    le = len(TheList)
    if le == 0:
        return
    x = le // 2
    if (x == le - 1 or TheList[x] >= TheList[x + 1]) and
    (x == 0 or TheList[x] >= TheList[x - 1]):
        return TheList[x]
    if x != le - 1 and TheList[x + 1] > TheList[x]:
        return find_peak(TheList[x + 1:])
    return find_peak(TheList[:m])
