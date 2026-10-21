class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            y = stones.pop()        # biggest, removed from the list
            x = stones.pop()        # second biggest, removed
            if x != y:
                stones.append(y - x)
        return stones[0] if stones else 0