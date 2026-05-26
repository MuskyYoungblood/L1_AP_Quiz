import random
import math

pi = math.pi
rounded_percentage = []

# Ultimate string checker. Can display any question with any given options.
def response_check(question, options):
   error = f"Please choose from the following: {options}"
   while True:
       response = input(question).lower()
       for opt in options:
           if response == opt or response == opt[0]:
               return opt
       print(error)


# Classic integer checker
def int_check(question, low=0):
   while True:
       try:
           response = int(input(question))
           if response > low:
               return response
           print(f"Please enter a number greater than {low}")
       except ValueError:
           print("Please enter a valid integer.")

# Checks if user answers are correct or incorrect
def question_check(answer):
   while True:
       try:
           user = float(input(question))
           answer = round(answer, 2)
           if user == answer:
               feedback = "You got the answer correct."
               history_feedback = f"Question {questions_answered} of {num_questions}: {feedback}"
               quiz_history.append(history_feedback)
               correct_ans.append(1)



               return
           else:
               feedback = "You got the answer incorrect."
               history_feedback = f"Question {questions_answered} of {num_questions}: {feedback}"
               quiz_history.append(history_feedback)

               return


       except ValueError:
           print("Please enter a number.")

def instruction():
    print('''

**** Instructions ****

Answer area and perimeter math questions according to the difficulty you set.

    ''')

# Main Routine
questions_answered = 0
quiz_history = []
correct_ans = []

print("Welcome to my math quiz!")

if response_check("\nDo you want to see the instructions? ", ["yes", "no"]) == "yes":
    instruction()

difficulty = response_check("Select a difficulty: ", ["easy", "medium", "hard"])

num_questions = int_check("How many questions would you like? ")

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

        if shape == "square":
            answer = random_num_a * random_num_a
            question = f"A square has a base of {random_num_a}{units}. What is its area? "

        if shape == "rectangle":
            answer = random_num_a * random_num_b
            question = f"A rectangle has a base of {random_num_a}{units} and a height of {random_num_b}{units}. What is its area? "
        if shape == "circle":
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
        else:
            answer = 2 * pi * random_num_a
            question = f"A circle has a radius of {random_num_a}{units}. What is its circumference? "

    # Displays the question
    questions_answered += 1
    question_check(answer)

see_history = response_check("\nDo you want to see your game history? ", ["yes", "no"])
if see_history == "yes":
    print("\nQuiz History:\n")
    for item in quiz_history:
        print(item)

    amount_of_correct = len(correct_ans)

    percentage = round((amount_of_correct / num_questions) * 100, 2)
    print(f"{percentage}% / 100%")


print("\nThank you for participating in my quiz!")