import random
import time

def clear_screen():
    print("\n" * 50)

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

class ListWizardGame:
    def __init__(self):
        self.player_spells = []
        self.available_spells = ['fireball', 'ice_shard', 'lightning_bolt', 'wind_gust']
        self.spell_book = []
        self.level = 1
        self.list_methods = {
            'append': "Adds an element to the end of the list",
            'extend': "Adds multiple elements from another list",
            'insert': "Adds an element at a specific position",
            'remove': "Removes the first occurrence of an element",
            'pop': "Removes and returns an element at given index",
            'clear': "Removes all elements from the list",
            'index': "Returns the index of the first occurrence of an element",
            'count': "Returns the number of occurrences of an element",
            'sort': "Sorts the list in ascending order",
            'reverse': "Reverses the order of elements",
            'copy': "Returns a shallow copy of the list"
        }

    def display_intro(self):
        slow_print("\n🧙‍♂️ Welcome to the List Wizard Academy! 🧙‍♀️")
        slow_print("Here you'll learn the ancient art of List Magic...")
        slow_print("Master different list methods to become a true List Wizard!\n")
        input("Press Enter to begin your journey...")

    def show_list_state(self):
        print("\n📜 Your current spell list:", self.player_spells)
        print("Available spells:", self.available_spells)

    def practice_method(self, method_name):
        clear_screen()
        print(f"\n=== Learning {method_name.upper()} ===")
        print(f"Description: {self.list_methods[method_name]}")
        
        self.show_list_state()
        
        if method_name == 'append':
            print("\nTask: Add a new spell to your list using append()")
            print("Example: spell_list.append('fireball')")
            
            while True:
                command = input("\nEnter your command (or 'help'): ").strip()
                if command == 'help':
                    print("\nHint: Use append() to add one of the available spells")
                    continue
                
                try:
                    eval(f"self.player_spells.{command}")
                    if len(self.player_spells) > 0 and self.player_spells[-1] in self.available_spells:
                        print("✨ Success! You've mastered append!")
                        return True
                except:
                    print("❌ That didn't work. Try again!")

        elif method_name == 'remove':
            if not self.player_spells:
                self.player_spells = ['fireball', 'ice_shard']
            print("\nTask: Remove a spell from your list using remove()")
            print("Example: spell_list.remove('fireball')")
            
            while True:
                command = input("\nEnter your command (or 'help'): ").strip()
                if command == 'help':
                    print("\nHint: Use remove() with the name of a spell in your list")
                    continue
                
                try:
                    initial_len = len(self.player_spells)
                    eval(f"self.player_spells.{command}")
                    if len(self.player_spells) < initial_len:
                        print("✨ Success! You've mastered remove!")
                        return True
                except:
                    print("❌ That didn't work. Try again!")

        elif method_name == 'sort':
            self.player_spells = ['wind_gust', 'fireball', 'ice_shard']
            print("\nTask: Sort your spells alphabetically using sort()")
            print("Example: spell_list.sort()")
            
            while True:
                command = input("\nEnter your command (or 'help'): ").strip()
                if command == 'help':
                    print("\nHint: Just use the sort() method")
                    continue
                
                try:
                    eval(f"self.player_spells.{command}")
                    if self.player_spells == sorted(['wind_gust', 'fireball', 'ice_shard']):
                        print("✨ Success! You've mastered sort!")
                        return True
                except:
                    print("❌ That didn't work. Try again!")

    def play(self):
        self.display_intro()
        
        methods_to_learn = ['append', 'remove', 'sort']  # Add more methods as needed
        
        for method in methods_to_learn:
            clear_screen()
            slow_print(f"\n📚 Level {self.level}: Master the {method.upper()} method!")
            input("Press Enter to start the lesson...")
            
            if self.practice_method(method):
                self.level += 1
                self.spell_book.append(method)
                slow_print(f"\n🎉 Congratulations! You've learned the {method} method!")
                slow_print(f"Your spell book now contains: {', '.join(self.spell_book)}")
                input("\nPress Enter to continue...")
        
        clear_screen()
        slow_print("\n🎓 Congratulations! You've graduated from the List Wizard Academy!")
        slow_print(f"You've mastered {len(self.spell_book)} list methods: {', '.join(self.spell_book)}")
        slow_print("\nBonus Knowledge:")
        slow_print("- Lists are ordered collections that can contain any type of data")
        slow_print("- List indices start at 0")
        slow_print("- Lists are mutable (can be modified after creation)")
        slow_print("\nKeep practicing to become a true List Wizard! ✨")

if __name__ == "__main__":
    game = ListWizardGame()
    game.play()
