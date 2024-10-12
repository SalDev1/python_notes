planets = ['Mercury', 'Venus', 'Earth', 'Mars',
           'Jupiter', 'Saturn', 'Uranus', 'Neptune']

for planet in planets:
    print(planet)


# Loop over tuples
tuples = (2, 2, 3, 4, 5, 6)
result = 1

for val in tuples:
    result *= val
print(result)

# Range is pretty good function
for i in range(5):
    print("Doing important work at i = ", i)

# While Loops
i = 0
while i < 10:
    print(i, end='')
    i += 1


squares_array = [n**2 for n in range(10)]
print(squares_array)

short_planets = [planet for planet in planets if len(planet) < 6]
print(short_planets)

short_planets_with_sql = [
    planet.upper() + '!' for planet in planets if len(planet) < 6]

print(short_planets)


def count_negatives(nums):
    return len([num for num in nums if num < 0])


def count_positives(nums):
    return len([num for num in nums if num > 0])


# Monte Carlo Method
def estimate_average_slot_payout(n_runs):
    """Run the slot machine n_runs times and return the average net profit per run.
    Example calls (note that return value is nondeterministic!):
    >>> estimate_average_slot_payout(1)
    -1
    >>> estimate_average_slot_payout(1)
    0.5
    """
    payouts = [play_slot_machine() - 1 for i in range(n_runs)]
    avg_payout = sum(payouts) / n_runs

    return avg_payout
    pass
