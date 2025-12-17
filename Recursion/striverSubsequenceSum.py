array = [1, 1, 2]
length = len(array)
targetSum = 2
#print all subsequences whose sum == targetSum or print a subsequence whose sum == targetSum
def printAllSubsequences(index, result, length, currentSum):
    if index >= length:
        if currentSum == targetSum:
            print(result)
            return True
        return False
    
    #choose the current index ell to proceed i.e left recursion 
    result.append(array[index])
    currentSum += array[index]
    index += 1
    if (printAllSubsequences(index, result, length, currentSum)):
        return True
    #not choosing the current index ell to proceed i.e right recrusion
    temp = result.pop() #need to pop the last ell because it was added above i.e to not choose it
    currentSum -= temp
    if (printAllSubsequences(index, result, length, currentSum)):
        return True
    
    return False

index = 0
result = []
currentSum = 0
printAllSubsequences(index, result, length, currentSum)

"""
Time Complexity: O(2^n) #generating 2^n subsequences (binary tree) 
Space Complexity: O(n) #auxiliary stack space (call stack)
"""