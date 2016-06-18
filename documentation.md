

At any point in your turn you can use your CharacterAbility(). Some are split. 

Character: Assassin
Turn: 1
Description: Announce a character you wish to murder. The murdered character
misses his entire turn. 
Ability: CharacterAbility(role = assassin)
Check if charactername =/= thief

Character: Thief
Turn: 2
Description: Announce a character from whom you wish to steal. When the player
with this card is revealed, take his gold.
Ability: CharacterAbility(role = thief, target = CharacterName)
Check if charactername =/= thief



Player has:
    -- variables -- 
    player.number  (1, 2, 3, .. , AMOUNT_PLAYERS)
    player.name (string)
    player.coins (int)
    player.buildings (array)
    player.points (int)
    player.cards_in_hand (array)
    player.is_turn (bool)
    player.has_king_figure (bool)
    player.character (string)
    player.turn_rank (characters.rank derived from player.character)
    player.passive_effects  (derived from player.character and player.buildings) 
    player.built_this_round  (max 1, expand to 3 if player.character = architect) 
    -- functions -- 
    player.start_action(x) (+2 gold or +2 cards from pile and discard 1) 
    player.character_ability(optional = target)
    player.send_msg(string) (for chatting, i.e. Turn 1. Player 1 (Thief) says: .. )
    player.build_building(card_id) (build building from hand)
    player.draw_card(amount) 
    player.discard_card() (to_discard_from = hand or last 2 cards)
    player.reveal_role()

Deck:
    -- variables --
    deck.cards (array)
    -- functions --
    deck.init() (random new deck)
    deck.shuffle()

CharacterDeck: 
    -- variables --
    CharacterDeck.Characters (list)
    -- functions -- 
    CharacterDeck.character_picked()
    CharacterDeck.shuffle() 
    CharacterDeck.discard(optional = open/closed) default is closed 
    
Character:
    -- variables --

    -- functions --

Card:
    -- variables --
    card.id
    card.name
    card.cost
    card.points
    card.description
    card.effcts
    --functions --
    card.show_info(card_id)
    

game:
    -- variables --
    game.deck(dict)
    game.characters(dict)
    -- functions --
    game.init_deck() (create new shuffle deck)
    game.nextround() 
        refreshes has_picked counters
        checks new startplayer
        refreshes character_deck 
        set all player.characters = "UNASSIGNED"



5	Tavern	1 green 
4	Market	2 green 
3	Trading Post	2 green 
3	Docks	3 green 
3	Harbor	4 green
2	Town Hall	5 green 
3	Temple	1 blue 
3	Church	2 blue 
3	Monastery	3 blue 
2	Cathedral	5 blue 
3	Watchtower	1 red 
3	Prison	2 red 
3	Battlefield	3 red 
2	Fortress	5 red 
5	Manor	3 yellow 
4	Castle	4 yellow 
3	Palace	5 yellow 
1	Haunted City2 purple 

2	Keep	3 purple 
1	Laboratory	5 purple 
1	Smithy	5 purple 
1	Graveyard	5 purple 
1	Observatory	5 purple 
1	School of Magic	6 purple 
1	Library	6 purple 
1	Great Wall	6 purple 
1	University	8 purple 
1	Dragon Gate	8 purple

--------------------------------------------------------------------------------

UML: name (PlayerAccount), variables, functions 

Elements outside the __init__ method are static elements, it means, they belong
to the class.  
Elements inside the __init__ method are elements of the object (self), they
don't belong to the class.


accepted
I like to use double quotes around strings that are used for interpolation or
that are natural language messages, and single quotes for small symbol-like
strings, but will break the rules if the strings contain quotes, or if I forget.
I use triple double quotes for docstrings and raw string literals for regular
expressions even if they aren't needed.

deck.sort() returns None, sorst the list in place. 
