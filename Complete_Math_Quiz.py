import random
import math

# Establishing variables
pi = math.pi
rounded_percentage = []
questions_answered = 0
quiz_history = []
correct_ans = []

def ult_str_check(question, options):
   """Ultimate string checker. Can display any question with any given options"""
   error = f"Please choose from the following: {options}"
   while True:
       response = input(question).lower()
       for opt in options:
           if response == opt or response == opt[0]:
               return opt
       print(error)

def int_check(question, low=0):
   """Classic integer checker"""
   while True:
       try:
           response = int(input(question))
           if response > low:
               return response
           print(f"Please enter a number greater than {low}")
       except ValueError:
           print("Please enter a valid integer.")

def question_check(answer):
   """Checks user's questions in comparison to the correct answer"""
   while True:
       try:
           user = float(input(question))
           answer = round(answer, 2)
           # If the user got the question correct or incorrect, it adds your feedback to the quiz history
           # History_feedback is what's displayed when user asks for quiz history
           if user == answer:
               feedback = "Congratulations! You got the answer correct!"
               history_feedback = f"Question {questions_answered} of {num_questions}:\n{feedback}\n"
               quiz_history.append(history_feedback)
               correct_ans.append(1)
               return
           else:
               feedback = f"The answer you gave was {user}, but the correct answer is {answer}. \nSorry, you got the answer incorrect."
               history_feedback = f"Question {questions_answered} of {num_questions}:\n{feedback}\n"
               quiz_history.append(history_feedback)
               return


       except ValueError:
           print("Please enter a number.")

def instruction():
    """Gives instructions"""

    print('''

**** Instructions ****

Answer area and perimeter math questions according to the difficulty you set: "easy", "medium", or "hard".

    ''')

# Main Routine
print("Welcome to my math quiz!")

# Asks user for instructions (options are 'yes' and 'no')
if ult_str_check("\nDo you want to see the instructions? ", ["yes", "no"]) == "yes":
    instruction()

# Asks users for difficulty (options are 'easy', 'medium', 'hard')
difficulty = ult_str_check("Select a difficulty: ", ["easy", "medium", "hard"])

# Asks users for questions
num_questions = int_check("How many questions would you like? ")

# Colour of mode depends on difficulty
difficulty_title = difficulty.title()
if difficulty_title == "Hard":
    print(f"\n\033[31m**** {difficulty.title()} Mode ****\033[0m")
elif difficulty_title == "Medium":
    print(f"\n\033[35m**** {difficulty.title()} Mode ****\033[0m")
elif difficulty_title == "Easy":
    print(f"\n\033[32m**** {difficulty.title()} Mode ****\033[0m")

# Game loop starts here
while num_questions > questions_answered:
    print(f"\nQuestion {questions_answered+1} of {num_questions}:\n")

    units = random.choice(["cm", "m", "ft", "mm"])
    random_num_a, random_num_b, random_num_c = random.randint(10, 30), random.randint(10, 30), random.randint(10, 30)

    # Difficulty question types
    if difficulty == "easy":
        question_type = "perimeter"
        shape = random.choice(["square", "rectangle"])
    if difficulty == "medium":
        question_type = random.choice(["perimeter", "area"])
        shape = random.choice(["square", "rectangle", "triangle"])
    if difficulty == "hard":
        question_type = random.choice(["perimeter", "area"])
        shape = random.choice(["triangle", "square", "rectangle", "circle"])

    # Area
    if question_type == "area":
        if shape == "triangle":
            answer = random_num_a * random_num_b / 2
            question = f"A triangle has a base of {random_num_a}{units} and a height of {random_num_b}. What is its area? "
        elif shape == "square":
            answer = random_num_a * random_num_a
            question = f"A square has a base of {random_num_a}{units}. What is its area? "
        elif shape == "rectangle":
            answer = random_num_a * random_num_b
            question = f"A rectangle has a base of {random_num_a}{units} and a height of {random_num_b}{units}. What is its area? "
        elif shape == "circle":
            answer = pi * (random_num_a * random_num_a)
            question = f"A circle has a radius of {random_num_a}{units}. What is its area? "


    # Perimeters
    if question_type == "perimeter":
        if shape == "triangle":
            answer = random_num_a + random_num_b + random_num_c
            question = f"A triangle has sides of {random_num_a}{units}, {random_num_b}{units}, and {random_num_c}{units}. What is its perimeter? "
        elif shape == "square":
            answer = random_num_a * 4
            question = f"A square has sides of {random_num_a}{units}. What is its perimeter? "
        elif shape == "rectangle":
            answer = random_num_a * 2 + random_num_b * 2
            question = f"A rectangle has sides of {random_num_a}{units} and {random_num_b}{units}. What is its perimeter? "
        elif shape == "circle":
            answer = 2 * pi * random_num_a
            question = f"A circle has a radius of {random_num_a}{units}. What is its circumference? "

    # Displays the question
    questions_answered += 1
    question_check(answer)

# Asks user for quiz history (options 'yes' and 'no')
see_history = ult_str_check("\nDo you want to see your game history? ", ["yes", "no"])

# Displays quiz history
if see_history == "yes":
    print("\nQuiz History:\n")
    for item in quiz_history:
        print(item)

    # Displays user's percentage
    amount_of_correct = len(correct_ans)
    percentage = round((amount_of_correct / num_questions) * 100, 2)
    print(f"{percentage}% / 100%")


print("\nThank you for participating in my quiz!")