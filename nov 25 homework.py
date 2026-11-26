test_dict = {'Sanay' : 3, 'wrote' : 2, 'this' : 4, 'code' : 2, 'very' : 1, 'well' : 3}
print("The Original Dictionary:" + str(test_dict))
K = int(input("Enter the number you would like to check the frequency for: "))
res = 0
for key in test_dict:
    if test_dict[key] == K:
        res = res + 1
print("Frequency of K is: " + str(res))