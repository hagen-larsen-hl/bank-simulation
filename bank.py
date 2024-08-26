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
        OverScoreThresholdPlayer("Over100Player", 100), 
        OverScoreThresholdPlayer("Over200Player", 200), 
        OverScoreThresholdPlayer("Over300Player", 300), 
        OverScoreThresholdPlayer("Over400Player", 400), 
        OverScoreThresholdPlayer("Over500Player", 500),
        OverScoreThresholdPlayer("Over600Player", 600),
        OverScoreThresholdPlayer("Over700Player", 700),
        OverScoreThresholdPlayer("Over800Player", 800),
        OverScoreThresholdPlayer("Over900Player", 900)
    ]
    GAMES = 10000
    ROUNDS = 20
    
    for i in range(0, GAMES):
        play_game(players, ROUNDS)

    players.sort(key=lambda p: p.name)

    print(tabulate([player.get_player_stats() for player in players], headers=["Player", f"Mean Rank (of {len(players)})", "Median Game Score", "Mean Banks/Game"], tablefmt="grid"))


if __name__ == "__main__":
    main()
