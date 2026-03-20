from sqlite3 import connect

from models.product import Product

class ProductRepository:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def save(self, product: Product):
        connection = self.db_connection.get_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO products (name, price, stock, active) VALUES (?, ?, ?, ?)",
                       (product.name, product.price, product.stock, product.active))
        connection.commit()
        connection.close()

    def find_all(self):
        connection = self.db_connection.get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT id, name, price, stock, active FROM products")
        rows = cursor.fetchall()
        connection.close()

        return [
            Product(
                id=row[0], name=row[1], price=row[2], stock=row[3],active=bool(row[4])
            )
            for row in rows
        ]

    def find_by_id(self, product_id):
        connection = self.db_connection.get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT id, name, price, stock, active
            FROM products
            WHERE id = ?
        """, (product_id,))
        row = cursor.fetchone()
        connection.close()

        if row:
            return Product(
                id=row[0], name=row[1], price=row[2], stock=row[3], active=bool(row[4])
            )
        return None

    def update(self, product: Product):
        connection = self.db_connection.get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            UPDATE products
            SET name = ?, price = ?, stock = ?, active = ?
            WHERE id = ?
        """, (product.name, product.price, product.stock, int(product.active), product.id))
        connection.commit()
        connection.close()

    def delete(self, product_id):
        connection = self.db_connection.get_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
        connection.commit()
        connection.close()