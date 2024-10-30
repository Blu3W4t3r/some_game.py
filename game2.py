class Game:
    def __init__(self):
        self.inventory = []
        self.current_room = "hall"
        self.game_running = True
        self.rooms = {
            "hall": {
                "name": "Great Hall",
                "description": "You are in a grand hall with marble floors. There's a staircase leading upstairs and doors to the east and west.",
                "exits": {"upstairs": "bedroom", "east": "kitchen", "west": "library"},
                "items": ["key"]
            },
            "kitchen": {
                "name": "Kitchen",
                "description": "A rustic kitchen with an old stove. There's a strange smell coming from somewhere.",
                "exits": {"west": "hall"},
                "items": ["knife", "apple"]
            },
            "library": {
                "name": "Library",
                "description": "Walls of ancient books surround you. A comfortable chair sits in the corner.",
                "exits": {"east": "hall"},
                "items": ["book"]
            },
            "bedroom": {
                "name": "Bedroom",
                "description": "A dusty bedroom with an old bed and a chest.",
                "exits": {"downstairs": "hall"},
                "items": ["coin"]
            }
        }

    def show_room(self):
        room = self.rooms[self.current_room]
        print(f"\n=== {room['name']} ===")
        print(room['description'])
        
        if room['items']:
            print("\nYou see:", ", ".join(room['items']))
        
        print("\nPossible exits:", ", ".join(room['exits'].keys()))
        print("\nInventory:", ", ".join(self.inventory) if self.inventory else "empty")

    def get_input(self):
        return input("\nWhat would you like to do? ").lower().split()

    def process_command(self, command):
        if len(command) == 0:
            return
        
        action = command[0]
        
        if action == "quit":
            self.game_running = False
            print("Thanks for playing!")
            return
            
        if action == "help":
            print("\nCommands:")
            print("go [direction] - Move in a direction")
            print("take [item] - Pick up an item")
            print("drop [item] - Drop an item")
            print("inventory - Show your inventory")
            print("look - Look around")
            print("quit - Exit the game")
            return

        if action == "go":
            if len(command) < 2:
                print("Go where?")
                return
                
            direction = command[1]
            if direction in self.rooms[self.current_room]['exits']:
                self.current_room = self.rooms[self.current_room]['exits'][direction]
                self.show_room()
            else:
                print("You can't go that way!")

        elif action == "take":
            if len(command) < 2:
                print("Take what?")
                return
                
            item = command[1]
            if item in self.rooms[self.current_room]['items']:
                self.rooms[self.current_room]['items'].remove(item)
                self.inventory.append(item)
                print(f"You picked up the {item}.")
            else:
                print("You don't see that here.")

        elif action == "drop":
            if len(command) < 2:
                print("Drop what?")
                return
                
            item = command[1]
            if item in self.inventory:
                self.inventory.remove(item)
                self.rooms[self.current_room]['items'].append(item)
                print(f"You dropped the {item}.")
            else:
                print("You don't have that.")

        elif action == "look":
            self.show_room()

        elif action == "inventory":
            print("\nInventory:", ", ".join(self.inventory) if self.inventory else "empty")

        else:
            print("I don't understand that command. Type 'help' for commands.")

def main():
    game = Game()
    print("\nWelcome to the Adventure Game!")
    print("Type 'help' for a list of commands.")
    game.show_room()
    
    while game.game_running:
        command = game.get_input()
        game.process_command(command)

if __name__ == "__main__":
    main()
