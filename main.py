import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from Card import Card
from SixDeck import SixDeck
from Player import Player
from Dealer import Dealer
import random
from tkinter import Tk, Canvas
from tkinter import Toplevel
from tkinter import Label
from PIL import ImageTk, Image
from io import BytesIO
from PIL import ImageEnhance
import requests

def game_frame(self, bg='gray', fg='blue', padx=None, pady=None):
    kwargs = {'bg': bg, 'fg': fg, 'padx' : padx, 'pady': pady}
    return self.game_frame
class SixDeck:
    def __init__(self):
        self.cards = []
        self.build()  
    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(1, 14):
                self.cards.append(Card(v, s))
    def shuffle(self):
        random.shuffle(self.cards)
    def draw(self):
        return self.cards.pop()
    def deckReset(self):
        self.cards = []
        self.build()

class Player:
    def __init__ (self):
        self.hand = []
        self.chips = 0
        v = 100
    def handValue(self):
        value = 0
        ace_count = 0
        for card in self.hand:
            if card.val >= 10:
                value += 10
            elif card.val == 1:
                ace_count += 1
                value += 11
            else:
                value += card.val
        while value > 21 and ace_count:
            value -= 10
            ace_count -= 1
        return value
    def draw(self, deck):
        card = deck.draw()
        self.hand.append(card)
    def addChips(self, v):
        self.chips += v
    def loseChips(self, v):
        self.chips -= v
    def getSuit(self):
        c = self.hand[len(self.hand) -1]
        return c.suit
    def getVal(self):
        c = self.hand[len(self.hand)-1]
        return c.val
    def chipCount(self):
        return self.chips
    def score(self):
        aceHand = False
        sum = 0
        count = 0
        for c in self.hand:
            if(c.val == 1):
                aceCard = self.hand.pop(count)
                aceHand = True
            elif(c.val > 10):
                sum += 10
            else:
                sum += c.val
            count += 1
        return self.chips
class Card:
    def __init__(self, val, suit):
        self.val = val
        self.suit = suit
    def __repr__(self):
        value_names = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"}
        val_str = value_names.get(self.val, str(self.val))
        return f"{val_str} of {self.suit}"
# ---------------------------------------------------------------------------------------------------------
class Dealer:
    def __init__(self):
        self.hand = []
        self.chips = 0
    def draw(self, deck):
        card = deck.draw()
        self.hand.append(card)
    def getSuit(self):
        return self.hand[-1].suit
    def getVal(self):
        return self.hand[-1].val
    def showHand(self):
        for card in self.hand:
            print(f"{card.val} of {card.suit}")
    def handValue(self):
        value = 0
        ace_count = 0
        for card in self.hand:
            if card.val >= 10:
                value += 10
            elif card.val == 1:
                ace_count += 1
                value += 11
            else:
                value += card.val
        while value > 21 and ace_count:
            value -= 10
            ace_count -= 1
        return value
    def play(self, deck,):
        while self.handValue() < 17:
            self.draw(deck)
        else:
            pass
        
def player_hand_label(self):
    player_hand_label = tk.Label(self.game_frame, text=f"Player's Hand: {self.player.handValue()}")
    return player_hand_label
    for card in self.player.hand:
        
        card_filename = card_image_filename(card)
        card_image_path = f'C:\\Users\\jbrou\\tkinter\\blackjack\\resources\\cards\\{card_filename}'
        card_image = Image.open(card_image_path)
        card_photo = ImageTk.PhotoImage(card_image)
        card_label = tk.Label(self.game_frame, image=card_photo)
        card_label.image = card_photo
        card_label.pack(side="left")
def card_to_image_filename(card):
    name, suit = card.lower().split(' of ')
    name = name.replace('jack', '11').replace('queen', '12').replace('king', '13').replace('ace', '1')
    suit = suit[0] 
    return f'{name}{suit}.png'

def dealer_hand_label(self):
    dealer_hand_label = tk.Label(self.game_frame, text=f"Dealer's Hand: ???: {self.dealer.handValue()}")
    return dealer_hand_label 
    for card in self.dealer.hand[:-1]:  
        card_filename = self.card_to_image_filename(card)
        card_image_path = f'C:\\Users\\jbrou\\tkinter\\blackjack\\resources\\cards\\{card_filename}'
        card_image = Image.open(card_image_path)
        card_photo = ImageTk.PhotoImage(card_image)
        card_label = tk.Label(self.game_frame, image=card_photo)
        card_label.image = card_photo
        card_label.pack(side="right")

    # Load the card back image
    card_back_image = Image.open('C:\\Users\\jbrou\\tkinter\\blackjack\\resources\\cards\\cardback.png')
    self.card_back_photo = ImageTk.PhotoImage(card_back_image)

    # Add card back for hidden card
    hidden_card_label = tk.Label(self.game_frame, image=self.card_back_photo)
    hidden_card_label.image = self.card_back_photo
    hidden_card_label.pack(side="right")

def player_hand_frame(self, text=None):
    self.player_hand_frame = tk.LabelFrame(self.game_frame, text="Player's Hand")
    self.player_hand_frame.pack(side="left", padx=10, pady=10)
    for card in self.player.hand:
        label = tk.Label(self.player_hand_frame, text=str(card))
        label.pack()

def dealer_hand_frame(self, text=None):
    self.dealer_hand_frame = tk.LabelFrame(self.game_frame, text="Dealer's Hand")
    self.dealer_hand_frame.pack(side="left", padx=10, pady=10)
    for card in self.dealer.hand:
        label = tk.Label(self.dealer_hand_frame, text=str(card))
        label.pack()
    

def second_card(self):
    while self.dealer.hand_value() < 17:
        self.dealer.draw(deck)
        return self.dealer
    else:
        self.update_gui()
        self.player.draw(deck)
        self.display_hand(self.game_frame, self.player, "Player's Hand", "left")
        
    hand_frame = tk.LabelFrame(self.game_frame, text=labels)
    hand_frame.pack(side=side, padx=10, pady=10)

    for card in self.player.hand:
        card_image_filename = self.card_to_image_filename(card)
        card_image = Image.open(f'C:\\Users\\jbrou\\tkinter\\blackjack\\resources\\cards\\{card_image_filename}')
        card_photo = ImageTk.PhotoImage(card_image)

        card_label = tk.Label(hand_frame, image=card_photo)
        card_label.image = card_photo  
        card_label.pack()
        

        hand_frame = tk.LabelFrame(self.game_frame, text=labels)
        hand_frame.pack(side="left", padx=10, pady=10)

        for i, card in enumerate(self.player.hand):
#DEALER FACE DOWN CARD
            if dealer_hand_label == "Dealer's Hand" and i == 0:  
                card_image = Image.open('C:\\Users\\jbrou\\tkinter\\blackjack\\resources\\cards\\cardback.png')
            else:
                card_image_filename = self.card_to_image_filename(card)
                card_image = Image.open(f'C:\\Users\\jbrou\\tkinter\\blackjack\\resources\\cards\\{card_image_filename}') 
            
            card_photo = ImageTk.PhotoImage(card_image)
            card_label = tk.Label(hand_frame, image=card_photo)
            card_label.image = card_photo  
            card_label.pack()    

class MyApp:
    def __init__(self):
        self.root = Tk()
        self.game_frame = tk.LabelFrame(self.root, bg='gray', padx=50, pady=50)
        self.game_frame.pack(fill="both", expand="yes")
        # self.card_back_image = Image.open(f'C:\\Users\\jbrou\\tkinter\\blackjack\\resources\\cards\\cardback.png')
        # self.card_back_photo = ImageTk.PhotoImage(self.card_back_image)
        # self.card_back_label = tk.Label(self.root, image=self.card_back_photo, text="Dealer's Hand")
        # self.card_back_label.pack(side='right'
        # , padx=10, pady=10)
        # self.card_back_labelp = tk.Label(self.root, image=self.card_back_photo)
        # self.card_back_labelp.pack(side='left', padx=10, pady=10)
        self.deck = SixDeck()
        self.deck.shuffle()
        self.player = Player()
        self.dealer = Dealer()
        self.player.draw(self.deck)
        self.dealer.draw(self.deck)
        self.playercard1 = player_hand_label(self)
        self.playercard1.pack()
        self.dealercard1 = dealer_hand_label(self)
        self.dealercard1.pack()
        self.Player_hand_frame1 = tk.LabelFrame(self.game_frame, text="Player's Hand")
        self.Player_hand_frame1.pack(side="left", padx=10, pady=10)
        for card in self.player.hand:
            self.label = tk.Label(self.Player_hand_frame1, text=str(card))
            self.label.pack()
        self.Dealer_hand_frame1 = tk.LabelFrame(self.game_frame, text="Dealer's Hand")
        self.Dealer_hand_frame1.pack(side="right", padx=10, pady=10)
    def update_gui(self):
        for widget in self.game_frame.winfo_children():
            widget.destroy()
        self.Player_hand_frame1 = tk.LabelFrame(self.game_frame, text="Player's Hand")
        self.Player_hand_frame1.pack(side="left", padx=10, pady=10)
        for card in self.player.hand:
            card_image_filename = card_to_image_filename(str(card))
            card_image = Image.open(f'C:\\Users\\jbrou\\tkinter\\blackjack\\resources\\cards\\{card_image_filename}')
            card_photo = ImageTk.PhotoImage(card_image)
            label = tk.Label(self.Player_hand_frame1, image=card_photo)
            label.image = card_photo  # keep a reference to the image
            label.pack()
        self.Dealer_hand_frame1 = tk.LabelFrame(self.game_frame, text="Dealer's Hand")
        self.Dealer_hand_frame1.pack(side="right", padx=10, pady=10)
        for i, card in enumerate(self.dealer.hand):
            if i == 0:  # if it's the dealer's first card
                card_image = Image.open(f'C:\\Users\\jbrou\\tkinter\\blackjack\\resources\\cards\\cardback.png')
            else:
                card_image_filename = card_to_image_filename(str(card))
                card_image = Image.open(f'C:\\Users\\jbrou\\tkinter\\blackjack\\resources\\cards\\{card_image_filename}')
            card_photo = ImageTk.PhotoImage(card_image)
            label = tk.Label(self.Dealer_hand_frame1, image=card_photo)
            label.image = card_photo
            label.pack()  
            
# NIT BUTTON
        self.hit_button = tk.Button(self.game_frame, text="Hit", command=self.player_hit)
        self.hit_button.pack()

# STAND BUTTON
        self.stand_button = tk.Button(self.game_frame, text="Stand", command=self.player_stand)
        self.stand_button.pack()
    def player_hit(self):
        self.player.draw(self.deck)
        self.update_gui()
        if self.player.handValue() > 21:
            self.losercard = tk.Label(self.game_frame, text="YOU BUSTED, YOU LOSE")
            self.losercard.pack(side="left", padx=100, pady=100)
            self.hit_button['state'] = 'disabled'
            self.stand_button['state'] = 'disabled'
            self.end_game()
    def player_stand(self):
# Dealer's turn 
        while self.dealer.handValue() < 17:
            self.dealer.draw(self.deck)  
        self.update_gui()
        if self.player.handValue() > 21:
                self.losercard = tk.Label(self.game_frame, text="YOU BUSTED, YOU LOSE")
# Check who won the game
        if self.dealer.handValue() > 21:
            self.winnercard = tk.Label(self.game_frame, text="DEALER BUSTED, YOU WIN")
        elif self.dealer.handValue() > self.player.handValue():
            self.winnercard = tk.Label(self.game_frame, text="DEALER WINS")
        elif self.dealer.handValue() < self.player.handValue():
            self.winnercard = tk.Label(self.game_frame, text="YOU WIN")
        else:
            self.winnercard = tk.Label(self.game_frame, text="IT'S A TIE")

            self.losercard.pack(side="left", padx=100, pady=100)
            self.hit_button['state'] = 'disabled'
            self.stand_button['state'] = 'disabled'
            if self.player.handValue() > 21 or self.dealer.handValue() > 21 or self.dealer.handValue() != self.player.handValue():
                self.end_game()
    def end_game(self):
        self.root.quit()
    def run(self):
        self.update_gui()
        self.root.mainloop()
            
app = MyApp()
app.run()

# class MyApp:
#     def __init__(self):
#         self.root = Tk()
#         self.game_frame = tk.LabelFrame(root, bg="gray")
#         self.game_frame.pack(fill="both", expand="yes")
#         self.card_back_image = Image.open(f'C:\\Users\\jbrou\\bj\\resources\\cards\\cardback.png')
#         self.card_back_photo = ImageTk.PhotoImage(self.card_back_image)
#         self.deck = SixDeck()
#         self.player.draw(deck)
#         self.dealer.draw(deck)
        
#     def deal(self):
#         card = self.deck.draw()
#         def update_gui(self):
#             def card_image_filename(card):
#             # Assuming the value of face cards are represented as 'J', 'Q', 'K', and 'A'
#                 value_map = {1: 'A', 11: 'J', 12: 'Q', 13: 'K'}
#             card_value = value_map.get(card.val, str(card.val))
#             return f'{card_value.lower()}{card.suit[0].lower()}.png'

#         deck = SixDeck()
#         deck.shuffle()
#         player = Player()
#         dealer = Dealer()
#         # Create the main window
#         root = tk.Tk()
#         root.title("Blackjack")
#         game_frame = tk.LabelFrame(root, bg="gray")
#         card_back_image = Image.open(f'C:\\Users\\jbrou\\bj\\resources\\cards\\cardback.png')
#         card_back_photo = ImageTk.PhotoImage(card_back_image)
#         # # def shuffle(self):
#         #     for i in range(1,15):
#         #         for i in range(len(self.cards) -1, 0, -1):
#         #             r = random.randint(0, i)
#         #             self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
#     def run(self):
#         self.root.mainloop()

#         app = MyApp()
#         app.run()   



# # --------------------------------------------------------------------------------------------------------------


# def update_gui(self):        
#     for widget in game_frame.winfo_children():
#         widget.destroy()

#     print("Your hand.. \n")
#     player_hand_label = tk.Label(game_frame, text=f"Player's Hand: {player.handValue()}")
#     player_hand_label.pack()
#     for card in player.hand:
#         card_filename = card_image_filename(card)
#         card_image_path = f'C:\\Users\\jbrou\\bj\\resources\\cards\\{card_filename}'
#         card_image = Image.open(card_image_path)
#         card_photo = ImageTk.PhotoImage(card_image)
#         card_label = tk.Label(game_frame, image=card_photo)
#         card_label.image = card_photo
#         card_label.pack(side="left")
#         print("\n\n")

#     print("Dealer's hand")
#     dealer_hand_label = tk.Label(game_frame, text="Dealer's Hand: ???")
#     dealer_hand_label.pack()
#     for card in dealer.hand[:-1]:  # Hide the last card of the dealer
#         card_filename = card_image_filename(card)
#         card_image_path = f'C:\\Users\\jbrou\\bj\\resources\\cards\\{card_filename}'
#         card_image = Image.open(card_image_path)
#         card_photo = ImageTk.PhotoImage(card_image)
#         card_label = tk.Label(game_frame, image=card_photo)
#         card_label.image = card_photo
#         card_label.pack(side="right")
#     # Add card back for hidden card
#     hidden_card_label = tk.Label(game_frame, image=card_back_photo)
#     hidden_card_label.image = card_back_photo
#     hidden_card_label.pack(side="right")


#     def hit():
#         player.draw(deck)
#         update_gui()
#         if player.handValue() > 21:
#             messagebox.showinfo("Game Over", "Player busts! Dealer wins.")
#             root.destroy()
#         else:
#             if player.handValue() <= 21:
#                 print(hit_button) + (stand_button)            
#                 turn2 = input.lower("Would you like to take a hit or stay with your current cards?\n")
#                 if turn2 == "yes" or turn2 == "ya":
#                     player.draw(deck)

#     def stand():
#         # Reveal dealer's full hand and play dealer's turn
#         while dealer.handValue() < 17:
#             dealer.draw(deck)
#             print("The dealer currently is below 17, he draws his third card....")
#         update_gui()

#         # Determine the winner
#         player_score = player.handValue()
#         dealer_score = dealer.handValue()
#         if dealer_score > 21 or player_score > dealer_score:
#             messagebox.showinfo("Game Over", "Player wins!")
#         elif player_score < dealer_score:
#             messagebox.showinfo("Game Over", "Dealer wins!")
#         else:
#             messagebox.showinfo("Game Over", "It's a tie!")

#         root.destroy()

#         # Add hit and stand buttons
#         hit_button = tk.Button(game_frame, text="Hit", command=hit)
#         hit_button.pack(side="bottom")
#         stand_button = tk.Button(game_frame, text="Stand", command=stand)
#         stand_button.pack(side="bottom")

#         # Update the GUI for the first time

#         # Start the Tkinter loop
#         root.mainloop()
