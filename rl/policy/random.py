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

# Custom library.
from rl.policy.base import BasePolicy


class RandomPolicy(BasePolicy):
    def __init__(self, env, **kwargs):
        super(RandomPolicy, self).__init__(env, **kwargs)

    def get(self, state, **kwargs):
        return self.env.sample()
