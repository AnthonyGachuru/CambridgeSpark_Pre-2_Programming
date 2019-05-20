# TRANSACTIONS ANALYSIS #
#
import datetime
#
# DO NOT MODIFY CONSTANTS
TRANSACTION_LOG_SAMPLE_1 = [
    {'name': 'SKIL', 'nature': 'buy', 'quantity': 11, 'unit-price': 442,
     'time': datetime.time(8, 22, 52, 0)},
    {'name': 'DOAA', 'nature': 'sell', 'quantity': 43, 'unit-price': 122,
     'time': datetime.time(7, 1, 10, 0)},
    {'name': 'DOAA', 'nature': 'sell', 'quantity': 2, 'unit-price': 119,
     'time': datetime.time(8, 3, 0, 0)},
    {'name': 'DOAA', 'nature': 'sell', 'quantity': 10, 'unit-price': 118,
     'time': datetime.time(8, 3, 41, 0)},
    {'name': 'DOAA', 'nature': 'sell', 'quantity': 20, 'unit-price': 116,
     'time': datetime.time(10, 8, 21, 0)},
    {'name': 'DOAA', 'nature': 'sell', 'quantity': 11, 'unit-price': 113,
     'time': datetime.time(11, 44, 14, 0)},
    {'name': 'SKIL', 'nature': 'sell', 'quantity': 8, 'unit-price': 450,
     'time': datetime.time(11, 22, 22, 0)},
    {'name': 'SKIL', 'nature': 'sell', 'quantity': 3, 'unit-price': 451,
     'time': datetime.time(11, 56, 0, 0)}
    ]


def summarize_transaction_log(transaction_log):
    """
    This function summarizes a transaction log. It should return a dictionary
    with the following fields:
    - total-volume (the total amount of money exchanged)
    - volume-per-hour (a list of amount of money exchanged per hour)
    - total-number-of-transactions
    - number-of-transaction-per-hour (also a list)

    The hour breakdowns should include one entry for each hour of the day.

    E.g., if summarize_transaction_log(TRANSACTION_LOG_SAMPLE_1) is summary
    then summary['total-number-of-transactions'] is 8
    and summary['number-of-transaction-per-hour']
    is [ …, 0, 1, 3, 0, 1, 3, 0, …]

    :param transaction_log: log of transactions. See sample.
    :return: summary as described above.
    :rtype: dict
    """

    # Create a list of hours
    hour = [n for n in range(24)]
    volume_per_hour = []
    lst_hours = []
    number_transaction_per_hour = [0] * 24
    for i in hour:
        # Get the volume of money exchanged per hour
        volume_per_hour.append(sum(item['quantity'] * item['unit-price'] for item in transaction_log if item['time'].hour == i))
        # Initiate a counter and list
        # Add every hour from dictionary into list
    for n in range(len(transaction_log)):
        lst_hours.append(transaction_log[n]['time'].hour)
    unique_hours = set(lst_hours)
    for item in unique_hours:
        number_transaction_per_hour[item] = lst_hours.count(item)

    total_vol_money_exchanged = sum(volume_per_hour)
    # Make dictionary
    summary_log = {'total-volume': total_vol_money_exchanged,
                   'volume-per-hour': volume_per_hour,
                   'total-number-of-transactions': len(transaction_log),
                   'number-of-transaction-per-hour': number_transaction_per_hour}

    return summary_log


# if __name__ == '__main__':
#     summary = summarize_transaction_log(TRANSACTION_LOG_SAMPLE_1)
#     print(summary)




