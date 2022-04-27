# Game-Theory-Voting-System

Based on https://www.stat.uchicago.edu/~lekheng/meetings/mathofranking/ref/rivest.pdf

## Setup

(_It is suggested to work in a virtual environment)_

Running `pip install -r requirements.txt` should install everything you need in order to run the code.

## Running simulations

To simulate elections, you can either run `simulate_election.py` directly, or run `./simulate_election.sh`

The command `./simulate_election.sh` takes arguments:

- arg1: `path_to_ballot_profile` (default: `"ballot_profiles/example_from_paper.txt"`)
- arg2: `number_of_simulations` (default: `100`)

To replicate the simple example from the paper, you can simply run `./simulate_election.sh`

To replicate the Schulze example from the paper, you can run `./simulate_election.sh ballot_profiles/Schulze_test.txt`

To see how candidates from the 2020 Iowa democratic caucus might fare under different voting systems, you can run `./simulate_election.sh ballot_profiles/Iowa_caucus.txt`

To replicate the main experiment which produces the cumulative margin table from the paper, you can run `./experiment.sh`

## Implementation details

- Borda tabulated using [borda](https://pypi.org/project/borda/)

- IRV tabulated using [pyrankvote](https://pypi.org/project/pyrankvote/)

- Minimax tabulated using [votelib](https://pypi.org/project/votelib/)

- Schulze tabulated using [schulze-voting](https://pypi.org/project/schulze-voting/)

- Optimal mixed strategy computed using [Nashpy](https://pypi.org/project/nashpy/)
