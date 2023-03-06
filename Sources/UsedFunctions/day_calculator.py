def timeNumber(timeString):
    splitParts = timeString.split(':')
    counter = splitParts[0] * 60 + splitParts[1]
    return counter

def daysNumber(dateString):
    """
    Function for calculating number of days from year 0
    :param dateString: A date using the format: "dd.mm.yyyy"
    :return: The number of days
    """
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    num_days = 0
    day = int(dateString.split(".")[0])
    month = int(dateString.split(".")[1])
    year = int(dateString.split(".")[2])
    for y in range(year):
        if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
            num_days += 366
        else:
            num_days += 365
    for m in range(1, month):
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) and m == 2:
            num_days += 29
        else:
            num_days += days_in_month[m]
    num_days += day
    return num_days