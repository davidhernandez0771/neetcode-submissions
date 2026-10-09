class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        

        r = 0
        n = len(nums)
        for i in range(n+1):
            r ^= i
        
        for num in nums:
            r ^= num
        return r