from collections import Counter
import os
import sys
import time

import numpy as np

from ballot_profile import BallotProfile

from voting_systems import Borda
from voting_systems import GT
from voting_systems import GTD
from voting_systems import IRV
from voting_systems import Minimax
from voting_systems import Plurality
from voting_systems import Schulze

from voting_systems.GT import calculate_optimal_mixed_strategy_from_ballot_profile


DEFAULT_NUMBER_OF_SIMULATIONS = 100

PATH_TO_BALLOT_PROFILE_FROM_THE_PAPER = "ballot_profiles/example_from_paper.txt"

# enumerate the voting systems we want to evaluate
METHODS = {
    "Plurality": lambda ballot_profile: Plurality.determine_winner_from_ballot_profile(ballot_profile),
    "IRV": lambda ballot_profile: IRV.determine_winner_from_ballot_profile(ballot_profile),
    "Borda": lambda ballot_profile: Borda.determine_winner_from_ballot_profile(ballot_profile),
    "minimax": lambda ballot_profile: Minimax.determine_winner_from_ballot_profile(ballot_profile),
    "Schulze": lambda ballot_profile: Schulze.determine_winner_from_ballot_profile(ballot_profile),
    "GTD": lambda ballot_profile: GTD.determine_winner_from_ballot_profile(ballot_profile),
    "GT": lambda ballot_profile: GT.determine_winner_from_ballot_profile(ballot_profile),
}

METHODS_STRING = ", ".join(METHODS)


def simulate(ballot_profile, number_of_simulations):
    def print_simulation_results(voting_system, ballot_profile, results, seconds_elapsed):
        # double check we got 1 winner per simulation
        assert sum([result[1] for result in results]) == number_of_simulations

        print(
            f"\nRan election {number_of_simulations} times using {voting_system} in {round(seconds_elapsed, 2)} seconds:"
        )

        for key, value in results:
            print(f"\t{key} won {value} times")

        # if voting system is GT or GTD, print the optimal mixed strategy
        if voting_system in ["GTD", "GT"]:
            # get the optimal mixed strategy
            optimal_mixed_strategy = calculate_optimal_mixed_strategy_from_ballot_profile(ballot_profile)

            # match candidates to their probabilities
            candidate_probabilites = [
                (
                    ballot_profile.candidates_alphabetically_sorted[i],
                    round(optimal_mixed_strategy[i], 2)  # round probability to 2 decimal places
                ) for i in range(len(optimal_mixed_strategy))
            ]
            
            # pretty print
            print(f"\tOptimal mixed strategy was: {candidate_probabilites}")

    # Simulate the election using every voting system
    for voting_system in METHODS:
        # initialize a counter to keep track of how many times a candidate wins
        winner_counter = Counter()

        # time the process
        start_time = time.time()
        for _ in range(number_of_simulations):
            # determine the winner
            winner = METHODS[voting_system](ballot_profile)
            winner_counter[winner] += 1

        print_simulation_results(
            voting_system=voting_system,
            ballot_profile=ballot_profile,
            results=winner_counter.most_common(),  # sort results by most wins
            seconds_elapsed=time.time()-start_time
        )


def main(*args):
    path_to_ballot_profile = None
    number_of_simulations = None

    # get the specified path to a ballot profile, and the desired number of simulations
    if args[0]:
        if len(args[0]) > 0:
            path_to_ballot_profile = args[0][0]

        if len(args[0]) > 1:
            number_of_simulations = int(args[0][1])

    if path_to_ballot_profile is None:
        print(
            f"\nNo ballot profile specified; defaulting to {PATH_TO_BALLOT_PROFILE_FROM_THE_PAPER}"
        )
        path_to_ballot_profile = PATH_TO_BALLOT_PROFILE_FROM_THE_PAPER

    if number_of_simulations is None:
        print(
            f"\nNumber of simulations not specified; defaulting to {DEFAULT_NUMBER_OF_SIMULATIONS}"
        )
        number_of_simulations = DEFAULT_NUMBER_OF_SIMULATIONS

    # make sure you have a valid path
    assert os.path.isfile(path_to_ballot_profile)

    # read in the ballot profile
    ballot_profile = BallotProfile(path=path_to_ballot_profile)

    # run the simulation
    print()
    print(f"Simulating election {number_of_simulations} times")
    print(f"Using ballot profile in {path_to_ballot_profile}")
    print(f"Using voting systems: {METHODS_STRING}")
    simulate(ballot_profile, number_of_simulations)


if __name__ == "__main__":
    # run the simulation
    main(sys.argv[1:])
