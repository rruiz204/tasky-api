from dotenv import load_dotenv
import os

load_dotenv()

# Database
DATABASE_URL = os.getenv("DATABASE_URL")

# Json Web Token
SECRET_KEY = os.getenv("SECRET_KEY")

# Prometheus Monitoring (Enable/Disable)
PROMETHEUS = os.getenv("PROMETHEUS")