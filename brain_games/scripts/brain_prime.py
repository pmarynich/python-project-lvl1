#!/usr/bin/env python3
import sympy
import prompt
import random


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    index = 0
    while index < 3:
        index += 1
        question = random.randrange(1, 100)
        print('Question: ' + str(question))
        answer = prompt.string('Your answer: ')
        result_bool = sympy.isprime(question)
        if result_bool is False:
            result = 'no'
        else:
            result = 'yes'
        if str(result) == str(answer):
            print('Correct!')
        elif result != answer:
            print("'" + str(answer) + "' is wrong answer ;(. Correct answer was '" + str(result) + "'.")
            print("Let's try again, " + name + '!')
            return None
    print('Congratulation, ' + name + '!')


if __name__ == '__main__':
    main()
