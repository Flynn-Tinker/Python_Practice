#Masterticket
import sys
TICKET_PRICE = 10
SERVICE_CHARGE = 2
tickets_remaining = 100

users_name = input("What is your name? ")

# Create calculate_price function. It takes number of tickets and returns
# number_of_tickets * TICKET_PRICE
def calculate_price(number_of_tickets):
    return number_of_tickets*TICKET_PRICE+SERVICE_CHARGE

while tickets_remaining > 0:
    print("There are {} tickets remaining.".format(tickets_remaining))
    try:
        number_of_tickets = int(input("Hi {}, how many tickets would you like? ".format(users_name)))
    except ValueError:
        print("Must be a number")
    else:
        # They put it in a try block instead
        while (tickets_remaining - number_of_tickets) < 0:
            print("We only have {} tickets left".format(tickets_remaining))
            number_of_tickets = int(input("Hi {}, how many tickets would you like? We have {} left. ".format(users_name, tickets_remaining)))

        #cost = int(number_of_tickets*TICKET_PRICE)
        cost = calculate_price(number_of_tickets)
        print("Your total price would be ${}.".format(cost))

        if input("Would you like to purchase the tickets? Y/N ") == "Y":
            print("SOLD!")
            tickets_remaining -= number_of_tickets
            #print("There are {} tickets remaining.".format(tickets_remaining))
        else:
            print("Thank you {}.".format(users_name))
            sys.exit()
                
print("Sorry, we are out of tickets!")
