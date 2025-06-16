from picklepy.game import Player, Game


def test_play_deterministic():
    p1 = Player("A", skill=1.0)
    p2 = Player("B", skill=0.0)
    game = Game(p1, p2)
    winner = game.play()
    assert winner == "A"
    assert game.score[winner] >= 11
