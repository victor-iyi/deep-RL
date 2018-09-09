"""
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


class Base(metaclass=ABCMeta):
    def __init__(self, env, **kwargs):
        self._env = env

    def __repr__(self):
        return 'policy.Base()'

    def __call__(self, state, **kwargs):
        pass

    def __getitem__(self, state):
        pass

    @abstractmethod
    def get(self, state):
        pass

    @property
    def env(self):
        return self._env
