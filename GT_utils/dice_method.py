import numpy as np
import random


def cumulative_probs_from_mixed_strat(mixed_strat):
    cumulative_probs = []
    cumulative_probs = [
        sum(mixed_strat[0:x:1])
        for x in range(0, len(mixed_strat) + 1)
    ]

    return cumulative_probs[1:]


def d10_generator(trials):
    dice_result = []

    for instance in range(trials):
        dice_result.append(random.randint(0, 9))

    return dice_result


def number_generator_from_d10(dice_result):
    dice_result.reverse()
    cumulative_digits_sum = 0

    for idx in range(len(dice_result)):
        cumulative_digits_sum += 10 ** (idx) * dice_result[idx]

    return cumulative_digits_sum / 10 ** (len(dice_result))


def pick_winner(x, cumulative_strat):
    winner_index = np.argwhere(np.array(cumulative_strat) > x)[0][0]
    return winner_index
