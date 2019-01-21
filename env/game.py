"""Game environment. Interaction with Markov Decision Process (MDP).

   @author
     Victor I. Afolabi
     Artificial Intelligence & Software Engineer.
     Email: javafolabi@gmail.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: game.py
     Created on 09 September, 2018 @ 12:25 AM.

   @license
     MIT License
     Copyright (c) 2018. Victor I. Afolabi. All rights reserved.
"""
from typing import Callable, Optional, Any

import gym
import numpy as np


class Game(object):

    def __init__(self, env: str, **kwargs):
        # Initialize the GYM environment.
        self._env = gym.make(env)

        # Extract keyword arguments.
        seed = kwargs.get('seed', None)
        self._env.seed(seed=seed)

        # Get the action & observation spaces.
        self._actions = self._get_space(self._env.action_space)
        self._observations = self._get_space(self._env.observation_space)
        self._state = self._env.reset()

    def __repr__(self):
        return 'Game(env={})'.format(self._env.env)

    def __call__(self, policy, **kwargs):
        return self.run(policy, *kwargs)

    def render(self, supress=False):
        if not supress:
            self._env.render()

    def run(self, policy: Callable, episodes: int = 100, **kwargs):
        # Default keyword arguments.
        render = kwargs.get('render', False)

        # Observation & total reward.
        obs, total_rewards = self._env.reset(), 0

        for episode in range(episodes):
            # Render env.
            if render:
                self._env.render()

            # Get an action.
            action = policy(obs, **kwargs)
            self._state, reward, done, info = self._env.step(action)
            total_rewards += reward

            if done:
                break

        return total_rewards

    @staticmethod
    def _get_space(space):
        # Discrete => n, shape
        if isinstance(space, gym.spaces.Discrete):
            return np.arange(space.n)

        # Box: low, high, shape
        elif isinstance(space, gym.spaces.Box):
            return space.low

        return np.zeros(shape=space.shape)

    @property
    def env(self):
        return self._env

    @property
    def action_space(self):
        # return self._env.action_space
        return self._actions.shape

    @property
    def observation_space(self):
        # return self._env.observation_space
        return self._observations.shape

    @property
    def state(self):
        return self._state

    @property
    def actions(self):
        return self._actions

    @property
    def observations(self):
        return self._observations

    @property
    def n_actions(self):
        return len(self._actions)

    @property
    def n_states(self):
        return len(self._observations)