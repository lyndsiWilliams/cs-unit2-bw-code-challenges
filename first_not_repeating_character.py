def first_not_repeating_character(s):
    # Create a list to hold the characters
    nr_chars = []
    # Create a dict to hold the count
    count = {}
    
    # Loop through the string
    for i in s:
        # If the letter is already in the dict
        if i in count:
            # Increment the count
            count[i] += 1
        # Otherwise, this is the first occurrence
        else:
            # Start the count
            count[i] = 1
            # Append the letter
            nr_chars.append(i)
            
    # Loop through the character list
    for i in nr_chars:
        # If the count is 1
        if count[i] == 1:
            # Return it. This should return the first occurrence of a non-repeating character
            return i
    
    # If the code reaches here, there are no repeating characters
    return '_'
