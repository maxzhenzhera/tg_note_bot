"""
Contains settings, constants and environment data.

.. const:: BASE_DIR
.. const:: CORE_DIR
.. const:: LOG_DIR

.. const:: LOGGING_CONFIG_PATH
.. const:: DEBUG_DB

.. const:: BOT_TOKEN

.. const:: DB_ENGINE
.. const:: DB_DRIVER
.. const:: DB_HOST
.. const:: DB_PORT
.. const:: DB_USER
.. const:: DB_PASSWORD
.. const:: DB_NAME

.. const:: REDIS_HOST
.. const:: REDIS_PORT

.. const:: ADMINS
.. const:: THROTTLING_RATE_LIMIT_IN_SECONDS

.. const:: EMPTY_VALUE
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
LOG_DIR = BASE_DIR / 'logs'
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# LOGGING - DEBUGGING ///////////////////////////////////////////////////////////////////////////////////////
LOGGING_CONFIG_PATH = CORE_DIR / 'utils' / 'logging_' / 'logging_config_with_files.yaml'

DEBUG_DB = True
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# API TOKENS ////////////////////////////////////////////////////////////////////////////////////////////////
BOT_TOKEN = os.getenv('TG_BOT_TOKEN')
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# DB SETTINGS ///////////////////////////////////////////////////////////////////////////////////////////////
DB_ENGINE = os.getenv('DB_ENGINE')
DB_DRIVER = os.getenv('DB_DRIVER')

DB_HOST = os.getenv('DB_HOST')
DB_PORT = int(os.getenv('DB_PORT'))

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

DB_NAME = os.getenv('DB_NAME')
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# REDIS SETTINGS ////////////////////////////////////////////////////////////////////////////////////////////
REDIS_HOST = os.getenv('REDIS_HOST')
REDIS_PORT = int(os.getenv('REDIS_PORT'))
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# BOT SETTINGS //////////////////////////////////////////////////////////////////////////////////////////////
ADMINS: list[int] = [int(admin_id) for admin_id in os.getenv('ADMINS').split(',')]
THROTTLING_RATE_LIMIT_IN_SECONDS: float = .2
THROTTLING_RATE_LIMIT_IN_SECONDS_FOR_BUG_COMMAND: float = 60 * 5
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# BOT VARS //////////////////////////////////////////////////////////////////////////////////////////////////
EMPTY_VALUE = '➡️ Pass'
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# USED EMOJIS ///////////////////////////////////////////////////////////////////////////////////////////////
NON_RUBRIC_CATEGORY = '🖤'   # also rubric shift

TO_SEE = '👀'
TO_CREATE = '💾'
TO_DELETE = '🗑'
TO_DO_SERIOUS_DELETE = '👊', '🔥'

RUBRIC_SHIFT = '🔘'
LINK_SHIFT = '👉'
INPUT_ARGUMENT = '📝'
ARGUMENT_ACCEPTED = '👌'
ARGUMENT_UNIQUE = '🔑'
ARGUMENT_REQUIRED = '❗️'    # !
ARGUMENT_OPTIONAL = '🆓'
ERROR_OCCURED = '🛑'
REQUEST_EXECUTED = '☑️ '    # grey ✅
ACTION_COMPLETED = '✅'
CHOOSE_CHOICE = '❔'
EMPTY_RESULT = '🕳'
TIME_POINT = '🧭'
NOTE_MESSAGE = '💿'
DANGEROUS = '☢️'
CANCELLED = '❌'

BOT_EMOJI = '🤖'
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# STICKERS /////////////////////////////////////////////////////////////////////////////////////////////////
STICKER_SMILE_WITH_GLASSES = 'CAACAgIAAxkBAAILAWB2tsnP5PjHlWOvqy0yMfzmCrpRAAL2AgACz9SRHPqp7mp8sY5lHwQ'
STICKER_CONDEMNING_FROG = 'CAACAgIAAxkBAAIPd2B4Yy5qYOPyjcNqjo1lrOwss8l-AAJrAAPBnGAMlrTfm5MoJjMfBA'
STICKER_KISSING_FROG = 'CAACAgIAAxkBAAIPf2B4bs3u-NPxpHDnreoZ0dUoUP-jAAJeAAPBnGAM2cOQTay6uFAfBA'
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
