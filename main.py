import generator

def main():

    print("========================")
    print("       CyberRoute")
    print("========================")

    lifepath = generator.generate_lifepath()
    build = generator.generate_build()

    print("\nYour Character")
    print("------------------------")

    print("Lifepath:", lifepath)
    print("Build:", build)


if __name__ == "__main__":
    main()