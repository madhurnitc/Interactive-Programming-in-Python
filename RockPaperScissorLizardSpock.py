__author__ = 'Madhur'

# This program can be run directly in CodeSkulptor Environment By clicking this link below
# http://www.codeskulptor.org/#user40_HZIqHS2D5x_2.py
# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import random

def name_to_number(name):
    # delete the following pass statement and fill in your code below


    # convert name to number using if/elif/else
    # don't forget to return the result!
    if ( name == "rock" ):
        return 0
    elif ( name == "Spock" ):
        return 1
    elif (  name == "paper"):
        return 2
    elif (  name == "lizard"):
        return 3
    elif (  name == "scissors"):
        return 4
    else :
        print "Invalid name " , name

def number_to_name(number):
    # delete the following pass statement and fill in your code below
    pass

    # convert number to a name using if/elif/else
    # don't forget to return the result!
    if ( number == 0 ):
        return "rock"
    elif (number == 1 ):
        return "Spock"
    elif (number == 2 ):
        return "paper"
    elif (number == 3 ):
        return "lizard"
    elif (number == 4 ):
        return "scissors"
    else :
        print "Invalid Number " , number

def rpsls(player_choice):
    # delete the following pass statement and fill in your code below


    # print a blank line to separate consecutive games
    print ""
    # print out the message for the player's choice
    print "Player's Choice is " , player_choice
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number( player_choice )
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name( comp_number )
    # print out the message for computer's choice
    print "Computer's Choice is " , comp_choice
    # compute difference of comp_number and player_number modulo five
    choice_diff = ( player_number - comp_number ) % 5
    winner =""
    if ( choice_diff == 1 or choice_diff == 2 ):
        winner = "Player"
    elif ( choice_diff == 0 ) :
        winner = "Tie"
    else :
        winner = "Computer"

    if ( winner != "Tie" ) :
        print winner + " wins !"
    else :
        print "Player and Computer Tie !"


    # use if/elif/else to determine winner, print winner message


# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric