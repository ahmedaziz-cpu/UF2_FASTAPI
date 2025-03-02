import conn
import random  # Usamos random para elegir una palabra aleatoria
from typing import List, Dict

read_conn = conn.connection_db()


def read_db() -> List[Dict[str, str]]:
    cursor = read_conn.cursor()  # Crear el cursor para la conexión
    sql = "SELECT DISTINCT theme FROM paraules"  # Consulta para obtener temas
    cursor.execute(sql)  # Ejecutar la consulta

    options = cursor.fetchall()

    return [{'id': idx, 'name': option[0]} for idx, option in enumerate(options)]


def read_word_db(option: str) -> Dict[str, str]:
    cursor = read_conn.cursor()  # Crear el cursor para la conexión
    sql = "SELECT word FROM paraules WHERE theme = %s;"  # Consulta para obtener palabras por tema
    values = (option,)  # Crear una tupla con el parámetro de la consulta
    cursor.execute(sql, values)  # Ejecutar la consulta con los parámetros

    options = cursor.fetchall()

    word = random.choice(options)[
        0]

    return {'word': word}
