import random

def generate_lifepath():
    lifepaths = ["Streetkid", "Nomad", "Corpo"]

    return random.choice(lifepaths)


def generate_build():
    builds = ["Netrunner", "Solo", "Edgerunner"]

    return random.choice(builds)