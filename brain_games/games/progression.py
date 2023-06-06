from random import randint


TASK = 'What number is missing in the progression?'


def get_question_answer():
    random_start = randint(0, 50)
    random_length = randint(7, 15)
    random_step = randint(2, 10)
    sequence = []
    while random_length:
        sequence.append(random_start)
        random_start += random_step
        random_length -= 1
    random_index = randint(0, len(sequence) - 1)
    answer = str(sequence. pop(random_index))
    sequence.insert(random_index, '..')
    question = ' '.join(map(str, sequence))
    return [question, answer]
