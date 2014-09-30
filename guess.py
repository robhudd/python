# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
#http://www.codeskulptor.org/#user38_ilB7GXxmSk_5.py

import simplegui
import random
import math

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    global get_input
    global num_range
    global count
    count = 0
    num_range = 100
    
    print ""
    
    if num_range == 100:
        return range100
        
    elif num_range == 1000:
        return range1000

    
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global secret_number
    global num_range
    global guess_max
    guess_max = 7
    num_range = 100
    secret_number = random.randrange(0,100)
    print "select a number between 1 - 100"
    print secret_number
    return secret_number    

    
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global secret_number
    global num_range
    global guess_max
    guess_max = 10
    num_range = 1000
    secret_number = random.randrange(0,1000)
    print "select a number between 1 - 1000"
    print secret_number
    return secret_number

   
def input_guess(guess):
    # main game logic goes here	
    global get_input
    global count
    global guess_max
    get_input = int(guess)
    print "Guess was " + str(get_input)
    
    count = count + 1

    
    if count < guess_max:
        if secret_number == get_input:
            print "Correct!"
            return new_game()
        elif secret_number > get_input:
            print "Higher"
        elif secret_number < get_input:
            print "Lower"
    else:
        print "Out of guesses"
        return new_game()
        

    
# create frame
f = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
f.add_button("Range is 0, 100", range100, 200)
f.add_button("Range is 0, 1000", range1000, 200)
f.add_input("Enter a guess", input_guess, 200)

# call new_game 
new_game()








# always remember to check your completed program against the grading rubric
