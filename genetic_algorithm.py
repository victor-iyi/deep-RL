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

# Third-party libraries.
import numpy as np

# Custom libraries.
from config import Log
from policy import RandomPolicy
from env import Game, names as env_names


def main(args):
    # Instantiate the env environment.
    env = Game(args.env)
    Log.debug(env)
    Log.debug('Action space: {}'.format(env.action_space))
    Log.debug('State  space: {}'.format(env.observation_space))

    if args.benchmark:
        Log.warn('Benchmarking with Random policy search...')

        # Get random policies & run it through the environment.
        rand_policies = [RandomPolicy(env) for _ in range(args.n)]
        rand_rewards = [env.run(rand_policy) for rand_policy in rand_policies]

        # Get average rewards & best rewards.
        rand_avg, rand_best = np.average(rand_rewards), np.amax(rand_rewards)
        Log.debug(('Random Policy => Average: {}'
                   '\tBest: {}').format(rand_avg, rand_best))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='Genetic Algorithm Policy',
        # usage='python3 genetic_algorithm.py -n=500',
        description='Uses genetic algorithm to solve RL.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    # Command line arguments.
    parser.add_argument('-n', type=int, default=500,
                        help='Number of population in a generation.')
    parser.add_argument(
        '-e', '--env', type=str, default=env_names.ClassicControl.CART_POLE,
        help='Name of environment to use. See `env.all_names()`'
    )
    parser.add_argument(
        '-b', '--benchmark', type=bool, default=True,
        help=('Benchmark Genetic Algorithms performance with Random '
              'Policy search.')
    )

    # Parse arguments.
    args = parser.parse_args()

    # Pretty-print argument list.
    Log.info(f'{"="*30}')
    Log.info(f'{"Options":<15}\t{"Default":<15}')
    Log.info(f'{"="*30}')
    for k, v in vars(args).items():
        Log.info(f'{k:<15}\t{v:<15}')

    # Run main.
    main(args=args)
