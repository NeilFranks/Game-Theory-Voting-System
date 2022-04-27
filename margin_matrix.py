import numpy as np

from generate_ballot_profile import generate_ballot_profile
from preference_matrix import construct_preference_matrix_from_ballot_profile


def construct_margin_matrix_from_preference_matrix(preference_matrix):
    # simple calculation to find the skew-symmetric margin matrix
    return preference_matrix - np.transpose(preference_matrix)


if __name__ == "__main__":
    ballot_profile = generate_ballot_profile(number_of_candidates=4)
    preference_matrix = construct_preference_matrix_from_ballot_profile(
        ballot_profile)
    margin_matrix = construct_margin_matrix_from_preference_matrix(
        preference_matrix)
