class HotelManagementSystem:
    def __init__(self):
        self.rooms = {}  # Dictionary to hold room numbers and guest names
        self.room_count = 10  # Number of rooms in the hotel
        self.initialize_rooms()

    def initialize_rooms(self):
        for i in range(1, self.room_count + 1):
            self.rooms[i] = None

    def check_in(self, room_number, guest_name):
        if room_number < 1 or room_number > self.room_count:
            print("Invalid room number.")
        elif self.rooms[room_number] is not None:
            print(f"Room {room_number} is already occupied.")
        else:
            self.rooms[room_number] = guest_name
            print(f"Guest {guest_name} has been checked into room {room_number}.")

    def check_out(self, room_number):
        if room_number < 1 or room_number > self.room_count:
            print("Invalid room number.")
        elif self.rooms[room_number] is None:
            print(f"Room {room_number} is already vacant.")
        else:
            guest_name = self.rooms[room_number]
            self.rooms[room_number] = None
            print(f"Guest {guest_name} has been checked out from room {room_number}.")

    def view_guests(self):
        print("Current guests in the hotel:")
        for room_number, guest_name in self.rooms.items():
            if guest_name is None:
                print(f"Room {room_number}: Vacant")
            else:
                print(f"Room {room_number}: {guest_name}")

def main():
    hotel = HotelManagementSystem()

    while True:
        print("\nHotel Management System")
        print("1. Check In")
        print("2. Check Out")
        print("3. View Guests")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            room_number = int(input("Enter room number: "))
            guest_name = input("Enter guest name: ")
            hotel.check_in(room_number, guest_name)
        elif choice == '2':
            room_number = int(input("Enter room number: "))
            hotel.check_out(room_number)
        elif choice == '3':
            hotel.view_guests()
        elif choice == '4':
            print("Exiting the system.")
            break
        else:  
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
