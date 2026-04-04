from os import getenv
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    'dbname':getenv("DB_NAME"),
    'user':getenv("DB_USER"),
    'password':getenv("DB_PASS"),
    'host':getenv("DB_HOST"),
    'port':getenv("DB_PORT"),
}
