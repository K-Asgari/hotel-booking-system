# Made for debugging purposes
import booking_system

def reset():
    n_rooms = len(booking_system.ROOMS)
    with open(booking_system.FILENAME, "w") as f:
        for i, room in enumerate(booking_system.ROOMS, 1):
            if i == 1:
                f.write("{\n")
            if i != n_rooms:
                f.write(f' "{room}": [],\n')
            else:
                f.write(f' "{room}": [] \n')
            if i == n_rooms:
                f.write("}\n")




if __name__ == "__main__":
    reset()
