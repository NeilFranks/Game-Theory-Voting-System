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

The script will simulated an election on a ballot profile `number_of_simulations` times. It is expected that GT voting system will be the only one where the same candidate may not win every simulation. This is due to GT's employment of random selection based on probabilities from the computed optimal mixed strategy.

To replicate the simple example from the paper, you can simply run `./simulate_election.sh`

To replicate the Schulze example from the paper, you can run `./simulate_election.sh ballot_profiles/Schulze_test.txt`

To see how candidates from the 2020 Iowa democratic caucus might fare under different voting systems, you can run `./simulate_election.sh ballot_profiles/Iowa_caucus.txt`

---

The main experiment of the paper simulates elections on 10,000 randomized ballot profiles, and enumerates the cumulative margin by which the voters prefer the outcome of one voting system versus another. To replicate this experiment, you can run `./experiment.sh`, which produces the table `cumulative_margins_table.csv`.

## Implementation details

- Borda tabulated using [borda](https://pypi.org/project/borda/)

- IRV tabulated using [pyrankvote](https://pypi.org/project/pyrankvote/)

- Minimax tabulated using [votelib](https://pypi.org/project/votelib/)

- Schulze tabulated using [schulze-voting](https://pypi.org/project/schulze-voting/)

- Optimal mixed strategy computed using [Nashpy](https://pypi.org/project/nashpy/)
