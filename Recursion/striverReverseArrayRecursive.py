arr = [0, 1, 2, 3, 4]

# two pointer approach

def reverse(arr):
    l, r = 0, len(arr)-1

    while l < r:
        temp = arr[r]
        arr[r] = arr[l]
        arr[l] = temp
        l += 1
        r -= 1
    print(arr)

reverse(arr)
