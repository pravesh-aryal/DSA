class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        """
        {
            ell: index of ell --format of hashmap
        }
        """

        for i in range(0, len(nums)):
            diff = target - nums[i]
            if(hashmap.get(diff) is not None):
                return [i, hashmap.get(diff)]
            hashmap[nums[i]] = i
