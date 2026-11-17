import generator

def main():
    print("What would you like to do?\n")

    print("[1] Generate a random character")
    print("[2] Recommend a build")

    inputV = input("\nSelect an option: ")
    if inputV == "1":
        print("========================")
        print("       CyberRoute")
        print("========================")

        lifepath = generator.generate_lifepath()
        appearance = generator.generate_character()
        build, weapons = generator.generate_build()
        print("\nCharacter Appearance")
        print("------------------------")
        for feature, result in appearance.items():
            print(feature.replace("_", " ").title() + ":", result)
        print("------------------------")
        print("Lifepath:", lifepath)
        print("------------------------")
        print("Build:", build)
        print("Recommended Weapons:", weapons)


    elif inputV == "2":
        print("========================")
        print("       CyberRoute")
        print("========================")

        build, weapons = generator.generate_build()

        print("\nRandom Build")
        print("------------------------")

        print("Build:", build)
        print("Recommended Weapons:", weapons)
    if build == "Netrunner":
        print("Recommended Operating CyberWare: ['Cyberdeck', 'Tetratronic Rippler']")
        print("Recommended arm CyberWare: ['Monowire', 'Gorilla Arms']\n")
        print("The GOD of the net, I recommend you to use a stealth and hacking playstle.")
        print("Recommended attributes: Intelligence and Cool would be my main two with either tech or body as a strong third. Body for if you want to be immortal and plan on using Monowire as a primary weapon.")
        print("Body for if you want to be immortal and plan on using Monowire as a primary weapon.")
        print("Tech if you want to go all in on cyberware and do the most damage or of tech weapons are somthing you grow to love.\n")
    elif build == "Solo":
        print("Recommended Operating CyberWare: ['Berserk', 'Chrome' 'Compressors']")
        print("Recommend Arm CyberWare: ['Gorilla Arms', 'projectile launch system']\n")
        print("The GOD of combat, I recommend using an up close and peronal playstyle.")
        print("Recommended attributes: Body and Tech would be my main two with either Reflexes or Cool as a strong third.")
        print("Reflexes if you want to focus movement and want to run through enemies.")
        print("Cool mostly to unlock the increased weapon dmg for thrown melee, pistols, revolvers, precision rifles, and snipers.")
        print("(I wouldn't recommend trying to go stealth solo as I found brute force more fun for this build)\n")
    elif build == "Edgerunner":
        print("Recommended Operating CyberWare: ['Sandevistan', 'Chrome Compressors']")
        print("Recommend Arm CyberWare: ['Mantis Blades', 'projectile launch system']\n")
        print("Ever wanted to fly as close to the sun as possible? Well Icarus this is it.")
        print("Recommended attributes: Reflexes and Tech would be my main two with either Body or cool as a strong third.")
        print("Body will make you a tank with the tech armor on top you'll be invincible, and since the perk Edgerunner eats your health its best to get it up with body.")
        print("However say you really do like to run on the edge Cool is for you with Cool you can use almost every weapon type in the game to their full potential.\n")
    else:
        print("Invalid input. Please enter 1 or 2.")

if __name__ == "__main__":
    main()