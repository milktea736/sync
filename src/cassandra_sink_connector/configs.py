from pathlib import Path

from dotenv import load_dotenv

import cassandra_sink_connector

PROJECT_BASE = Path(cassandra_sink_connector.__file__).parent
DOTENV_FILE_PATH = PROJECT_BASE / '.env.prod'

load_dotenv(DOTENV_FILE_PATH)
