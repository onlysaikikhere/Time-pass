import time
import os
import sys
import webbrowser
import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN, A_BOLD, A_UNDERLINE
from random import randint
def a(string):
    for i in string:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.05)
os.system('clear')
a("hello\n") 
a(".................\n")
a("what do you want to do?\n")
k=input("use calculator(1) \nlisten music (2)) \nGo sleep (3) \nPLay snek game(4)")
################################################################################################################################
if k == "1":
    a("calculator is Launching please wait .\n")
elif k == "2":
    a("lets listen to some music\n")
elif k == "3":
    a("Good Night")
    webbrowser.open("https://www.youtube.com/watch?v=bP9gMpl1gyQ") 
    exit()
elif k == "4":
    print("lets playyy")
else:
    print("bye bye")
    exit()
################################################################################################################################
################################################################################################################################
if k == "1":
    def add(x, y):
  
            return x + y

    def subtract(x, y):
        """This function subtracts two numbers"""

        return x - y

    def multiply(x, y):
        """This function multiplies two numbers"""

        return x * y

    def divide(x, y):
        """This function divides two numbers"""

        return x / y

    # take input from the user
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    choice = input("Enter choice(1/2/3/4):")

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if choice == '1':
        print(num1,"+",num2,"=", add(num1,num2))

    elif choice == '2':
        print(num1,"-",num2,"=", subtract(num1,num2))

    elif choice == '3':
        print(num1,"*",num2,"=", multiply(num1,num2))

    elif choice == '4':
        print(num1,"/",num2,"=", divide(num1,num2))
    else:
        print("Invalid input")
        exit()

################################################################################################################################
if k == "2":
    a("what type of songs would you like to listen? \n")
    sng=input("\nLoFi(1) \nJazz(2) \nHandpicked JPop(3) \n")
    if sng == "1":
        a("\nplaying LoFi")
        webbrowser.open("https://www.youtube.com/watch?v=5qap5aO4i9A")
    elif sng == "2":
        a("\nplaying Jazz")
        webbrowser.open("https://www.youtube.com/watch?v=neV3EPgvZ3g")
    elif sng == "3":
        a("\nhere is my playlist of japanese songs")
        webbrowser.open("https://youtube.com/playlist?list=PL2XPOPAqfxq42PdhIVQiRoHsjipAfB5HJ")
    else :
        a("\nsorry , cannot comprehend input.")
        exit()
################################################################################################################################
################################################################################################################################
################################################################################################################################
if k=="4":
    print(KEY_UP, KEY_RIGHT, KEY_DOWN, KEY_LEFT)                                        # Put this print statement so you can see what these values are in case you don't want to go look for them. Will print after the game ends.
    curses.initscr()                                                                    # This is the initialization of the terminal window.
    win = curses.newwin(50, 120, 5, 10)                                                 # This will size the window to what you want.

    win.attron(A_BOLD)                                                                  # Makes the message "snake attack!" in bold lettering
    win.addstr( 15, 25, 'Snake attack!' )                                               # Just a fun message, immediately eaten by the snake when it starts. It doesn't add body to the snake
    win.attroff(A_BOLD)                                                                 # Ends the bold lettering for "snake attack!"
    win.keypad(1)                                                                       # Keep 1. 1 = yes. 0 = no. 
    curses.noecho()
    curses.curs_set(0)                                                                  # Curser 0 = invis. 1 = visible. 2 = very freakin visible.
    win.nodelay(1)                                                                      # Why is this not making a difference?


    key = KEY_RIGHT                                                                     # Assigning value for key
    score = 0                                                                           # Assigning value to score
    count = 0
    snake = [[15,15],[0,0]]                                                             # snake[0] is the starting position. Each new list within the list is a "body part" so in this case the snake starts with 2 body parts.

    food = [randint(1, 49), randint(1, 119)]                                            # coordinates of where the first piece of food will be in the window. Random makes it more fun than the same spot each time.
    win.addch(food[0], food[1], '$')                                                    # Assigns a character for that particular spot on the window where the food will start. Both index 0, and index 1, of Food will need the same char symbol. Think about it.

    while key != 27:                                                                    # This is where the fun happens. 27 ASCII code for 'ESC'. When you hit it, while it's moving. It will break the while loop and end the window.
        win.attron(A_BOLD)                                                              
        win.border(0)                                                                   
        win.addstr(0, 15, ' Score : ' + str(score) + ' ')                               # Printing 'Score' on the window. You can position it where ever you want.
        win.addstr(0, 45, ' SNAKE! Traveled - ' + str(count) + ' spaces! ')             # Printing 'SNAKE' on the window. You can position it where ever you want
        win.attroff(A_BOLD)                                                    
        
        speed = int(90 - (len(snake)/5 + len(snake)/10) % 120)                          # Adjusts the speed. Write it out if it helps you do the math on how this equates. 
        win.timeout(speed)                                                              # Each time you eat food and a body part extends the body, this number will adjust to make it go faster.
        count += 1 
        
        prevKey = key                                                                   # Assigns var prevKey to the current key, or the last key pressed if unpressed again.
        event = win.getch()                                                             # var event waiting for win.getch() to capture character from user so it can exist.
        key = key if event == -1 else event                                             

        if key == ord(' '):                                                             # empty space == '32' which is ASCII for 'space bar'. If the keystroke is spacebar, key is assigned to 32 and gets stuck in this if statement. Then key is reassigned to -1.
            key = -1                                                                    # one (Pause/Resume)

            while key != ord(' '):                                                      # Tried to explain the loop but it takes too much text. Figure it out :D
                key = win.getch()                                                       
                curses.beep()                                                           # Added a beep so you can hear when it repeats the loop. Just delete if it's annoying.

            key = prevKey
            continue

        if key not in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, 27]:                      # If an invalid key is pressed it reverts back to the stored prevKey
            key = prevKey

        # This insert actually adds a new list (head) to the snake, then the if statement below about the food, the else: in that statement actually pops the last list within the list so it appears to stay the same length when in fact it does increase here.
        snake.insert(0, [snake[0][0] + (key == KEY_DOWN and 1) + (key == KEY_UP and -1), snake[0][1] + (key == KEY_LEFT and -1) + (key == KEY_RIGHT and 1)])

        # Will exit the game if the borders are touched by the snake.
        if snake[0][0] == 0 or snake[0][0] == 49 or snake[0][1] == 0 or snake[0][1] == 119:
            curses.beep() 
            break


        if snake[0] in snake[1:]:                                       # If the snakehead's [x,y] list values match another value within the snakes list. It will exit.  
            break

        
        if snake[0] == food:                                            # When snakes postion on the window matches the foods position = "eaten". This if statement will execute.
            food = []                                                   # Reassigns food to an empty list, ready to be reassigned.    
            score += 1                                                  # LVL UP!
            while food == []:                                           # Executed because the window is hungry for food.
                food = [randint(1, 48), randint(1, 118)]                # Random [x,y] list generated for the food, placing it somewhere on the window next.
                if food in snake:                                       # If the new generated food list values match a set of values within the snakes list, it will reset the while. 
                    food = []                                          
            win.addch(food[0], food[1], '$')                            # WHen the new food passes the while validator, it will then be assigned to actual food variable.
        else:    
            last = snake.pop()                                          # Since the snake.insert statement above is adding new snake list (head), if the snake doesn't eat the food, then it's here that the snake.pop() pops the last [x,y] list within the snake list. (the tail end of the simulated snake)
            win.addch(last[0], last[1], ' ')                            # Now the snakes list doesn't contain this [x,y] but it's still printed to the screen. So this is called to fill that particular [x,y] coordinate with blanks. Essentially eraseing the symbol.
            
        win.addch(snake[0][0], snake[0][1], '@')                        # This keeps the head a '@'
        win.addch(snake[1][0], snake[1][1], '$')                        # Keeps the body of the snake '$' making it look more like a snake in action!
    
    curses.endwin()                                                     # You should be able to figure this out.

    print('Your score was ' + str(score) + '!')     

################################################################################################################################
################################################################################################################################
################################################################################################################################


