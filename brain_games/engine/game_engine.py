import prompt


def game(mod):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!\n{mod.task}')

    count = 3

    while count != 0:
        question, answer = mod.question_answer()
        print(f'Question: {question}')
        user_answer = input('Your answer: ')

        if answer == user_answer:
            print('Correct!')
            count -= 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct "
                  f"answer was '{answer}'.\nLet's try again, {user_name}!")
            count = 3
    print(f'Congratulations, {user_name}!')
