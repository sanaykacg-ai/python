def calc_change(paid, cost):
    change = paid - cost
    return change

ticket = 15

print("===== PARKING TICKET PAYMENT HELPER =====")
print(f"Your parking ticket costs: ${ticket}")
print("Accepted coins/notes: 1, 2, 5, 10, 20, 50, 100")

total = 0
coins = 0

while True:
    coin_note = int(input("Insert a coin/note (1, 2, 5, 10, 20, 50, 100): "))

    if coin_note != 1 and coin_note != 2 and coin_note != 5 and coin_note != 10 and coin_note != 20 and coin_note != 50 and coin_note != 100:
        print("Invalid coin or note, please try again!\n")
        continue

    total += coin_note
    coins += 1
    print(f"Inserted {coin_note}. Total currently: {total}\n")

    if total >= ticket:
        print("Enough money inserted!\n")
        break

change_due = calc_change(total, ticket)

print("Printing Ticket...")

if change_due == 0:
    pass
else:
    print(f"Here's your change: ${change_due}")

print("\n===== PURCHASE SUMMARY =====")
print("Ticket Cost:", ticket, "dollars")
print("Coins Inserted:", coins, "coin(s)/note(s)")
print("Total Paid:", total, "dollars")
print("Change Given", change_due, "dollar(s)")
print("============================")
print("Thank you for paying your ticket!")