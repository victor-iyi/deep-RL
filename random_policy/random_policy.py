"""Demo of an agent chosing policy at random.

   @author
     Victor I. Afolabi
     Artificial Intelligence & Software Engineer.
     Email: javafolabi@gmail.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: random_policy.py
     Created on 19 August, 2018 @ 5:31 PM.

   @license
     MIT License
     Copyright (c) 2018. Victor I. Afolabi. All rights reserved.
"""
import gym
import gym.spaces


class RandomPolicy(object):

  def __init__(self):
      pass

  def __repr__(self):
      return 'RandomPolicy()'
  
  def __str__(self):
      return self.__repr__()


def main():
    # noinspection PyUnresolvedReferences
    env = gym.make('FrozenLake-v0')
    env.render()


if __name__ == '__main__':
    main()
