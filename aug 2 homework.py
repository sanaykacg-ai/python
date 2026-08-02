sport = input("What sport do you like?: ")

temperature = int(input("Enter the temperature today in Celsius: "))

rain = input("Is it raining today? (yes/no): ")

if rain == "yes":
    side = "inside"
    print("It is raining")
    print("Stay", side)
else:
    if temperature < 10:
        side = "inside"
        print("It is cold today")
        print("Stay", side)
    else:
        side = "outside"
        print("It is warm today")
        print("Go", side, "and play", sport)

homework = input("Do you have homework? (yes/no): ")

if homework == "yes":
    second = " your homework"
    print("Do", second)
else:
    second = "videogames"
    print("Play", second)

hungry = input("Are you hungry? (yes/no): ")

if hungry == "yes":
    third = "eat dinner"
    print("Eat dinner")
else:
    third = "play games longer"
    print("Play games longer")

tired = input("Are you tired? (yes/no): ")

if tired == "yes":
    fourth = "to sleep"
    print("Go to sleep")
else:
    fourth = "read, sleep in 1/2 hour"
    print("Read a book")

print("")
print("Daily Routine complete!")

print("===== DAILY ROUTINE =====")
print("1st: Go", side)
print("2nd: Do", second)
print("3rd: Go", third)
print("4th: Go", fourth)
print("=========================")