import psycopg2


def conectar_db():
    conexion = psycopg2.connect(
        host="localhost",
        database="penjat",
        user="user",
        password="pass",
        port="5433"
    )
    return conexion


def crear_tablas():
    conexion = conectar_db()

    cursor = conexion.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS word (
        id SERIAL PRIMARY KEY,  
        word VARCHAR(255) NOT NULL,  
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- data crear
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS theme (
        id SERIAL PRIMARY KEY,  -- Identificador único
        theme_name VARCHAR(255) NOT NULL, 
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- data crear
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS word_theme (
        word_id INT REFERENCES word(id) ON DELETE CASCADE,  -- Clave fora'
        theme_id INT REFERENCES theme(id) ON DELETE CASCADE, 
        PRIMARY KEY (word_id, theme_id)  -- Combinacio'
    );
    """)

    conexion.commit()

    print("Tablas creadas exitosamente")

    cursor.close()
    conexion.close()

if __name__ == "__main__":
    crear_tablas()
