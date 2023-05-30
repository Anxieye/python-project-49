import prompt
from random import randint


def even_or_not():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!\nAnswer "yes" if the number is even, '
          f'otherwise answer "no".')

    count = 3

    while count != 0:
        random_number = randint(0, 100)
        print(f'Question: {random_number}')
        user_answer = input('Your answer: ')

        if random_number % 2 == 0 and user_answer == 'yes':
            print('Correct!')
            count -= 1
        elif random_number % 2 != 0 and user_answer == 'no':
            print('Correct!')
            count -= 1
        else:
            if random_number % 2 == 0:
                print(f"'{user_answer}' is wrong answer ;(. Correct "
                      f"answer was 'yes'.\nLet's try again, {user_name}")
            elif random_number % 2 != 0:
                print(f"'{user_answer}' is wrong answer ;(. Correct "
                      f"answer was 'no'.\nLet's try again, {user_name}")
            count = 3
    print(f'Congratulations, {user_name}!')
