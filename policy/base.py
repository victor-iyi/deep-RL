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
# from env.game import Game

import numpy as np
import copy

##############################################################################
# +——————————————————————————————————————————————————————————————————————————+
# | Policy - policy[get], policy.actions(), policy.states(), policy.sample()
# +——————————————————————————————————————————————————————————————————————————+
##############################################################################


class BasePolicy():

    __metaclass__ = ABCMeta

    def __init__(self, env, **kwargs):
        # RL environment.
        self._env = env

        # Action & observations (states).
        self._state = self._env.state
        self._actions = self._env._actions

        # Policy. Shape: (n_states, n_actions)
        self._policy = np.zeros(shape=(len(self._state.shape),
                                       len(self._actions.shape)))

    def __repr__(self):
        return 'BasePolicy(env={})'.format(self._env)

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

    def evaluate(self, game, episodes=100, **kwargs):
        # Total accumulated reward.
        total_rewards = 0.0

        for episode in range(episodes):
            total_rewards += game.run(self, **kwargs)

        # Average reward over episodes.
        return total_rewards / episodes

    # Create alias for `evaluate`.
    fitness = evaluate

    def sample(self):
        """Returns a random action from the environment's action space."""
        return self._env.acion_space.sample()

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
