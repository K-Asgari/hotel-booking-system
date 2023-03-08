"""
Working!
Todo:
    kommenter kode
    search funksjon
"""

import json
import os
import re
from datetime import datetime, date


DATE_FORMAT = "%Y-%m-%d"  # "YYYY-MM-DD"
FILENAME = "bookings.json"
ROOMS = ["room1", "room2", "room3"]


class Booking:
    """
    Booking object
    -> Completed.
    """

    def __init__(self, name, phone, check_in, check_out) -> None:
        self.name = name
        self.phone = phone
        self.check_in = check_in
        self.check_out = check_out

    def view_booking(self) -> None:
        print("",
              f"Navn: {self.name}",
              f"Tlf: {self.phone}",
              f"Innsjekk: {self.check_in}",
              f"Utsjekk: {self.check_out}",
              "", sep="\n")


def get_name_from_user(prompt: str) -> str:
    """
    -> Completed
    """
    name = None
    while name is None:
        name = input(prompt)
        if len(name.split()) < 2:
            name = None
            print("Fullt navn kreves. Skriv inn mer enn ett navn.")
    return name.title()


def get_phone_from_user(prompt: str) -> str:
    """
    -> Completed
    """
    phone = None
    while phone is None:
        phone = input(prompt)
        if not len(phone) == 8:
            phone = None
            print("Ugyldig nummer. Skriv inn 8 siffer.")
    return phone


def get_date_from_user(prompt: str) -> str:
    """
    Klager fram til gyldig dato er valgt.
    -> Completed
    """

    date = None
    while date is None:
        try:
            user_input = input(prompt)
            date_string = "-".join(re.split(r"\D", user_input))
            date = datetime.strptime(date_string, DATE_FORMAT)
            if date < datetime.today():
                date = None
                raise Exception
            date = date.strftime(DATE_FORMAT)

        except (ValueError, TypeError) as e:
            print("Ugyldig format, prøv igjen!")
        except Exception:
            print("Kan ikke velge dato i dag eller tilbake i tid.")
    return date


def write_booking_to_json(booking: dict, room: str) -> None:
    """
    -> Completed
    """

    if not os.path.exists(FILENAME):
        print("Missing 'bookings.json'")
    try:
        with open(FILENAME, "r+") as file:
            bookings = json.load(file)
            bookings[room].append(booking)
            file.seek(0)
            json.dump(bookings, file, indent=4)
    except (TypeError, FileNotFoundError) as e:
        print(e)
        quit()


def make_reservation(name=None, phone=None) -> None:
    """
    -> Completed
    """
    if name is None or phone is None:
        name = get_name_from_user("Navn: ")
        phone = get_phone_from_user("Tlf: ")
    check_in = get_date_from_user("Innsjekk(YYYY-MM-DD): ")
    check_out = get_date_from_user("Utsjekk(YYYY-MM-DD): ")
    booking = Booking(name, phone, check_in, check_out)

    if datetime.strptime(check_in, DATE_FORMAT) >= datetime.strptime(check_out, DATE_FORMAT):
        print("Innsjekk kan ikke være etter eller samme dag som utsjekk\n")
        make_reservation(name, phone)
        return

    while (room := input(f"Hvilket rom vil du booke? {ROOMS}: ")) not in ROOMS:
        print("Ugyldig rom, prøv igjen!")

    if not is_room_available(room, check_in, check_out):
        print("Rommet er allerede booket denne dagen. Prøv igjen.\n")
        make_reservation(name, phone)
        return

    write_booking_to_json(booking=vars(booking), room=room)
    print("Booking fullført!\n")


def is_room_available(room: str, check_in: str, check_out: str) -> bool:
    """
    -> Completed
    """

    with open(FILENAME) as file:
        bookings = json.load(file).get(room, [])
        booking_history = []
        for booking in bookings:
            booking_history.append((booking["check_in"], booking["check_out"]))

        check_in = datetime.strptime(check_in, DATE_FORMAT)
        check_out = datetime.strptime(check_out, DATE_FORMAT)
        for b in booking_history:
            history_in = datetime.strptime(b[0], DATE_FORMAT)
            history_out = datetime.strptime(b[1], DATE_FORMAT)

            if history_in <= check_in <= history_out or history_in <= check_out <= history_out:
                return False
        return True


# debugging
if __name__ == "__main__":
    pass
