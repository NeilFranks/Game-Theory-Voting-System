import random

from ballot_profile import generate_random_ballot_profile
from GT_utils.preference_matrix import construct_preference_matrix_from_ballot_profile
from GT_utils.margin_matrix import construct_margin_matrix_from_preference_matrix
from GT_utils.optimal_mixed_strategy import calculate_optimal_mixed_strategy_from_margin_matrix
from GT_utils.dice_method import *

def calculate_optimal_mixed_strategy_from_ballot_profile(ballot_profile):
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

    return optimal_mixed_strategy

def determine_winner_from_ballot_profile(ballot_profile):

    # calculate optimal mixed strategy
    optimal_mixed_strategy = calculate_optimal_mixed_strategy_from_ballot_profile(ballot_profile)

    # select winner using the dice method from paper
    cumulative_probs = cumulative_probs_from_mixed_strat(optimal_mixed_strategy)
    dice_rolls = d10_generator(9)
    comparison_number = number_generator_from_d10(dice_rolls)
    winner_index = pick_winner(comparison_number, cumulative_probs)

    winner = ballot_profile.candidates_alphabetically_sorted[winner_index]
    return winner
