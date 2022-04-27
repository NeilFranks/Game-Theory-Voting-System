import numpy as np

from generate_ballot_profile import generate_ballot_profile


def construct_preference_matrix_from_ballot_profile(ballot_profile):
    # How many candidates?
    # Get the first key in the ballot profile, and split it up at spaces to count the number of candidates
    sample_list_of_candidates = list(ballot_profile.keys())[0].split(" ")
    number_of_candidates = len(sample_list_of_candidates)

    # determine some canonical ordering of candidates; alphabetical order works
    candidates_alphabetically_sorted = sorted(sample_list_of_candidates)

    # initialize preference matrix
    preference_matrix = np.zeros((number_of_candidates, number_of_candidates))

    for row in ballot_profile:
        list_of_candidates = row.split(" ")
        for idx_1 in range(len(list_of_candidates)):
            # find index of this candidate in the alphabetical list
            candidate_1_index = candidates_alphabetically_sorted.index(
                list_of_candidates[idx_1]
            )

            for idx_2 in range(idx_1 + 1, len(list_of_candidates)):
                # find index of this candidate in the alphabetical list
                candidate_2_index = candidates_alphabetically_sorted.index(
                    list_of_candidates[idx_2]
                )

                # mark the number of voters who have the candidates in this order
                preference_matrix[
                    candidate_1_index, candidate_2_index
                ] += ballot_profile[row]

    return preference_matrix


if __name__ == "__main__":
    ballot_profile = generate_ballot_profile(number_of_candidates=4)
    preference_matrix = construct_preference_matrix_from_ballot_profile(ballot_profile)

