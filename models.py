import sqlite3
from db import DB_PATH

class OrderModel:
    @staticmethod
    def list_menu():
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute('SELECT id,name,price,category,stock FROM menu WHERE stock>0')
        rows = cur.fetchall()
        conn.close()
        return rows

    @staticmethod
    def add_dish(dish_id, qty):
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute('SELECT price,stock FROM menu WHERE id=?', (dish_id,))
        price, stock = cur.fetchone()
        if qty > stock:
            raise ValueError('库存不足')
        cur.execute('INSERT INTO orders(dish_id,qty,price) VALUES(?,?,?)',
                    (dish_id, qty, price * qty))
        cur.execute('UPDATE menu SET stock=stock-? WHERE id=?', (qty, dish_id))
        conn.commit()
        conn.close()

    @staticmethod
    def current_order():
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute('''
            SELECT m.name, o.qty, o.price
            FROM orders o JOIN menu m ON o.dish_id=m.id
        ''')
        rows = cur.fetchall()
        conn.close()
        return rows

    @staticmethod
    def checkout(discount):
        rows = OrderModel.current_order()
        total = sum(r[2] for r in rows)
        final = total * discount
        return total, final

    @staticmethod
    def clear_order():
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute('DELETE FROM orders')
        conn.commit()
        conn.close()