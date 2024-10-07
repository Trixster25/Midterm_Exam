import requests
import json

# Create variable to enter access token
# -------------------------------------
choice = input("Do you want to use the hard-coded token? (y/n): ")

# Conditional statement to use default access token when user enters N/n
# --------------------------------------------------------------------
if choice.lower() == "n":
    accessToken = input("Enter your access token: ")
    accessToken = "Bearer " + accessToken
else:
    accessToken = "Bearer N2U0NTEwMTItMmU3OS00Y2Y2LWEzNGMtYTA1MzQ4MmJmYjY1MWExNDY3ZTMtNzMy_P0A1_d8874c41-f836-471b-bf45-f4bf285408d0"

# Function to get rooms
def get_rooms():
    resp = requests.get(
        "https://webexapis.com/v1/rooms",
        headers={"Authorization": accessToken}
    )
    
    if resp.status_code != 200:
        raise Exception("Incorrect reply from Webex Teams API. Status code: {}. Text: {}".format(resp.status_code, resp.text))

    return resp.json().get("items", [])

# Function to create a message
def create_message(room_id, message_text):
    payload = {
        "roomId": room_id,
        "text": message_text
    }
    resp = requests.post(
        "https://webexapis.com/v1/messages",
        headers={"Authorization": accessToken, "Content-Type": "application/json"},
        json=payload
    )
    
    if resp.status_code != 200:
        raise Exception("Failed to create message. Status code: {}. Text: {}".format(resp.status_code, resp.text))

    return resp.json()

# Function to view messages in a room
def view_messages(room_id):
    params = {"roomId": room_id, "max": 50}
    resp = requests.get(
        "https://webexapis.com/v1/messages",
        params=params,
        headers={"Authorization": accessToken}
    )
    
    if resp.status_code != 200:
        raise Exception("Failed to retrieve messages. Status code: {}. Text: {}".format(resp.status_code, resp.text))

    return resp.json().get("items", [])

# Function to delete a message
def delete_message(message_id):
    resp = requests.delete(
        f"https://webexapis.com/v1/messages/{message_id}",
        headers={"Authorization": accessToken}
    )
    
    if resp.status_code != 204:
        raise Exception("Failed to delete message. Status code: {}. Text: {}".format(resp.status_code, resp.text))

    print(f"Message {message_id} deleted successfully.")

# Main program
rooms = get_rooms()
print("Available rooms:")
for room in rooms:
    print(f"Room name: '{room['title']}' ID: {room['id']}")

room_id = input("Enter the room ID to send/view/delete messages: ")

while True:
    print("\nOptions: (1) Create Message, (2) View Messages, (3) Delete Message, (4) Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        message_text = input("Enter the message you want to send: ")
        response = create_message(room_id, message_text)
        print("Message sent successfully:", response)

    elif choice == "2":
        messages = view_messages(room_id)
        if messages:
            print("Messages in the room:")
            for message in messages:
                print(f"Message ID: {message['id']}, Text: {message['text']}, From: {message['personEmail']}")
        else:
            print("No messages found in this room.")

    elif choice == "3":
        message_id = input("Enter the message ID to delete: ")
        delete_message(message_id)

    elif choice == "4":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
