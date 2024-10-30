import os
import time
import random

class PythonTeacher:
    def __init__(self):
        self.score = 0
        self.player_name = ""
        self.lessons_completed = 0
        
        # Store all lessons and their challenges
        self.lessons = {
            1: {
                'title': 'Variables & Data Types',
                'content': '''
Python has several basic data types:
1. Strings (text): "Hello" or 'World'
2. Integers (whole numbers): 42
3. Floats (decimal numbers): 3.14
4. Booleans: True or False

Example:
name = "Alice"    # String
age = 25         # Integer
height = 1.75    # Float
is_student = True # Boolean
''',
                'questions': [
                    {
                        'question': 'What data type is "Hello, World!"?',
                        'answer': 'string',
                        'hint': 'Text values are called...'
                    },
                    {
                        'question': 'What data type is 42?',
                        'answer': 'integer',
                        'hint': 'Whole numbers are called...'
                    }
                ]
            },
            2: {
                'title': 'Basic Operations',
                'content': '''
Python supports various mathematical operations:
+ : Addition
- : Subtraction
* : Multiplication
/ : Division
// : Integer Division
% : Modulus (remainder)
** : Exponentiation

Examples:
5 + 3 = 8
10 - 4 = 6
3 * 4 = 12
8 / 2 = 4
''',
                'questions': [
                    {
                        'question': 'What is 15 % 4? (remainder when 15 is divided by 4)',
                        'answer': '3',
                        'hint': 'Divide 15 by 4 and look at the remainder'
                    },
                    {
                        'question': 'What is 2 ** 3? (2 to the power of 3)',
                        'answer': '8',
                        'hint': 'Multiply 2 by itself 3 times'
                    }
                ]
            },
            3: {
                'title': 'Lists',
                'content': '''
Lists are ordered collections of items:
- Created using square brackets []
- Can store different types of data
- Index starts at 0

Example:
fruits = ['apple', 'banana', 'orange']
numbers = [1, 2, 3, 4, 5]

Access items:
fruits[0]    # returns 'apple'
fruits[-1]   # returns last item
''',
                'questions': [
                    {
                        'question': "If colors = ['red', 'blue', 'green'], what is colors[0]?",
                        'answer': 'red',
                        'hint': 'Remember, indexing starts at 0'
                    },
                    {
                        'question': "How do you write an empty list?",
                        'answer': '[]',
                        'hint': 'Use square brackets'
                    }
                ]
            }
        }

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_slow(self, text):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.02)
        print()

    def show_welcome(self):
        self.clear_screen()
        print("""
╔═══════════════════════════════════════╗
║     Welcome to Python Learning Game    ║
║         Learn Python with Fun!         ║
╚═══════════════════════════════════════╝
        """)
        self.player_name = input("Enter your name: ").strip()
        if not self.player_name:
            self.player_name = "Student"

    def show_lesson(self, lesson_num):
        self.clear_screen()
        lesson = self.lessons[lesson_num]
        print(f"\n=== Lesson {lesson_num}: {lesson['title']} ===\n")
        print(lesson['content'])
        input("\nPress Enter when you're ready for the challenge...")

    def ask_question(self, question_data):
        self.clear_screen()
        print(f"\nQuestion: {question_data['question']}")
        
        attempts = 3
        while attempts > 0:
            answer = input("\nYour answer: ").strip().lower()
            
            if answer == question_data['answer'].lower():
                self.print_slow("\n🎉 Correct! +10 points!")
                self.score += 10
                return True
            else:
                attempts -= 1
                if attempts > 0:
                    print(f"\n❌ Not quite. You have {attempts} attempts left.")
                    print(f"Hint: {question_data['hint']}")
                else:
                    print(f"\n❌ The correct answer was: {question_data['answer']}")
        return False

    def show_progress(self):
        self.clear_screen()
        print(f"\nPlayer: {self.player_name}")
        print(f"Score: {self.score}")
        print(f"Lessons Completed: {self.lessons_completed}/{len(self.lessons)}")
        input("\nPress Enter to continue...")

    def play(self):
        self.show_welcome()
        
        for lesson_num in self.lessons:
            self.show_lesson(lesson_num)
            
            # Ask all questions for this lesson
            for question in self.lessons[lesson_num]['questions']:
                self.ask_question(question)
            
            self.lessons_completed += 1
            self.show_progress()
        
        self.show_game_over()

    def show_game_over(self):
        self.clear_screen()
        max_score = sum(len(lesson['questions']) * 10 for lesson in self.lessons.values())
        percentage = (self.score / max_score) * 100

        print(f"""
╔═══════════════════════════════════════╗
║            Game Complete!             ║
╠═══════════════════════════════════════╣
║ Player: {self.player_name:<27} ║
║ Final Score: {self.score}/{max_score:<20} ║
║ Percentage: {percentage:.1f}%{' ' * 19} ║
╚═══════════════════════════════════════╝
        """)

        if percentage >= 80:
            print("🌟 Outstanding! You're a Python natural!")
        elif percentage >= 60:
            print("👍 Good job! Keep practicing!")
        else:
            print("💪 Nice try! Remember, learning takes time!")

        if input("\nWould you like to play again? (yes/no): ").lower().startswith('y'):
            self.__init__()
            self.play()
        else:
            print("\nThanks for learning Python! Keep coding! 👋")

if __name__ == "__main__":
    game = PythonTeacher()
    game.play() 