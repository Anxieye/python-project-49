from random import randint


task = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_simple(num):
    if num < 2:
        return False
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            return False
    return True


def question_answer():
    random_number = randint(0, 100)
    answer = None

    if is_simple(random_number):
        answer = 'yes'
    else:
        answer = 'no'

    question = str(random_number)

    return [question, answer]
