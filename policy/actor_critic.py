"""(Asynchronous) Advantage Actor-Critic Methods. - A3C/A2C.

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
# Third-party libraries.
import numpy as np

# Custom libraries.
from policy import BasePolicy


class A2C(BasePolicy):
    def __init__(self, **kwargs):
        super(BasePolicy, self).__init__(**kwargs)

    def get(self, state: np.ndarray, **kwargs):
        pass


class A3C(BasePolicy):
    def __init__(self, *args, **kwargs):
        super(BasePolicy, self).__init__(**kwargs)

    def get(self, state: np.ndarray, **kwargs):
        pass
