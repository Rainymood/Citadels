# -*- coding: utf-8 -*-
import random
import time 
import os
import platform
import logging
import textwrap
#from __future__ import print_functions
from pprint import pprint
from cards import CARDS # import card objects 
from cards import deck
os.system("mode con: cols=80 lines=80")

# set up logger 
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create a file handler
handler = logging.FileHandler('hello.log')
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)
logger.info("Starting program")

CHARACTER_RANKS = {
        'assassin':  1,
        'thief':     2,
        'magician':  3,
        'king':      4,
        'bishop':    5,
        'merchant':  6,
        'architect': 7,
        'warlord':   8
}

CHARACTER_DECK = ['assassin', 'thief', 'architect', 'bishop', 'king', 'magician', 'merchant', 'warlord']

class Player(object):
    def __init__(self, name, seat_number):
        self.name = name 
        self.seat_number = seat_number # used for queen character
        self.coins = 2 # everyone starts with 2 coins 
        self.is_turn = 0 # perhaps depreciated? 
        self.is_murdered = 0
        self.is_being_stolen_from = 0 
        self.character = "UNASSIGNED"
        self.has_picked = 0 # character
        self.has_taken = 0 # has taken either gold or +2 cards and then -1
        self.has_used_power = 0
        self.has_king_figure = 0
        self.rank = 0 
        self.character_visible = 0
        # buildings 
        self.buildings_built = []
        self.has_built = 0 # has built during his turn  yes/no
        self.amount_built = 0 
        self.yellow_buildings = 0 
        self.green_buildings = 0
        self.blue_buildings = 0
        self.red_buildigs = 0
        self.purple_buildings = 0
        # cards 
        self.cards_in_hand = [] 
        self.amount_cards_in_hand = len(self.cards_in_hand) # show back web

    def pick_character(self, character):
        """Lets a player pick a character from the deck and removes that element
        from the deck

        input: LIST, INT
        output: DECK
        side effects: mutates deck and player.character 
        """
        global character_deck
        global CHARACTER_RANKS
        if character in character_deck:
            self.character = character
            self.rank = CHARACTER_RANKS[character]
            self.has_picked = 1
            character_deck.remove(character)
        else:
            raise ValueError("Picked character not in deck")
            logger.warning("Picked character not in deck")
    
    def use_power(self):
        print "{0} is invoking the {1}'s power!".format(self.name, self.character)
        self.has_used_power = 1 
        ### ASSASSIN ###
        if self.character == 'assassin':
            # desc
            print "The Assassin's power reads as follows:"
            print "(Active) Announce a character you wish to murder. The murdered character misses his entire turn."
            # user 
            targets = ['thief', 'magician', 'king', 'bishop', 
                    'merchant', 'architect', 'warlord']

            print "List of possible targets: "+', '.join(targets)
            target = raw_input("Announce a character you wish to murder: ")
            while target not in targets:
                print "Invalid target."
                target = raw_input("Announce a character you wish to murder: ")
            print "O lord! The {0} has been murdered!".format(target)
            for player in players:
                if player.character == target:
                    player.is_murdered = 1
        ### THIEF ### 
        elif self.character == 'thief':
            # desc
            print "The Thief's power reads as follows: " 
            print "Announce a character from whom you wish to steal. When that character is revealed, take his gold."
            # user 
            targets = ['assassin', 'magician', 'king', 'bishop', 'merchant', 'architect', 'warlord']
            print "List of possible targets: "+', '.join(targets)
            target = raw_input("Announce a character you steal to from: ")
            while target not in targets:
                print "Invalid target."
                target = raw_input("Announce a character you wish to steal from: ")
            print "The thief has stolen the {0}'s gold!".format(target)
            for player in players:
                if player.character == target:
                    player.is_being_stolen_from = 1
            
        ### MAGICIAN ### 
        elif self.character == 'magician':
            pass
        ### KING ###
        elif self.character == 'king':
            pass
        ### BISHOP ### 
        elif self.character == 'bishop':
            # print bishop.description()
            print "The Bishop's power reads as follows:"
            print "(Active) You receive 1 gold for each religious (blue) district in your city."
            print "(Passive) Your districts can not be destroyed by the Diplomat or Warlord."
            # user 
            print "{0} has {1} blue buildings and thus receives {2} gold.".format(self.name, self.blue_buildings, self.blue_buildings)
            self.coins += self.blue_buildings
            print "{0} now has {1} gold.".format(self.name, self.coins)
        ### MERCHANT ### 
        elif self.character == 'merchant':
            # desc
            print "The Merchant's power reads as follows: "
            print "(Active) You receive 1 gold for each trade (green) district in your city."
            print "(Passive) After you take an action, you receive one additional gold."
            # user 
            print "{0} has {1} green buildings and thus receives {2} gold.".format(self.name, self.green_buildings, self.green_buildings)
            self.coins += self.green_buildings
            print "{0} now has {1} gold.".format(self.name, self.coins)
        ### ARCHITECT ### 
        elif self.character == 'architect':
            print "The Architect's power reads as follows: "
            print "(Passive) After you take an action, draw two extra cards and put both in your hand."
            print "(Passive) You may build up to three districts turing your turn"
            print "Nothing happens."
        ### WARLORD ### 
        elif self.character == 'warlord':
            # check if building destroyed is owned by bishop 
            pass

    def build(self):
        print "player builds building"
        pass 
        # check duplicates (can not build more than 2)

    def take_action(self, arg):
    # take_action(gold) or take_action(draw)
        player.has_taken = 1
        if arg == "gold":
            self.coins += 2
            print "{0} received 2 gold. {0} now has {1} gold.\n".format(self.name, self.coins)
        elif arg == "draw":
            self.draw(2, discard=1)
        elif arg == "power":
            self.use_power()
        else:
            pass

    def draw(self, amount, discard):
    # mutates deck (current play deck of game)
    # werkt nog niet goed met updaten observatory 
        print "{0} drew {1} cards and will discard {2}.".format(self.name, amount, discard)
        if discard == 0:
            for i in xrange(amount):
                drawn_card = deck[0]
                self.cards_in_hand.append(drawn_card)
                deck.remove(drawn_card)
                print "(HIDDEN) You drew {0}. Added to hand".format(drawn_card)
                print "Cards in hand: {0}".format(', '.join(self.cards_in_hand))
        else:
            # WARNING! Not functional if discard =/= 1 or 0 I think 
            if 'Observatory' in self.buildings_built:
                # draw 2+1 and put 2 on bottom of deck
                print "Because of the Observatory, {0} may draw 3 cards and choose 1. The discarded cards go to the bottom of the deck.".format(self.name)
                drawn_cards = []
                for i in xrange(amount+1):
                    drawn_cards.append(deck[i])
                print "You drew {0}".format(', '.join(drawn_cards))

                keep_card = raw_input("What card do you wish to keep: ")
                while keep_card not in drawn_cards:
                    keep_card = raw_input("What card do you wish to keep: ")

                drawn_card = keep_card
                drawn_card_index = drawn_cards.index(keep_card)
                deck.remove(deck[drawn_card_index])
                # silly .remove() returning none... list comprehension then
                discarded_cards = [x for x in drawn_cards if x != keep_card]
                deck.extend(discarded_cards)
                print "(HIDDEN) added {0} to bottom of the deck".format(', '.join(discarded_cards))
                self.cards_in_hand.append(drawn_card)
                print "Cards in hand: {0}".format(', '.join(self.cards_in_hand))
            else:
                drawn_cards = []
                for i in xrange(amount):
                    drawn_cards.append(deck[i])
                print "You drew {0}".format(', '.join(drawn_cards))
                keep_card = raw_input("What card do you wish to keep: ")
                while keep_card not in drawn_cards:
                    keep_card = raw_input("What card do you wish to keep : ")

                drawn_card = keep_card
                drawn_card_index = drawn_card.index(keep_card)

                deck.remove(deck[drawn_card_index])
                self.cards_in_hand.append(drawn_card)
                print "Cards in hand: {0}".format(', '.join(self.cards_in_hand))

    def show(self):
        print "Your name is {}".format(self.name)
        print "(HIDDEN) You are playing as the {}".format(self.character)
        print "You currently have {} coins".format(self.coins)
        print "And you have {} cards in your hand".format(self.amount_cards_in_hand)
        if self.has_used_power == 1:
            print "You have used your power already."
        else:
            print "You have not used your power yet."
        if self.has_king_figure == 1:
            print "You are in posession of the king figure."
        else:
            print "You are not in posession of the king figure."
        print ""

    def show_own_board(self):
        print '{:^80}'.format('-'*33 + "Cards in hand:" + '-'*33)
        print
        self.show_cards(self.cards_in_hand)
        print '{:^80}'.format('-'*32 + "Built buildings:" + '-'*32)
        self.show_cards(self.buildings_built)
        print "Your player name is {}".format(self.name)
        print "You are playing as the {}".format(self.character)
        print "You currently have {} coins".format(self.coins)

        if self.has_used_power == 1:
            print "You have used your power already."
        else:
            print "You have not used your power yet."
        if self.has_king_figure == 1:
            print "You are in posession of the king figure."
        else:
            print "You are not in posession of the king figure."
        print ""

    def show_board_to_public(self):
        print '{:^80}'.format('-'*32 + "Built buildings:" + '-'*32)
        self.show_cards(self.buildings_built)
        print "Player name: {0}".format(self.name)
        print "Character: {0}".format(self.character if self.character_visible else "Hidden")

    def show_cards(self, cards):
        global CARDS

        amount_of_cards = len(cards)
        max_line_length = 22
        max_lines = 15
        print_table = ["" for x in range(amount_of_cards)]

        for card, i in zip(cards, range(amount_of_cards)):
            print_table[i] = [""]
            print_table[i].append("-"*max_line_length)
            print_table[i].append('~ ' + CARDS[card].name + ' ~')
            print_table[i].append("Cost: " + 'O ' * CARDS[card].cost + (CARDS[card].points - CARDS[card].cost) * '0 ' )
            print_table[i].append("Color: " + CARDS[card].color)
            print_table[i].append("")

            split_description = (textwrap.fill(CARDS[card].description, max_line_length)).splitlines()

            for line in split_description:
                print_table[i].append(str(line))

            while len(print_table[i]) < max_lines: 
                print_table[i].append("")

            print_table[i].append("-" * max_line_length)

            del print_table[i][0]

        # Print cards on multiple rows if there is more than 3
        if amount_of_cards > 3:
            temp_table = [print_table[i:i+3] for i in range(0, len(print_table), 3)]

            for l in temp_table:
                self.print_cards(l, max_lines, len(l))
                print
        else: 
            self.print_cards(print_table, max_lines, amount_of_cards)

    # A function to print a 2d list as a card.
    def print_cards(self, cards_print, max_cols, max_rows):
        for i in range(max_cols):
            for j in range(max_rows):
                val = cards_print[j][i]
                if type(val) is str and val.startswith('~'):
                    print '|{:^22}|'.format(val),
                elif val.startswith('-'):
                    print 'o{:<22}o'.format(val ),
                else:
                    print '|{:<22}|'.format(val ),
            print




### GENERATE PLAYER OBJECTS ### 

NUMBER_OF_PLAYERS = 4 # raw input later 
PLAYER_NAMES = ['Jan', 'Jelle', 'Lasse', 'Woody'] # change to raw input later 

# Generate player objects and put them in a list 
players = []
for i in xrange(NUMBER_OF_PLAYERS):
    playerobject = Player(PLAYER_NAMES[i], i+1)
    players.append(playerobject)

# Convenient when debugging (player1.character = .. etc)
player1 = players[0]
player2 = players[1]
player3 = players[2]
player4 = players[3]

players[3].character_visible = 1

def genr_hand(amount):
    # generates random hand of cards (list) of length amount
    hand = []
    for i in xrange(amount):
        hand.append(random.choice(deck))
    return hand

players[0].cards_in_hand = genr_hand(5)
players[1].cards_in_hand = genr_hand(1)
players[2].cards_in_hand = genr_hand(10)
players[3].cards_in_hand = genr_hand(2)

players[0].buildings_built = ['Temple','Harbour']
players[1].buildings_built = ['Library', 'Smithy']
players[2].buildings_built = ['School of Magic']
players[3].buildings_built = ['Keep', 'Graveyard', 'Tavern']


def nextplayer(player_number): 
    global NUMBER_OF_PLAYERS 
    if player_number > NUMBER_OF_PLAYERS or player_number < 1:
        raise ValueError("nextplayer() called with player_number > NUMBER_OF_PLAYERS")
        logger.warning("Calling nextplayer with wrong argument.")
    elif player_number == NUMBER_OF_PLAYERS:
        return 1
    else: 
        return player_number + 1 

def show_board_to_player(player):
    for other_player in players:
        if other_player is not player:
            other_player.show_board_to_public()

def remove_characters():
    """ Silently removes 1 character, then depending on amount of players removes
    either 0, 1, or 2 and announces which ones have been removed.

    input: LIST
    output: LIST
    """
    global NUMBER_OF_PLAYERS 
    global character_deck 
    facedown_remove = random.choice(character_deck)
    logger.info("Removed one character from deck face down: {0}".format(facedown_remove))
    character_deck.remove(facedown_remove)

    # TODO implement 2, 3, and 7 special cases 
    if NUMBER_OF_PLAYERS == 6 or NUMBER_OF_PLAYERS == 7:
       characters_to_remove = 0
    elif NUMBER_OF_PLAYERS == 5:
        characters_to_remove = 1
    elif NUMBER_OF_PLAYERS == 4:
        characters_to_remove = 2
    else:
        raise ValueError("HAVENT IMPLEMENTED 2, 3 or 7 players yet.")
        logger.warning("Unimplemented amount of players")
    faceup_remove = random.sample(character_deck, characters_to_remove)
    for character in faceup_remove:
        character_deck.remove(character)
    print "(HIDDEN) Characters removed face down: {}".format(facedown_remove.encode("hex"))
    print "Characters revealved on table: {}".format(', '.join(faceup_remove))

SLEEPY = 0

print """
================================================================================
    ..|'''.| '||' |''||''|     |     '||''|.   '||''''|  '||'       .|'''.|  
  .|'     '   ||     ||       |||     ||   ||   ||  .     ||        ||..  '  
  ||          ||     ||      |  ||    ||    ||  ||''|     ||         ''|||.  
  '|.      .  ||     ||     .''''|.   ||    ||  ||        ||       .     '|| 
   ''|....'  .||.   .||.   .|.  .||. .||...|'  .||.....| .||.....| |'....|'
================================================================================
"""

print  "====== PHASE 0: REFRESH TURN ===== \n"

# give king figure to oldest player if no one has king
# set has_picked = 0 for all players 


print "====== PHASE 1: REMOVE CHARACTERS ===== \n"

if SLEEPY: time.sleep(1)

character_deck = ['assassin', 'thief', 'architect', 'bishop', 'king', 'magician', 'merchant', 'warlord']
print "Original character deck:", ", ".join(character_deck)
remove_characters()
print "Characters to pick from:", ", ".join(character_deck)

if SLEEPY: time.sleep(1)


print "\n===== PHASE 2: PICK CHARACTERS ===== \n"

for player in players:
    print"Characters available to choose from: ",", ".join(character_deck)
    #pickedclass = raw_input("Pick a character: ")
    # TODO remove after testing
    pickedclass = random.choice(character_deck)
    while True:
        if pickedclass in character_deck:
            print "(HIDDEN) player {0} picked {1}".format(player.seat_number, pickedclass)
            player.pick_character(pickedclass)
            #print "player ranked {0}".format(player.rank)
            break
        else:
            print "Character not in deck. Try again. "
            pickedclass = raw_input("Pick a character: ")

if SLEEPY: time.sleep(1)

print "\n==== PHASE 3: PLAYER TURNS ==== \n"

for rank in range(1,9):
    for player in players:
        if player.rank == rank:
            print "=== PLAYER: {0} ({1}) ===\n".format(player.name, player.character)
            player.character_visible = 1
            turn_end = False
            while not turn_end:
                actions = {'show': 'show information'}
                if player.has_used_power == 0:
                    actions['power'] = 'to use character power.'
                if turn_end == False:
                    actions['end'] = 'to end turn.'
                if player.has_taken == 0:
                    actions['coins'] = 'to receive 2 coins.'
                    actions['draw'] = 'to draw 2 cards and discard 1.'
                if player.has_built == 0:
                    actions['build'] = 'to build .'
                if player.has_taken == 0 and player.has_built == 0:
                    actions.pop('build', None)
                if len(player.cards_in_hand) > 0:
                    actions['show hand'] = "Shows your hand"

                for action in actions:
                   print "--",action, "-- ", actions[action]
                print ""

                action = raw_input("Type your action: ")
                print "" 
                while action not in actions.keys():
                    print "Invalid action.\n"
                    action = raw_input("Type your action: ")
                    print ""

                if action == "power":
                    player.use_power()
                elif action == "coins":
                    player.take_action("gold")
                elif action == "draw":
                    player.take_action("draw")
                elif action == "build":
                    player.build()
                elif action == "end":
                    turn_end = True
#                elif action == "show":
#                    player.show()
                elif action == "show":
                    show_board_to_player(player)
                    #player.show_own_board()
                elif action == "show hand":
                    player.show_own_board()
