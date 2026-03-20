from models.product import Product

class ProductService:
    def __init__(self, repository):
        self.repository = repository

    def create_product(self, name, price, stock, active):
        product = Product(
            name=name.strip(),
            price=float(price),
            stock=int(stock),
            active=active
        )
        self.repository.save(product)

    def get_all_products(self):
        return self.repository.find_all()

    def get_product_by_id(self, product_id):
        return self.repository.find_by_id(product_id)

    def update_product(self, id, name, price, stock, active):
        product = Product(
            id=id,
            name=name.strip(),
            price=float(price),
            stock=int(stock),
            active=active
        )
        self.repository.update(product)

    def remove_product(self, product_id):
        self.repository.delete(product_id)




