import random


TASK = 'What is the result of the expression?'


def game_data():
    random_digit_1 = random.randint(1, 30)
    random_digit_2 = random.randint(1, 30)
    math_operations = ['+', '-', '*']
    math_op = random.choice(math_operations)
    question = f'{random_digit_1} {math_op} {random_digit_2}'
    if math_op == '+':
        correct_answer = str(random_digit_1 + random_digit_2)
    if math_op == '-':
        correct_answer = str(random_digit_1 - random_digit_2)
    if math_op == '*':
        correct_answer = str(random_digit_1 * random_digit_2)
    return question, correct_answer
