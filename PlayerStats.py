import statistics as stats
from tabulate import tabulate

class PlayerStats():

    def __init__(self):
        self.ranks = []
        # self.scores = [[round score, round score, ...], [round score, round score, ...], ...]
        # list of lists - a list of game scores, which are represented as a list of round scores
        # if the round score is zero, we can deduce the play did not bank
        self.scores = []

    def start_new_game(self):
        self.scores.append([])

    def start_new_round(self):
        self.scores[-1].append(0)

    def add_round_score(self, score):
        self.scores[-1][-1] = score

    def add_rank(self, rank):
        self.ranks.append(rank)

    def get_mean_rank(self):
        return stats.mean(self.ranks)
    
    def get_mean_game_score(self):
        game_scores = []
        for round_scores in self.scores:
            game_scores.append(sum(round_scores))
        return stats.mean(game_scores)
    
    def get_median_game_score(self):
        game_scores = []
        for round_scores in self.scores:
            game_scores.append(sum(round_scores))
        return stats.median(game_scores)
    
    def get_mean_banks(self):
        return stats.mean([len([score for score in round_score if score > 0]) for round_score in self.scores])

    def get_stats(self):
        return [self.get_mean_rank(), self.get_median_game_score(), self.get_mean_banks()]
