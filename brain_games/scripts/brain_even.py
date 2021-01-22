#!/usr/bin/env python3
import random
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    index = 0
    while index < 3:
        question = random.randrange(1, 100)
        print('Question: ' + str(question))
        answer = prompt.string('Your answer: ')
        if (question % 2 == 0 and answer == 'yes') or (question % 2 == 1 and answer == 'no'):
            print('Correct!')
        else:
            right = ''
            if answer == 'yes':
                right = 'no'
            elif answer == 'no':
                right = 'yes'
            else:
                if question % 2 == 0:
                    right = 'yes'
                else:
                    right = 'no'
            print("'" + answer + "'" + " is wrong answer ;(.")
            print("Correct answer was '" + right + "'.")
            print("Let's try again, " + name + '!')
            return None
        index += 1
    print('Congratulation, ' + name + '!')


if __name__ == '__main__':
    main()
