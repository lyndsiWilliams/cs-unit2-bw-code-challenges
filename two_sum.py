class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a cache
        numbers = {}
        
        # loop through list of nums
        # mapping nums to their indices
        for i, num in enumerate(nums):
            # if target - num is already cached, return it
            if target - num in numbers:
                return [numbers[target - num], i]
            # Otherwise, it's not cached yet so store it
            numbers[num] = i
        # If the loop runs and there is no sum, return empty brackets
        return []