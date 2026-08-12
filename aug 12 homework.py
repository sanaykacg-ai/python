print("=== Smart Library Visit Planner ===")
print("Answer these quick questions and I will suggest a smart plan!\n")
# Questions
day = input("What day is it today? (Monday to Sunday): ").strip().capitalize()
weather = input("How is the weather today? (sunny / cloudy / rainy): ").strip().capitalize()
days = int(input("How many days have you had the book for? (in numbers): "))
read = input("Have you finished reading your book? (yes / no): ")
# Overdue Decider
if days < 14:
    book = "Not overdue"
else:
    book = "Overdue"
# Umbrella Decider
if weather == "cloudy" or weather == "rainy":
    umbrella = "yes"
elif weather == "sunny":
    umbrella = "No"
else:
    umbrella = "Please enter a correct weather (sunny / cloudy rainy) to see whether you should bring an umbrella"

if read == "yes" and book == "Not overdue":
    time = "On time with books!"
elif not (read == "yes") and not (book == "Not overdue"):
    time = "Manage time with books better"
else:
    time = "Speed up read or return times"
# Final Print
print("\n===== LIBRARY VISIT PLAN COMPLETE =====")
print("What you should do:")
if day == "Sunday":
    library = "Closed"
    if read == "yes":
        if book == "Overdue":
            print("Go outside and play, make sure to return your book and get a new one tomorrow!")
        else:
            print("Go outside and play, library is closed today, make sure to get a new book from the library tomorrow!")
    else:
        if book == "Overdue":
            print("Library is closed today so keep reading, remember to renew it tomorrow!")
        else:
            print("Relax, and enjoy reading your book!")

elif day in ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"):
    library = "Open"
    if read == "yes":
        if book == "Overdue":
            print("Return your book, and make sure to get a new one!")
        else:
            print("Go get a new book and enjoy reading it!")
    else:
        if book == "Overdue":
            print("Go renew your book, then enjoy reading it!")
        else:
            print("Relax, and enjoy reading your book!")
else:
    print("Day not specified, please check your spelling and enter a correct day to see a plan")
    library = "Please enter correct day to see library status"
    print("Library:", library)
print("Umbrella:", umbrella)
print("Book:", book)
print("Time-Management:", time)