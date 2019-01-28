name = input("Please enter your name: ")
number = input("Please enter a number: ")

# TODO: Make sure the number is an integer
number = int(number)


# TODO: Print out the User's name and the number entered,
# making sure the two statements are on separate lines of output.
print("Hi {} your number is {}.".format(name,number))


# TODO: Compare the number the user gave with the different
# FizzBuzz conditions. 
# *********************
# If the number is divisible by both 3 and 5, print "is a FizzBuzz number."
if (number%3 == 0 and number%5 == 0):
  print(number, "is a FizzBuzz number.")
  
# If the number is divisible by 3, print "is a Fizz number."
elif number%3 == 0:
  print(number, "is a Fizz number.")

# If the number is divisible by 5, print "is a Buzz number."
elif number%5 == 0:
  print(number, "is a Buzz number.")

# Otherwise, print "is neither a fizzy or a buzzy number."
else:
  print(number, "is neither a fizzy or a buzzy number.") 
# *********************



