import random
import time 
import logging
import cards # import card objects 

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
        # buildings 
        self.has_built = 0
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
            print "{0} drew 2 cards and will discard one.".format(self.name)
        elif arg == "power":
            self.use_power()
        else:
            pass

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

print  "====== PHASE 0: REFRESH TURN ===== \n"

# give king figure to oldest player if no one has king
# set has_picked = 0 for all players 

time.sleep(1)

print "====== PHASE 1: REMOVE CHARACTERS ===== \n"

time.sleep(1)

character_deck = ['assassin', 'thief', 'architect', 'bishop', 'king', 'magician', 'merchant', 'warlord']
print "Original character deck:", ", ".join(character_deck)
remove_characters()
print "Characters to pick from:", ", ".join(character_deck)

time.sleep(1)


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

time.sleep(1)
print "\n==== PHASE 3: PLAYER TURNS ==== \n"

for rank in range(1,9):
    for player in players:
        if player.rank == rank:
            print "=== PLAYER: {0} ({1}) ===\n".format(player.name, player.character)

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
                elif action == "show":
                    player.show()
