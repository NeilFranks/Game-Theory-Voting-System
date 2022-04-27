import pyrankvote

from ballot_profile import generate_random_ballot_profile


def determine_winner_from_ballot_profile(ballot_profile):
    # instantiate dictionary of candidates
    candidate_dictionary = {
        candidate: pyrankvote.Candidate(candidate)
        for candidate in ballot_profile.candidates_alphabetically_sorted
    }

    # deduce ballots from ballot_profile
    ballots = []
    for preference_list, number_of_voters in ballot_profile:
        # make sure preference list is a list, not a str
        if isinstance(preference_list, str):
            preference_list = preference_list.split(" ")

        # add the necessary number of ballots
        ballots.extend(
            [
                pyrankvote.Ballot(
                    ranked_candidates=[
                        candidate_dictionary[candidate]
                        for candidate in preference_list
                    ]
                )
            ] * number_of_voters
        )

    # tabulate winner(s)
    result = pyrankvote.instant_runoff_voting(
        candidates=list(candidate_dictionary.values()),
        ballots=ballots
    )
    winners = result.get_winners()

    # may have multiple "winners" (tie); just take the first one
    winner = winners[0]

    return winner


if __name__ == "__main__":
    ballot_profile = generate_random_ballot_profile(number_of_candidates=4)
    print(f"\n\tBallot Profile:\n\n{ballot_profile}")

    winner = determine_winner_from_ballot_profile(ballot_profile)
    print(f"\n\tIRV declares a winner!:\n{winner}")
