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
from policy import BasePolicy


class GeneticAlgorithm(BasePolicy):
    def __init__(self, **kwargs):
        super(GeneticAlgorithm, self).__init__(**kwargs)

    def __repr__(self):
        return 'GeneticAlgorithm()'

    def get(self, state, **kwargs):
        pass

    def fitness(self):
        pass

    def mutate(self):
        pass


if __name__ == '__main__':
    ga = GeneticAlgorithm()
    print(ga)
