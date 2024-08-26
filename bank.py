from Roll import Roll
from OverDoublesThresholdPlayer import OverDoublesThresholdPlayer
from OverScoreThresholdPlayer import OverScoreThresholdPlayer
from ScoreAndDoublesThresholdPlayer import ScoreAndDoublesThresholdPlayer
from GameStats import GameStats

from tabulate import tabulate

def play_round(round_number, players, game_stats):
    for player in players:
        player.start_new_round()
    
    round_total = 0
    
    for i in range(0, 3):
        roll = Roll()
        roll_sum = roll.get_sum()
        score = roll_sum if roll_sum != 7 else 70
        game_stats.record_score(round_number, score)
        round_total += score

    while True:
        # Roll the dice and adjust the pot
        roll = Roll()
        if roll.get_sum() == 7:
            return round_total
        elif roll.is_doubles():
            score = round_total
        else:
            score = roll.get_sum()
        
        game_stats.record_score(round_number, score)
        round_total += score

        # Let players bank or continue based on the last roll and/or the current round total
        for player in players:
            if player.is_in_round():
                player.bank_or_play(roll, round_total)


def play_game(players, rounds):
    for player in players:
        player.start_new_game()

    game_stats = GameStats(players)

    for i in range(0, rounds):
        play_round(i, players, game_stats)
    
    players.sort(key=lambda p: p.score, reverse=True)

    for i in range(0, len(players)):
        players[i].add_rank(i + 1)


def main():
    players = [
        OverScoreThresholdPlayer("OverOneHundredPlayer", 100), 
        OverDoublesThresholdPlayer("TwoDoublesPlayer", 2),
        OverDoublesThresholdPlayer("ThreeDoublesPlayer", 3),
        OverScoreThresholdPlayer("OverThreeHundredPlayer", 300),
        OverScoreThresholdPlayer("OverOneThousandPlayer", 1000),
        ScoreAndDoublesThresholdPlayer("OverTwoDoublesAndOverTwoHundredPlayer", 2, 300)
    ]
    games = 10000
    rounds = 10
    
    for i in range(0, games):
        play_game(players, rounds)

    players.sort(key=lambda p: p.name)

    print(tabulate([player.get_player_stats() for player in players], headers=["Player", f"Mean Rank (of {len(players)})", "Median Game Score", "Mean Banks/Game"], tablefmt="grid"))


if __name__ == "__main__":
    main()
