array = [3, 1, 2]
length = len(array)

#print all subsequences
def printAllSubsequences(index, result, length):
    if index >= length:
        print(result)
        return
    
    #choose the current index ell to proceed i.e left recursion 
    result.append(array[index])
    index += 1
    printAllSubsequences(index, result, length)
    #not choosing the current index ell to proceed i.e right recrusion
    result.pop() #need to pop the last ell because it was added above i.e to not choose it
    printAllSubsequences(index, result, length)

index = 0
result = []
printAllSubsequences(index, result, length)

"""
Time Complexity: O(n * 2^n) #generating 2^n subsequences (binary tree) each in O(n) time because of print call
Space Complexity: O(n) #auxiliary stack space (call stack)
"""