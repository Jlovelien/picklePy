import argparse
from .game import Player, Game, DoublesGame
from .simulation import simulate_rounds
from .storage import PlayerDB


def main():
    parser = argparse.ArgumentParser(description="CLI Pickleball Simulator")
    parser.add_argument("player1", help="Name of player 1")
    parser.add_argument("player2", help="Name of player 2")
    parser.add_argument("--skill1", type=float, default=0.5, help="Skill for player 1 (0-1)")
    parser.add_argument("--skill2", type=float, default=0.5, help="Skill for player 2 (0-1)")
    parser.add_argument("--dupr1", type=float, default=3.0, help="DUPR rating for player 1")
    parser.add_argument("--dupr2", type=float, default=3.0, help="DUPR rating for player 2")
    parser.add_argument("--partner1", help="Partner name for player 1 (doubles)")
    parser.add_argument("--partner2", help="Partner name for player 2 (doubles)")
    parser.add_argument("--dupr3", type=float, default=3.0, help="DUPR rating for partner1")
    parser.add_argument("--dupr4", type=float, default=3.0, help="DUPR rating for partner2")
    parser.add_argument("--winning-score", type=int, default=11, help="Points needed to win")
    parser.add_argument("--win-by", type=int, default=2, help="Points needed to win by")
    parser.add_argument("--rounds", type=int, default=1, help="Number of simulated games")
    parser.add_argument("--verbose", action="store_true", help="Display score after each rally")
    args = parser.parse_args()

    db = PlayerDB()

    def load_player(name: str, skill_arg: float, dupr_arg: float) -> Player:
        saved = db.get(name)
        skill = saved.skill if saved and skill_arg == parser.get_default("skill1") else skill_arg
        dupr = saved.dupr if saved and dupr_arg == parser.get_default("dupr1") else dupr_arg
        return Player(name, skill=skill, dupr=dupr)

    p1 = load_player(args.player1, args.skill1, args.dupr1)
    p2 = load_player(args.player2, args.skill2, args.dupr2)

    if args.partner1 and args.partner2:
        partner1 = load_player(args.partner1, args.skill1, args.dupr3)
        partner2 = load_player(args.partner2, args.skill2, args.dupr4)

        def factory():
            return DoublesGame(
                [p1, partner1],
                [p2, partner2],
                winning_score=args.winning_score,
                win_by=args.win_by,
            )
    else:
        def factory():
            return Game(p1, p2, winning_score=args.winning_score, win_by=args.win_by)

    if args.rounds > 1:
        results = simulate_rounds(factory, rounds=args.rounds)
        for name, wins in results.items():
            print(f"{name} won {wins} games")
    else:
        game = factory()
        winner = game.play(verbose=args.verbose)
        print(game.score_display())
        print(f"Winner: {winner}")

    # update database with results
    db.upsert(p1)
    db.upsert(p2)
    if args.partner1 and args.partner2:
        db.upsert(partner1)
        db.upsert(partner2)


if __name__ == "__main__":
    main()
