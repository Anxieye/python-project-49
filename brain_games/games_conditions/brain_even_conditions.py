from random import randint


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def question_answer():
    random_number = randint(0, 100)
    question = random_number
    answer = ''

    if question % 2 == 0:
        answer += 'yes'
    elif question % 2 != 0:
        answer += 'no'
    return [question, answer]
