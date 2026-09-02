import sqlite3
from werkzeug.security import generate_password_hash

DATABASE = "spendly.db"

def get_db():
    """Opens connection to spendly.db and returns it with row_factory and foreign keys enabled."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def init_db():
    """Creates both tables using CREATE TABLE IF NOT EXISTS."""
    with get_db() as conn:
        conn.executescript("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                created_at TEXT DEFAULT (datetime('now'))
            );

            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                date TEXT NOT NULL,
                description TEXT,
                created_at TEXT DEFAULT (datetime('now')),
                FOREIGN KEY (user_id) REFERENCES users (id)
            );
        """)
        conn.commit()

def seed_db():
    """Inserts one demo user and 8 sample expenses if the database is empty."""
    with get_db() as conn:
        # Check if users table already has data
        cursor = conn.execute("SELECT count(*) FROM users")
        if cursor.fetchone()[0] > 0:
            return

        # Insert demo user
        demo_user_data = {
            "name": "Demo User",
            "email": "demo@spendly.com",
            "password_hash": generate_password_hash("demo123", method='pbkdf2:sha256')
        }

        cursor = conn.execute(
            "INSERT INTO users (name, email, password_hash) VALUES (?, ?, ?)",
            (demo_user_data["name"], demo_user_data["email"], demo_user_data["password_hash"])
        )
        user_id = cursor.lastrowid

        # Sample expenses covering all categories:
        # Food, Transport, Bills, Health, Entertainment, Shopping, Other
        expenses = [
            (user_id, 15.50, "Food", "2026-09-01", "Lunch at Cafe"),
            (user_id, 45.00, "Transport", "2026-09-02", "Gas Refill"),
            (user_id, 120.00, "Bills", "2026-09-01", "Electricity Bill"),
            (user_id, 30.00, "Health", "2026-09-03", "Pharmacy"),
            (user_id, 12.00, "Entertainment", "2026-09-02", "Cinema Ticket"),
            (user_id, 65.00, "Shopping", "2026-09-01", "New T-shirt"),
            (user_id, 10.00, "Other", "2026-09-03", "Postage Stamps"),
            (user_id, 22.00, "Food", "2026-09-02", "Dinner"),
        ]

        conn.executemany(
            "INSERT INTO expenses (user_id, amount, category, date, description) VALUES (?, ?, ?, ?, ?)",
            expenses
        )
        conn.commit()
