class Product:
    def __init__(self, id=None, name="", price=0.0, stock=0, active=False):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock
        self.active = active

    def __repr__(self):
        return(
            f"Product(id={self.id}, name={self.name}, "
            f"price={self.price}, stock={self.stock}, activ={self.active})"
        )