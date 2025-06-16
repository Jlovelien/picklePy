# picklePy

A simple command line pickleball simulator written in Python. It supports
singles or doubles play and can run multiple simulated rounds.

## Usage

Install dependencies and run the CLI:

```bash
python -m picklepy.cli Alice Bob --skill1 0.7 --skill2 0.5
```

This will simulate a game to 11 points and display the final score and winner.
To play doubles, pass partner names:

```bash
python -m picklepy.cli Alice Bob --partner1 Carol --partner2 Dave
```

You can also set DUPR ratings, run multiple rounds and enable verbose output to
see shot-by-shot results.

### Persistent players

Player ratings and win/loss records are stored in `~/.picklepy_players.json` so
you only need to set them once. The CLI will load saved players by name and
update their records after each game.
