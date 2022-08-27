class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}  # value:index (mapping value to index)

        for i, n in enumerate(nums):
            diff = target-n
            if diff in map:
                return [map[diff], i]
            map[n] = i
        return
