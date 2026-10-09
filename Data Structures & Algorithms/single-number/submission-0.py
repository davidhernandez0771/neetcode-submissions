class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        #XOR if the bits are diff = 1

        r = 0

        for num in nums:
            r = num ^ r
        return r

