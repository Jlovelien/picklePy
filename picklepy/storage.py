import json
import os
from pathlib import Path
from typing import Optional

from .game import Player


DEFAULT_PATH = Path.home() / ".picklepy_players.json"


class PlayerDB:
    """Simple JSON-backed database for player information."""

    def __init__(self, path: Path = DEFAULT_PATH):
        self.path = Path(path)
        self.players = {}
        if self.path.exists():
            with open(self.path, "r", encoding="utf-8") as fh:
                try:
                    self.players = json.load(fh)
                except json.JSONDecodeError:
                    self.players = {}

    def save(self) -> None:
        with open(self.path, "w", encoding="utf-8") as fh:
            json.dump(self.players, fh, indent=2)

    def get(self, name: str) -> Optional[Player]:
        data = self.players.get(name)
        if not data:
            return None
        return Player(name=name, skill=data.get("skill", 0.5), dupr=data.get("dupr", 3.0))

    def upsert(self, player: Player) -> None:
        entry = self.players.get(player.name, {"wins": 0, "losses": 0})
        entry["skill"] = player.skill
        entry["dupr"] = player.dupr
        self.players[player.name] = entry
        self.save()

    def record_result(self, winner: Player, loser: Player) -> None:
        self.upsert(winner)
        self.upsert(loser)
        self.players[winner.name]["wins"] = self.players[winner.name].get("wins", 0) + 1
        self.players[loser.name]["losses"] = self.players[loser.name].get("losses", 0) + 1
        self.save()
