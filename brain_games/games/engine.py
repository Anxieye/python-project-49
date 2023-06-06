import prompt


def run_game(game):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!\n{game.TASK}')

    COUNT = 3

    while COUNT != 0:
        question, answer = game.get_question_answer()
        print(f'Question: {question}')
        user_answer = input('Your answer: ')

        if answer == user_answer:
            print('Correct!')
            COUNT -= 1
        else:
            return print(f"'{user_answer}' is wrong answer ;(. Correct an"
                         f"swer was '{answer}'.\nLet's try again, {user_name}!")
    print(f'Congratulations, {user_name}!')
