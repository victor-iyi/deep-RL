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

from policy.base import BasePolicy
from policy.random import RandomPolicy
from policy.genetic import GeneticAlgorithm
from policy.actor_critic import A2C, A3C


__all__ = [
    # Base class.
    'BasePolicy',
    # Policies sub-classes.
    'RandomPolicy', 'GeneticAlgorithm', 'A2C', 'A3C',
]
