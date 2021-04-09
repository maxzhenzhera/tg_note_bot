"""
Contains settings.

.. const:: BASE_DIR
.. const:: CORE_DIR

.. const:: LOGGING_CONFIG_PATH
.. const:: DEBUG_DB

.. const:: BOT_TOKEN

.. const:: DB_ENGINE
.. const:: DB_DRIVER
.. const:: DB_NAME
.. const:: DB_PATH
"""

import os
import pathlib

from dotenv import load_dotenv


# LOAD ENV  /////////////////////////////////////////////////////////////////////////////////////////////////
load_dotenv()
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# PATH SETTINGS /////////////////////////////////////////////////////////////////////////////////////////////
BASE_DIR = pathlib.Path(__file__).parent.parent
CORE_DIR = pathlib.Path(__file__).parent
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# LOGGING - DEBUGGING ///////////////////////////////////////////////////////////////////////////////////////
LOGGING_CONFIG_PATH = CORE_DIR / 'utils' / 'logging_' / 'logging_config.yaml'

DEBUG_DB = True
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


# API TOKENS ////////////////////////////////////////////////////////////////////////////////////////////////
BOT_TOKEN = os.getenv('TG_BOT_TOKEN')
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


# DB SETTINGS ///////////////////////////////////////////////////////////////////////////////////////////////
DB_ENGINE = os.getenv('DB_ENGINE')
DB_DRIVER = os.getenv('DB_DRIVER')
DB_NAME = os.getenv('DB_NAME')

DB_PATH = BASE_DIR / f'{DB_NAME}.db'
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
