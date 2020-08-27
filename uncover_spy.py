def uncover_spy(n, trust):
    # Create a list to hold trusted person
    trusted_person = []
    # Create a list to hold trusted partner
    trusted_partner = []
    # Create a dict to hold the trust count
    count = {}
    
    # Loop through the pairs
    for i in trust:
        # If the first person is already in the count
        if i[0] in count:
            # Increment the count
            count[i[0]] += 1
        # Otherwise, this is the first occurrence
        else:
            # Start the count
            count[i[0]] = 1
            # Add the first person to the trusted partner list
            trusted_partner.append(i[0])

        # If the second person is already in the count
        if i[1] in count:
            # Increment the count
            count[i[1]] += 1
        # Otherwise, this is the first occurrence
        else:
            # Start the count
            count[i[1]] = 1
            # Add the first person to the trusted partner list
            trusted_person.append(i[1])

    # Loop through the trusted partner list
    for i in trusted_person:
        if count[i] == 0:
            return -1
        # If the trusted person isn't in the trusted partner list
        if i not in trusted_partner:
            # They are a spy!
            return i
        # else:
        #     # Otherwise, there is no spy
        #     return -1

n = 3
trust = [[1,2], [3,4]]
uncover_spy(n, trust)