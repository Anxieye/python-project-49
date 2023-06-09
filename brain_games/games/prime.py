from random import randint


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            return False
    return True


def get_question_answer():
    random_number = randint(0, 100)
    answer = None

    if is_prime(random_number):
        answer = 'yes'
    else:
        answer = 'no'

    question = random_number

    return [question, answer]
