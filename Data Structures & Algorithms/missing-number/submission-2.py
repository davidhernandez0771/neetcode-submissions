class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        

        result = 0 # We use this as the default bit of 000...
        n = len(nums) # grab the length of the list nums , 0,1,2,3...

        # first loop will be for what should be there as a regular list 0, 1, 2, 3 fully
        for i in range(n + 1): #n +1 in n = 0 is 0 since range doesnt go to the last one
            result ^= i # We XOR i, meaning the bits that are different get a 1
        
        for num in nums: # The actual list we have
            result ^= num # we do XOR again for this list, having the previous r from the other loop
                    # This makes it so that we get 0 if they are the same and 1 if diff
        
        return result