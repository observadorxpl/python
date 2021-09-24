import sqlite3;

def connect():
    conn = sqlite3.connect("midb.db")
    cursor = conn.cursor()
    return conn, cursor

def create_table():
    conn, cursor = connect()
    sql = """
        CREATE TABLE IF NOT EXISTS AGENDA(
            ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            NOMBRE VARCHAR(20) NOT NULL,
            TELEFONO VARCHAR(14) NOT NULL
        )
    """
    if cursor.execute(sql):
        print("Tabla creada")
    else:
        print("No se pudo crear la tabla")
    conn.close()
    
    
def insert(datos):
    conn, cursor = connect()
    sql = """
        INSERT INTO AGENDA (NOMBRE, TELEFONO) VALUES (?, ?)
    """
    
    if cursor.execute(sql, datos):
        print("Datos insertados")
    else:
        print("No se pudo insertar")
    conn.commit()
    conn.close()

def consultar():
    conn, cursor = connect()
    cursor.execute("SELECT ID, NOMBRE, TELEFONO FROM AGENDA")
    for fila in cursor:
        print(f"{fila[0]} , {fila[1]}, {fila[2]}")

def modificar(id, telefono):
    conn, cursor = connect()
    cursor.execute("UPDATE AGENDA SET TELEFONO = ? WHERE ID = ?", (telefono, id))
    conn.commit()
    conn.close()


def borrar(id):
    conn, cursor = connect()
    cursor.execute("DELETE FROM AGENDA WHERE ID ="+id)
    conn.commit()
    conn.close()
create_table()
insert(("Jose", "927377406"))
insert(("Luis", "927377435"))
modificar("22","988012997")
borrar("22")
consultar()