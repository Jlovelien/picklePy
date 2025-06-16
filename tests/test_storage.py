from pathlib import Path
from picklepy.game import Player
from picklepy.storage import PlayerDB

def test_playerdb_roundtrip(tmp_path):
    db_path = tmp_path / "players.json"
    db = PlayerDB(db_path)
    alice = Player("Alice", skill=0.6, dupr=4.0)
    db.upsert(alice)

    db2 = PlayerDB(db_path)
    loaded = db2.get("Alice")
    assert loaded is not None
    assert loaded.skill == 0.6
    assert loaded.dupr == 4.0
