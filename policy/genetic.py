"""A Markov Model that generates policy based on Genetic Algorithms.

   @author
     Victor I. Afolabi
     Artificial Intelligence & Software Engineer.
     Email: javafolabi@gmail.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: genetic_algorithm.py
     Created on 08 September, 2018 @ 11:32 PM.

   @license
     MIT License
     Copyright (c) 2018. Victor I. Afolabi. All rights reserved.
"""
import numpy as np

from policy import BasePolicy


class GeneticAlgorithm(BasePolicy):

    def __init__(self, **kwargs):
        super(GeneticAlgorithm, self).__init__(**kwargs)

    def get(self, state, **kwargs):
        pass

    def crossover(self, policy: GeneticAlgorithm):
        pass

    def mutate(self):
        pass
