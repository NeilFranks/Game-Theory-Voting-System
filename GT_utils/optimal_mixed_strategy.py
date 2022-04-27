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
