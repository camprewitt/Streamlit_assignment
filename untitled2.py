# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vUNOSsXkOE9JHhGz8u6TSqbJb5mnQkHT
"""

class Player:
    def __init__(self, name, championships, mvps, all_star_appearances, scoring_titles, finals_mvps, defensive_player_of_the_year):
        self.name = name
        self.championships = championships
        self.mvps = mvps
        self.all_star_appearances = all_star_appearances
        self.scoring_titles = scoring_titles
        self.finals_mvps = finals_mvps
        self.defensive_player_of_the_year = defensive_player_of_the_year

    def display_achievements(self):
        print(f"Achievements of {self.name}:")
        print(f"Championships: {self.championships}")
        print(f"MVPs: {self.mvps}")
        print(f"All-Star Appearances: {self.all_star_appearances}")
        print(f"Scoring Titles: {self.scoring_titles}")
        print(f"Finals MVPs: {self.finals_mvps}")
        print(f"Defensive Player of the Year: {self.defensive_player_of_the_year}")
        print("-----------------------------")


def compare_achievements(player1, player2):
    print(f"Comparing achievements of {player1.name} and {player2.name}:\n")

    print(f"Championships: {player1.name} - {player1.championships} | {player2.name} - {player2.championships}")
    print(f"MVPs: {player1.name} - {player1.mvps} | {player2.name} - {player2.mvps}")
    print(f"All-Star Appearances: {player1.name} - {player1.all_star_appearances} | {player2.name} - {player2.all_star_appearances}")
    print(f"Scoring Titles: {player1.name} - {player1.scoring_titles} | {player2.name} - {player2.scoring_titles}")
    print(f"Finals MVPs: {player1.name} - {player1.finals_mvps} | {player2.name} - {player2.finals_mvps}")
    print(f"Defensive Player of the Year: {player1.name} - {player1.defensive_player_of_the_year} | {player2.name} - {player2.defensive_player_of_the_year}")
    print("-----------------------------")


# LeBron James' achievements
lebron = Player(
    name="LeBron James",
    championships=4,
    mvps=4,
    all_star_appearances=19,
    scoring_titles=1,
    finals_mvps=4,
    defensive_player_of_the_year=0
)

# Michael Jordan's achievements
jordan = Player(
    name="Michael Jordan",
    championships=6,
    mvps=5,
    all_star_appearances=14,
    scoring_titles=10,
    finals_mvps=6,
    defensive_player_of_the_year=1
)

# Display achievements for both players
lebron.display_achievements()
jordan.display_achievements()

# Compare their achievements
compare_achievements(lebron, jordan)