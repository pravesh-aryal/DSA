def selectionSort(array):
    sortedArray = []
    """
    If heap / priority  queue was used, TC would be O(nlogn) 
    because min operation takes log(n) instead of O(n)
    
    """
    for i in range(0, len(array)):
        sortedArray.append(min(array))
        array.remove(min(array))

    print(sortedArray)

selectionSort([3, 1, 5, 0, 2])