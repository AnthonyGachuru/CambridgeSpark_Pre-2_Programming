# BUSINESS INTELLIGENCE #
#
# DO NOT MODIFY CONSTANTS
DEVELOPMENT_COST = 1000
MANUFACTURING_COST_PER_UNIT = 20


def minimum_profitable_volume(sell_price):
    """
    This function computes the minimum number of units that need to be
    manufactured and sold in order for the process to be profitable. That is,
    given a selling price (as argument), find how many units need to be built
    and sold in order for the development and manufacturing cost to be
    entirely covered by sales.

    E.g., minimum_profitable_volume(1020) is 1
    E.g., minimum_profitable_volume(1019) is 2
    E.g., minimum_profitable_volume(600) is 2
    E.g., minimum_profitable_volume(30) is 100
    E.g., minimum_profitable_volume(21) is 1000

    :param sell_price: price each unit is sold at
    :return: number of units that need to be made and sold
    :rtype: float | int
    """
    import math
    if sell_price == 20:
        raise ValueError(f"Your sell price cannot be equal to {MANUFACTURING_COST_PER_UNIT}!")
    else:
        min_unit = math.ceil(DEVELOPMENT_COST / (sell_price - MANUFACTURING_COST_PER_UNIT))
    return min_unit


# if __name__ == '__main__':
#     print(minimum_profitable_volume(1020))
    # print(minimum_profitable_volume(1019))
    # print(minimum_profitable_volume(600))
    # print(minimum_profitable_volume(30))
    # print(minimum_profitable_volume(21))
