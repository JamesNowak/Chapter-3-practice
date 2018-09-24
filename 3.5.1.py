customer_age = int(input("How old is the customer?   "))
cost = 0

if customer_age <= 3:
    cost = 0
    print("Your cost for a customer who is " + str(customer_age) + " years old")
    print("is $" + format(cost, ",.2f"))
else:
    if 4 <= customer_age <= 11:
        cost = .99 * customer_age
        print("Your cost for a customer who is " + str(customer_age) + " years old")
        print("is $" + format(cost, ",.2f"))
    else:
        if 12 <= customer_age <= 61:
            cost = 12.89
            print("Your cost for a customer who is " + str(customer_age) + " years old")
            print("is $" + format(cost, ",.2f"))
        else:
            print("The price is 9.89")
