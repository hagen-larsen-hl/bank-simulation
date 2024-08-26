### Run Steps
1. As written, you will need to `pip install` the `tabulate` package to view the statistical output. Or you can change how things are printed.
2. You can just tweak the global variables `GAMES` AND `ROUNDS` then run `python bank.py`, maybe I'll add those as CLI arguments.

## Description
This runs a number of games of the game bank with players primarily banking with two strategies - either after a certain number of doubles are rolled, or after the pot reaches a certain threshold. The mean rank of each player at the end of the game is recorded, along with the median game score for the player and the mean number of banks per game a player could expect to have. Fewer banks likely means more volatility in final positioning.

## Observations
One simulation of 10,000 20-round games produced the following output:
```
hagenlarsen@Hagens-MBP ~/D/s/bank (main)> python3 bank.py
+---------------------------------------+--------------------+---------------------+-------------------+
| Player                                |   Mean Rank (of 6) |   Median Game Score |   Mean Banks/Game |
+=======================================+====================+=====================+===================+
| OverOneHundredPlayer                  |             3.7722 |                1339 |            9.4905 |
+---------------------------------------+--------------------+---------------------+-------------------+
| OverOneThousandPlayer                 |             3.5689 |                1384 |            1.102  |
+---------------------------------------+--------------------+---------------------+-------------------+
| OverThreeHundredPlayer                |             2.8537 |                1464 |            3.7999 |
+---------------------------------------+--------------------+---------------------+-------------------+
| OverTwoDoublesAndOverTwoHundredPlayer |             3.8537 |                1464 |            3.7999 |
+---------------------------------------+--------------------+---------------------+-------------------+
| ThreeDoublesPlayer                    |             3.4466 |                1378 |            2.4958 |
+---------------------------------------+--------------------+---------------------+-------------------+
| TwoDoublesPlayer                      |             3.5049 |                1395 |            5.0062 |
+---------------------------------------+-----
```

It seems to be that the best strategy is to just pick a score to bank at and stick with it.
```
hagenlarsen@Hagens-MBP ~/D/s/bank (main)> python3 bank.py
+---------------+--------------------+---------------------+-------------------+
| Player        |   Mean Rank (of 9) |   Median Game Score |   Mean Banks/Game |
+===============+====================+=====================+===================+
| Over100Player |             5.4477 |              1337   |            9.4948 |
+---------------+--------------------+---------------------+-------------------+
| Over200Player |             5.07   |              1434   |            5.3613 |
+---------------+--------------------+---------------------+-------------------+
| Over300Player |             5.0017 |              1460   |            3.8024 |
+---------------+--------------------+---------------------+-------------------+
| Over400Player |             4.9614 |              1476   |            2.8237 |
+---------------+--------------------+---------------------+-------------------+
| Over500Player |             4.9614 |              1454   |            2.2152 |
+---------------+--------------------+---------------------+-------------------+
| Over600Player |             4.938  |              1490   |            1.9529 |
+---------------+--------------------+---------------------+-------------------+
| Over700Player |             4.9137 |              1470.5 |            1.6949 |
+---------------+--------------------+---------------------+-------------------+
| Over800Player |             4.8639 |              1360   |            1.4548 |
+---------------+--------------------+---------------------+-------------------+
| Over900Player |             4.8422 |              1372   |            1.2612 |
+---------------+--------------------+-----
```

This doesn't really account for social influences like banking one roll after a specific person, or banking at a number slightly higher than another person. When I run this script multiple times with the same input, the results for players waiting for higher numbers (700, 800, 900) are inconsistent. I think this is because so much depends on the first couple of rolls. If a pot gets to 400, it likely won't ever get to 600, because the only way the pot gets significantly higher is if the pot is doubled to 800+.

A simulation of 1,000,000 20-round games produces the following results:
```
hagenlarsen@Hagens-MBP ~/D/s/bank (main)> python3 bank.py
+---------------+--------------------+---------------------+-------------------+
| Player        |   Mean Rank (of 9) |   Median Game Score |   Mean Banks/Game |
+===============+====================+=====================+===================+
| Over100Player |            5.43013 |                1337 |           9.47256 |
+---------------+--------------------+---------------------+-------------------+
| Over200Player |            5.03484 |                1434 |           5.34936 |
+---------------+--------------------+---------------------+-------------------+
| Over300Player |            4.97648 |                1462 |           3.79666 |
+---------------+--------------------+---------------------+-------------------+
| Over400Player |            4.9692  |                1460 |           2.79984 |
+---------------+--------------------+---------------------+-------------------+
| Over500Player |            4.97401 |                1444 |           2.1933  |
+---------------+--------------------+---------------------+-------------------+
| Over600Player |            4.94309 |                1480 |           1.93129 |
+---------------+--------------------+---------------------+-------------------+
| Over700Player |            4.9112  |                1460 |           1.67693 |
+---------------+--------------------+---------------------+-------------------+
| Over800Player |            4.89674 |                1348 |           1.43122 |
+---------------+--------------------+---------------------+-------------------+
| Over900Player |            4.86431 |                1358 |           1.23881 |
+---------------+--------------------+---------------------+-------------------+
hagenlarsen@Hagens-MBP ~/D/s/bank (main)> 
```

So I guess you really should just shoot for the moon.