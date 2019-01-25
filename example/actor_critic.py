"""Using the (Asynchronous) Advantage Actor-Critic model to solve a Reinforcement Learning problem.

   @author
     Victor I. Afolabi
     Artificial Intelligence & Software Engineer.
     Email: javafolabi@gmail.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: actor_critic.py
     Created on 10 September, 2018 @ 1:44 AM.

   @license
     MIT License
     Copyright (c) 2018. Victor I. Afolabi. All rights reserved.
"""

# Custom libraries.
from config import Log
from rl import Game, A2C
from rl.env import names as env_names


def main(args):
    # Instantiate the env environment.
    env = Game(args.env)

    Log.debug(env)
    Log.debug('Action space: {}'.format(env.action_space))
    Log.debug('State  space: {}'.format(env.observation_space))


if __name__ == '__main__':
    # Built-in libraries.
    import argparse

    parser = argparse.ArgumentParser(prog='Random Policy Search',
                                     usage='python3 random_policy.py -n=500',
                                     description='Get the best score of n random policies',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n', type=int, default=500,
                        help='How many random policies to generate.')
    parser.add_argument('--env', type=str, default=env_names.Atari.MS_PACMAN,
                        help='Name of env. See `env.names`')

    args = parser.parse_args()

    Log.info(f'{"="*30}')
    Log.info(f'{"Options":<15}\t{"Default":<15}')
    Log.info(f'{"="*30}')
    for k, v in vars(args).items():
        Log.info(f'{k:<15}\t{v:<15}')

    main(args=args)
