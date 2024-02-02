import sqlite3


class DatabaseManager:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        price REAL,
        photo TEXT,
        about TEXT,
        category TEXT,
        status INTEGER,
        created_at TEXT
        )""")
        self.conn.commit()

    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
        )""")
        self.conn.commit()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_id INTEGER,
        full_name TEXT,
        phone_number TEXT
        )""")
        self.conn.commit()

    def add_category(self, name):
        try:
            self.cursor.execute(f"INSERT INTO categories (name) VALUES ('{name}')")
            self.conn.commit()
            return True
        except Exception as exc:
            print(exc)
            return False

    def get_all_categories(self):
        try:
            return self.cursor.execute("SELECT * FROM categories;").fetchall()
        except Exception as exc:
            print(exc)
            return False

    def get_category_by_name(self, name):
        try:
            return self.cursor.execute(f"SELECT * FROM categories WHERE name='{name}'").fetchone()
        except Exception as exc:
            print(exc)
            return False

    def get_products_by_cat_id(self, cat_id):
        try:
            return self.cursor.execute(f"SELECT * FROM products WHERE category={cat_id}").fetchall()
        except Exception as exc:
            print(exc)
            return False

    def add_product(self, data: dict):
        try:
            name = data.get('name')
            price = data.get('price')
            photo = data.get('photo')
            about = data.get('about')
            category = data.get('category')
            status = data.get('status')
            created_at = data.get('created_at')
            self.cursor.execute("""
            INSERT INTO products (name, price, photo, about, category, status, created_at) VALUES (?,?,?,?,?,?,?)
            """, (name, price, photo, about, category, status, created_at))
            self.conn.commit()
            return True
        except Exception as exc:
            print(exc)

    def get_all_product(self):
        try:
            return self.cursor.execute("SELECT * FROM products;").fetchall()
        except Exception as exc:
            print(exc)
            return False

    def get_product_by_name(self, name):
        try:
            return self.cursor.execute(f"SELECT * FROM products WHERE name='{name}' AND status=1").fetchone()
        except Exception as exc:
            print(exc)
            return False

    def delete_table(self, table_name):
        self.cursor.execute(f"DROP TABLE {table_name}")
        self.conn.commit()

    def register_user(self, data: dict):
        try:
            full_name = data.get('full_name')
            phone_number = data.get('phone_number')
            telegram_id = data.get('telegram_id')
            self.cursor.execute("""
            INSERT INTO users (full_name, phone_number, telegram_id) VALUES (?,?,?)
            """, (full_name, phone_number, telegram_id))
            self.conn.commit()
            return True
        except Exception as exc:
            print(exc)

    def get_user(self, telegram_id):
        try:
            return self.cursor.execute(f"SELECT * FROM users WHERE telegram_id='{telegram_id}'").fetchone()
        except Exception as exc:
            print(exc)
            return False

    def get_product_by_category(self, name):
        try:
            return self.cursor.execute(f"SELECT * FROM products WHERE category='{name}'").fetchall()
        except Exception as exc:
            print(exc)
            return False

    def delete_table_for_id(self):
        self.cursor.execute(f"DELETE FROM products WHERE id=8")
        self.conn.commit()
