import requests
import json
import webexteamssdk

accessToken = "Bearer N1U0NTEwMTItMmU3OS00Y2Y2LWEzNGMtYTA1MzQ4MmJmYjY1MWExNDY3ZTMtNzMy_P0A1_d8874c41-f836-471b-bf45-f4bf285408d0"

choice = input("Do you wish to use the hard coded token? (y/n)")

if choice.lower() == "n":
    accessToken = input("Enter your access token: ")
    accessToken = "Bearer " + accessToken

def setHeaders():         
    webex_api_header = {"Authorization" : accessToken, 
                        "Content-Type": "application/json"}
    return webex_api_header

def getRooms(theHeader):    
    uri = "https://webexapis.com/v1/rooms"  # Corrected endpoint for listing rooms
    resp = requests.get(uri, headers=theHeader)
    return resp.json()

def createRoom(theHeader, roomName):
    uri = "https://webexapis.com/v1/rooms"
    payload = {"title": roomName}
    resp = requests.post(uri, headers=theHeader, json=payload)
    return resp.json()

header = setHeaders()
value = getRooms(header)

jsonData = value

print(
    json.dumps(
        jsonData,
        indent=4
    )
)

rooms = jsonData["items"]
for room in rooms:
    print("Room name: '" + room["title"] + "' ID: " + room["id"])

while True:
    choice = input("Do you want to (1) list rooms or (2) create a room? (Enter 1 or 2): ")
    if choice == "1":
        roomNameToSearch = input("Enter full or partial name of the room to find: ")
        found = False
        for room in rooms:
            if room["title"].lower().find(roomNameToSearch.lower()) != -1:
                found = True
                print("Found room: '" + room["title"] + "' ID: " + room["id"])
        if not found:
            print("Did not find a room with '{}' in its title.".format(roomNameToSearch))
    elif choice == "2":
        roomName = input("Enter the name of the room you want to create: ")
        response = createRoom(header, roomName)
        print("Room '{}' created with ID: {}".format(response["title"], response["id"]))
    else:
        print("Invalid choice. Please enter either 1 or 2.")
