import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine

# Locate the .env file in the root directory of the project
env_path = Path(__file__).resolve().parent.parent / ".env"

# Load environment variables from .env file
load_dotenv(env_path)

# Read the database URL
database_url = os.getenv("DATABASE_URL")

if not database_url:
    raise RuntimeError("Please set the DATABASE_URL environment variable in the .env file.")

# Set up the SQL engine
engine = create_engine(
    database_url,
    pool_pre_ping=True,
    connect_args={"connect_timeout": 5},
)