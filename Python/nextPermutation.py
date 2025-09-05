#permutation = in how many ways you can arrange n items 
#next permutation is always > than before, if it is largest of the possible we get back to where we started
#3, 2, 1 will produce 1, 2, 3


def nextPermutation(nums):
    pivot_index = -1
    end = len(nums)
    i = end - 1
    while i > 0:
        if nums[i-1] < nums[i]:
            pivot_index = i-1
            break
        i = i - 1

    if pivot_index == -1:
        nums.reverse()
        return nums
    
    i = end - 1
    while i > pivot_index:
        if nums[pivot_index] < nums[i]:
            nums[pivot_index], nums[i] = nums[i], nums[pivot_index]
            break
        i = i-1

    nums[pivot_index+1:] = reversed(nums[pivot_index+1:])
    print(nums)
    



nums = [1, 5, 4, 9, 8, 7, 6, 1]
# nums = [1, 2, 3, 4]
# nums = [1, 0, 6, 8, 5]
nextPermutation(nums)



