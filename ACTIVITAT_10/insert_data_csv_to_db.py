import psycopg2


def insert_data_csv_to_db(pos, data):
    try:
        # Establecer la conexión a la base de datos
        conn = psycopg2.connect(
            database="penjat",
            user="user",
            password="pass",
            host="localhost",
            port="5433"
        )

        cur = conn.cursor()


        word = data.get("WORD")[pos]
        theme = data.get("THEME")[pos]

        # Inserción de datos en la tabla
        sql = "INSERT INTO word (word, theme) VALUES (%s, %s);"
        values = (word, theme)

        # Ejecutar la consulta de inserción
        cur.execute(sql, values)
        conn.commit()  # Confirmar la transacción

        cur.close()
        conn.close()

        return {"Message": "Data inserted successfully"}

    except Exception as e:
        # Manejar cualquier error durante la conexión o ejecución
        return {"Error": str(e)}
