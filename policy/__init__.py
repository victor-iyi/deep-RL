"""
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
from policy.base import Base
from policy.random import RandomPolicy
from policy.genetic import GeneticAlgorithm

__all__ = [
    # Base class.
    'Base',
    # Policies sub-classes.
    'RandomPolicy', 'GeneticAlgorithm'
]
