__author__ = 'Madhur'


# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")

# initialize some useful global variables
in_play = False
outcome = "Hit or Stand "
score = 0
message = ""

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank),
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)

    def drawBack(self, canvas, pos):
        card_loc = (CARD_BACK_CENTER[0], CARD_BACK_CENTER[1])
        canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE,
                          [pos[0] + CARD_BACK_CENTER[0] + 1,
                           pos[1] + CARD_BACK_CENTER[1] + 1],
                          CARD_BACK_SIZE)

# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.hand_list =  []

    def __str__(self):
        # return a string representation of a hand
        msg = ""
        for card in self.hand_list :
            msg = msg + str(card) + " "
        return msg

    def add_card(self, card):
        # add a card object to a hand
        self.hand_list.append(card)


    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        hand_value = 0
        for card in self.hand_list :
            hand_value = hand_value + VALUES[card.get_rank()]
        for card in self.hand_list :
            card_rank = card.get_rank()
            if card_rank =='A' and hand_value <= 11 :
                hand_value = hand_value + 10
        return hand_value


    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        for card in self.hand_list :
            pos[0] = pos[0] + CARD_SIZE[0] + 20
            card.draw(canvas,pos)



# define deck class
class Deck:
    def __init__(self):
        # create a Deck object
        self.cards = [Card(suit, rank) for suit in SUITS for rank in RANKS]

    def shuffle(self):
        # shuffle the deck
        random.shuffle(self.cards)

    def deal_card(self):
        # deal a card object from the deck
        return self.cards.pop()



    def __str__(self):
        # return a string representing the deck
        msg = ""
        for card in self.cards :
            msg = msg + str(card) + " "
        return msg



#define event handlers for buttons
def deal():
    global outcome, in_play, cards_deck, hand_player, hand_dealer, side_player, side_dealer, score, message


    # your code goes here
    if in_play :
        score = score - 1
        in_play = False
        deal()
    else  :
        cards_deck = Deck()
        cards_deck.shuffle()
        hand_player = Hand()
        hand_dealer = Hand()
        hand_player.add_card(cards_deck.deal_card())
        hand_player.add_card(cards_deck.deal_card())
        hand_dealer.add_card(cards_deck.deal_card())
        hand_dealer.add_card(cards_deck.deal_card())
        outcome = "Hit or Stand"
        side_player = "Player"
        side_dealer = "Dealer"
        message = ""
        in_play = True

def hit():
    # replace with your code below

    # if the hand is in play, hit the player

    # if busted, assign a message to outcome, update in_play and score

    global in_play, cards_deck, hand_player, score, side_player, message, outcome
    if in_play :
        if  hand_player.get_value() < 22:
            hand_player.add_card(cards_deck.deal_card())
            if hand_player.get_value() > 21 :
                side_player = "Busted!"
                message = " Busted. You Loose!"
                score = score - 1
                outcome = "New Deal?"
                in_play = False


def stand():
    # replace with your code below

    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

    global in_play, outcome,hand_dealer,hand_player,score,side_dealer, message
    if in_play:
        while( hand_dealer.get_value() < 17 ):
            hand_dealer.add_card(cards_deck.deal_card())
        if hand_dealer.get_value() > 21 :
            side_dealer = "Busted!"
            message = "Dealer Busted! You win!!"
            score = score +  1
            outcome = "New Deal?"
            in_play = False
        elif hand_player.get_value() > hand_dealer.get_value() :
            message = "Your hand's stronger! You win!"
            score = score + 1
            outcome = "New Deal"
            in_play = False
        else :
            message = "Your hand's weaker! You loose!"
            score = score - 1
            outcome = "New Deal?"
            in_play = False


# draw handler
def draw(canvas):
    canvas.draw_text("Blackjack", (60, 100), 40, "Aqua")
    lDealer = canvas.draw_text(side_dealer, (60, 185), 33, "Black")
    lPlayer = canvas.draw_text(side_player, (60, 385), 33, "Black")
    lOutcome = canvas.draw_text(outcome, (250, 385), 33, "Black")
    lMessage = canvas.draw_text(message, (250, 185), 25, "Black")
    lScore = canvas.draw_text("Score: " + str(score), (450, 100), 33, "Black")
    hand_dealer.draw(canvas, [-65, 200])
    hand_player.draw(canvas, [-65, 400])
    if in_play:
        hand_dealer.hand_list[0].drawBack(canvas, [28, 200])

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric