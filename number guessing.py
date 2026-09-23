secret = 38
hearts = 5

print("Guess the number! (1 - 50):")

for heart in range(5):
    while True:
        guess = int(input("Enter your guess: "))
        #Win (break while)
        if guess == secret:
            print("You got it! Number =", secret, "\n")
            break
        #Hints
        elif guess > 0 and guess < secret - 15:
            print("Hint: Ice Cold")
        elif guess >= secret - 15 and guess < secret - 10:
            print("Hint: Cold")
        elif guess >= secret - 10 and guess < 5:
            print("Hint: Warm")
        elif guess >= 5 and guess < secret:
            print("Hint: Hot")
        elif guess > secret and guess <= secret + 5:
            print("Hint: Warm")
        elif guess > secret + 5 and guess <= 48:
            print("Hint: Cold")
        elif guess > 48 and guess <= 50:
            print("Hint: Ice Cold") 
        #If value not between 1 - 50
        else:
            print("Please enter a number from 1 to 50:")
            continue
        #Minus heart    
        hearts -= 1
        print("Hearts left:", hearts)
        break
    #Win (break for)
    if guess == secret:
        break
#Loss
if hearts == 0:
    print("You lost! Number =", secret, "\n")   