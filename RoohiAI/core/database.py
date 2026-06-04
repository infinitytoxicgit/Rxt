# RoohiAI/core/database.py

import sqlite3
from pathlib import Path
from threading import Lock

# ==========================================================
# DATABASE PATH
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent.parent
DB_DIR = BASE_DIR / "data"
DB_DIR.mkdir(exist_ok=True)

DB_PATH = DB_DIR / "roohi.db"

# ==========================================================
# LOCK
# ==========================================================

_db_lock = Lock()

# ==========================================================
# DATABASE CLASS
# ==========================================================

class Database:

    def __init__(self):
        self.db_path = str(DB_PATH)
        self.initialize()

    def connect(self):
        return sqlite3.connect(
            self.db_path,
            check_same_thread=False
        )

    def execute(
        self,
        query,
        params=(),
        fetchone=False,
        fetchall=False
    ):
        with _db_lock:
            conn = self.connect()
            cur = conn.cursor()

            cur.execute(query, params)

            data = None

            if fetchone:
                data = cur.fetchone()

            elif fetchall:
                data = cur.fetchall()

            conn.commit()
            conn.close()

            return data

    # ======================================================
    # TABLES
    # ======================================================

    def initialize(self):

        conn = self.connect()
        cur = conn.cursor()

        # USERS

        cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            first_name TEXT,
            username TEXT,
            language TEXT DEFAULT 'en',
            ai_model TEXT DEFAULT 'openrouter',
            joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        # GROUPS

        cur.execute("""
        CREATE TABLE IF NOT EXISTS groups (
            chat_id INTEGER PRIMARY KEY,
            title TEXT,
            added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        # AI HISTORY

        cur.execute("""
        CREATE TABLE IF NOT EXISTS ai_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            prompt TEXT,
            response TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        # PLAYLISTS

        cur.execute("""
        CREATE TABLE IF NOT EXISTS playlists (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            title TEXT,
            url TEXT
        )
        """)

        # QUIZ SCORES

        cur.execute("""
        CREATE TABLE IF NOT EXISTS quiz_scores (
            user_id INTEGER PRIMARY KEY,
            score INTEGER DEFAULT 0
        )
        """)

        # SETTINGS

        cur.execute("""
        CREATE TABLE IF NOT EXISTS settings (
            chat_id INTEGER PRIMARY KEY,
            music_enabled INTEGER DEFAULT 1,
            ai_enabled INTEGER DEFAULT 1,
            quiz_enabled INTEGER DEFAULT 1
        )
        """)

        conn.commit()
        conn.close()

# ==========================================================
# INSTANCE
# ==========================================================

db = Database()

# ==========================================================
# USER FUNCTIONS
# ==========================================================

def add_user(
    user_id,
    first_name="",
    username=""
):
    db.execute(
        """
        INSERT OR IGNORE INTO users
        (
            user_id,
            first_name,
            username
        )
        VALUES (?, ?, ?)
        """,
        (
            user_id,
            first_name,
            username
        )
    )

def get_user(user_id):
    return db.execute(
        """
        SELECT *
        FROM users
        WHERE user_id=?
        """,
        (user_id,),
        fetchone=True
    )

# ==========================================================
# GROUP FUNCTIONS
# ==========================================================

def add_group(
    chat_id,
    title=""
):
    db.execute(
        """
        INSERT OR IGNORE INTO groups
        (
            chat_id,
            title
        )
        VALUES (?, ?)
        """,
        (
            chat_id,
            title
        )
    )

# ==========================================================
# HISTORY
# ==========================================================

def save_chat(
    user_id,
    prompt,
    response
):
    db.execute(
        """
        INSERT INTO ai_history
        (
            user_id,
            prompt,
            response
        )
        VALUES (?, ?, ?)
        """,
        (
            user_id,
            prompt,
            response
        )
    )

# ==========================================================
# PLAYLISTS
# ==========================================================

def add_playlist(
    user_id,
    title,
    url
):
    db.execute(
        """
        INSERT INTO playlists
        (
            user_id,
            title,
            url
        )
        VALUES (?, ?, ?)
        """,
        (
            user_id,
            title,
            url
        )
    )

# ==========================================================
# QUIZ
# ==========================================================

def update_score(
    user_id,
    points
):
    db.execute(
        """
        INSERT OR IGNORE INTO quiz_scores
        (
            user_id,
            score
        )
        VALUES (?, 0)
        """
    )

    db.execute(
        """
        UPDATE quiz_scores
        SET score = score + ?
        WHERE user_id = ?
        """,
        (
            points,
            user_id
        )
    )

def get_score(user_id):
    result = db.execute(
        """
        SELECT score
        FROM quiz_scores
        WHERE user_id=?
        """,
        (user_id,),
        fetchone=True
    )

    if result:
        return result[0]

    return 0