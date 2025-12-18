from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCountMap = defaultdict(int)
        for num in nums:
            numCountMap[num] += 1

        
        array = [[] for i in range(len(nums)+1)]
        #array index corresponds to count, value corresponds to elements having that count
        for key, value in numCountMap.items():
            array[value].append(key)

        result = []
        for i in range(len(array)-1, 0, -1):
            for num in array[i]:
                result.append(num)
                if len(result) == k:
                    return result