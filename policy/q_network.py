"""
   @author
     Victor I. Afolabi
     Artificial Intelligence & Software Engineer.
     Email: javafolabi@gmail.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: q_network.py
     Created on 10 September, 2018 @ 12:57 AM.

   @license
     MIT License
     Copyright (c) 2018. Victor I. Afolabi. All rights reserved.
"""
import policy


class QNetwork(policy.BasePolicy):
    def __init__(self, **kwargs):
        super(QNetwork, self).__init__(**kwargs)

    def __repr__(self):
        return 'QNetwork()'

    def get(self, state, **kwargs):
        pass
