def uncover_spy(n, trust):
    # Create a list to hold trusted person
    trusted_person = []
    # Create a list to hold trusted partner
    trusted_partner = []
    
    # Loop through the pairs
    for i in trust:
        # Add the first person to the trusted partner list
        trusted_partner.append(i[0])
        # Add the second person to the trusted person list
        trusted_person.append(i[1])

    # Loop through the trusted partner list
    for i in trusted_person:
        # If the trusted person isn't in the trusted partner list
        if i not in trusted_partner:
            # They are a spy!
            return i
        else:
            # Otherwise, there is no spy
            return -1

n = 4
trust = [[1,2], [3,4]]
uncover_spy(n, trust)

# trusted by = length(n) - 1 
# Spy trusts nobody