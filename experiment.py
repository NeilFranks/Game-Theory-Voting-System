import numpy as np
import pandas as pd

from GT_utils.preference_matrix import construct_preference_matrix_from_ballot_profile
from GT_utils.margin_matrix import construct_margin_matrix_from_preference_matrix

from ballot_profile import generate_random_ballot_profile

from voting_systems import Borda
from voting_systems import GT
from voting_systems import GTD
from voting_systems import IRV
from voting_systems import Minimax
from voting_systems import Plurality
from voting_systems import Schulze

"""
This is an implementation of the paper's main experiment,
which holds one elections for 10,000 randomized ballot profiles,
and enumerates the cumulative number of voters who preferred the
outcome of one voting system over another.
"""


# parameters from the paper's main experiment
NUMBER_OF_CANDIDATES = 5
NUMBER_OF_VOTERS = 100
NUMBER_OF_SIMULATIONS = 10000

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

METHODS_CANONICAL_LIST = [
    "Plurality",
    "IRV",
    "Borda",
    "minimax",
    "Schulze",
    "GTD",
    "GT"
]

SAVE_PATH = "cumulative_margins_table.csv"


def run():
    # initialize cumulative margins table,
    # which will show how many voters preferred one voting system over another
    cumulative_margins_table = np.zeros((len(METHODS), len(METHODS)))

    for i in range(NUMBER_OF_SIMULATIONS):
        print(f"\tSimulation {i+1}/{NUMBER_OF_SIMULATIONS}", end="\r")

        # generate ballot profile
        ballot_profile = generate_random_ballot_profile(
            number_of_candidates=NUMBER_OF_CANDIDATES,
            number_of_voters=NUMBER_OF_VOTERS
        )

        # construct a margin matrix, which will allow us to know which results voters preferred
        preference_matrix = construct_preference_matrix_from_ballot_profile(
            ballot_profile
        )
        margin_matrix = construct_margin_matrix_from_preference_matrix(
            preference_matrix
        )

        # initialize a winner dictionary,
        # which will indicate which candidate won under each voting system
        winner_dictionary = {
            voting_system: METHODS[voting_system](ballot_profile)
            for voting_system in METHODS
        }

        # compare the winners each voting system named,
        # in terms of voters' preference
        for row_voting_system in winner_dictionary:
            # get one voting system's winner
            row_winner = winner_dictionary[row_voting_system]

            # get indices in canonical lists
            row_winner_index = ballot_profile.candidates_alphabetically_sorted.index(
                row_winner
            )
            row_index = METHODS_CANONICAL_LIST.index(row_voting_system)

            for column_voting_system in winner_dictionary:
                # get another voting system's winner
                column_winner = winner_dictionary[column_voting_system]

                # get indices in canonical lists
                column_winner_index = ballot_profile.candidates_alphabetically_sorted.index(
                    column_winner
                )
                column_index = METHODS_CANONICAL_LIST.index(
                    column_voting_system
                )

                # add the margin to the table
                cumulative_margins_table[row_index][column_index] += margin_matrix[row_winner_index][column_winner_index]

    print("\n\n\tCumulative margins table:")
    print(cumulative_margins_table)

    # Finally, save the table to a CSV
    df = pd.DataFrame(
        cumulative_margins_table,
        index=METHODS_CANONICAL_LIST,
        columns=METHODS_CANONICAL_LIST
    )
    df.to_csv(SAVE_PATH, index=True, header=True)

    print(f"\nSaved cumulative margins table to {SAVE_PATH}")


if __name__ == "__main__":
    # run the experiment
    run()
