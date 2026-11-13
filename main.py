import generator

def main():

    print("========================")
    print("       CyberRoute")
    print("========================")

    lifepath = generator.generate_lifepath()
    build, weapons = generator.generate_build()

    print("\nYour Character")
    print("------------------------")

    print("Lifepath:", lifepath)
    print("Build:", build)
    print("Weapons:", weapons)

    appearance = generator.generate_appearance()

    print("\nCharacter Appearance")
    print("------------------------")

    for feature, result in appearance.items():
        print(feature.replace("_", " ").title() + ":", result)


if __name__ == "__main__":
    main()