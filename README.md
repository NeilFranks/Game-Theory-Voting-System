# Game-Theory-Voting-System

Based on https://www.stat.uchicago.edu/~lekheng/meetings/mathofranking/ref/rivest.pdf

## Running simulations

To simulate elections, you can either run `simulate_election.py` directly, or run `./simulate_election.sh`

The command `./simulate_election.sh` takes arguments:

- arg1: `path_to_ballot_profile` (default: `"ballot_profiles/example_from_paper.txt"`)
- arg2: `number_of_simulations` (default: `100`)

For the simple example from the paper, you can simply run `./simulate_election.sh`

For the Schulze example from the paper, you can run `./simulate_election.sh ballot_profiles/Schulze_test.txt`

## Implementation details

- Borda tabulated using [borda](https://pypi.org/project/borda/)

- IRV tabulated using [pyrankvote](https://pypi.org/project/pyrankvote/)

- Minimax tabulated using [votelib](https://pypi.org/project/votelib/)

- Schulze tabulated using [schulze-voting](https://pypi.org/project/schulze-voting/)

- Optimal mixed strategy computed using [Nashpy](https://pypi.org/project/nashpy/)
