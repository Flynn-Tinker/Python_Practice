#team

player_names = []
count = 1
while input("Would you like to add players to the game? y/n ") == "y":
    player = input("What is the player's name? ")
    player_names.append(player)

else:
    print("There are ",len(player_names)," on the team.")
    for names in player_names:
        #names acts as your counter, don't need player_names[count-1]
        print("Player ",count,": ",names)
        count += 1
    keeper = int(input("Please select goal keeper using player number "))
    print(player_names[keeper-1], " is your goal keeper!")
    #print(player_names)
