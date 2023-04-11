import random


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_data():
    digit = random.randint(1, 100)
    question = digit
    correct_answer = str(is_prime(digit))
    return question, correct_answer


def is_prime(digit):
    # отрицательные числа, 0 и 1 не являются простыми
    if digit > 1:
        for i in range(2, int(digit/2)+1):
            if digit % i == 0:
                return 'no'
        return 'yes'
    else:
        return 'no'
