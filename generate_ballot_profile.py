from collections import Counter
import random
import string

import numpy as np


class RandomPosition:
    def __init__(self, name=None, dimensions=2):
        self.name = name
        self.coordinates = np.array(
            [random.randrange(0, 100) for _ in range(dimensions)]
        )

    def distance_to(self, otherPosition):
        return np.linalg.norm(self.coordinates - otherPosition.coordinates)


def generate_ballot_profile(number_of_candidates=None):
    # How many candidates? How many voters?
    if number_of_candidates is None:
        number_of_candidates = random.randrange(2, 20)  # up to 20 candidates!
    number_of_voters = random.randrange(100, 10000)

    # Will determine which candidates a voter likes according to their proximity on some plane
    candidates = [
        RandomPosition(name=string.ascii_uppercase[index])  # candidates named by letter
        for index in range(number_of_candidates)
    ]
    voters = [RandomPosition() for _ in range(number_of_voters)]

    ballot_profile = Counter()

    for voter in voters:
        # generate the voter's ballot based on proximity to each candidate
        preferred_candidates = sorted(candidates, key=lambda c: voter.distance_to(c))

        # stringified order of candidates
        ballot = " ".join([c.name for c in preferred_candidates])

        # count it
        ballot_profile[ballot] += 1

    return ballot_profile


if __name__ == "__main__":
    generate_ballot_profile()
