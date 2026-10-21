discount = 25
valid = False
while not valid:
    try:
        bill = float(input("Enter your bill amount: "))

        while bill <= 0:
            print("Bill must be greater than 0!")
            bill = float(input("\nEnter your bill amount:"))

        percentage = bill * discount / 100
        discounted = bill - percentage
    
        print("Discount:", discount, "% off")
        print("Savings:", percentage)
        print("New Bill:", discounted)
        
        valid = True

    except ValueError:
        print("Please enter a valid number")
    except ZeroDivisionError:
        print("Numbers cannot be divided by 0!")
    finally:
        print("\nThank you for using the discount calculator!")