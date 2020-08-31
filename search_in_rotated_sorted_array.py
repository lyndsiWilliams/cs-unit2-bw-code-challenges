class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Binary Search Tree
        # Initialize the left and right sides
        left = 0
        right = len(nums) - 1
        
        # Start BST traversal
        while left <= right:
            # Calculate the mid's index
            mid = (left + right) // 2
            
            # If the value at mid is the target, return it
            if nums[mid] == target:
                return mid
            
            # Search the left side
            if nums[left] <= nums[mid]:
                # If the target is between the value of
                # left and mid
                if target >= nums[left] and target < nums[mid]:
                    # Cut the right side in half
                    right = mid - 1
                # Otherwise, the target is between the value
                # of right and mid
                else:
                    # Cut the left side in half
                    left = mid + 1
            # Search the right side
            else:
                # If the target is between the value of
                # right and mid
                if target <= nums[right] and target > nums[mid]:
                    # Cut the left side in half
                    left = mid + 1
                # Otherwise, the target is between the value
                # of left and mid
                else:
                    # Cut the right side in half
                    right = mid - 1
                    
        # If the code reaches this point,
        # the value is not in the parameter list
        return -1