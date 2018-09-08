"""
   @author
     Victor I. Afolabi
     Artificial Intelligence & Software Engineer.
     Email: javafolabi@gmail.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: env.py
     Created on 08 September, 2018 @ 11:42 PM.

   @license
     MIT License
     Copyright (c) 2018. Victor I. Afolabi. All rights reserved.
"""
from collections import namedtuple

# Environments.
_Atari = namedtuple('Atari', ['PONG', 'BREAKOUT', 'SPACE_INVADER'])
_Box2d = namedtuple('Box2d', ['BIPEDAL_WALKER', 'CART_POLE'])
_Text = namedtuple('Text', ['TAXI', 'FROZEN_LAKE_8x8'])

# Atari environments.
Atari = _Atari(SPACE_INVADER='',
               PONG='',
               BREAKOUT='')

# Box2D environments
Box2D = _Box2d(BIPEDAL_WALKER='BipedalWalker-v2',
               CART_POLE='Cart-Pole-v4')

# Text Environments.
Text = _Text(TAXI='Taxi-v4',
             FROZEN_LAKE_8x8='FrozenLake8x8-v0')
