#!/usr/bin/env python
from brain_games.cli import welcome_user


def main():
    print('Welcome to the Brain Games!')
    greet = welcome_user()
    print(greet)


if __name__ == '__main__':
    main()
