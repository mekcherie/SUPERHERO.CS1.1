
import random

class Armor:
    def __init__(self, name, max_block):
        '''
        Initialize the values passed into this method as instance variables.
        '''
        self.name = name
        self.max_block = max_block

    def block(self):
        random_block_value = random.randint(0, int(self.max_block))
        return random_block_value
















    if __name__ == "__main__":
        # If you run this file from the terminal
        # this block is executed.
        armor = Armor("Debugging Shield", 10)
        print(armor.name)
        print(armor.block())