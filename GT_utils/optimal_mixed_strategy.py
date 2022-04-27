import numpy as np

import nashpy as nash

from ballot_profile import generate_random_ballot_profile
from GT_utils.preference_matrix import construct_preference_matrix_from_ballot_profile
from GT_utils.margin_matrix import construct_margin_matrix_from_preference_matrix


def calculate_optimal_mixed_strategy_from_margin_matrix(margin_matrix):
    # use the margin matrix as the payoff matrix for a 2-player zero-sum game
    game = nash.Game(margin_matrix)

    # use vertex enumeration to compute all optimal mixed strategies
    optimal_mixed_strategies = game.vertex_enumeration()

    # check if you have more than one optimal mixed strategy
    optimal_mixed_strategy = next(optimal_mixed_strategies)
    try:
        another_optimal_mixed_strategy = next(optimal_mixed_strategies)
        if another_optimal_mixed_strategy:
            print(
                f"Oooh, margin matrix has more than one optimal mixed strategy:\n{margin_matrix}"
            )

            # TODO: find the most balanced optimal mixed strategy
    except:
        pass

    # optimal_mixed_strategy contains one for P1 and P2; just return the first one
    return optimal_mixed_strategy[0]


if __name__ == "__main__":
    # print neatly
    np.set_printoptions(precision=5, suppress=True)

    ballot_profile = generate_random_ballot_profile(
        number_of_candidates=4,
        number_of_voters=100,
        dimensions=4
    )
    print(f"\n\tBallot Profile:\n\n{ballot_profile}")

    preference_matrix = construct_preference_matrix_from_ballot_profile(
        ballot_profile
    )
    print(f"\n\tPreference Matrix:\n\n{preference_matrix}")

    margin_matrix = construct_margin_matrix_from_preference_matrix(
        preference_matrix
    )
    print(f"\n\tMargin Matrix:\n\n{margin_matrix}")

    optimal_mixed_strategy = calculate_optimal_mixed_strategy_from_margin_matrix(
        margin_matrix
    )
    print(f"\n\tOptimal Mixed Strategy:\n\n{optimal_mixed_strategy}")
