print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_ 
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____ 
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_ 
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____ 
/______/______/______/______/______/______/______/______/______/______/_____ / 
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your quest: find the hidden treasure!")

# Level 1: Choosing a Direction
first_choice = input("Choose a path: Left or Right?\nType Left/Right: ").lower()
if first_choice == "right":
    print(''' ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣿⣿⣿⣿⣿⣿⣆⡀⠀⠀⠀⠀⣠⣴⣦⡄⢤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣷⣷⣶⣶⣿⣿⣿⣿⡀⣽⡿⣶⣦⡀⠀⠀⠀⠀⠀
⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡿⣿⣿⣿⣿⣆⠀⠀⠀⠀
⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣦⠀⠀⠀
⠀⠀⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣟⣿⣿⣿⣿⣿⡿⢟⣿⣷⡀⠀
⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣭⣿⣿⣽⣿⣽⣾⣿⣿⣿⠛⠉⠉⠀⢈⣿⣿⡇⠀
⠀⠀⠀⢻⣿⣿⠛⠉⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠡⠤⠄⠁⠀⠀⢻⣿⡇⠀
⠀⠀⠀⠘⣿⣿⠄⠀⠀⠀⠀⠀⣉⠙⠋⢿⣿⣯⠀⠀⠀⠀⠀⠀⣰⣿⣿⡿⡃⠀
⠀⠀⠀⠀⢹⣿⣇⣀⠀⠈⠉⠉⠁⠀⣤⢠⣿⣿⣧⡆⣤⣤⡀⣾⣿⣿⣿⢠⡇⠀
⠀⠀⠀⠀⠀⣿⣿⣿⣷⣤⠄⣀⣴⣧⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⠇⠀
⠀⠀⠀⠀⠀⠸⣿⣯⠉⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⡯⠁⡌⠀⠀
⠀⠀⠀⠀⠀⠀⠙⢿⡄⢿⣿⣿⣿⣿⣿⣎⠙⠻⠛⣁⣼⣿⣿⡿⠛⠁⡸⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⢿⡄⠉⣿⡿⣿⣿⣿⣿⣷⣬⣿⡿⠟⠋⢀⣴⡞⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⠀⠀⠀⠀⠉⠉⠋⠉⠉⠁⠀⢀⣴⣿⡿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣿⠿⢃⣴⣿⣿⣿⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''')

    print("You've stumbled into one of Joker's traps. Try again... if you dare.")
else:
    print('''
     _                                                           
    | |                                                          
    | |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ __ ___   __ _ _ __  
    | __| '__/ _ \/ _` / __| | | | '__/ _ \ '_ ` _ \ / _` | '_ \ 
    | |_| | |  __/ (_| \__ \ |_| | | |  __/ | | | | | (_| | |_) |
    \__|_|  \___|\__,_|___/\__,_|_|  \___|_| |_| |_|\__,_| .__/ 
                                                        | |    
                                                        |_| 
    ''')
    print("You avoided Joker's trap... for now.")

    # Level 2: Cross the River or Wait
    second_choice = input("You arrive at a river. Do you Swim or Wait?\nType Swim/Wait: ").lower()
    if second_choice == "swim":
        print("A swarm of Joker's piranhas! Game Over.")
    else:
        print("Wise choice. You crossed safely.")

        # Level 3: Enter the Dark Alley or the Abandoned Funhouse
        third_choice = input("Joker’s laugh echoes nearby. Do you Enter the Alley or the Funhouse?\nType Alley/Funhouse: ").lower()
        if third_choice == "funhouse":
            print("You've found Joker’s hidden vault of chaos! Congratulations!")
        else:
            print('''
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠴⠚⠉⠁⠙⢶⡤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣞⣴⣿⠞⠋⠀⠀⠀⠀⠀⠀⠀⠀⠙⠉⢿⣦⢠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡀⢠⠴⠿⠋⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⢱⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣼⣧⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠺⣻⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⡏⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠽⢿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⠸⣷⠀⠀⠀⠀⣠⠶⠤⣄⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣄⣀⠀⠀⠀⠀⠀⣽⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣦⣯⠁⠀⠀⢠⡏⠀⠀⠈⠙⠲⡄⠀⠀⢀⡠⠊⠁⠀⠀⠸⡇⠀⠀⠀⠈⠛⡶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⢣⡉⠁⠀⠀⠀⣧⠀⢀⠀⠀⠀⡈⠑⠒⠉⠀⠀⣀⣀⠀⢠⠇⠀⠀⠀⣠⡎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠹⣦⠀⠀⠀⢸⠀⠁⠪⡂⠀⢳⠀⠀⠀⠠⠜⣓⣦⡀⢸⠀⠀⠀⠀⣺⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⠛⢦⡀⡞⢠⣶⣦⠁⠀⠘⢧⠀⠀⠀⣰⣡⣶⣧⢻⡀⠠⣶⡞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⢢⠸⣿⠁⢋⣼⣿⣿⡃⠀⡔⢥⠀⢐⣿⣯⣝⠒⠬⣇⡴⡟⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠸⣎⢂⣿⢠⠛⠻⣿⣿⡿⠦⠷⠼⣶⣿⣿⠿⠛⠐⠛⣿⣼⡵⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⢿⠀⢧⡀⠀⠀⢠⠄⠀⠀⠛⣄⠀⠀⢀⡠⠇⡟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡼⣧⠘⣿⣭⡉⠙⠢⡀⢀⠴⢋⣱⣶⣤⣤⢠⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣀⣀⠤⠴⠒⢚⡽⠋⠀⡟⣧⠘⣿⣟⡫⠶⣮⣵⡮⠷⣾⣯⣿⢃⣾⡄⠹⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠉⠁⠀⠀⠀⠀⣰⠏⠀⠀⢰⡇⢻⢣⡘⢟⠿⣖⣤⣦⣷⠿⣻⢏⡴⢫⠇⡇⠀⢹⡄⠉⠳⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡼⠃⠀⠀⠀⢸⠀⠸⡄⡷⡶⣑⣲⡼⢿⣾⣚⣥⠎⢀⠎⢸⠁⠀⠀⣷⠀⠀⠀⠈⠛⢶⣄⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⡼⠁⠀⠀⠀⠀⢸⠀⠀⢻⣿⣿⣄⡀⠀⠀⠁⢀⠎⣠⠏⠀⡞⠀⠀⠀⢹⠀⠀⠀⠀⠀⠀⠈⠙⠷⣄⠀⠀⠀⠀⠀
⠀⠀⢠⠞⠁⠀⠀⠀⠀⠀⡟⠀⢠⡜⢿⢿⣟⠷⣄⣠⠴⠋⡴⠃⠀⢰⠃⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢄⠀⠀⠀
⠀⠀⠘⢦⡀⠀⠀⠀⠀⢀⣷⣀⡟⢹⣸⠀⠙⡆⠀⠀⣠⠞⡇⠀⢠⡟⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀
⠀⠀⠀⠀⠈⢳⡄⠀⠀⢸⠇⠉⠀⠈⠻⡄⠀⡇⢀⡼⠃⠀⣇⣠⡾⠁⢠⡶⠦⠤⠼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⠴⠒⠋⠀⠀⠀⣸⡇⠀⠀⠀⠀⢳⠀⣱⠎⠀⠀⠀⢛⣿⠃⠀⠀⠓⠦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠘⣆⠀⠀⠀⠀⠀⡟⢱⠀⠀⠀⠀⠈⡟⠀⠀⠀⠀⢀⣾⠇⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠘⡆⠀⠀⠀⠀⡇⠈⢇⠀⠀⠀⠀⡇⠀⠀⠀⣠⠋⡿⠀⠀⠀⠀⠀⢀⡞⠀⠀⠀⣀⣀⣀⣀⣀⡀⣀⣀⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠘⡄⠀⠀⢠⡇⠀⠈⢦⡀⠀⠀⣇⠀⠀⡴⠁⣼⠃⠀⠀⠀⠀⢀⡜⠁⠀⠀⠀⣿⢿⠿⠙⠇⠟⠟⠇⠁⠀⠀⠈⠃⠀⠀⠀⠀⠀
            Game Over.
            ''')
