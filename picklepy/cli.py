import argparse
from .game import Player, Game


def main():
    parser = argparse.ArgumentParser(description="CLI Pickleball Simulator")
    parser.add_argument("player1", help="Name of player 1")
    parser.add_argument("player2", help="Name of player 2")
    parser.add_argument("--skill1", type=float, default=0.5, help="Skill for player 1 (0-1)")
    parser.add_argument("--skill2", type=float, default=0.5, help="Skill for player 2 (0-1)")
    parser.add_argument("--winning-score", type=int, default=11, help="Points needed to win")
    parser.add_argument("--win-by", type=int, default=2, help="Points needed to win by")
    parser.add_argument("--verbose", action="store_true", help="Display score after each rally")
    args = parser.parse_args()

    p1 = Player(args.player1, skill=args.skill1)
    p2 = Player(args.player2, skill=args.skill2)
    game = Game(p1, p2, winning_score=args.winning_score, win_by=args.win_by)
    winner = game.play(verbose=args.verbose)
    print(game.score_display())
    print(f"Winner: {winner}")


if __name__ == "__main__":
    main()
