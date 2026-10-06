class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
    
        seen = set()             # my mental list, starts empty
        for n in nums:           # hear each number one at a time
            if n in seen:        # "have I heard this before?"
                return True      # yes → duplicate found
            seen.add(n)          # no → remember it
        return False             # heard everything, no repeats