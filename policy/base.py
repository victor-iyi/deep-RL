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
# Built-in libraries.
import copy
from abc import ABCMeta, abstractmethod

# Third-party libraires.
import numpy as np

# Custom libraries.
from env.game import Game


class BasePolicy(metaclass=ABCMeta):

    def __init__(self, env, **kwargs):
        if isinstance(env, Game):
            raise TypeError("Inappropriate argument type for `env`."
                            f"Expected env.game.Game got {type(env)}")

        # RL environment.
        self._env = env
        self._name = kwargs.get('name', self.__class__.__name__)

        # Action & observations (states).
        self._state = self._env.state
        self._actions = self._env._actions

        # Policy. Shape: (n_states, n_actions)
        self._policy = np.zeros(shape=(self._env.n_states,
                                       self._n_actions))

    def __repr__(self):
        return '{}(env={})'.format(self._name, self._env)

    def __call__(self, state, **kwargs):
        # TODO: Do some validation
        return self.get(state, **kwargs)

    def __getitem__(self, state):
        return self.get(state)

    @abstractmethod
    def get(self, state, **kwargs):
        return NotImplemented

    def copy(self):
        return copy.deepcopy(self)

    def evaluate(self, game: Game, episodes: int=100, **kwargs):
        # Total accumulated reward.
        total_rewards = 0.0

        for episode in range(episodes):
            total_rewards += game(self, **kwargs)

        # Average reward over episodes.
        return total_rewards / episodes

    # Create alias for `evaluate`.
    fitness = evaluate

    def sample(self):
        """Returns a random action from the environment's action space."""
        return self._env.sample()

    @property
    def env(self):
        return self._env

    @property
    def actions(self):
        return self._actions

    @property
    def state(self):
        return self._state

    # Create alias for `states`.
    observation = state
