"""Base class for various kinds of policy networks.

   @author
     Victor I. Afolabi
     Artificial Intelligence & Software Engineer.
     Email: javafolabi@gmail.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: base.py
     Created on 09 September, 2018 @ 9:06 PM.

   @license
     MIT License
     Copyright (c) 2018. Victor I. Afolabi. All rights reserved.
"""

from abc import ABCMeta, abstractmethod
from env.game import Game


class BasePolicy(metaclass=ABCMeta):
    def __init__(self, env, **kwargs):
        self._env = env

    def __repr__(self):
        return 'policy.Base()'

    def __call__(self, state, **kwargs):
        # TODO: Do some validation
        return self.get(state, **kwargs)

    def __getitem__(self, state):
        return self.get(state)

    @abstractmethod
    def get(self, state, **kwargs):
        return NotImplemented

    def evaluate(self, game: Game, episodes: int = 100, **kwargs):
        # Total accumulated reward.
        total_rewards = 0.0

        for episode in range(episodes):
            total_rewards += game.run(self, **kwargs)

        # Average reward over episodes.
        return total_rewards / episodes

    def random_action(self):
        """Returns a random action from the environment's action space."""
        return self._env.acion_space.sample()

    @property
    def env(self):
        return self._env
