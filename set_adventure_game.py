# set_adventure_game.py

class SetAdventureGame:
    def __init__(self):
        self.player_set = set()
        self.current_room = 'start'

    def start(self):
        print("Welcome to the Set Adventure Game!")
        while True:
            if self.current_room == 'start':
                self.start_room()
            elif self.current_room == 'forest':
                self.forest_room()
            elif self.current_room == 'cave':
                self.cave_room()
            elif self.current_room == 'treasure':
                self.treasure_room()
            else:
                print("Game Over!")
                break

    def start_room(self):
        print("\nYou are in a room with two doors: one to the left and one to the right.")
        choice = input("Do you want to go left or right? ").lower()
        if choice == 'left':
            self.current_room = 'forest'
        elif choice == 'right':
            self.current_room = 'cave'
        else:
            print("Invalid choice. Try again.")

    def forest_room(self):
        print("\nYou are in a forest. You find some fruits: {apple, banana, cherry}.")
        self.player_set.update({'apple', 'banana', 'cherry'})
        print(f"Your current set of fruits: {self.player_set}")
        choice = input("Do you want to go deeper into the forest or return to the start? ").lower()
        if choice == 'deeper':
            self.current_room = 'treasure'
        elif choice == 'return':
            self.current_room = 'start'
        else:
            print("Invalid choice. Try again.")

    def cave_room(self):
        print("\nYou are in a cave. You find some gems: {ruby, emerald}.")
        gems = {'ruby', 'emerald'}
        print(f"Gems found: {gems}")
        self.player_set = self.player_set.union(gems)
        print(f"Your current set of items: {self.player_set}")
        choice = input("Do you want to explore the cave further or return to the start? ").lower()
        if choice == 'explore':
            print("You found a hidden treasure! You win!")
            self.current_room = 'treasure'
        elif choice == 'return':
            self.current_room = 'start'
        else:
            print("Invalid choice. Try again.")

    def treasure_room(self):
        print("\nYou are in the treasure room. Congratulations, you found the treasure!")
        print(f"Your final set of items: {self.player_set}")
        choice = input("Do you want to play again? (yes/no) ").lower()
        if choice == 'yes':
            self.player_set.clear()  # Reset the player's set
            self.current_room = 'start'
        else:
            print("Thanks for playing!")
            self.current_room = 'end'

if __name__ == "__main__":
    game = SetAdventureGame()
    game.start()
