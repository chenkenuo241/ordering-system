import sqlite3, pathlib
DB_PATH = pathlib.Path(__file__).with_suffix('.db')

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS menu(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            price REAL,
            category TEXT,
            stock INTEGER
        )
    ''')
    cur.execute('''
        CREATE TABLE IF NOT EXISTS orders(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            dish_id INTEGER,
            qty INTEGER,
            price REAL,
            FOREIGN KEY(dish_id) REFERENCES menu(id)
        )
    ''')
    sample = [('宫保鸡丁', 28, '热菜', 99),
              ('凉拌黄瓜', 12, '凉菜', 99),
              ('可乐', 5, '饮品', 999)]
    cur.executemany('INSERT OR IGNORE INTO menu(name,price,category,stock) VALUES(?,?,?,?)', sample)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()