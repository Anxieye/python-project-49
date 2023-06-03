from math import gcd
from random import randint


TASK = 'Find the greatest common divisor of given numbers.'


def question_answer():
    random_number = randint(0, 100)
    random_number_2 = randint(0, 100)
    question = f'{random_number} {random_number_2}'
    answer = str(gcd(random_number, random_number_2))
    return [question, answer]
