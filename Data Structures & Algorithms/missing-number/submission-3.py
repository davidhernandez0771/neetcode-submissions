class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        

        result = 0                      # empty bag
        n = len(nums)                   # how many numbers we have, so the range is 0..n

        for i in range(n + 1):          # add every number that SHOULD exist (0..n)
            result ^= i

        for num in nums:                # add every number that DOES exist
            result ^= num               # present numbers now appear twice → cancel (x ^ x = 0)

        return result                   # only the missing number appeared once → it's left