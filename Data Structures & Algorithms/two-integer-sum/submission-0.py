class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {} # Creates dictionary
        n = len(nums) # Makes n the length of the list nums

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement],i]
            numMap[nums[i]] = i # Put key 3, with index 0, i never changes, nums[i] gets the number ofc
            #numsMap == store a key
        return []