# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, location, score, inventory = []):
        self.location = location
        self.inventory = inventory
        self.score = score

    def __str__(self):
        return 'Current Location: {}, Current inventory: {}'.format(self.location, self.inventory)

    def change_location(self, new_location):
        self.location = new_location
