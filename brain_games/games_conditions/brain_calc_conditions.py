from random import randint, choice


TASK = 'What is the result of the expression?'


def question_answer():
    random_operator = choice(('+', '-', '*'))
    random_number = randint(0, 100)
    random_number_2 = randint(0, 100)
    question = f'{random_number} {random_operator} {random_number_2}'
    answer = str(eval(question))
    return [question, answer]
