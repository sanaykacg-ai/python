num = int(input("Enter the number of which you have to find the power: "))
pw = int(input("Enter the power: "))
g = 1
for n in range(pw):
    g = g*num
print(g)