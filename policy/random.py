"""A randomly chosen policy from the action space.

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
import numpy as np

import policy


class RandomPolicy(policy.Base):
    def __init__(self, env, **kwargs):
        super(RandomPolicy, self).__init__(env, **kwargs)

    def __repr__(self):
        return 'RandomPolicy()'

    def getPolicy(self, observation):
        action_space = self.env.action_space
        action = np.random.uniform(low=action_space.low,
                                   high=action_space.high,
                                   size=action_space.shape)
        return action


def main():
    # Game environment.
    env = gym.make('BipedalWalker-v2')

    # Observation & action space.
    obs_space = env.observation_space
    action_space = env.action_space
    print('env.observation_space = {}'.format(obs_space.shape))
    print('env.action_space = {}'.format(action_space.shape))

    # Q-matrix.
    Q = np.zeros((obs_space.shape[0], action_space.shape[0]))
    print('Q.shape = {}'.format(Q.shape))

    # episodes, frames = 20, 100
    # policy = RandomPolicy()

    # for episode in range(episodes):
    #     state = env.reset()
    #     done, total_reward = False, 0

    #     for f in range(frames):
    #         env.render()

    #         # Take random actions.
    #         action = policy(env)
    #         state, reward, done, info = env.step(action)

    #         total_reward += reward

    #          print('Episode {}\tTotal reward: {}'.format(episode + 1, total_reward))


if __name__ == '__main__':
    main()
