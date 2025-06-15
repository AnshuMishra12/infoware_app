import sqlite3

def connect_db():
    return sqlite3.connect("database.sqlite")

def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    # ✅ User login table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    """)

    # ✅ Default operator users
    cursor.execute("INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)", ("operator1", "pass1"))
    cursor.execute("INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)", ("operator2", "pass2"))

    # ✅ Product master table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS product_master (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            barcode TEXT,
            sku TEXT,
            category TEXT,
            subcategory TEXT,
            name TEXT,
            description TEXT,
            tax REAL,
            price REAL,
            unit TEXT,
            image_path TEXT
        )
    """)

    conn.commit()
    conn.close()
