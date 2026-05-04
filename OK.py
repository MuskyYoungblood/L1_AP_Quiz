import random
import math
pi = math.pi
def response_check(question, options):
  error = f"Please choose from the following: {options}"
  while True:
      response = input(question).lower()
      for opt in options:
          if response == opt or response == opt[0]:
              return opt
      print(error)
def int_check(question, low=0):
  while True:
      try:
          response = int(input(question))
          if response > low:
              return response
          print(f"Please enter a number greater than {low}")
      except ValueError:
          print("Please enter a valid integer.")
# UPDATED: now returns result info
def question_check(question, answer, units):
  while True:
      try:
          user = float(input(question))
          answer = round(answer, 2)
          if user == answer:
              print("Correct answer!")
              return user, answer, True
          else:
              print(f"Incorrect. Answer is {answer}{units}")
              return user, answer, False
      except ValueError:
          print("Please enter a number.")
def instruction():
   print('''
**** Instructions ****
Answer area and perimeter math questions.
   ''')
# Main Routine
questions_answered = 0
quiz_history = []
print("Welcome to my math quiz!")
if response_check("\nDo you want to see the instructions? ", ["yes", "no"]) == "yes":
   instruction()
difficulty = response_check("Select a difficulty: ", ["easy", "medium", "hard"])
num_questions = int_check("How many questions would you like? ")
# Game loop starts here
for i in range(num_questions):
   print(f"\nQuestion {i+1} of {num_questions}\n")
   units = random.choice(["cm", "m", "ft", "mm"])
   random_num_a, random_num_b, random_num_c = random.randint(10, 30), random.randint(10, 30), random.randint(10, 30)
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
           question = f"A triangle has a base of {random_num_a}{units} and a height of {random_num_b}{units}. What is its area? "
       if shape == "square":
           answer = random_num_a * random_num_a
           question = f"A square has a base of {random_num_a}{units}. What is its area? "
       if shape == "rectangle":
           answer = random_num_a * random_num_b
           question = f"A rectangle has a base of {random_num_a}{units} and a height of {random_num_b}{units}. What is its area? "
       if shape == "circle":
           answer = pi * (random_num_a * random_num_a)
           question = f"A circle has a radius of {random_num_a}{units}. What is its area? "
   # Perimeter
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
   # Get result
   user, correct_ans, correct = question_check(question, answer, units)
   # Store history
   quiz_history.append({
       "question": question,
       "user": user,
       "answer": correct_ans,
       "correct": correct
   })
# Ask to show history
if response_check("\nDo you want to see your quiz history? ", ["yes", "no"]) == "yes":
   print("\n**** Quiz History ****")
   for i, item in enumerate(quiz_history):
       result = "✅ Correct" if item["correct"] else "❌ Incorrect"
       print(f"\nRound {i+1}")
       print(item["question"])
       print(f"Your answer: {item['user']}")
       print(f"Correct answer: {item['answer']}")
       print(result)