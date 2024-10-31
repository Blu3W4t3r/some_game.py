class StackGame:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"Item '{item}' pushed to stack.")

    def pop(self):
        if not self.stack:
            print("Stack is empty. Cannot pop.")
        else:
            item = self.stack.pop()
            print(f"Item '{item}' popped from stack.")

    def display(self):
        if not self.stack:
            print("Stack is empty.")
        else:
            print("Stack contents:", self.stack)

    def start(self):
        print("Welcome to the Stack Game!")
        while True:
            print("\nChoose an action:")
            print("1. Push item")
            print("2. Pop item")
            print("3. Display stack")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                item = input("Enter item to push: ")
                self.push(item)
            elif choice == '2':
                self.pop()
            elif choice == '3':
                self.display()
            elif choice == '4':
                print("Exiting game. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    game = StackGame()
    game.start()