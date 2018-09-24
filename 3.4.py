# write code that accepts a number from between 1 and 5 from the user
# and returns a roman numeral for that number. If the number entered is
# not between 1 and 5, have the else statement print "That is not a
# valid number"
a1 = "I"
a2 = "II"
a3 = "III"
a4 = "IV"
a5 = "V"
pick = int(input("Pick a number: "))
if pick == 1:
    print(a1)
else:
    if pick == 2:
        print(a2)
    else:
        if pick == 3:
            print(a3)
        else:
            if pick == 4:
                print(a4)
            else:
                if pick == 5:
                    print(a5)
                else:
                    print("Not a valid number.")
