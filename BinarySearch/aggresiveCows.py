"""
You are given an array with unique elements of stalls[], which denote the positions of stalls. You are also given an integer k which denotes the number of aggressive cows. The task is to assign stalls to k cows such that the minimum distance between any two of them is the maximum possible.

Examples:

Input: stalls[] = [1, 2, 4, 8, 9], k = 3
Output: 3
Explanation: The first cow can be placed at stalls[0], 
the second cow can be placed at stalls[2] and 
the third cow can be placed at stalls[3]. 
The minimum distance between cows in this case is 3, which is the largest among all possible ways.

Input: stalls[] = [10, 1, 2, 7, 5], k = 3
Output: 4
Explanation: The first cow can be placed at stalls[0],
the second cow can be placed at stalls[1] and
the third cow can be placed at stalls[4].
The minimum distance between cows in this case is 4, which is the largest among all possible ways.

Input: stalls[] = [2, 12, 11, 3, 26, 7], k = 5
Output: 1
Explanation: There are 6 stalls and only 5 cows, we try to place the cows such that the minimum distance between any two cows is as large as possible.
The minimum distance between cows in this case is 1, which is the largest among all possible ways.
"""

# stalls = [2, 12, 11, 3, 26, 7]
# k = 5

stalls = [1, 2, 4, 8, 9]
k = 3

# stalls = [10, 1, 2, 7, 5]
# k = 3

#O(d)
# def aggresiveCows(stalls, k):
#     #first sort the stalls array
#     stalls = sorted(stalls) #TC: O(N log N)
#     #[2, 3, 7, 11, 12, 26]
#     #max possible difference in between any two stalls would be max(stalls) - min(stalls)
#     #iterate from 1 to max until we can fit k cows in the stalls, last one is the answer
    
#     #say this loop runs for d times where d is max difference
#     d = max(stalls) - min(stalls)
#     for i in range(1, d):
#         if canMaintainThisDistance(stalls, i):
#             continue
#         else:
#             return i - 1

# O(logN) optimized using Binary Search
def aggresiveCows(stalls, k):
    #first sort the stalls array
    stalls = sorted(stalls) #TC: O(N log N)
    #[2, 3, 7, 11, 12, 26]
    #max possible difference in between any two stalls would be max(stalls) - min(stalls)
    #iterate from 1 to max until we can fit k cows in the stalls, last one is the answer
    
    #say this loop runs for d times where d is max difference
    d = max(stalls) - min(stalls)
    low = 1
    high = d #say 9
    result = -1
    #[1, 2, 3, 4, 5, 6, 7, 8, 9]
    while low <= high:
        mid = (low + high) // 2 #say mid = 5
        if canMaintainThisDistance(stalls, mid):
            result = mid
            low = mid + 1
        else:
            high = mid - 1

    return result

# TC: O(N)
def canMaintainThisDistance(stalls, dist):
    countCows = 1 #sorted = [1, 2, 5, 7, 10]
    currEll = stalls[0]
    for i in range(1, len(stalls)):
        if (stalls[i] - currEll >= dist):
            countCows += 1
            currEll = stalls[i]
        else:
            continue
        
    if countCows >= k:
        return True
        
    return False

print(aggresiveCows(stalls, k))
