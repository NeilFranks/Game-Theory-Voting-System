import numpy as np

from ballot_profile import generate_random_ballot_profile


def construct_preference_matrix_from_ballot_profile(ballot_profile):
    # How many candidates?
    number_of_candidates = ballot_profile.number_of_candidates

    # determine some canonical ordering of candidates; alphabetical order works
    candidates_alphabetically_sorted = ballot_profile.candidates_alphabetically_sorted

    # initialize preference matrix
    preference_matrix = np.zeros((number_of_candidates, number_of_candidates))

    for key, value in ballot_profile:
        list_of_candidates = key.split(" ")
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
                ] += value

    return preference_matrix


if __name__ == "__main__":
    ballot_profile = generate_random_ballot_profile(
        number_of_candidates=4
    )
    print(f"\n\tBallot Profile:\n\n{ballot_profile}")

    preference_matrix = construct_preference_matrix_from_ballot_profile(
        ballot_profile
    )
    print(f"\n\tPreference Matrix:\n\n{preference_matrix}")
