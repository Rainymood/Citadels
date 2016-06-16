import csv 
from random import shuffle

class Card(object):
    def __init__(self, name, description, cost, points, color, amount):
    # effects are incorporated in the game logic 
        self.name = name
        self.description = description
        self.cost = cost
        self.points = points
        self.color = color
        self.amount = amount

CARDS = {}
with open('cards.csv', 'rU') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', dialect =csv.excel_tab)
    for row in reader:
        card_object = Card(name = row['name'],
                           description = row['description'],
                           cost = int(row['cost']),
                           points = int(row['points']),
                           color = row['color'],
                           amount = int(row['amount'])
                           )
        CARDS[row['name']] = card_object

def create_shuffled_deck(CARDS):
    # creates deck list from cards object
    deck = []
    for key in CARDS:
        for _ in xrange(CARDS[key].amount):
            deck.append(key)
        print "Added", key, CARDS[key].amount, "times"
    shuffle(deck)
    return deck

deck = create_shuffled_deck(CARDS)
print deck


