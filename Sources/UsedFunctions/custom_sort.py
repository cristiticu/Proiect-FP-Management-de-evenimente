import copy
from UsedFunctions.day_calculator import daysNumber
from UsedFunctions.day_calculator import timeNumber

def compareEvent(event, otherEvent, key1=lambda k: daysNumber(k.extractEvent().getDate()), key2=lambda k: timeNumber(k.extractEvent().getTime())):
    if key1(event) > key1(otherEvent):
        return True
    elif key1(event) < key1(otherEvent):
        return False
    else:
        if key2(event) > key2(otherEvent):
            return True
        elif key2(event) < key2(otherEvent):
            return False

def customSortedBubble(iterable, key=lambda k: k, reverse=False, cmp=lambda x, y: x > y):
    """
    Custom sort function using a bubble sort implementation
    :param iterable: A list of objects
    :param key: The key to use when comparing
    :param reverse: If the list should be sorted in reverse order
    :param cmp: A sort function
    :return: A sorted list
    """
    iterableCopy = copy.deepcopy(iterable)
    keepSort = True
    while keepSort:
        keepSort = False
        for i in range(len(iterableCopy) - 1):
            if cmp(key(iterableCopy[i]), key(iterableCopy[i+1])):
                keepSort = True
                iterableCopy[i], iterableCopy[i+1] = iterableCopy[i+1], iterableCopy[i]
    if reverse:
        iterableCopy.reverse()
    return iterableCopy

def customSortedShell(iterable, key = lambda k: k, reverse=False, cmp=lambda x, y: x > y):
    """
        Custom sort function using a shell sort implementation
        :param iterable: A list of objects
        :param key: The key to use when comparing
        :param reverse: If the list should be sorted in reverse order
        :param cmp: A sort function
        :return: A sorted list
        """
    iterableCopy = copy.deepcopy(iterable)
    shellGaps = [701, 301, 132, 57, 23, 10, 4, 1] #Marcin Ciura Sequence

    for gap in shellGaps:
        for i in range(len(iterableCopy)):
            temporaryCopy = iterableCopy[i]
            j = i
            while j >= gap and cmp(key(iterableCopy[j - gap]), key(temporaryCopy)):
                iterableCopy[j] = iterableCopy[j - gap]
                j -= gap
            iterableCopy[j] = temporaryCopy
    if reverse:
        iterableCopy.reverse()
    return iterableCopy

def customSortedWrapper(iterable, function="Shell", key=lambda k: k, reverse=False, cmp=lambda x, y: x > y):
    if function == "Shell":
        return customSortedShell(iterable, key, reverse, cmp)
    else:
        return customSortedBubble(iterable, key, reverse, cmp)
