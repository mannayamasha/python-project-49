import prompt

import random


def parity_check():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        random_digit = random.randint(1, 100)
        print(f'Question: {random_digit}')
        answer = prompt.string('Your answer: ')
        correct_answer = 'yes' if random_digit % 2 == 0 else 'no'
        if answer.lower() == correct_answer:
            print('Correct!')
            i += 1
            if i == 3:
                print(f'Congratulations, {name}!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {name}!")
            break
