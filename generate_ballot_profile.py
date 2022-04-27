from collections import Counter
import random
import string

import numpy as np


class BallotProfile:
    def __init__(self, counter):
        # sort by keys with the highest values
        self.profile = counter.most_common()

        # How many candidates?
        # Get the first key in the ballot profile, and split it up at spaces to count the number of candidates
        sample_list_of_candidates = self.profile[0][0].split(" ")
        self.number_of_candidates = len(sample_list_of_candidates)

        # determine some canonical ordering of candidates; alphabetical order works
        self.candidates_alphabetically_sorted = sorted(
            sample_list_of_candidates)

    def __str__(self):
        s = ""
        for key, value in self.profile:
            s += f"{key}: {value}\n"
        return s

    def __getitem__(self, index):
        return self.profile[index]


class RandomPosition:
    def __init__(self, name=None, dimensions=2):
        self.name = name
        self.coordinates = np.array(
            [random.randrange(0, 100) for _ in range(dimensions)]
        )

    def distance_to(self, otherPosition):
        return np.linalg.norm(self.coordinates - otherPosition.coordinates)


def generate_ballot_profile(number_of_candidates=None, number_of_voters=None, dimensions=2):
    # How many candidates? How many voters?
    if number_of_candidates is None:
        number_of_candidates = random.randrange(2, 20)  # up to 20 candidates!
    if number_of_voters is None:
        number_of_voters = random.randrange(100, 10000)

    # Will determine which candidates a voter likes according to their proximity on some plane
    candidates = [
        RandomPosition(
            name=string.ascii_uppercase[index],  # candidates named by letter
            dimensions=dimensions  # dimensions of "space" a candidate can exist in
        )
        for index in range(number_of_candidates)
    ]
    voters = [
        RandomPosition(dimensions=dimensions)
        for _ in range(number_of_voters)
    ]

    ballot_profile_counter = Counter()

    for voter in voters:
        # generate the voter's ballot based on proximity to each candidate
        preferred_candidates = sorted(
            candidates, key=lambda c: voter.distance_to(c))

        # stringified order of candidates
        ballot = " ".join([c.name for c in preferred_candidates])

        # count it
        ballot_profile_counter[ballot] += 1

    return BallotProfile(ballot_profile_counter)


if __name__ == "__main__":
    generate_ballot_profile()
