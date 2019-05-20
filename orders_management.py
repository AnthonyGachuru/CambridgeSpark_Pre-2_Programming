# ORDER AND CART MANAGEMENT #
#
# Orders are list of ordered items
# An order item has four components:
# - a name
# - a quantity (the number of such items bought)
# - a price (in pence)
# - a weight (in pounds)
#
# DO NOT MODIFY CONSTANTS
ORDER_SAMPLE_1 = [
    ("Lamp", 2, 2399, 2),
    ("Chair", 4, 3199, 10),
    ("Table", 1, 5599, 85)
    ]

ORDER_SAMPLE_2 = [
    ("Sofa", 1, 18399, 140),
    ("Bookshelf", 2, 4799, 40)
    ]

CATALOGUE = [
    ('table', 9999, 20),
    ('chair', 2999, 5),
    ('lamp', 1999, 10)
]


def delivery_charges(order):
    """
    Compute the delivery charges for an order. The company charges a flat £50
    fee plus £20 for each 100lbs (additional weight under 100lbs is ignored).

    E.g., delivery_charges([("Desk", 1, 11999, 160)]) is 7000 (pence)
    E.g., delivery_charges([("Desk", 2, 11999, 160)]) is 11000 (pence)
    E.g., delivery_charges([("Lamp", 1, 2399, 2)]) is 5000 (pence)
    E.g., delivery_charges([("Lamp", 50, 2399, 2)]) is 7000 (pence)

    :param order: order to process. See samples for examples.
    :return: delivery fee in pence
    :rtype: float | int
    """
    if not order:
        raise ValueError("The order is empty!")
    else:
        import math
        delivery_fee = []
        # CALCULATION IS WRONG WHEN COMPARED WITH K.A.T.E
        for n in range(len(order)):
            units = order[n][1]
            weight = math.floor(order[n][3] * units / 100)
            delivery_fee.append(100 * (50 + 20 * weight))
        delivery_fee = sum(delivery_fee)
        return delivery_fee


# if __name__ == '__main__':
#     print(delivery_charges([("Desk", 1, 11999, 160),
#                             ("Desk", 2, 11999, 160),
#                             ("Lamp", 1, 2399, 2),
#                             ("Lamp", 50, 2399, 2),
#                             ]))


def total_charge(order):
    """
    Compute the total charge for an order. It includes:
        - total price of items,
        - VAT (20% of the price of items),
        - delivery fee

    NOTE: in this computation, VAT is not applied to the delivery

    E.g., total_charge([("Desk", 2, 11999, 160)]) is 39797 (pence)
    E.g., total_charge([("Lamp", 50, 2399, 2)]) is 150940 (pence)

    Hint: Look up the built-in Python function round().

    :param order: order to process. See samples.
    :return: total price, in pence, rounded to the nearest penny.
    :rtype: float | int
    """
    if not order:
        raise ValueError("The order is empty!")
    else:
        price = []
        for n in range(len(order)):
            # Calculate price of each item
            nb_units = order[n][1]
            price_novat = order[n][2] * nb_units
            price_withvat = price_novat + price_novat * 0.2
            price.append(price_withvat)
        # Calculate delivery fees
        delivery_fee = delivery_charges(order)
        total = sum(price) + delivery_fee
    return total


def add_item_to_order(name, quantity, order):
    """
    When a customer adds items to their basket, you need to update their
    order. The customer provides some of the details (the name of the item and
    the quantity they want); the CATALOGUE contains additional details (price
    and weight).

    NOTE: you must return a new order list and leave the argument unmodified.

    NOTE: if the order already contains some of the item, you must update the
    quantity field for that item; otherwise, you must add a new entry in the
    order

    NOTE: if the item cannot be found in the order or the catalogue, the function
    should return the original order.

    E.g., add_item_to_order("table", 1, [("table", 1, 9999, 20)]) is
    [("table", 2, 9999, 20)]
    E.g., add_item_to_order("chair", 1, [("table", 1, 9999, 20)]) is
    [("table", 1, 9999, 20), ("chair", 1, 2999, 5)]

    :param name: name of the item to add
    :param quantity: number of items to add
    :param order: previous order
    :return: a new order with the added items. If the item is unknown, return
    None instead.
    :rtype: list | NoneType
    """
    # Check if the item is in the order
    # If the item is in the order, add quantity to the order quantity
    # if name in order[0]:
    #     order[0][1] += quantity
    #     return order
#
#     Transform nested tuples into nested lists
    catalogue = [list(CATALOGUE[n]) for n in range(len(CATALOGUE))]
    order = [list(order[n]) for n in range(len(order))]
#     Capitalize the first letter of 'name'
    name = name.capitalize()
#     Capitalise first letter of each word
    for n in range(len(catalogue)):
        catalogue[n][0] = catalogue[n][0].capitalize()
#     Sort nested list
    import operator
    catalogue = sorted(catalogue, key=operator.itemgetter(0))
    order = sorted(order, key=operator.itemgetter(0))

#     Add item to order
    for n in range(len(order)):
        if name in order[n]:
            print(name)
            order[n][1] += quantity
            print(order[n][1])
#             print(order[n])
        elif name in catalogue[n] and name not in order[n]:
            order.append(catalogue[n])
            order[len(order) - 1].insert(1, quantity)
        else:
            pass
    return order


name = "table"
quantity = 1
order = [("table", 1, 9999, 20)]

if __name__ == '__main__':
    print(add_item_to_order(name, quantity, order))
