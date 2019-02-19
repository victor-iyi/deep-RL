"""Policy: Mapping from state to action.

   @author
     Victor I. Afolabi
     Artificial Intelligence & Software Engineer.
     Email: javafolabi@gmail.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: __init__.py
     Created on 09 September, 2018 @ 8:30 PM.

   @license
     MIT License
     Copyright (c) 2018. Victor I. Afolabi. All rights reserved.
"""

from rl.policy.base import BasePolicy
from rl.policy.q_network import QNetwork
from rl.policy.random import RandomPolicy
from rl.policy.actor_critic import A2C, A3C
from rl.policy.genetic import GeneticAlgorithm
from rl.policy.q_learning import ValueIteration, PolicyIteration, QLearning

__all__ = [
    # Base class.
    'BasePolicy',
    # Policies sub-classes.
    'RandomPolicy', 'GeneticAlgorithm', 'A2C', 'A3C',
    'ValueIteration', 'PolicyIteration', 'QLearning',
    'QNetwork',
]
