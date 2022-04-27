import sys  # NOQA
sys.path.append('../Game-Theory-Voting-System')  # NOQA

from collections import Counter

from ballot_profile import generate_random_ballot_profile


def determine_winner_from_ballot_profile(ballot_profile):
    # count how many times each candidate was voted most preferred
    most_preferred_counter = Counter()

    for preference_list, number_of_voters in ballot_profile:
        # make sure preference list is a list, not a str
        if isinstance(preference_list, str):
            preference_list = preference_list.split(" ")

        # take note of most preferred candidate
        most_preferred_counter[preference_list[0]] += number_of_voters

    # tabulate winner
    sorted_candidates_by_vote = sorted(
        most_preferred_counter.items(),
        key=lambda pair: (
            # pair[0] is the candidate name
            # pair[1] is the number of times they were most-preferred

            # sort first by number of votes
            -pair[1],
            # if there's a tie, defer to first in the alphabet
            pair[0]
        )
    )
    winner, _ = sorted_candidates_by_vote[0]

    return winner


if __name__ == "__main__":
    ballot_profile = generate_random_ballot_profile(number_of_candidates=4)
    print(f"\n\tBallot Profile:\n\n{ballot_profile}")

    winner = determine_winner_from_ballot_profile(ballot_profile)
    print(f"\n\tPlurality declares a winner!:\n{winner}")
