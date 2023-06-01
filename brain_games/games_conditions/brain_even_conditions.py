from random import randint


task = 'Answer "yes" if the number is even, otherwise answer "no".'


def question_answer():
    question = randint(0, 100)
    answer = ''

    if question % 2 == 0:
        answer += 'yes'
    elif question % 2 != 0:
        answer += 'no'
    return [question, answer]
