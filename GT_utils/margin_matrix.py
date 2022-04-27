import numpy as np

from ballot_profile import generate_random_ballot_profile
from GT_utils.preference_matrix import construct_preference_matrix_from_ballot_profile


def construct_margin_matrix_from_preference_matrix(preference_matrix):
    # simple calculation to find the skew-symmetric margin matrix
    return preference_matrix - np.transpose(preference_matrix)


if __name__ == "__main__":

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
