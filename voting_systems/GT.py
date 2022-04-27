import random

import numpy as np

from ballot_profile import generate_random_ballot_profile
from GT_utils.preference_matrix import construct_preference_matrix_from_ballot_profile
from GT_utils.margin_matrix import construct_margin_matrix_from_preference_matrix
from GT_utils.optimal_mixed_strategy import calculate_optimal_mixed_strategy_from_margin_matrix


def determine_winner_from_ballot_profile(ballot_profile):
    # turn ballot profile into a preference matrix
    preference_matrix = construct_preference_matrix_from_ballot_profile(
        ballot_profile
    )

    # turn preference matrix into a margin matrix
    margin_matrix = construct_margin_matrix_from_preference_matrix(
        preference_matrix
    )

    # use the margin matrix as a payoff matrix, and compute the optimal mixed strategy
    optimal_mixed_strategy = calculate_optimal_mixed_strategy_from_margin_matrix(
        margin_matrix
    )

    # select a winner using the probabilities from the optimal mixed strategy
    winner = random.choices(
        population=ballot_profile.candidates_alphabetically_sorted,
        weights=optimal_mixed_strategy
    )[0]

    return winner


if __name__ == "__main__":
    ballot_profile = generate_random_ballot_profile(number_of_candidates=4)
    print(f"\n\tBallot Profile:\n\n{ballot_profile}")

    winner = determine_winner_from_ballot_profile(ballot_profile)
    print(f"\n\tGT declares a winner!:\n{winner}")
