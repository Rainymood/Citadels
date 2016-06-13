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
    def __init__(self, name, seat_number):
        self.name = name 
        self.seat_number = seat_number
        self.coins = 2 # everyone starts with 2 coins 
        self.points = 0
        self.is_turn = 0
        self.cards_in_hand = 0
        self.has_king_figure = 0
        self.character = "UNASSIGNED"
        self.has_picked = 0 
        self.rank = 0 

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

NUMBER_OF_PLAYERS = 4 # raw input later 
PLAYER_NAMES = ['Jan', 'Jelle', 'Lasse', 'Woody'] # change to raw input later 

# Generate player objects and put them in a list 
players = []
for i in xrange(NUMBER_OF_PLAYERS):
    # player[0] == player1 !! 
    # seatnumber is a number between 1 and NUMBER_PLAYERS 
    playerobject = Player(PLAYER_NAMES[i], i+1)
    players.append(playerobject)

def nextplayer(player_number): 
    global NUMBER_OF_PLAYERS 
    if player_number > NUMBER_OF_PLAYERS or player_number < 1:
        raise ValueError("nextplayer() called with player_number > NUMBER_OF_PLAYERS")
        logger.warning("Calling nextplayer with wrong argument.")
    elif player_number == NUMBER_OF_PLAYERS:
        return 1
    else: 
        return player_number + 1 


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

print """
================================================================================
    ..|'''.| '||' |''||''|     |     '||''|.   '||''''|  '||'       .|'''.|  
  .|'     '   ||     ||       |||     ||   ||   ||  .     ||        ||..  '  
  ||          ||     ||      |  ||    ||    ||  ||''|     ||         ''|||.  
  '|.      .  ||     ||     .''''|.   ||    ||  ||        ||       .     '|| 
   ''|....'  .||.   .||.   .|.  .||. .||...|'  .||.....| .||.....| |'....|'
================================================================================
"""

print "====== PHASE 1: REMOVE CHARACTERS ===== \n"
character_deck = ['assassin', 'thief', 'architect', 'bishop', 'king', 'magician', 'merchant', 'warlord']
print "Original character deck:", ", ".join(character_deck)
remove_characters()
print "Characters to pick from:", ", ".join(character_deck)

print "\n===== PHASE 2: PICK CHARACTERS ===== \n"
for player in players:
    print"Characters available to choose from: ",", ".join(character_deck)
    pickedclass = raw_input("Pick a character: ")
    while True:
        if pickedclass in character_deck:
            print "player {0} picked {1}".format(player.seat_number, pickedclass)
            player.pick_character(pickedclass)
            break
        else:
            print "Character not in deck. Try again. "
            pickedclass = raw_input("Pick a character: ")

