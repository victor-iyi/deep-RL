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


class Game(object):
    def __init__(self, env):
        self._env = gym.make(env)

    def __repr__(self):
        return 'Game(env={})'.format(self._env.class_name())

    def __call__(self, *args, **kwargs):
        pass

    def run(self, policy, episode=100, render=False, **kwargs):
        pass

    @property
    def env(self):
        return self._env

    @property
    def action_space(self):
        return self._env.action_space

    @property
    def observation_space(self):
        return self._env.observation_space
