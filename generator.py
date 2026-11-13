import random
weapons = {
    "Netrunner" : ["smart guns", "pistols", "snipers", "precision rifles", "thrown melee"],
    "Solo" :["shotguns", "lmgs", "blunt weapons"],
    "Edgerunner": ["assault rifles", "submachine guns", "bladed melee"]
}

def generate_lifepath():
    lifepaths = ["Streetkid", "Nomad", "Corpo"]

    return random.choice(lifepaths)


def generate_build():
    builds = ["Netrunner", "Solo", "Edgerunner"]
    
    buildKey = random.choice(builds)
    return buildKey, weapons[buildKey]

def generate_character():
    appearance = {
        "skin_tone": ["Light", "Medium", "Dark"],
        "hairstyle": ["Short", "Long", "Mohawk", "Undercut"],
        "hair_color": ["Black", "Brown", "Blonde", "Red"],
        "eye_color": ["Blue", "Green", "Brown", "Gray"],
        "tattoos": ["Yes", "No"]
    }

    character_appearance = {}

    for feature, options in appearance.items():
        character_appearance[feature] = random.choice(options)

    return character_appearance