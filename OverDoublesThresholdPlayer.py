from Player import Player

# This player banks after a number of doubles are rolled during a round (after the first three rolls)
class OverDoublesThresholdPlayer(Player):

    def __init__(self, name, max_doubles):
        super().__init__(name)
        self.current_doubles = 0
        self.max_doubles = max_doubles

    def start_new_round(self):
        super().start_new_round()
        self.current_doubles = 0

    def _should_bank(self, roll, round_total):
        if roll.is_doubles():
            self.current_doubles += 1

        return self.current_doubles == self.max_doubles
