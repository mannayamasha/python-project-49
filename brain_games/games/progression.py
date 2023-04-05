import random


TASK = 'What number is missing in the progression?'


def game_data():
    start = random.randint(1, 40)
    step = random.randint(1, 20)
    progression_length = random.randint(5, 10)
    stop = start + step * progression_length
    progression = []
    for i in range(start, stop, step):
        progression.append(i)
    random_i = random.randint(0, progression_length - 1)
    correct_answer = str(progression[random_i])
    # заменяем элемент по случайно выбранному индексу
    progression[random_i] = '..'
    question = ", ".join(map(str, progression))
    return question, correct_answer
