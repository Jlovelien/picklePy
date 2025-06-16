import random
from dataclasses import dataclass


@dataclass
class Player:
    name: str
    skill: float = 0.5  # probability of winning a rally


class Game:
    def __init__(self, player1: Player, player2: Player, winning_score: int = 11):
        self.player1 = player1
        self.player2 = player2
        self.winning_score = winning_score
        self.score = {player1.name: 0, player2.name: 0}
        self.server = player1

    def rally_winner(self) -> Player:
        """Return the player that wins the rally based on skill."""
        if random.random() < self.player1.skill:
            return self.player1
        return self.player2

    def play(self) -> str:
        """Simulate a pickleball game."""
        while max(self.score.values()) < self.winning_score or abs(self.score[self.player1.name] - self.score[self.player2.name]) < 2:
            winner = self.rally_winner()
            self.score[winner.name] += 1
            self.server = winner
        return max(self.score, key=self.score.get)

    def score_display(self) -> str:
        return f"{self.player1.name}: {self.score[self.player1.name]} - {self.player2.name}: {self.score[self.player2.name]}"
