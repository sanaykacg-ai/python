# Take input from user
rows = int(input("Please Enter the total Number of Rows: "))
number = 1 # Initialise by 1

print("Floyd's Triangle")
# Outer loop for number of rows
for i in range(1, rows + 1):
    # Inner loop for number of columns
    for j in range(1, i + 1):
        # DIsplay result
        print(number, end = '  ')
        number = number + 1
    print()