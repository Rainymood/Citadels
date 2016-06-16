class Card(object):
    def __init__(self, name, description, cost, points):
    # effects are incorporated in the game logic 
        self.name = name
        self.description = description
        self.cost = cost
        self.points = points
        self.color = color

# migrate to different file and import cards
tavern = Card(name = "tavern",
              description = "A tavern.",
              cost = 1,
              points = 1,
              color = "green"
              )
