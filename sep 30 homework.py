def greeting():
    print("\nWelcome to the Art Store!")

greeting()

item_price = float(input("Enter the cost of the item: "))
items_sold = int(input("Enter the number of items sold: "))

def calculate_total(price, items):
    total = price * items
    return total

total_cost = calculate_total(item_price, items_sold)

rounded_total = round(total_cost, 2)
print("Final Cost:", rounded_total)

paid = float(input("Enter the amount paid by the customer: "))

def calculate_change(paid, total):
    change = paid - total
    return change

change_due = calculate_change(paid, rounded_total)
rounded_change = round(change_due, 2)

def thanks(items):
    if items >= 7:
        return "What a big order! Thank you for your support!"
    else:
        return "Thank you for your purchase!"

closing = thanks(items_sold)

print("")
print("===== ART SUPPLIES RECEIPT =====")
print("Individual Item Cost:", item_price)
print("Items Sold:", items_sold)
print("Total Cost:", rounded_total)
print("Amount Paid:", paid)
print("Change Due:", rounded_change)
print(closing)
print("================================")