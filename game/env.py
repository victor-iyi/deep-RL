"""Collections of common OpenAI environments used in this project.

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


##############################################################################
# +——————————————————————————————————————————————————————————————————————————+
# | Atari Environments.
# +——————————————————————————————————————————————————————————————————————————+
##############################################################################
class Atari:
    PONG = 'Pong-v0'
    PHOENIX = 'Phoenix-v0'
    BOWLING = 'Bowling-v0'
    ASSAULT = 'Assault-v0'
    BREAKOUT = 'Breakout-v0'
    MS_PACMAN = 'MsPacman-v0'
    SPACE_INVADER = 'SpaceInvaders-v0'


##############################################################################
# +——————————————————————————————————————————————————————————————————————————+
# | Box2D Environments.
# +——————————————————————————————————————————————————————————————————————————+
##############################################################################
class Box2D:
    BIPEDAL_WALKER = 'BipedalWalker-v2'
    CAR_RACING = 'CarRacing-v0'
    LUNAR_LAUNDER = 'LunarLaunder-v2'


##############################################################################
# +——————————————————————————————————————————————————————————————————————————+
# | Classic controls Environments.
# +——————————————————————————————————————————————————————————————————————————+
##############################################################################
class ClassicControl:
    ACROBOT = 'Acrobot-v1'
    CART_POLE = 'CartPole-v1'
    MOUNTAIN_CAR = 'MountainCar-v0'
    PENDULUM = 'Pendulum-v0'


##############################################################################
# +——————————————————————————————————————————————————————————————————————————+
# | Toy Text Environments.
# +——————————————————————————————————————————————————————————————————————————+
##############################################################################
class ToyText:
    TAXI = 'Taxi-v2'
    FROZEN_LAKE = 'FrozenLake-v0'
    FROZEN_LAKE_8x8 = 'FrozenLake8x8-v0'
