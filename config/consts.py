"""Project global constant definitions.

   @author
     Victor I. Afolabi
     Artificial Intelligence & Software Engineer.
     Email: javafolabi@gmail.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: fs.py
     Created on 21 January, 2018 @ 01:05 PM.

   @license
     MIT License
     Copyright (c) 2018. Victor I. Afolabi. All rights reserved.
"""

# Built-in libraries.
import os.path

# Custom libraries.
from config.config import Config

# Exported configurations.
__all__ = [
    'FS', 'LOGGER', 'SETUP',
]


################################################################################################
# +--------------------------------------------------------------------------------------------+
# | FS: File System.
# +--------------------------------------------------------------------------------------------+
################################################################################################
class FS:
    # Project name & absolute directory.
    PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))
    APP_NAME = os.path.basename(PROJECT_DIR)

################################################################################################
# +--------------------------------------------------------------------------------------------+
# | Setup configuration constants.
# +--------------------------------------------------------------------------------------------+
################################################################################################
class SETUP:
    # Global setup configuration.
    __global = Config.from_cfg(os.path.join(FS.PROJECT_DIR,
                                            "config/setup/global.cfg"))
    # Build mode/type.
    MODE = __global['config']['MODE']


################################################################################################
# +--------------------------------------------------------------------------------------------+
# | Logger: Logging configuration paths.
# +--------------------------------------------------------------------------------------------+
################################################################################################
class LOGGER:
    # Root Logger:
    ROOT = os.path.join(FS.PROJECT_DIR, 'config/logger', f'{SETUP.MODE}.cfg')

    # Another logger goes here: (and updated in helpers/utils.py)
