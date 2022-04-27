import votelib
import votelib.evaluate.condorcet

from ballot_profile import generate_random_ballot_profile
from GT_utils.preference_matrix import construct_preference_matrix_from_ballot_profile
from GT_utils.margin_matrix import construct_margin_matrix_from_preference_matrix


def determine_winner_from_ballot_profile(ballot_profile):
    # instantiate canonical order of candidates
    canonical_list_of_candidates = [
        votelib.candidate.Person(candidate)
        for candidate in ballot_profile.candidates_alphabetically_sorted
    ]

    # from the ballot profile, extract pairwise wins
    # can use preference matrix for this :)
    preference_matrix = construct_preference_matrix_from_ballot_profile(
        ballot_profile
    )
    # margin_matrix = construct_margin_matrix_from_preference_matrix(
    #     preference_matrix
    # )
    # pairwise_margin_dictionary = {
    #     # the key is the tuple (row_candidate, column_candidate)
    #     (
    #         canonical_list_of_candidates[row_index],
    #         canonical_list_of_candidates[column_index]
    #     ): int(margin_matrix[row_index][column_index])  # the value is the margin at margin_matrix[row][column]

    #     for row_index in range(len(margin_matrix))
    #     for column_index in range(len(margin_matrix))
    # }

    # also need to get pairwise wins
    pairwise_wins_dictionary = {
        # the key is the tuple (row_candidate, column_candidate)
        (
            canonical_list_of_candidates[row_index],
            canonical_list_of_candidates[column_index]
        ): int(preference_matrix[row_index][column_index])  # the value is the margin at preference_matrix[row][column]

        for row_index in range(len(preference_matrix))
        for column_index in range(len(preference_matrix))
    }

    # run Minimax based on margins
    results = votelib.evaluate.condorcet.MinimaxCondorcet(
        pairwin_scoring="margins"
    ).evaluate(
        votes=pairwise_wins_dictionary,
        n_seats=1
    )

    # may have multiple "winners" (tie); break all ties
    winner = votelib.evaluate.core.Tie.break_by_list(
        elected=results,
        breaker=canonical_list_of_candidates  # alphabetical order is tiebreaker
    )[0]
    return winner.name
