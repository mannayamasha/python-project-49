import random


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_data():
    question = random.randint(1, 30)
    correct_answer = 'yes' if question % 2 == 0 else 'no'
    return question, correct_answer
