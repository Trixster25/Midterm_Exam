import requests
import json
import sys

accessToken = "Bearer N2U0NTEwMTItMmU3OS00Y2Y2LWEzNGMtYTA1MzQ4MmJmYjY1MWExNDY3ZTMtNzMy_P0A1_d8874c41-f836-471b-bf45-f4bf285408d0"

choice = input("Do you wish to use the hard coded token? (y/n): ")

if choice.lower() == "n":
    accessToken = input("Enter your access token: ")
    accessToken = "Bearer " + accessToken

def setHeaders():
    return {
        "Authorization": accessToken,
        "Content-Type": "application/json"
    }

def getRooms(theHeader):
    uri = "https://webexapis.com/v1/rooms"
    resp = requests.get(uri, headers=theHeader)
    return resp.json()

def createRoom(theHeader, roomName):
    uri = "https://webexapis.com/v1/rooms"
    payload = {"title": roomName}
    resp = requests.post(uri, headers=theHeader, json=payload)
    return resp.json()

def addMemberToRoom(theHeader, roomId, personEmail):
    uri = "https://webexapis.com/v1/memberships"
    payload = {"roomId": roomId, "personEmail": personEmail}
    resp = requests.post(uri, headers=theHeader, json=payload)
    return resp.json()

header = setHeaders()
value = getRooms(header)

rooms = value.get("items", [])
for room in rooms:
    print(f"Room name: '{room['title']}' ID: {room['id']}")

while True:
    choice = input("Do you want to (1) list rooms, (2) create a room, (3) add member to a room, or (4) exit? (Enter 1, 2, 3, or 4): ")

    if choice == "1":
        roomNameToSearch = input("Enter full or partial name of the room to find: ")
        found = False
        for room in rooms:
            if room["title"].lower().find(roomNameToSearch.lower()) != -1:
                found = True
                print(f"Found room: '{room['title']}' ID: {room['id']}")
        if not found:
            print(f"Did not find a room with '{roomNameToSearch}' in its title.")

    elif choice == "2":
        roomName = input("Enter the name of the room you want to create: ")
        response = createRoom(header, roomName)
        print(f"Room '{response.get('title', 'Unknown')}' created with ID: {response.get('id', 'Unknown')}")

    elif choice == "3":
        roomId = input("Enter the ID of the room you want to add a member to: ")
        personEmail = input("Enter the email of the person you want to add: ")
        response = addMemberToRoom(header, roomId, personEmail)
        if "id" in response:
            print("Member added successfully to the room.")
        else:
            print("Failed to add member to the room. Error:", response.get("message", "Unknown error"))

    elif choice == "4":
        print("Exiting the program.")
        sys.exit()

    else:
        print("Invalid choice. Please enter either 1, 2, 3, or 4.")
