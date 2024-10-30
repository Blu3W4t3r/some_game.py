import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()

def game_over():
    print_slow("\nGAME OVER")
    play_again = input("\nWould you like to play again? (yes/no): ").lower()
    if play_again == 'yes':
        start_game()
    else:
        print_slow("\nThanks for playing!")
        exit()

def make_choice(options):
    while True:
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        
        choice = input("\nEnter your choice (number): ")
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return int(choice)
        print("\nInvalid choice. Please try again.")

def start_game():
    clear_screen()
    print_slow("Welcome to the Adventure Game!")
    print_slow("\nYou wake up in a mysterious forest clearing...")
    print_slow("There are two paths ahead of you.")
    
    choice = make_choice(["Take the dark path to the left",
                         "Take the sunny path to the right"])
    
    if choice == 1:
        dark_path()
    else:
        sunny_path()

def dark_path():
    clear_screen()
    print_slow("\nYou venture down the dark path...")
    print_slow("You hear strange noises in the distance.")
    
    choice = make_choice(["Investigate the noise",
                         "Turn back",
                         "Hide behind a tree"])
    
    if choice == 1:
        print_slow("\nYou follow the noise and find an ancient treasure chest!")
        print_slow("Congratulations! You've won!")
    elif choice == 2:
        print_slow("\nWhile turning back, you trip and fall into a pit!")
        game_over()
    else:
        print_slow("\nWhile hiding, a friendly wizard finds you and grants you a wish!")
        print_slow("Congratulations! You've won!")

def sunny_path():
    clear_screen()
    print_slow("\nYou walk down the sunny path...")
    print_slow("You come across a peaceful meadow with a small cottage.")
    
    choice = make_choice(["Knock on the cottage door",
                         "Search around the cottage",
                         "Continue past the cottage"])
    
    if choice == 1:
        print_slow("\nA kind old lady invites you in for tea and cookies!")
        print_slow("Congratulations! You've won!")
    elif choice == 2:
        print_slow("\nYou find a magic ring in the garden!")
        print_slow("Congratulations! You've won!")
    else:
        print_slow("\nYou get lost in the woods and cannot find your way back!")
        game_over()

if __name__ == "__main__":
    start_game() 