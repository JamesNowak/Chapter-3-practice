# complete the code below, if the user input matches the password
# string, display "that is correct" otherwise display "that is not
# correct"
password = "Avenger"
user_password = input("Please input a password. ")

if password == user_password:
    print("This is correct, accessing Avenger database")
else:
    print("This is incorrect, access denied.")
