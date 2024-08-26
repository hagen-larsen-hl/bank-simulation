from Player import Player

# This player banks any time the pot is greater than or equal to a threshold AND a certain ambount of doubles have been rolled
class ScoreAndDoublesThresholdPlayer(Player):
    def __init__(self, name, doubles_threshold, score_threshold):
        super().__init__(name)
        self.current_doubles = 0
        self.score_threshold = score_threshold
        self.doubles_threshold = doubles_threshold

    def _should_bank(self, roll, round_total):
        if roll.is_doubles():
            self.current_doubles += 1

        return round_total >= self.score_threshold and self.current_doubles >= self.doubles_threshold
