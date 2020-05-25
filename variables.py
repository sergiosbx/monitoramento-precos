import os
import re

_confs = re.split(r"\://|:|\@|/", os.environ['DATABASE_URL'])

DATABASE_BASE_URL = _confs[3]
DATABASE_PORT = _confs[4]
DATABASE_NAME = _confs[5]
DATABASE_USERNAME = _confs[1]
DATABASE_PASSWORD = _confs[2]
DATABASE_CONNECT_TIMEOUT = os.environ.get('DATABASE_CONNECT_TIMEOUT', '30')
DATABASE_MAX_CONNECTIONS = os.environ.get('DATABASE_MAX_CONNECTIONS', '10')
QUERYS_DIR = "querys"
