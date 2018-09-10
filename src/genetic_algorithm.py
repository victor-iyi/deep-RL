"""Using evolutionary algorithm to solve a Reinforcement Learning problem.

   @author
     Victor I. Afolabi
     Artificial Intelligence & Software Engineer.
     Email: javafolabi@gmail.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: genetic_algorithm.py
     Created on 10 September, 2018 @ 2:50 AM.

   @license
     MIT License
     Copyright (c) 2018. Victor I. Afolabi. All rights reserved.
"""
import numpy as np
import argparse

import game
import policy


def main(args):
    # Instantiate the game environment.
    env = game.Game(args.game)

    print(env)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='Random Policy Search',
                                     usage='python3 src/random_policy.py -n=500',
                                     description='Get the best score of n random policies',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n', type=int, default=500,
                        help='How many random policies to generate.')
    parser.add_argument('--game', type=str, default=game.ClassicControl.CART_POLE,
                        help='Name of game. See gym.env.registry.all()')

    args = parser.parse_args()

    print(f'\n{"="*25}',
          f'\n{"Options":<15}\t{"Default":<15}',
          f'\n{"="*25}')
    for k, v in vars(args).items():
        print(f'{k:<15}\t{v:<15}')

    main(args=args)
