#!/usr/bin/python

import argparse


def find_max_profit(prices):
    maximum = max(prices)
    minimum = maximum
    count = len(prices) - 1
    profits = []
    if prices.index(maximum) == 0:
        while count > 0:
            profits.append(prices[count] - prices[count - 1])
            count -= 1

        return max(profits)
    else:
        for i in range(prices.index(maximum)):
            if prices[i] < minimum:
                minimum = prices[i]
        return maximum - minimum


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
