class Product:
    def __init__(self, id=None, name="", price=0.0, stock=0, activo=False):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock
        self.activo = activo

    def __repr__(self):
        return(
            f"Product(id={self.id}, name={self.name}, "
            f"precio={self.price}, stock={self.stock}, activo={self.activo})"
        )