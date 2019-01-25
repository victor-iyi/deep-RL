"""
   @author
     Victor I. Afolabi
     Artificial Intelligence & Software Engineer.
     Email: javafolabi@gmail.com | victor.afolabi@zephyrtel.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: __init__.py.py
     Created on 25 January, 2019 @ 21:50.

   @license
     MIT License
     Copyright (c) 2019. Victor I. Afolabi. All rights reserved.
"""
# Environment.
from rl.env.game import Game
from rl.env.names import Atari, ClassicControl, Box2D, ToyText

# Policy (Agents).
from rl.policy import RandomPolicy, QNetwork, GeneticAlgorithm, A2C, A3C


__all__ = [
    'Game', 'Atari', 'ClassicControl', 'Box2D', 'ToyText',
    'A2C', 'A3C', 'QNetwork', 'GeneticAlgorithm', 'RandomPolicy',
]
