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


class GeneticAlgorithm(object):
    def __init__(self, population):
        self._population = population

    def __repr__(self):
        return 'GeneticAlgorithm()'

    def __call__(self, *args, **kwargs):
        pass

    def fitness(self):
        pass

    def mutate(self):
        pass


if __name__ == '__main__':
    ga = GeneticAlgorithm()
    print(ga)
