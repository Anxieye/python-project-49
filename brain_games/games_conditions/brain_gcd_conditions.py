from random import randint


TASK = 'Find the greatest common divisor of given numbers.'


def gcd(a, b):
    max_num = max(a, b)
    gcd = None

    for i in range(1, max_num + 1):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd


def question_answer():
    random_number = randint(0, 100)
    random_number_2 = randint(0, 100)
    question = f'{random_number} {random_number_2}'
    answer = str(gcd(random_number, random_number_2))
    return [question, answer]
