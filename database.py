import sqlite3


def create_database():
    connection = sqlite3.connect("ner_analysis.db")
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS analyses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        text TEXT NOT NULL,
        language TEXT NOT NULL
    )
""")

    connection.commit()
    connection.close()


def save_analysis(text, language):
    connection = sqlite3.connect("ner_analysis.db")
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO analyses (text, language) VALUES (?, ?)",
        (text, language)
    )

    connection.commit()
    connection.close()


def get_analysis_history():
    connection = sqlite3.connect("ner_analysis.db")
    cursor = connection.cursor()

    cursor.execute(
        "SELECT id, text, language FROM analyses ORDER BY id DESC"
    )

    rows = cursor.fetchall()

    connection.close()

    return rows
