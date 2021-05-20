import random
# To randomize customer ticket number

# Prices & Cust. total
sPizza = 10
mPizza = 12
lPizza = 14

orderCost = 0

# Main loop
welcome = input("Welcome to Pizza World! Would you like to order a pizza? (y/n)\n")
if welcome[0:1].capitalize() == "Y":
    ordering = True
    while ordering:
        while True:
            size = input(("\nWhat size pizza would you like?\n-Small pizza: ${}\n-Medium pizza: ${}\n"
                          "-Large pizza: ${}\n").format(sPizza, mPizza, lPizza))
            if size[0:1].capitalize() == "S":
                orderCost += sPizza
                break
            elif size[0:1].capitalize() == "M":
                orderCost += mPizza
                break
            elif size[0:1].capitalize() == "L":
                orderCost += lPizza
                break
            else:
                print("\nSorry. I don't think we sell that size here.")
        while True:
            try:
                topping = int(input("\nHow many toppings would you like on your pizza?\n"
                            "*Customers please note*: The first three toppings are free. Any additional toppings will"
                            " cost an extra dollar each.\nThere is a limit of 6 toppings per pizza.\n"))
                if topping >6:
                    print("\nThat's too many toppings! leave some for the other customers.")
                    topping = 0
                elif topping <=0:
                    print("\nYou can't have a pizza with nothing on it!")
                    topping = 0
                elif topping <=3:
                    print("\nAlright, that'll be no extra charge.")
                    break
                elif topping >3 and topping <=6:
                    print("\nYou've selected some additional toppings. Your bill will be updated accordingly.")
                    topping -= 3
                    orderCost += topping
                    break
            except ValueError:
                print("\nSorry, you can only enter numbers here. Our ordering system isn't as high-tech as Domino's.")
        again = input("\nWould you like another pizza? (y/n)\n")
        if again[0:1].capitalize() == "N":
            ordering = False
    print(
        "\nThank you for eating with Pizza World!"
        " Please present this ticket to the counter when your number is called.\n")
    print("--------------------\n"
          "Ticket no.: " + str(random.randint(0, 50)) +
          "\nOrder total: ${}\n"
          "--------------------\n".format(orderCost))
else:
    print("\nAlright. Have a nice day.")