# Using try and except
try:
    number = int(input("Enter a number: "))
    print("The number entered is:", number)
# Using Value Errors
except ValueError as ex:
    print("Exception:", ex)
