from database import db


# Define la clase `Sweet` que hereda de `db.Model`
# `Sweet` representa la tabla `sweets` en la base de datos
class Sweet(db.Model):
    __tablename__ = "sweets"

    # Define las columnas de la tabla `sweets`
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(100), nullable=False)
    peso = db.Column(db.String(100), nullable=False)
    sabor = db.Column(db.String(100), nullable=False)
    origen = db.Column(db.String(100), nullable=False)

    # Inicializa la clase `Sweet`
    def __init__(self, marca, peso, sabor, origen):
        self.marca = marca
        self.peso = peso
        self.sabor = sabor
        self.origen = origen

    # Guarda un Sweet en la base de datos
    def save(self):
        db.session.add(self)
        db.session.commit()

    # Obtiene todos los sweets de la base de datos
    @staticmethod
    def get_all():
        return Sweet.query.all()

    # Obtiene un Sweet por su ID
    @staticmethod
    def get_by_id(id):
        return Sweet.query.get(id)

    # Actualiza un Sweet en la base de datos
    def update(self, marca=None, peso=None, sabor=None, origen=None):
        if marca is not None:
            self.marca = marca
        if peso is not None:
            self.peso = peso
        if sabor is not None:
            self.sabor = sabor
        if origen is not None:
            self.origen = origen
        db.session.commit()

    # Elimina un Sweet de la base de datos
    def delete(self):
        db.session.delete(self)
        db.session.commit()