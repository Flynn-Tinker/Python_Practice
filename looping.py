#looping
name = input("What is your name: ")
while input("{} do you understand Python while loops? \n(Enter yes/no)".format(name)) == "no":
    print("While loops are continuous until the user inputs an accepted value")
print("Thank you {} for learning about while loops".format(name))
