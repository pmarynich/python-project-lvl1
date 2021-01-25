#!/usr/bin/env python3
import random
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('What number is missing in the progression?')
    index = 0
    while index < 3:
        index += 1
        array = []
        number = random.randrange(5, 10)
        char = random.randrange(1, 10)
        random_position = random.randrange(1, number)
        step = random.randrange(1, 10)
        i = 0
        secret = ''
        while i < number:
            i += 1
            char += step
            array.append(str(char))
        secret = array[random_position]
        array[random_position] = '..'
        print('Question: ' + ' '.join(array))
        answer = prompt.string('Your answer: ')
        if str(secret) == str(answer):
            print('Correct!')
        elif str(secret) != str(answer):
            print("'" + str(
                answer) + "' is wrong answer ;(. Correct answer was '" + str(
                    secret) + "'.")
            print("Let's try again, " + name + '!')
            return None

    print('Congratulations, ' + name + '!')


if __name__ == '__main__':
    main()
