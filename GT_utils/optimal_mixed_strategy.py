import numpy as np

import nashpy as nash

from ballot_profile import generate_random_ballot_profile
from GT_utils.preference_matrix import construct_preference_matrix_from_ballot_profile
from GT_utils.margin_matrix import construct_margin_matrix_from_preference_matrix


def calculate_optimal_mixed_strategy_from_margin_matrix(margin_matrix):
    # if margin matrix is all zeros, no need to try to compute the optimal mixed strategy;
    # all candidates have equal probability
    if margin_matrix.max() == 0 and margin_matrix.min() == 0:
        optimal_mixed_strategy = [1 / len(margin_matrix)] * len(margin_matrix)
        
    else:
        # use the margin matrix as the payoff matrix for a 2-player zero-sum game
        game = nash.Game(margin_matrix)

        # use vertex enumeration to compute all optimal mixed strategies
        optimal_mixed_strategies = game.vertex_enumeration()

        try:
            optimal_mixed_strategies = list(optimal_mixed_strategies)

            # each optimal mixed strategy contains a strategy for player 1 and player 2.
            # we can use either one (they're the same)
            P1_optimal_mixed_strategies = [
                optimal_mixed_strategy[0]
                for optimal_mixed_strategy in optimal_mixed_strategies
            ]

            # if there is more than one optimal mixed strategy,
            # then the best one is the one the least sum of squares of its values
            sorted_P1_optimal_mixed_strategies = sorted(
                P1_optimal_mixed_strategies,
                key=lambda mixed_strategy: np.sum(mixed_strategy ** 2)
            )

            optimal_mixed_strategy = sorted_P1_optimal_mixed_strategies[0]

        except Exception as e:
            print(e)

            # On any failure, just pick one optimal mixed strategy
            optimal_mixed_strategy = next(optimal_mixed_strategies)[0]

    return optimal_mixed_strategy
