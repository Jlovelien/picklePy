import random
from dataclasses import dataclass


@dataclass
class Player:
    name: str
    skill: float = 0.5  # probability of winning a rally


class Game:
    def __init__(self, player1: Player, player2: Player, winning_score: int = 11, win_by: int = 2):
        """Initialize a game.

        Parameters
        ----------
        player1, player2:
            The :class:`Player` instances participating in the game.
        winning_score:
            Minimum score required to win the game.
        win_by:
            Margin that a player must lead by to claim victory.
        """

        self.player1 = player1
        self.player2 = player2
        self.winning_score = winning_score
        self.win_by = win_by
        self.score = {player1.name: 0, player2.name: 0}
        # Player1 serves first by default
        self.server = player1

    def rally_winner(self) -> Player:
        """Return the player that wins the rally based on the current server's skill."""
        if random.random() < self.server.skill:
            return self.server
        # Return the opposing player if the server loses the rally
        return self.player1 if self.server is self.player2 else self.player2

    def play_point(self) -> Player:
        """Play a single rally and update internal state."""
        winner = self.rally_winner()
        self.score[winner.name] += 1
        self.server = winner
        return winner

    def _game_finished(self) -> bool:
        """Check if the current score meets winning conditions."""
        high_score = max(self.score.values())
        score_diff = abs(self.score[self.player1.name] - self.score[self.player2.name])
        return high_score >= self.winning_score and score_diff >= self.win_by

    def play(self, verbose: bool = False) -> str:
        """Simulate a pickleball game.

        Parameters
        ----------
        verbose:
            If ``True``, display the score after each rally.
        """
        while not self._game_finished():
            self.play_point()
            if verbose:
                print(self.score_display())
        return max(self.score, key=self.score.get)

    def score_display(self) -> str:
        """Return a human readable representation of the current score."""
        return (
            f"{self.player1.name}: {self.score[self.player1.name]} - "
            f"{self.player2.name}: {self.score[self.player2.name]}"
        )
