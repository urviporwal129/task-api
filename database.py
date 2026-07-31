import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

def get_connection():
    return psycopg.connect(DATABASE_URL)

def get_all_tasks():
    conn = get_connection()

    with conn.cursor() as cur:
        cur.execute("SELECT * FROM tasks;")
        rows = cur.fetchall()

    conn.close()

    tasks = []

    for row in rows:
        tasks.append({
            "id": row[0],
            "title": row[1],
            "done": row[2]
        })

    return tasks

def get_task_by_id(task_id):
    conn = get_connection()

    with conn.cursor() as cur:
        cur.execute(
            "SELECT * FROM tasks WHERE id = %s;",
            (task_id,)
        )

        row = cur.fetchone()

    conn.close()

    if row is None:
        return None

    return {
        "id": row[0],
        "title": row[1],
        "done": row[2]
    }

def create_task(title, done):
    conn = get_connection()

    with conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO tasks (title, done)
            VALUES (%s, %s)
            RETURNING id, title, done;
            """,
            (title, done)
        )

        row = cur.fetchone()

    conn.commit()
    conn.close()

    return {
        "id": row[0],
        "title": row[1],
        "done": row[2]
    }

def update_task(task_id, title, done):
    conn = get_connection()

    with conn.cursor() as cur:
        cur.execute(
            """
            UPDATE tasks
            SET title = %s, done = %s
            WHERE id = %s
            RETURNING id, title, done;
            """,
            (title, done, task_id)
        )

        row = cur.fetchone()

    conn.commit()
    conn.close()

    if row is None:
        return None

    return {
        "id": row[0],
        "title": row[1],
        "done": row[2]
    }

def delete_task(task_id):
    conn = get_connection()

    with conn.cursor() as cur:
        cur.execute(
            """
            DELETE FROM tasks
            WHERE id = %s
            RETURNING id;
            """,
            (task_id,)
        )

        row = cur.fetchone()

    conn.commit()
    conn.close()

    if row is None:
        return False

    return True
    
if __name__ == "__main__":
    conn = get_connection()

    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id SERIAL PRIMARY KEY,
                title TEXT NOT NULL,
                done BOOLEAN DEFAULT FALSE
            );
        """)
        cur.execute("SELECT COUNT(*) FROM tasks;")
        count = cur.fetchone()[0]

        if count == 0:
            cur.execute("""
            INSERT INTO tasks (title, done)
            VALUES
                ('Learn FastAPI', FALSE),
                ('Learn PostgreSQL', FALSE),
                ('Build Task API', FALSE);
            """)

    conn.commit()
    conn.close()


    print("tasks table created successfully!")