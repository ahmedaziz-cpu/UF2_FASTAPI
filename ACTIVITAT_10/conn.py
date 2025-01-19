import psycopg2


def connection_db():


   conn = psycopg2.connect(
       database = "penjat",
       password = "pass",
       host = "localhost",
       user="user",
       port = "5433"
   )


   print("Connexió establerta correctament")
   return conn



