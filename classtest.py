import random
import logging

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

class Player(object):
    def __init__(self, name, number):
        self.name = name 
        self.number = number 
        self.coins = 2 # everyone starts with 2 coins 
        self.points = 0
        self.is_turn = 0
        self.cards_in_hand = 0
        self.has_king_figure = 0
        self.character = "UNASSIGNED"
        self.has_picked = 0 

    def pick_character(self, character):
        """Lets a player pick a character from the deck and removes that element
        from the deck

        input: LIST, INT
        output: DECK
        side effects: mutates deck and player.character 
        """
        global character_deck
        if character in character_deck:
            self.character = character
            self.has_picked = 1
            character_deck.remove(character)
        else:
            raise ValueError("Picked character not in deck")
            logger.warning("Picked character not in deck")

name = "Jan"
playernumber = 1

NUMBER_OF_PLAYERS = 4

# Instantiate players 
player1 = Player(name, playernumber)
print player1.name
print player1.coins
player1.coins = player1.coins + 1 
print player1.coins


def nextplayer(player_number): 
    global NUMBER_OF_PLAYERS 
    if player_number > NUMBER_OF_PLAYERS or player_number < 1:
        raise ValueError("nextplayer() called with player_number > NUMBER_OF_PLAYERS")
        logger.warning("Calling nextplayer with wrong argument.")
    elif player_number == NUMBER_OF_PLAYERS:
        return 1
    else: 
        return player_number + 1 

character_deck = ['assassin', 'thief', 'architect', 'bishop', 'king', 'magician', 'merchant', 'warlord']

def remove_characters(deck):
    """ Silently removes 1 character, then depending on amount of players removes
    either 0, 1, or 2 and announces which ones have been removed.

    input: LIST
    output: LIST
    """
    global NUMBER_OF_PLAYERS 
    facedown_remove = random.choice(deck)
    logger.info("Removed one character from deck face down: {0}".format(facedown_remove))
    deck.remove(facedown_remove)

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
    faceup_remove = random.sample(deck, characters_to_remove)
    for character in faceup_remove:
        deck.remove(character)
    print("Removed face down {}".format(facedown_remove))
    print("Removed face up {}".format(faceup_remove))
    return deck


print "Original character deck", character_deck 
characters_to_pick = remove_characters(character_deck)
print "New character deck" 

pickedclass = raw_input("Pick a character from {0}: \n".format(characters_to_pick))
while True:
    print character_deck
    if pickedclass in character_deck:
        print "player picked {0}".format(pickedclass)
        player1.pick_character(pickedclass)
        break
    else:
        print "Character not in deck. Try again. \n"
        pickedclass = raw_input()

