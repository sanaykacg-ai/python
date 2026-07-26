t1 = 109
t2 = 122
t3 = 86
t4 = 124
t5 = 78

total = t1 + t2 + t3 + t4 + t5
average = total / 5

print("Total points among teams:", total, "points")
print("Average points among teams:", average, "points")

points_per_box = 5
overall = total * points_per_box
print("Overall points from boxes:", overall, "points")

boxes = total // 10
leftover = total % 10

print("Boxes filled:", boxes, "boxes")
print("Stars leftover:", leftover, "stars")

last_year = 450
print("Did we get more points than last year?:", total > last_year)
print("Did we get the same points as last year?:", total == last_year)
print("Did we get at least last year's score?:", total >= last_year)

total += 25
print("After 5 participation points for each team were added:", total, "points")

total -= 10
print("After 2 penalty points from each team were deducted:", total, "points")

total *= 3
print("Individual points counted between students from each team:", total, "points")

total /= 5
print("Individual points given to classes participating as a team:", total, "points")

boxes = total // 10
print("Final boxes filled with stars:", boxes, "boxes")