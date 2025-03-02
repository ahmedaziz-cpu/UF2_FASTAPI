import csv
import insert_data_csv_to_db as insert_data

def csv_to_json():
    data = []
    with open("paraules_temàtica_penjat.csv", mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)  # Utiliza DictReader para convertir cada fila en un diccionario
        for row in csv_reader:
            data.append(row)  # Agregar cada fila como un diccionario a la lista
    return data

data = csv_to_json()

for i in range(len(data)):
    insert_data.insert_data_csv_to_db(i, data[i])  # Pasar cada fila como un diccionario
