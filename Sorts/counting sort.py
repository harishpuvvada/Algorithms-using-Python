
'''
Create a function that takes in a list of unsorted prices (integers) and a maximum possible price value, and return a sorted list of prices.

Note : Counting sort works well when you know the range of the values in the list.

'''


def solution(unsorted_prices,max_price):

    # list of 0s at indices 0 to max_price
    prices_to_counts = [0]* (max_price+1)

    # populate prices
    for price in unsorted_prices:
        prices_to_counts[price] +=1

    # populate final sorted prices
    sorted_prices = []

    # For each price in prices_to_counts
    for price,count in enumerate(prices_to_counts):

        # for the number of times the element occurs
        for time in range(count):

            # add it to the sorted price list
            sorted_prices.append(price)

            print()

    return sorted_prices
