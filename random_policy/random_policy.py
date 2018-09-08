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

    def __call__(self, env):
        action = env.action_space.sample()
        return action


def main():
    # Game environment.
    env = gym.make('BipedalWalker-v2')

    episodes, frames = 20, 100
    policy = RandomPolicy()

    for episode in range(episodes):
        state = env.reset()
        done, total_reward = False, 0

        for f in range(frames):
            env.render()

            # Take random actions.
            action = policy(env)
            state, reward, done, info = env.step(action)

            total_reward += reward

        print('Episode {}\tTotal reward: {}'.format(episode + 1, total_reward))


if __name__ == '__main__':
    main()
