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
    else:
        print("Invalid input. Please enter 1 or 2.")

if __name__ == "__main__":
    main()