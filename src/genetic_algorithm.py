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
# Built-in libraries.
import argparse

# Custom libraries.
from env import game, names as env_names


def main(args):
    # Instantiate the env environment.
    env = game.Game(args.env)

    print(env)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='Random Policy Search',
                                     usage='python3 src/random_policy.py -n=500',
                                     description='Get the best score of n random policies',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n', type=int, default=500,
                        help='How many random policies to generate.')
    parser.add_argument('--env', type=str, default=env_names.ClassicControl.CART_POLE,
                        help='Name of environment to use. See env.names')

    args = parser.parse_args()

    print(f'\n{"="*25}',
          f'\n{"Options":<15}\t{"Default":<15}',
          f'\n{"="*25}')
    for k, v in vars(args).items():
        print(f'{k:<15}\t{v:<15}')

    main(args=args)
