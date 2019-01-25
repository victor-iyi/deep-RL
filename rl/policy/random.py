"""A randomly chosen policy from the action space.

   @author
     Victor I. Afolabi
     Artificial Intelligence & Software Engineer.
     Email: javafolabi@gmail.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: random_policy.py
     Created on 19 August, 2018 @ 5:31 PM.

   @license
     MIT License
     Copyright (c) 2018. Victor I. Afolabi. All rights reserved.
"""

# Custom library.
from rl.config import Log
from rl.policy.base import BasePolicy
from rl.env import Game, names as env_names


class RandomPolicy(BasePolicy):
    def __init__(self, env, **kwargs):
        super(RandomPolicy, self).__init__(env, **kwargs)

    def get(self, state, **kwargs):
        return self.env.sample()


def test():
    # Game environment.
    env = Game(env_names.ClassicControl.CART_POLE)
    policy = RandomPolicy(env)

    Log.debug("env = {}".format(env))
    Log.debug("policy = {}".format(policy))

    # Observation & action space.
    Log.info('env.observation_space = {}'.format(env.observation_space))
    Log.info('env.action_space = {}'.format(env.action_space))


if __name__ == '__main__':
    test()
