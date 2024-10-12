numbers = {'one': 1, 'two': 2, 'three': 3}
print(numbers['one'])


numbers['eleven'] = 11
print(numbers)

planets = ['Mercury', 'Venus', 'Earth', 'Mars',
           'Jupiter', 'Saturn', 'Uranus', 'Neptune']

# Planet name as the key and value will be their initials
planets_inital = {planet: planet[0] for planet in planets}
print(planets_inital)

print('Pluto' in planets)

for k in numbers:
    print('{} : {}'.format(k, numbers[k]))

print("".join(sorted(planets_inital.values())))

for planet, initial in planets_inital.items():
    print("{} begins with \"{}\"".format(planet.rjust(10), initial))

last_name = ""
print(len(last_name))


def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all documents 
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    indices = []

    for i, doc in enumerate(doc_list):
        tokens = doc.split()

        normalized = [token.rstrip('.,').lower() for token in tokens]
        if keyword.lower() in normalized:
            indices.append(i)

    return indices
    pass


# Check your answer
q2.check()
