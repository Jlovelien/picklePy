from typing import Callable, Dict

from .game import Game


def simulate_rounds(game_factory: Callable[[], Game], rounds: int = 1) -> Dict[str, int]:
    """Run multiple games and tally the winners."""
    results: Dict[str, int] = {}
    for _ in range(rounds):
        game = game_factory()
        winner = game.play()
        results[winner] = results.get(winner, 0) + 1
    return results
