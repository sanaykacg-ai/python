total = 6
original = total
print(f"You have {original} subjects of homework to do today!\n")

completed = 0
hw_num = 1

while hw_num <= total:
    if hw_num == 1:
        next = "Do your maths homework"
    elif hw_num == 2:
        next = "Do your english essay"
    elif hw_num == 3:
        next = "Do your humanities project"
    elif hw_num == 4:
        next = "Do you science homework"
    elif hw_num == 5:
        next = "Do your computer science project"
    else: next = "Do your music project"

    answer = input(f"Have you finished: {next} (yes/no): ")

    if answer == "yes":
        completed += 1
        hw_num += 1
        print("Great job! Homework done.")
    else:
        print("Finish your homework and come back after.")

    print("Homework remaining:", total - completed)
    print()

print("===== HOMEWORK COMPLETE! =====")
print("Great work finishing all your homework today!\n")

print("Infinite loop")
test = 0
safety = 0
while test <= 0:
    print("A never changing statement, meaning this will go on forever")
    safety += 1
    if safety == 3:
        print("This stops on purpose, but a real infinite loop would never stop on its own")
        break
print("\n===== HOMEWORK CHECKLIST SUMMARY =====")
print("Homework Assigned:", original)
print("Homework Completed:", completed)
print("Homework Remaining", total - completed)
print("======================================")