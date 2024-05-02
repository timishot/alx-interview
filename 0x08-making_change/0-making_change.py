#!/usr/bin/python3
"""Making Change Problem"""


def makeChange(coins, total):
    """ Determines the fewest number of coins
    needed to meet a given amount total"""
    if total <= 0:
        return 0

    currTotalCoins = 0
    usedCoins = 0
    coins = sorted(coins, reverse=True)
    for coin in coins:
        r = (total - currTotalCoins) // coin
        currTotalCoins += r * coin
        usedCoins += r
        if currTotalCoins == total:
            return usedCoins
    return -1
