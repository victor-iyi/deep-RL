"""Q-Learning - Using a Bellman's Equation to solve a Reinforcement Learning problem.

   @author
     Victor I. Afolabi
     Artificial Intelligence & Software Engineer.
     Email: javafolabi@gmail.com | victor.afolabi@zephyrtel.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: q_learning.py
     Created on 26 January, 2019 @ 02:21.

   @license
     MIT License
     Copyright (c) 2019. Victor I. Afolabi. All rights reserved.
"""
# Custom libraries.
from config.utils import Log
from rl import Game, ValueIteration
from rl.env import names as env_names


def main(args):
    env = Game(env=args.env)
    Log.debug(env)
    Log.debug('Action space {}'.format(env.action_space))
    Log.debug('Observation space {}'.format(env.observation_space))

    # Value Iteration.
    value_iter_policy = ValueIteration(env=env)
    Log.debug(value_iter_policy)


if __name__ == '__main__':
    # Built-in libraries.
    import argparse

    parser = argparse.ArgumentParser(prog='Q-Learning',
                                     usage='python3 example/q_learning.py -n=500',
                                     description='Get the best score of n random policies',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n', '--episodes', type=int, default=500,
                        help='How many episodes to play.')
    parser.add_argument('-e', '--env', type=str, default=env_names.ToyText.FROZEN_LAKE,
                        help='Name of env. See `env.names.get_all()`')

    args = parser.parse_args()

    Log.info(f'{"=" * 30}')
    Log.info(f'{"Options":<15}\t{"Default":<15}')
    Log.info(f'{"=" * 30}')
    for k, v in vars(args).items():
        Log.info(f'{k:<15}\t{v:<15}')

    main(args=args)
