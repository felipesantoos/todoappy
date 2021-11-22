# Importação do SQLite 3.
import sqlite3

# Conexão com o banco de dados (caso não exista é criado).
conn = sqlite3.connect("todo-app.db")

def create_todo_table():
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS todo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT,
            complete INTEGER
        );
        """
    )

def add(task):
    conn.execute("INSERT INTO todo (task, complete) VALUES (?, 0)", (task,))
    conn.commit()

def remove(id):
    conn.execute("DELETE FROM todo WHERE id = ?", (id,))
    conn.commit()

def complete(id):
    conn.execute("UPDATE todo SET complete = 1 WHERE id = ?", (id,))
    conn.commit()

def get_todos():
    return conn.execute("SELECT * FROM todo")
