# array = [53, 61, 74, 85, 97, 12, 19, 27 , 34, 46]
array = [4, 5, 6, 7, 0, 1, 2, 3, 3.5]
#i have to find the cutoff index from where two arrays are divided into

target = 0

low, high = 0, len(array) - 1

while (low <= high):
    mid = (low+high) // 2
    print(low, mid, high)

    if (array[mid] == target):
        print("Element found ", array.index(target))
        break

    elif (array[mid] > target):
        if (array[low] > target):
            low = mid+1
        elif (array[low] == target):
            print("Element found ", array.index(target))
            break
        else:
            low = low + 1

    else:
        if (array[low] > target):
            low = mid + 1
        elif (array[low] == target):
            print ("Element found ", array.index(target))
            break
        else:
            high = high - 1