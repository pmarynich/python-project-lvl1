#!/usr/bin/env python3
import random
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('What is the result of the expression?')
    index = 0
    while index < 3:
        first_number = random.randrange(1, 20)
        second_number = random.randrange(1, 20)
        ops = ['+', '-', '*']
        operation = random.choice(ops)
        result = eval(str(first_number) + operation + str(second_number))
        question = str(first_number) + operation + str(second_number)
        print('Question: ' + str(question))
        answer = prompt.string('Your answer: ')
        if str(result) == str(answer):
            print('Correct!')
        elif result != answer:
            print("'" + str(answer) + "' is wrong answer ;(. Correct answer was '" + str(result) + "'.")
            print("Let's try again, " + name + '!')
            return None
        index += 1
    print('Congratulation, ' + name + '!')


if __name__ == '__main__':
    main()
