import math

def split_check(check_amount,number_of_people):
  # Want to make sure number of people is more than 1!
  if number_of_people <= 1:
    raise ValueError("More than one person is needed to split a check.")
  return math.ceil(check_amount/number_of_people)

try:
  total_due = float(input("How much was the total check?: "))
  total_people = int(input("How many people are in your part?: "))
  amount_due = split_check(total_due,total_people)
except ValueError as err:
  # If they enter a string instead of a number
  print("That's not a valid value. try again")
  print("{}".format(err))
else:
  print('Each person owes $',amount_due)
