import sqlite3
from sqlite3 import OperationalError


class Database:

    def __init__(self):
        self.connection = sqlite3.connect(r"E:\\QAAuto\\QAAuto_course\\"
                                          +r"become_qa_auto.db")
        self.cursor = self.connection.cursor()

    def test_connection(self):
        sqlite_select_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_Query)
        record = self.cursor.fetchall()
        print(f'Connected sucessfully. SQLite Database Version is: {record}')

    def get_all_users(self):
        query = 'SELECT name, address, city FROM customers'
        self.cursor.execute(query)
        record = self.cursor.fetchall()

        return record

    def get_product_by_id(self, product_id: int):
        query = (f"SELECT id, name, description, quantity FROM products "
                 f"WHERE id={product_id}")
        self.cursor.execute(query)
        record = self.cursor.fetchall()

        return record

    def get_address_by_name(self, name):
        query = (f"SELECT address, city, postalCode, country "
                 f"FROM customers WHERE name = '{name}'")
        self.cursor.execute(query)
        record = self.cursor.fetchall()

        return record

    def update_product_qnt_by_id(self, product_id: int, qnt: int):
        query = f"UPDATE products SET quantity = {qnt} WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def select_product_qnt_by_id(self, product_id):
        query = f"SELECT quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchone()

        return record

    def insert_product(self, product_id: int, name: str, description: str, qnt: int):
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity)"\
                 f"VALUES ({product_id}, '{name}', '{description}', {qnt})"

        self.cursor.execute(query)
        self.connection.commit()

    def delete_product_by_id(self, product_id: int):
        query = f"DELETE FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_detailed_orders(self):
        query = "SELECT orders.id, customers.name, products.name, "\
                 "products.description, orders.order_date "\
                 "FROM orders "\
                 "JOIN customers ON orders.customer_id = customers.id "\
                 "JOIN products ON orders.product_id = products.id"
        self.cursor.execute(query)
        record = self.cursor.fetchall()

        return record

    def get_detailed_order_by_order_id(self, order_id: int):
        query = f"SELECT orders.id, customers.name, products.name, "\
                 f"products.description, orders.order_date "\
                 f"FROM orders "\
                 f"JOIN customers ON orders.customer_id = customers.id "\
                 f"JOIN products ON orders.product_id = products.id "\
                 f"WHERE orders.id = {order_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()

        return record

    def input_order_details(self, order_id: int, product_id: int, customer_id: int):
        query = f"INSERT OR REPLACE INTO orders (order_id, product_id, customer_id)"\
                f"VALUES ({order_id}, {product_id}, {customer_id})"
        self.cursor.execute(query)
        self.connection.commit()

    def select_customers_by_first_letter(self, letter:str):
        query = f"SELECT * FROM customers WHERE name LIKE '{letter}%'"
        self.cursor.execute(query)

        result = self.cursor.fetchall()

        return result

