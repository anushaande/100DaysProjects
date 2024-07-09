print("Welcome to Treasure Island. Your mission is to find the treasure.")
l_or_r = input("Do you want to go left or right?").lower()
if l_or_r == "left":
    s_or_w = input("Do you wanna swim or do you wanna wait?").lower()
    if s_or_w == "wait":
        door = input("Choose the door. Red, Blue, Yellow?").lower()
        if door == "yellow":
            print("You Win!")
        else:
            print("Game Over.")
    else:
        print("Game Over.")
else:
    print("Game Over.")