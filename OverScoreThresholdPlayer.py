from Player import Player

# This player banks any time the pot is greater than or equal to a specified threshold
class OverScoreThresholdPlayer(Player):
    def __init__(self, name, threshold):
        super().__init__(name)
        self.threshold = threshold

    def _should_bank(self, roll, round_total):
        return round_total >= self.threshold
