import mysql.connector
print("Testing MySQL connection...")
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="mydb"
)
print("Connection object:", conn)
print("Connected:", conn.is_connected())
conn.close()