# Documentació ACTIVITAT 9

## 1. **PostgreSQL - Vista de la Taula d'Usuaris**

Aquí es mostra una captura de pantalla de la taula `users` a **PostgreSQL**, on s'emmagatzemen els usuaris.

### Captura de la Taula `users` a PostgreSQL
![Captura de la taula d'usuaris a PostgreSQL](imatges/postgres.png)

**Descripció:**
En aquesta captura, es pot veure la taula `users` amb els camps `id`, `username` i `email`, que s'utilitzen per emmagatzemar la informació dels usuaris a la base de dades.



## 2. **Postman - Crear Usuari**

En aquesta captura de pantalla, pots veure com es realitza una sol·licitud **POST** a **Postman** per crear un nou usuari. El cos de la sol·licitud inclou els paràmetres `username` i `email`.

### Captura de la Sol·licitud POST a Postman per Crear un Usuari
![Captura de sol·licitud POST a Postman del usuari](imatges/postman.png)

**Descripció:**
En aquest exemple, es realitza una sol·licitud **POST** a `http://127.0.0.1:8000/users/` amb les dades d'un nou usuari: `username` i `email`. Al realitzar aquesta sol·licitud, es crea un usuari a la base de dades.

---

## 3. **Swagger UI - Endpoint per Obtener Usuaris**

A continuació es mostra com interactuar amb el endpoint `GET /users/` a **Swagger UI** per obtenir la llista d'usuaris.

### Captura de Swagger UI - Obtenir Usuaris
![Captura de Swagger UI - Obtenir Usuaris](imatges/swagger.png)

**Descripció:**
Aquesta captura mostra com es pot obtenir la llista d'usuaris registrats a la base de dades utilitzant el endpoint `GET /users/` des de **Swagger UI**. La resposta es mostrarà en format JSON.

