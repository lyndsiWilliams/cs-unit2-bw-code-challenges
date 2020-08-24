class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # If every number is unique then the set length will be the same as the list length
        # If it's a different length, then there is a duplicate.
        return len(set(nums)) != len(nums)