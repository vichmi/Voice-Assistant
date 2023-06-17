import mysql.connector as mc
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()

db = mc.connect(
    host = os.getenv('DB_HOST'),
    user = os.getenv('DB_USER'),
    password = os.getenv('DB_PASSWORD'),
    database = os.getenv('DB_NAME')
)
