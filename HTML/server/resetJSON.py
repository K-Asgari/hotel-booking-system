"""
Made for debugging:
Resets/init JSON file
"""

import json

FILENAME = 'data.json'
PATH = 'HTML/server/'

data = {
  "bookings": []
}

with open(PATH + FILENAME, 'w') as json_file:
    json.dump(data, json_file)

print(f"{FILENAME} has been reset.")
