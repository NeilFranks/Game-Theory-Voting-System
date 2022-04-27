import borda.count

from ballot_profile import generate_random_ballot_profile


def determine_winner_from_ballot_profile(ballot_profile):
    # instantiate an election
    election = borda.count.Election()

    # set the candidates
    election.set_candidates(
        ballot_profile.candidates_alphabetically_sorted
    )

    # cast votes based on ballot profile
    for preference_list, number_of_voters in ballot_profile:

        # make sure preference list is a list, not a str
        if isinstance(preference_list, str):
            preference_list = preference_list.split(" ")

        for _ in range(number_of_voters):
            voter = borda.count.Voter(
                election=election,
                name=""
            )

            voter.votes(preference_list)

    # tabulate winner
    sorted_candidates_by_vote = sorted(
        election.votes,
        key=lambda candidate: election.votes[candidate],
        reverse=True
    )
    winner = sorted_candidates_by_vote[0]
    return winner
