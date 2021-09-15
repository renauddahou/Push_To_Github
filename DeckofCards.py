#Tutorial with TokyoEdTech(youtube)
import turtle 
import time
import random
win = turtle.Screen()
win.bgcolor("Black")
win.setup(800, 600)
win.title("Deck of Cards")
pen = turtle.Turtle()
#pen.speed(0)
pen.hideturtle()
time.sleep(3)
class Card():
    def __init__(self, name, suit):
        self.name = name
        self.suit = suit
        self.symbols = {"D": "♦", "C":"♣", "S": "♠", "H": "♥"}
    def print_card(self):
        print(f'{self.name} {self.symbols[self.suit]}')
    def render(self, x, y, pen):
        #draw board:
        pen.penup()
        pen.goto(x, y)
        pen.color("blue")
        pen.goto(x-50,y+75)
        pen.begin_fill()
        pen.pendown()
        pen.goto(x+50, y+75)
        pen.goto(x+50, y-75)
        pen.goto(x-50,y-75)
        pen.goto(x-50,y+75)
        pen.end_fill()
        pen.penup()
        #draw suit in middle:
        pen.color("white")
        pen.goto(x-18,y-30)
        pen.write(self.symbols[self.suit], False, font=("Courier New", 48, "normal"))
        #draw top left:
        pen.goto(x-40, y+45)
        pen.write(self.name, False, font=("Courier New", 18, "normal"))
        pen.goto(x-40, y+25)
        pen.write(self.symbols[self.suit], False, font=("Courier New", 18, "normal"))
        #draw bottom right:
        pen.goto(x+30,y-55)
        pen.write(self.name, False, font=("Courier New", 18, "normal"))
        pen.goto(x+30, y-80)
        pen.write(self.symbols[self.suit], False, font=("Courier New", 18, "normal"))
class Deck():
        def __init__(self):
            self.cards = []
            names = ("A", "K", "Q", "J","T","9","8","7", "6","5","4","3","2")
            suits = ("D","C","H","S")
            for name in names:
                for suit in suits:
                    card = Card(name, suit)
                    self.cards.append(card)
        def shuffle(self):
            random.shuffle(self.cards)
        def get_card(self):
            card = self.cards.pop()
            return card
        def reset_deck(self):
            self.cards = []
            names = ("A", "K", "Q", "J","T","9","8","7", "6","5","4","3","2")
            suits = ("D","C","H","S")
            for name in names:
                for suit in suits:
                    card = Card(name, suit)
                    self.cards.append(card) 
            self.shuffle()
#Create Deck:
deck = Deck()
#Reset Deck:
deck.reset_deck()
#Render cards:
for _ in range(5):
    card = deck.get_card()
    card.render(0,0,pen)
    time.sleep(5)
    pen.clear()

win.mainloop()