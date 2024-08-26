from random import randint

class Roll():
    def __init__(self, early_roll=False):
        self.roll = [randint(1, 6), randint(1, 6)]
        self.sum = self.roll[0] + self.roll[1]
        self.early_roll = early_roll

    def get_roll(self):
        return self.roll
    
    def get_sum(self):
        return self.sum
    
    def is_doubles(self):
        return self.roll[0] == self.roll[1]
    
    def __repr__(self):
        return f"Roll [{self.roll[0]}, {self.roll[1]}]"