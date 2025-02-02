-- Eliminar tablas si ya existen
DROP TABLE IF EXISTS usuaris CASCADE;
DROP TABLE IF EXISTS paraules CASCADE;
DROP TABLE IF EXISTS registre_joc CASCADE;
DROP TABLE IF EXISTS informacio_pantalla CASCADE;

-- Taula usuaris
CREATE TABLE usuaris (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(255) NOT NULL,
    correu_electronic VARCHAR(255) UNIQUE NOT NULL,
    contrasenya VARCHAR(255) NOT NULL,
    data_creacio TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Taula paraules
CREATE TABLE paraules (
    id SERIAL PRIMARY KEY,
    paraula VARCHAR(255) NOT NULL,
    dificultat VARCHAR(10) CHECK (dificultat IN ('fàcil', 'mitjà', 'difícil')) NOT NULL
);

-- Taula registre de joc
CREATE TABLE registre_joc (
    id SERIAL PRIMARY KEY,
    usuari_id INT,
    paraula_id INT,
    intents INT DEFAULT 0,
    estat VARCHAR(10) CHECK (estat IN ('guanyat', 'perdut')) NOT NULL,
    data_partida TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuari_id) REFERENCES usuaris(id),
    FOREIGN KEY (paraula_id) REFERENCES paraules(id)
);

-- Taula informació per renderitzar la pantalla principal
CREATE TABLE informacio_pantalla (
    id SERIAL PRIMARY KEY,
    titol VARCHAR(255) NOT NULL,
    descripcio TEXT NOT NULL,
    data_actualitzacio TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Crear un trigger per actualitzar automàticament la columna data_actualitzacio
CREATE OR REPLACE FUNCTION update_data_actualitzacio()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_actualitzacio = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_data_actualitzacio_trigger
BEFORE UPDATE ON informacio_pantalla
FOR EACH ROW
EXECUTE FUNCTION update_data_actualitzacio();

--psql -h localhost -U ahmedaziz -d ACT11 -f "d:/descargasahmed/Activitat_11/schema.sql"