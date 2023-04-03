import random
import math


TASK = 'Find the greatest common divisor of given numbers.'


def game_data():
    random_digit_1 = random.randint(1, 30)
    random_digit_2 = random.randint(1, 30)
    question = f'{random_digit_1} {random_digit_2}'
    correct_answer = str(math.gcd(random_digit_1, random_digit_2))
    return question, correct_answer
