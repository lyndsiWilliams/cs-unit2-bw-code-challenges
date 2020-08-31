class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Create a dict to hold the seen numbers
        seen = {}
        # Create a variable to hold the duplicate number
        dupe = 0

        # Loop through the parameter numbers
        for i in nums:
            # If the number hasn't been seen yet
            if i not in seen:
                # Start it's count in the seen dict
                seen[i] = 1
            # Otherwise, this number has been seen before
            else:
                if seen[i] == 1:
                    # Store this number as a duplicate
                    dupe += i
                # Increase the seen count
                seen[i] += 1
        
        # Return the duplicate number
        return dupe