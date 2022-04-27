import schulze_voting

from ballot_profile import generate_random_ballot_profile


def convert_preference_list_into_ranking(preference_list, canonical_order):
    # - preference_list may look like [C, D, B, A], indicating a preference for C over all others
    # - canonical_order lists the candidates in alphabetical order; e.g. [A, B, C, D]
    # - If the preference_list is [C, D, B, A], SchulzeVote is expected to look like [3, 2, 0, 1],
    #   which indicated A is ranked lowest, B is ranked next lowest, C is ranked highest, and D is ranked second highest

    # make sure preference list is a list, not a str
    if isinstance(preference_list, str):
        preference_list = preference_list.split(" ")

    return [
        preference_list.index(candidate)
        for candidate in canonical_order
    ]


def determine_winner_from_ballot_profile(ballot_profile):
    # cast votes from ballot profile
    votes = [
        schulze_voting.SchulzeVote(
            ranking=convert_preference_list_into_ranking(
                preference_list,
                ballot_profile.candidates_alphabetically_sorted
            ),
            weight=number_of_voters
        )
        for preference_list, number_of_voters in ballot_profile
    ]

    # calculate winner(s)
    result = schulze_voting.evaluate_schulze(
        votes=votes,
        n=ballot_profile.number_of_candidates
    )
    winner_indices = result.candidate_wins[0]

    # may have multiple "winners" (tie); just take the first one
    winner_index = winner_indices[0]
    winner = ballot_profile.candidates_alphabetically_sorted[winner_index]

    return winner


if __name__ == "__main__":
    ballot_profile = generate_random_ballot_profile(number_of_candidates=4)
    print(f"\n\tBallot Profile:\n\n{ballot_profile}")

    winner = determine_winner_from_ballot_profile(ballot_profile)
    print(f"\n\tSchulze declares a winner!:\n{winner}")
