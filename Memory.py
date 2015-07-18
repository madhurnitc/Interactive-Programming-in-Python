__author__ = 'Madhur'

# http://www.codeskulptor.org/#user40_ymc3mrYVMd_2.py

# implementation of card game - Memory

import simplegui
import random

# helper function to initialize globals
def new_game():
    global deck,exposed,index1,index2,nTurns,state
    index1 = -1
    index2 = -1
    nTurns = 0
    state = 0
    deck = [x for x in range(8)]*2
    random.shuffle(deck)
    exposed = [False for x in range(8)]*2


# define event handlers
def mouseclick(pos):
    global deck,exposed,index1,index2,nTurns,state
    clickedCard = list(pos)[0]//50
    if not exposed[clickedCard]:
        if state == 0 :
            exposed[clickedCard] = True
            index1 = clickedCard
            state = 1
        elif state == 1 :
            exposed[clickedCard] = True
            index2 = clickedCard
            state = 2
            nTurns = nTurns +1
            label.set_text("Turns = " + str(nTurns))
        else :
            if deck[index1] != deck[index2] :
                exposed[index1] = False
                exposed[index2] = False
                index1 = -1
                index2 = -1
            index1 = clickedCard
            exposed[clickedCard] = True
            state = 1


# cards are logically 50x100 pixels in size
def draw(canvas):
    for i in range(16):
        if exposed[i] :
            canvas.draw_polygon([[i*50, 0], [(i+1)*50, 0], [(i+1)*50, 100], [i*50, 100]], 1, "Black", "White")
            canvas.draw_text(str(deck[i]), (i*50+11, 69), 55, "Black")
        else :
            canvas.draw_polygon([[i*50, 0], [(i+1)*50, 0], [(i+1)*50, 100], [i*50, 100]], 1, "Black", "Green")
    label.set_text("Turns = " + str(nTurns))


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric