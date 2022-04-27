from collections import Counter

from ballot_profile import BallotProfile
import GT
import GTD


NUMBER_OF_SIMULATIONS = 100

# enumerate the voting systems we want to evaluate
METHODS = {
    "GT": lambda ballot_profile: GT.determine_winner_from_ballot_profile(ballot_profile),
    "GTD": lambda ballot_profile: GTD.determine_winner_from_ballot_profile(ballot_profile),
}

# create the ballot profile seen in the paper
ballot_profile_counter = Counter()
ballot_profile_counter["A B C D"] = 40
ballot_profile_counter["B C A D"] = 30
ballot_profile_counter["C A B D"] = 20
ballot_profile_counter["C B A D"] = 10
ballot_profile = BallotProfile(ballot_profile_counter)


def print_simulation_results(voting_system, results):
    # double check we got 1 winner per simulation
    assert sum([result[1] for result in results]) == NUMBER_OF_SIMULATIONS

    print(f"Ran election {NUMBER_OF_SIMULATIONS} times using {voting_system}:")

    for key, value in results:
        print(f"\t{key} won {value} times")


# Simulate the election using every voting system
for voting_system in METHODS:
    winner_counter = Counter()
    for _ in range(NUMBER_OF_SIMULATIONS):
        winner = METHODS[voting_system](ballot_profile)
        winner_counter[winner] += 1

    print_simulation_results(
        voting_system=voting_system,
        results=winner_counter.most_common()  # sort results by most wins
    )
