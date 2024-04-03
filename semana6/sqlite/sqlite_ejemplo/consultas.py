# Importar módulo sqlite3
import sqlite3

# Crear conexión a la base de datos
conn = sqlite3.connect("restaurante.db")

# Consultar datos de pedidos INNER JOIN
print("\nPEDIDOS: INNER JOIN")
cursor = conn.execute(
    """
    SELECT PEDIDOS.id, PLATOS.nombre, MESAS.numero, PEDIDOS.cantidad, PEDIDOS.fecha 
    FROM PEDIDOS
    JOIN PLATOS ON PEDIDOS.plato_id = PLATOS.id 
    JOIN MESAS ON PEDIDOS.mesa_id = MESAS.id
    """
)
for row in cursor:
    print(row)

# Consultar datos de platos LEFT JOIN
print("\nPLATOS LEFT JOIN:")
cursor = conn.execute(
    """
    SELECT PLATOS.nombre
    FROM PLATOS
    LEFT JOIN PEDIDOS ON PLATOS.id = PEDIDOS.plato_id;
    """
)
for row in cursor:
    print(row)
