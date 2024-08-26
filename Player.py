from PlayerStats import PlayerStats

class Player():
    def __init__(self, name):
        self.name = name
        self.in_round = True
        self.score = 0
        self.player_stats = PlayerStats()

    def bank_or_play(self, roll, round_total):
        if self._should_bank(roll, round_total):
            self._bank(round_total)

    def _bank(self, round_total):
        self.score += round_total
        self.in_round = False
        self.player_stats.add_round_score(round_total)

    def start_new_game(self):
        self.score = 0
        self.player_stats.start_new_game()

    def start_new_round(self):
        self.in_round = True
        self.player_stats.start_new_round()

    def add_rank(self, rank):
        self.player_stats.add_rank(rank)

    def get_player_stats(self):
        return [self.name] + self.player_stats.get_stats()

    def is_in_round(self):
        return self.in_round
    
    def _should_bank(self, roll, round_total):
        pass

    