"""Reinforcement Learning Environment. Built on top of OpenAI's Gym.

   @author
     Victor I. Afolabi
     Artificial Intelligence & Software Engineer.
     Email: javafolabi@gmail.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: __init__.py
     Created on 08 September, 2018 @ 11:42 PM.

   @license
     MIT License
     Copyright (c) 2018. Victor I. Afolabi. All rights reserved.
"""
from rl.env.game import Game
from rl.env.names import Atari, Box2D, ClassicControl, ToyText

__all__ = [
    # Game.
    'Game',

    # Environments.
    'Atari', 'Box2D', 'ClassicControl', 'ToyText',
]
