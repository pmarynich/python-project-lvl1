#!/usr/bin/env python3
import random
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Find the greatest common divisor of given numbers.')
    index = 0
    gcd = 0
    while index < 3:
        first_number = random.randrange(1, 100)
        second_number = random.randrange(1, 100)
        question = str(first_number) + ' ' + str(second_number)
        while first_number != 0 and second_number != 0:
            if first_number > second_number:
                first_number = first_number % second_number
            else:
                second_number = second_number % first_number
        gcd = first_number + second_number
        print('Question: ' + str(question))
        answer = prompt.string('Your answer: ')
        if str(gcd) == str(answer):
            print('Correct!')
        elif gcd != answer:
            print("'" + str(
                answer) + "' is wrong answer ;(. Correct answer was '" + str(
                    gcd) + "'.")
            print("Let's try again, " + name + '!')
            return None
        index += 1
    print('Congratulations, ' + name + '!')


if __name__ == '__main__':
    main()
