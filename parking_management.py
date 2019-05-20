# PARKING MANAGEMENT #
#
import datetime
#
# For insurance purposes, the management of an office building is required to
# maintain, at all time, an accurate list of all the vehicles in the dedicated
# parking. In addition, for billing the different companies, the office
# building management wants to record occupation of the parking at different
# times and automatically emit bills to each specific companies.
#
# You are tasked with completing the series of functions below that fill the
# need of the office building parking management. You are allowed (and
# encouraged) to create additional, intermediate functions.
#
# The main data structure that your suite of function handles is a record of
# entrances and exits. A sample is given below. It consist of a pair of lists
# of tuples. The first list gives the timestamps and license plate number of
# vehicles entering the parking, the second exiting.
#
# DO NOT MODIFY CONSTANTS
PARKING_DATA_SAMPLE = (
    [
        (datetime.datetime(2017, 12, 12, 7, 13, 44, 0), 'LR10GHT'),
        (datetime.datetime(2017, 12, 12, 7, 13, 48, 0), 'LC11FBF'),
        (datetime.datetime(2017, 12, 12, 7, 13, 59, 0), 'LR10ZPP'),
        (datetime.datetime(2017, 12, 12, 7, 15, 2, 0), 'LJ65OSN'),
        (datetime.datetime(2017, 12, 12, 7, 15, 22, 0), 'LA63EWH'),
        (datetime.datetime(2017, 12, 12, 13, 1, 42, 0), 'LC11FBF')
    ],
    [
        (datetime.datetime(2017, 12, 12, 12, 13, 1, 0), 'LC11FBF'),
        (datetime.datetime(2017, 12, 12, 16, 42, 10, 0), 'LR10ZPP'),
        (datetime.datetime(2017, 12, 12, 17, 2, 41, 0), 'LR10GHT'),
        (datetime.datetime(2017, 12, 12, 17, 2, 58, 0), 'LA63EWH'),
        (datetime.datetime(2017, 12, 12, 17, 4, 3, 0), 'LJ65OSN'),
        (datetime.datetime(2017, 12, 12, 17, 10, 21, 0), 'LC11FBF')
    ]
    )
#
# A secondary data structure includes billing information. It is a dictionary
# that maps company names to a list of registered license plates.
#
# DO NOT MODIFY CONSTANTS
COMPANY_REGISTRATIONS_SAMPLE = {
    'Shire Tobacco Inc.': ['LR10GHT', 'LA63EWH'],
    'Rohan Equestrian Equipments': [],
    'Moria Construction Hardware': ['LC11FBF', 'LS66XKE', 'LR10ZPP', 'LJ65OSN']
    }


def register_car(registration, company, plate):
    """
    Registers a new car.

    NOTE: this function should not modify the registration dictionary that is
    given, instead it should create a new dictionary.
    NOTE: this function should not introduce duplicates in the registration
    system. Specifically, if a car is already registered with the given
    company it should return an identical registration information. If the car
    is registered with a different company it should remove the first
    registration.
    NOTE: if the company is not listed in the dictionary, it should not
    introduce it. Instead it should just return an identical registration.

    E.g., register_car({'Stark Industries': ['IRNMN']}, 'Stark Industries',
                       'JARVIS')
    is {'Stark Industries': ['IRNMN', 'JARVIS']}
    E.g., register_car({'Stark Industries': ['IRNMN']}, 'Wayne Enterprises',
                       'IMBTMN')
    is {'Stark Industries': ['IRNMN']}

    :param registration: preexisting registration information
    :param company: company to register the car for
    :param plate: license plate of the car to register
    :return: new registration information dictionary with added registration
    :rtype: dict
    """

    if not company:
        raise ValueError("The company has not been provided!")
    elif not plate:
        raise ValueError("The plate has not been provided!")
    if not registration:
        return {}
        # raise ValueError("The registration has not been provided!")

    # Copy the company registration dict
    copied_registration = registration.copy()
    # Check if the plate is registered
    for k, v in copied_registration.items():
        if k == company and plate in v:
            return copied_registration
            # Check if plate registered
        elif k == company and plate not in v:
            v.append(plate)
            return copied_registration
        elif k != company and plate in v:
            # Delete the old entry
            v.remove(plate)
            # Add the new plate
            copied_registration[company] = [plate]
            return copied_registration


if __name__ == '__main__':
    new_registration = register_car({'Stark Industries': ['IRNMN', 'JARVIS'],
                                     'Wayne Enterprise': ['Batmobile']}, "Itrisso", 'JARVIS')
    print(new_registration)
    print(type(new_registration))


def occupancy(parking_data, time=None):
    """
    Computes the occupancy of the parking at a given time. If no time is
    provided, check the current occupancy.

    E.g.,
    data = ([(datetime.datetime(2017, 12, 12,  7, 13, 44, 0), 'LR10GHT')], [])
    occupancy(data, time=datetime.datetime(2017, 12, 12,  7, 13, 45, 0))
    is ['LR10GHT']
    E.g.,
    data = ([(datetime.datetime(2017, 12, 12,  7, 13, 44, 0), 'LR10GHT')], [])
    occupancy(data, time=datetime.datetime(2017, 12, 12,  7, 13, 43, 0))
    is []

    :param parking_data: tuple of list of timestamped arrival and departure
    information including license plate. See sample above.
    :param time: time (as a datetime.datetime object) at which to check for
    occupancy. If no time is provided, use now.
    :return: list of cars present in the parking at the given time.
    :rtype: list
    """
    time_entry = parking_data[0]
    time_exit = parking_data[1]
    cars_in = []
    cars_out = []
    # Make a list of cars parked
    for n in range(len(time_entry)):
        if time_entry[n][0] <= time:
            cars_in.append(time_entry[n][1])

    # Make a list of cars which have left the car park
    for i in range(len(time_exit)):
        if time_exit[i][0] <= time:
            cars_out.append(time_exit[n][1])
    updated_occupancy = [plate for plate in cars_in if plate not in cars_out]
    # print(f"Cars parked: {cars_in}\n")
    # print(f"Cars out: {cars_out}\n")
    # print(f"Occupancy: {updated_occupancy}")
    return updated_occupancy


# if __name__ == '__main__':
#     occupancy(PARKING_DATA_SAMPLE, datetime.datetime(2017, 12, 12,  12, 14, 50, 0))


def company_bill(parking_data, company_registration, company, t_start, t_end):
    """
    Computes the total, cumulated time in seconds, ignoring milliseconds, that
    cars registred with a given company stayed in the parking during the
    interval between t_start and t_end.

    E.g.,
    parking_data = (
        [(datetime.datetime(2017, 12, 12,  7, 13, 44, 0), 'LR10GHT')],
        [(datetime.datetime(2017, 12, 12,  7, 13, 45, 0), 'LR10GHT')]
    )
    company_registration = {'Shire Tobacco Inc.': ['LR10GHT']}
    company_bill(parking_data, company_registration,
                 'Shire Tobacco Inc.', …, …)
    is 1

    :param parking_data: see sample above
    :param company_registration: see sample above
    :param company: name of the company to compute billing for
    :param t_start: start of the billing interval
    :param t_end: end of the billing interval
    :return: cumulated number of seconds of car park occupancy
    :rtype: float | int
    """
    if not parking_data or parking_data == []:
        raise ValueError("Parking data is empty!")
    elif not company_registration or company_registration == {}:
        raise ValueError("Company registration is empty!")
    elif not company:
        raise ValueError("Company not provided!")
    elif not t_start:
        raise ValueError("Starting time not provided!")
    elif not t_end:
        raise ValueError("End time not provided!")

    # Sort parking_data
    parking_data = sorted(parking_data, key=lambda x: x[0])
    entries_exits = []
    # Check whether we have the right company
    for k, v in company_registration.items():
        if k == company:
            print(f"Company: {k}; Plate: {v[0]}\n")
            # Make a list of entries and exit of the car
            for n in range(len(parking_data)):
                # Check the plate
                for item in v:
                    if item in parking_data[n][0]:
                        entries_exits.append(parking_data[n][0][0])
                        updated_entries_exits = [tm for tm in entries_exits if t_start <= tm <= t_end]
                        # print(f"Updated entries-exits: {updated_entries_exits}")
                        # Calculate total seconds
                        seconds = updated_entries_exits[1].second - updated_entries_exits[0].second
                        # print(f"Seconds: {seconds}")
                        return seconds
                    else:
                        raise ValueError("The provided plate in not registered!")
        else:
            raise ValueError("The provided company does not match the registration!")
    # print(f"Entries-Exit list: {entries_exits}")
    # Make new list entries_exits with t_start t_end condition


#
# if __name__ == '__main__':
#     company_bill(parking_data=(
#         [(datetime.datetime(2017, 12, 12,  7, 13, 44, 0), 'LR10GHT')],
#         [(datetime.datetime(2017, 12, 12,  7, 13, 45, 0), 'LR10GHT')]
#     ), company_registration={'Shire Tobacco Inc.': ['LR10GHT']}, company='Shire Tobacco Inc.',
#         t_start=datetime.datetime(2017, 12, 12, 7, 0, 0, 0),
#         t_end=datetime.datetime(2017, 12, 12, 7, 20, 0, 0))
