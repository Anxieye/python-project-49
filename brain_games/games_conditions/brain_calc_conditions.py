from random import randint, choice


TASK = 'What is the result of the expression?'


def find_operator(a, b, operator):
    value = None

    if operator == '+':
        value = a + b
    elif operator == '-':
        value = a - b
    else:
        value = a * b
    return value


def question_answer():
    random_operator = choice(('+', '-', '*'))
    random_number = randint(0, 100)
    random_number_2 = randint(0, 100)
    question = f'{random_number} {random_operator} {random_number_2}'
    answer = str(find_operator(random_number, random_number_2, random_operator))
    return [question, answer]
