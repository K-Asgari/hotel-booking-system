import booking_system

full_names = ["John Smith",
              "Emily Johnson",
              "Michael Davis",
              "Sarah Rodriguez",
              "David Lee"
              ]
phone_numbers = ['45404850',
                 '40112926',
                 '44783246',
                 '41783813',
                 '47444902'
                 ]
dates = [('2023-05-24', '2023-05-25'),
         ('2023-05-15', '2023-05-16'),
         ('2023-05-30', '2023-05-31'),
         ('2023-05-19', '2023-05-20'),
         ('2023-06-09', '2023-06-10')
         ]

if __name__ == "__main__":
    for i in range(5):
        b = {
            "name": full_names[i],
            "phone": phone_numbers[i],
            "check_in": dates[i][0],
            "check_out": dates[i][1]
            }

        booking_system.write_booking_to_json(b, "room1")
