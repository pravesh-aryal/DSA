array = [0, 5, 9, 11, 15, 21, 44, 55, 99, 100]

#5
def binarySearch(array, number):
    low, high = 0, len(array)-1

    while (low <= high):
        mid = (low+high) // 2
        if (array[mid] == number):
            return f"Number {number} found at {array.index(number)}th index"
        elif (array[mid] < number):
            low = mid+1
        else:
            high = mid-1
            
print(binarySearch(array, 5))