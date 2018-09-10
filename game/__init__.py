"""
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
from .env import Atari, Box2D, ClassicControl, ToyText
from .game import Game

__all__ = [
    # Environments.
    'Atari', 'Box2D', 'ClassicControl', 'Text',

    # Game.
    'Game',
]
