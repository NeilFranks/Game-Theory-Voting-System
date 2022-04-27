import numpy as np

from ballot_profile import generate_random_ballot_profile
from GT_utils.preference_matrix import construct_preference_matrix_from_ballot_profile


def construct_margin_matrix_from_preference_matrix(preference_matrix):
    # simple calculation to find the skew-symmetric margin matrix
    return preference_matrix - np.transpose(preference_matrix)
