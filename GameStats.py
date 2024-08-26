import statistics as stats

class GameStats():
    def __init__(self, players):
        self.game_total = 0
        self.round_scores = []
        self.players = players

    def get_game_total(self):
        return self.game_total
    
    def record_score(self, round_number, score):
        if round_number == len(self.round_scores):
            self.round_scores.append([])
        
        self.round_scores[round_number].append(score)
        self.game_total += score
    
    def get_mean_round_score(self):
        return stats.mean([sum(round) for round in self.round_scores])
    
    # The length of a round does not inclue the '7' that ends the round
    def get_mean_round_length(self):
        return stats.mean([len(round) for round in self.round_scores])
