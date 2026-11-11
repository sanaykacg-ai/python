# Function to create list of square numbers
def SquaredValues(beg, end):
    lst = []
    # Store all the values of square of numbers
    # Between given range in a list
    for i in range(beg, end):
        # append value to the list
        lst.append(i**2)

    lst_even = []
    lst_odd = []

    # Check and store odd and even squares in seperate lists
    for i in lst:
        if i % 2 == 0:
            # Append value to the list
            lst_even.append(i)
        else:
            # Append value to the list
            lst_odd.append(i)

    print("Here's a list of even squares within specified range", lst_even)
    print("Here's a list of odd squares within the specified range", lst_odd)

# Take input from user for range of numbers
beg = int(input("Enter starting range: "))
end = int(input("Enter end range: "))
# Function call
SquaredValues(beg, end)