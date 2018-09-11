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
import gym
from typing import Callable


class Game(object):
    def __init__(self, env: str):
        self._env = gym.make(env)

    def __repr__(self):
        return 'Game(env={})'.format(self._env.env)

    def __call__(self, policy, **kwargs):
        return self.run(policy, *kwargs)

    def run(self, policy: Callable, episodes: int = 100, **kwargs):
        # Default keyword arguments.
        render = kwargs.get('render', False)

        # Observation & total reward.
        obs, total_rewards = self._env.reset(), 0

        for episode in range(episodes):
            # Render env env.
            if render:
                self._env.render()

            # Get an action.
            action = policy(obs, **kwargs)
            obs, reward, done, info = self._env.step(action)
            total_rewards += reward

            if done:
                break

        return total_rewards

    @property
    def env(self):
        return self._env

    @property
    def action_space(self):
        return self._env.action_space

    @property
    def observation_space(self):
        return self._env.observation_space
