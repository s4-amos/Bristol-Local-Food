"""Wait for the PostgreSQL database to be ready before starting Django."""
import os
import time
import psycopg

MAX_RETRIES = 30
RETRY_DELAY = 2  # seconds


def wait_for_db():
    host = os.getenv("POSTGRES_HOST", "db")
    port = os.getenv("POSTGRES_PORT", "5432")
    dbname = os.getenv("POSTGRES_DB", "bristol")
    user = os.getenv("POSTGRES_USER", "bristol")
    password = os.getenv("POSTGRES_PASSWORD", "bristolpass")

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            conn = psycopg.connect(
                host=host, port=port, dbname=dbname, user=user, password=password
            )
            conn.close()
            print("Database is ready.")
            return
        except psycopg.OperationalError:
            print(f"Attempt {attempt}/{MAX_RETRIES}: Database not ready, retrying in {RETRY_DELAY}s...")
            time.sleep(RETRY_DELAY)

    raise SystemExit("Database not available after maximum retries.")


if __name__ == "__main__":
    wait_for_db()
