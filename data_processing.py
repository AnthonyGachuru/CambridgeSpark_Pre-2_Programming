# DATA PROCESSING #
#
# DO NOT MODIFY CONSTANTS
PRICES_PER_HOUR_PER_DAY_SAMPLE = [
    [11300, 12000, 12100, 12100, 11800, 11100, 10300, 9400],
    [10100, 10300, 10200, 10300, 10200, 10100, 10200, 10200],
    [10600, 10700, 10100, 10000, 9800, 8400, 7500, 9000],
    [9100, 9600, 10200, 10200, 10200, 10300, 10100, 10400],
    [10500, 10600, 13200, 10800, 10500, 10200, 9900, 9800]
    ]


def normalize_prices(prices):
    """
    This function takes an observation of prices of some commodity for
    business hours during the days of the week (represented as a list (for
    different days) of list (for different hours) of numbers (for the prices).
    It normalises the prices so the first value is worth 100.

    E.g., normalize_prices([[1, 2], [3, 4]]) is [[100, 200], [300, 400]]
    E.g., normalize_prices([[200, 20], [30, 400]]) is [[100, 10], [15, 200]]

    :param prices: list of list of prices
    :return: normalised list of list of prices where the first price is 100
    and the other prices are scaled accordingly
    :rtype: list
    """
    # TRANSFORM ONLY FIRST ELEMENT OF EACH LIST!!!
    normalised_prices = [[int(item * (100 / prices[0][0])) for item in prices[n]] for n in range(len(prices))]
    # normalised_prices = [int(item) for item in normalised_prices]
    return normalised_prices


def flip_prices(prices):
    """
    This function returns a list of daily prices for each observed hour given
    a list of hourly prices for each observed day.

    E.g., flip_prices([[1, 2, 3], [4, 5, 6]]) is [[1, 4], [2, 5], [3, 6]]

    :param prices: list (for days) of list (for hours) of prices
    :return: list (for hours) of list (for days) of prices
    :rtype: list
    """
    # First nested list
    first_nested_list = prices[0]
    # Get length first nested list
    length_nested_list = len(first_nested_list)
    # Make flipped list
    flipped = [[item[n] for item in prices] for n in range(length_nested_list)]
    return flipped



# if __name__ == '__main__':
    # normalised_price = normalize_prices(PRICES_PER_HOUR_PER_DAY_SAMPLE)
    # print(f"Normalised prices: {normalised_price}")
    # flipped_prices = flip_prices([[1, 2, 3], [4, 5, 6]])
    # print(f"Flipped prices: {flipped_prices}")
    # print(flip_prices([[1, 2, 3],
    #              [4, 5, 6],
    #              [7, 8, 9]]))


