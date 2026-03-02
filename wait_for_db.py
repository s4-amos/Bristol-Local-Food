import os
import time
import psycopg

host = os.getenv("POSTGRES_HOST", "db")
port = int(os.getenv("POSTGRES_PORT", "5432"))
db = os.getenv("POSTGRES_DB", "bristol")
user = os.getenv("POSTGRES_USER", "bristol")
password = os.getenv("POSTGRES_PASSWORD", "bristolpass")

deadline = time.time() + 60  # wait up to 60 seconds

while True:
    try:
        psycopg.connect(host=host, port=port, dbname=db, user=user, password=password).close()
        print("Database is ready!")
        break
    except Exception as e:
        if time.time() > deadline:
            print("Database not ready in time:", e)
            raise
        print("Waiting for database...")
        time.sleep(2)