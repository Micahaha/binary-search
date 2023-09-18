def search(a, first: int, target: int):
    """Searches part of a sorted list for a specified target starting at a[first]

    Args:
        a (int): the list to search
        first (int): the list index at which the search will start
        target (int): the element to search for

    Returns:
        int: If the target appears in the list, index of the, element 
        that contains target; else -1 
    """    

    # set a boolean variable found to false
    found = False

    # set an int variable size to list length - first
    size = len(a) - first

    # set an int variable middle to first + size / 2
    middle = int(first + size / 2)
    
    # if there are no more elements to search
    if (size <= 0):
        return -1
    else: 
        # while there are no more elements to search
        # and the target hasn't been found
        while (size > 0 and not found):
            # if value in the middle element is the target
            if (a[middle] == target):
                found = True
            elif (a[middle] > target):
                # else if the value is the middle element is
                # greater thean the target
                size = int(size / 2)
            else:
                # else if the value in the middle element is 
                # less than the target
                first = middle + 1
                size = int((size - 1) / 2)

            # recompute middle
            middle = int(first + size / 2)
    # check if the target was found 
    if(found):
        return middle
    else:
        return -1 