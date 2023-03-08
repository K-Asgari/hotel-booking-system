import booking_system


menu = ["",
        "Meny:",
        "[0] Lukk program.",
        "[1] Book et rom.",
        "[2] Søk etter booking.",
        ""
        ]


if __name__ == "__main__":
    user_input = None
    while user_input != "0":
        print(*menu, sep="\n")
        user_input = input("Valg: ")
        match user_input:
            case "1":
                booking_system.make_reservation()
            case "2":
                print("Ikke tilgjengelig enda.")
    print("På gjensyn!")
