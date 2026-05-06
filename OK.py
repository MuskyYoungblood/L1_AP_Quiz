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
