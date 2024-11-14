# day 6 27/10/23

def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Move forward until a wall is encountered
while front_is_clear():
    move()
turn_left() 

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()