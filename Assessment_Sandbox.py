import random
import math

pi = math.pi

def string_checker(question, valid_ans=("yes", "no")):
    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # Get user response and make sure it's lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item

            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        # print error if user does not enter something that is valid
        print(error)
        print()

def difficulty_check(question, valid_ans=("easy", "medium", "hard")):
    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # Get user response and make sure it's lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item

            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        # print error if user does not enter something that is valid
        print(error)
        print()


def instruction():
    print('''

**** Instructions ****

Answer area and perimeter math questions.

    ''')

def int_check(question, num_type=int, low=0, exit_code="xxx"):
    error = f"Please enter an integer than is more than {low}."

    while True:
        # Ask user question and return response if exit code is entered
        response = input(question)
        if response == exit_code:
            return response

        # Check response is more than the minimum
        try:
            response = num_type(response)

            if response > low:
                return response
            else:
                print(error)

        # Show error if response is invalid
        except ValueError:
            print(error)

def ans_check():
    """Checks users enter a number"""

    error = "Please enter a number."

    correct_ans = "Correct answer!"

    while True:
        try:
            if question_type == "perimeter":
                if shape == "circle":
                    response = float(input(f"Calculate the circumference of the circle: "))
                else:
                    response = float(input(f"What is the perimeter of the {shape}? "))
            if question_type == "area":
                if shape == "circle":
                    response = float(input(f"Calculate the area of the circle: "))
                else:
                    response = float(input(f"What is the area of the {shape}? "))

            rounded_answer = round(answer, 2)
            if response == rounded_answer:
                print(correct_ans)
            else:
                print(f"Incorrect.\nAnswer is {rounded_answer}{units}")
            if response == str:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

# Main Routine Starts Here

# Initialise game variables
mode = "regular"
questions_answered = 0
end_game = "no"
feedback = ""

quiz_history = []

print("Welcome to my math quiz!")
print()

want_instructions = string_checker("Do you want to read the instructions? ")

# Check users enter yes (y) or no (n)
if want_instructions == "yes":
    instruction()

# Ask user for difficulty
difficulty = difficulty_check("Select a difficulty: ")

# Ask user for number of rounds
num_questions = int_check("How many rounds would you like? ")


# Game loop starts here
while questions_answered < num_questions:

    # Rounds headings
    if mode == "infinite":
        question_heading = f"\nQuestion {questions_answered + 1} (Infinite Mode)"
    else:
        question_heading = f"\nQuestion {questions_answered + 1} of {num_questions}"

    print(question_heading)
    print()

    # Defines the question type, shape, units, and numbers of sides
    circle_question = random.choice(["radius", "diameter"])
    units = random.choice(["cm", "m", "ft", "mm"])
    random_num_a = random.randint(3, 10)
    random_num_b = random.randint(3, 10)
    random_num_c = random.randint(3, 10)
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
            print(f"A triangle has a base of {random_num_a}{units} and a height of {random_num_b}.")
        if shape == "square":
            answer = random_num_a * random_num_a
            print(f"A square has a base of {random_num_a}{units}.")
        if shape == "rectangle":
            answer = random_num_a * random_num_b
            print(f"A rectangle has a base of {random_num_a}{units} and a height of {random_num_b}{units}.")
        if shape == "circle":
            answer = pi * (random_num_a * random_num_a)
            print(f"A circle has a radius of {random_num_a}{units}.")


    # Perimeters
    if question_type == "perimeter":
        if shape == "triangle":
            answer = random_num_a + random_num_b + random_num_c
            print(f"A triangle has sides of {random_num_a}{units}, {random_num_b}{units}, and {random_num_c}{units}.")
        if shape == "square":
            answer = random_num_a * 4
            print(f"A square has sides of {random_num_a}{units}.")
        if shape == "rectangle":
            answer = random_num_a * 2 + random_num_b * 2
            print(f"A rectangle has sides of {random_num_a}{units} and {random_num_b}{units}.")
        if shape == "circle":
            if circle_question == "radius":
                answer = 2 * pi * random_num_a
                print(f"A circle has a radius of {random_num_a}{units}.")
            if circle_question == "diameter":
                answer = pi * random_num_a
                print(f"A circle has a diameter of {random_num_a}{units}.")

    ans_check()

    print()
    print("End of Round.")

    questions_answered += 1



