print("====================================")
print("     Welcome to Holiday Planner     ")
print("====================================")
print()

print("Step 1: Pick your climate preference:")
print("  1 - Warm")
print("  2 - Cold")

ca = int(input("Enter 1 or 2: "))
print()

if ca == 1:
    print("Step 2: Pick your holiday type:")
    print("  1 - Relaxing")
    print("  2 - Adventurous")
    print("  3 - Nature")

    cba = int(input("Enter 1, 2, or 3: "))
    print()

    if cba == 1:
        print("Step 3: Pick your location:")
        print("  1 - Fiji")
        print("  2 - Bali (Indonesia)")
        print("  3 - Thailand")
        print("  4 - Rarotonga (Cook Islands)")
        
        ccaa = int(input("Enter 1, 2, 3, or 4: "))
        print()
        
        if ccaa == 1:
            print("Your location     : Fiji")
            print("Your holiday type : Relaxing")
            print("Your climate      : Warm")
        elif ccaa == 2:
            print("Your location     : Bali (Indonesia)")
            print("Your holiday type : Relaxing")
            print("Your climate      : Warm")
        elif ccaa == 3:
            print("Your location     : Thailand")
            print("Your holiday type : Relaxing")
            print("Your climate      : Warm")
        elif ccaa == 4:
            print("Your location     : Rarotonga (Cook Islands)")
            print("Your holiday type : Relaxing")
            print("Your climate      : Warm")
        else:
            print("Invalid answer, please specify '1', '2', '3', or '4'.")

    elif cba == 2:
        print("Step 3: Pick your location:")
        print("  1 - Costa Rica")
        print("  2 - Peru")
        print("  3 - Jordan")
        print("  4 - Belize")

        ccab = int(input("Enter 1, 2, 3, or 4: "))
        print()

        if ccab == 1:
            print("Your location     : Costa Rica")
            print("Your holiday type : Adventurous")
            print("Your climate      : Warm")
        elif ccab == 2:
            print("Your location     : Peru")
            print("Your holiday type : Adventurous")
            print("Your climate      : Warm")
        elif ccab == 3:
            print("Your location     : Jordan")
            print("Your holiday type : Adventurous")
            print("Your climate      : Warm")
        elif ccab == 4:
            print("Your location     : Belize")
            print("Your holiday type : Adventurous")
            print("Your climate      : Warm")
        else:
            print("Invalid answer, please specify '1', '2', '3', or '4'.")

    elif cba == 3:
        print("Step 3: Pick your location:")
        print("  1 - Tanzania")
        print("  2 - Australia")
        print("  3 - Madagascar")
        print("  4 - Philippines")

        ccac = int(input("Enter 1, 2, 3, or 4: "))
        print()

        if ccac == 1:
            print("Your location     : Tanzania")
            print("Your holiday type : Nature")
            print("Your climate      : Warm")
        elif ccac == 2:
            print("Your location     : Australia")
            print("Your holiday type : Nature")
            print("Your climate      : Warm")
        elif ccac == 3:
            print("Your location     : Madagascar")
            print("Your holiday type : Nature")
            print("Your climate      : Warm")
        elif ccac == 4:
            print("Your location     : Philippines")
            print("Your holiday type : Nature")
            print("Your climate      : Warm")
        else:
            print("Invalid answer, please specify '1', '2', '3', or '4'.")

elif ca == 2:
    print("Step 2: Pick your holiday type:")
    print("  1 - Relaxing")
    print("  2 - Adventurous")
    print("  3 - Nature")

    cbb = int(input("Enter 1, 2, or 3: "))
    print()

    if cbb == 1:
        print("Step 3: Pick your location:")
        print("  1 - Iceland")
        print("  2 - Norway")
        print("  3 - Switzerland")
        print("  4 - New Zealand")
    
        ccba = int(input("Enter 1, 2, 3, or 4: "))
        print()

        if ccba == 1:
            print("Your location     : Iceland")
            print("Your holiday type : Relaxing")
            print("Your climate      : Cold")
        elif ccba == 2:
            print("Your location     : Norway")
            print("Your holiday type : Relaxing")
            print("Your climate      : Cold")
        elif ccba == 3:
            print("Your location     : Switzerland")
            print("Your holiday type : Relaxing")
            print("Your climate      : Cold")
        elif ccba == 4:
            print("Your location     : New Zealand")
            print("Your holiday type : Relaxing")
            print("Your climate      : Cold")
        else:
            print("Invalid answer, please specify '1', '2', '3', or '4'.")

    elif cbb == 2:
        print("Step 3: Pick your location:")
        print("  1 - Chile")
        print("  2 - Argentina")
        print("  3 - Canada")
        print("  4 - Finland")

        ccbb = int(input("Enter 1, 2, 3, or 4: "))
        print()

        if ccbb == 1:
            print("Your location     : Chile")
            print("Your holiday type : Adventurous")
            print("Your climate      : Cold")
        elif ccbb == 2:
            print("Your location     : Argentina")
            print("Your holiday type : Adventurous")
            print("Your climate      : Cold")
        elif ccbb == 3:
            print("Your location     : Canada")
            print("Your holiday type : Adventurous")
            print("Your climate      : Cold")
        elif ccbb == 4:
            print("Your location     : Finland")
            print("Your holiday type : Adventurous")
            print("Your climate      : Cold")
        else:
            print("Invalid answer, please specify '1', '2', '3', or '4'.")
    
    elif cbb == 3:
        print("Step 3: Pick your location:")
        print("  1 - Greenland")
        print("  2 - Japan")
        print("  3 - Sweden")
        print("  4 - Alaska")

        ccbc = int(input("Enter 1, 2, 3, or 4: "))
        print()

        if ccbc == 1:
            print("Your location     : Greenland")
            print("Your holiday type : Nature")
            print("Your climate      : Cold")
        elif ccbc == 2:
            print("Your location     : Japan")
            print("Your holiday type : Nature")
            print("Your climate      : Cold")
        elif ccbc == 3:
            print("Your location     : Sweden")
            print("Your holiday type : Nature")
            print("Your climate      : Cold")
        elif ccbc == 4:
            print("Your location     : Alaska")
            print("Your holiday type : Nature")
            print("Your climate      : Cold")
        else:
            print("Invalid answer, please specify '1', '2', '3', or '4'.")
else:
    "Invalid answer, please specify '1', or '2'."

print()
print("====================================")
print("       Holiday plan complete!       ")
print("         Enjoy your holiday!        ")
print("====================================")