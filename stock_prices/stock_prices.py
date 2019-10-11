#!/usr/bin/python

import argparse

stock_prices = [1050, 270, 1540, 3800, 2]
def find_max_profit(prices):
    elements = len(prices)
    profits = [0] * elements
    sorted_prices = []
    smallest_so_far = 1000000000
    for index, p in enumerate(prices):
        if p < smallest_so_far and index > 0:
          smallest_so_far = p
          print(f"new smallest = {p} at index {index}")





print(find_max_profit(stock_prices))


#
# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()
#
#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))