"""Q-Learning using Bellman Equation to solve a Reinforcement Learning problem.

   @author
     Victor I. Afolabi
     Artificial Intelligence & Software Engineer.
     Email: javafolabi@gmail.com | victor.afolabi@zephyrtel.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: q_learning.py
     Created on 26 January, 2019 @ 02:28.

   @license
     MIT License
     Copyright (c) 2019. Victor I. Afolabi. All rights reserved.
"""
import numpy as np

# Custom libraries.
from config.utils import Log
from rl.policy.base import BasePolicy

__all__ = [
    'ValueIteration', 'PolicyIteration',
]


class ValueIteration(BasePolicy):
    def __init__(self, env, **kwargs):
        super(ValueIteration, self).__init__(env, **kwargs)
        self._gamma = kwargs.get('gamma', 0.99)

        # Value for each state.
        self._V = self.get_value(**kwargs)

        # Retrieve policy from the value of each state.
        self._policy = self.get_policy(self._V)

    def get(self, state, **kwargs):
        """Policy: Mapping from state to action.

        Args:
            state (int): Current state of the agent.

        Keyword Args:
            None

        Raises:
            AssertionError: Cannot perform Value Iteration in this environment.

        Returns:
            int: Action to be taken in the given state.
        """
        if not isinstance(state, int):
            raise AssertionError("Cannot perform Value Iteration in this environment.")

        return self._policy[state]

    def get_value(self, epochs: int = 1000, **kwargs):
        # Extract keyword arguments.
        eps = kwargs.get('eps', 1e-8)

        # Number of states & actions.
        n_states, n_actions = self._env.n_states, self._env.n_actions

        # Value of every state.
        V = np.zeros(shape=[n_states])

        for epoch in range(epochs):
            # Copy of value for each state.
            v = np.copy(V)
            # Go through every state.
            for s in range(n_states):
                # Value for each action.
                V_sa = np.zeros(shape=[n_actions])
                # Take all actions in this state.
                for a in range(n_actions):
                    for p, s_, r, _ in self.env.transition(s, a):
                        # Update the value of this state & action.
                        V_sa[a] += p * (r + self._gamma * v[s])
                V[s] = np.amax(V_sa)

            # Convergence
            if np.sum(np.fabs(v, V)) <= eps:
                break

        return V

    def get_policy(self, value: np.ndarray):
        """Compute policy from value function.

        Args:
            value (np.ndarray): Computed value for each state.

        Returns:
            np.ndarray: Array-like containing actions to be taken for every state.
        """
        # Total number of states & actions.
        n_states, n_actions = self._env.n_states, self._env.n_actions

        # Policy.
        policy = np.zeros(shape=[n_states])

        for s in range(n_states):
            # Value for possible actions to be taken in current state.
            V_sa = np.zeros(shape=[n_actions])

            for a in range(n_actions):
                for (p, s_, r, _) in self.env.transition(s, a):
                    # Update the value of this state while taking this action.
                    V_sa[a] += p * (r + self._gamma * value[s_])
            # Policy of the current state is the argmax over all possible actions.
            policy[s] = np.argmax(V_sa)

        return policy


class PolicyIteration(BasePolicy):
    def __init__(self, env, **kwargs):
        super(PolicyIteration, self).__init__(env, **kwargs)

    def get(self, state, **kwargs):
        Log.warn(state)
