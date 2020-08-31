class Solution:
    def decodeString(self, s: str) -> str:
        # Next index in s to be decoded
        self.i = 0
        # Decode each character in the string
        # Then join and return the results
        return "".join(self.decode(s))
    
    def decode(self, s):
        # Create a list for the result
        result = []
        nums = "0123456789"
        
        # Loop through each character in the string,
        # breaking at the end of the string (ending bracket)
        while self.i < len(s) and s[self.i] != "]":
            # Loop through the letters
            if s[self.i] not in nums:
                # Append the letter to the result
                result.append(s[self.i])
                # Increment the index
                self.i += 1
            else:
                # Track the repeats
                repeats = 0
                
                # Loop through the numbers
                while s[self.i] in nums:
                    # Calculate the number of repetitions
                    repeats = repeats * 10 + int(s[self.i])
                    # Increment the index
                    self.i += 1
                    
                # Skip over the first bracket
                self.i += 1
                # Recursively decode each character inside the brackets,
                # then store in result list
                result += (self.decode(s) * repeats)
                # Skip over the ending bracket
                self.i += 1
                
        # Return the decoded string
        return result