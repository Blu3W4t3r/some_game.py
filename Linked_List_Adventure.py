class Room:
    def __init__(self, description):
        self.description = description
        self.next_room = None  # Pointer to the next room (node)

class LinkedListAdventure:
    def __init__(self):
        self.start_room = None

    def add_room(self, description):
        new_room = Room(description)
        if not self.start_room:
            self.start_room = new_room
        else:
            current = self.start_room
            while current.next_room:
                current = current.next_room
            current.next_room = new_room

    def play(self):
        current = self.start_room
        while current:
            print("\nYou are in a room.")
            print(current.description)
            choice = input("Do you want to move to the next room? (yes/no): ").strip().lower()
            if choice == "yes":
                if current.next_room:
                    current = current.next_room
                else:
                    print("There are no more rooms. You have reached the end of the adventure!")
                    break
            elif choice == "no":
                print("Thanks for playing!")
                break
            else:
                print("Invalid choice. Please type 'yes' or 'no'.")

# Set up the adventure
adventure = LinkedListAdventure()
adventure.add_room("A dark and eerie room with strange markings on the walls.")
adventure.add_room("A brightly lit room filled with ancient books and scrolls.")
adventure.add_room("A forest glade with sunlight streaming down and birds chirping.")
adventure.add_room("A misty cave where you can hear water dripping somewhere in the darkness.")

# Start the game
print("Welcome to Linked List Adventure!")
adventure.play()
