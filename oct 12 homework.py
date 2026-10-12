def bill(total, people):
    return total / people

def seating(people):
    '''This function calculates seating arrangements'''

    if people == 0 or people == 1:
        return 1
    else:
        return people * seating(people - 1)
    
print(seating.__doc__)
print("Bill per person:", bill(100, 4))
print("Seating arrangements:", seating(3))