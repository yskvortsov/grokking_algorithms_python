def binary_search(array, target) -> int:
    """
    Binary search only works when your list is in sorted order.
    :param array: sorted list or tuple
    :param target: element to search for
    :return: index of target element
    """
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = array[mid]
        if guess == target:
            return mid
        elif guess > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1
