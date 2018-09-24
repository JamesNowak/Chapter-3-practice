# add code below to determine if age is greater than or equal to
# 18. Depending on the answer, display the appropriate statement:
# "You are old enough to vote" or "You are not old enough to vote"
# Use the if-else structureage = input("how old are you? ")
age = input("How old are you? ")

if int(age) > 18:
    print("you are able to vote!")
else:
    print("You are not able to vote!")
