import mysql.connector

def connect_to_database():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="mydb",
        )

    if conn.is_connected():
        print("Connected to MySQL database successfully!")
        
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM student")
        rows = cursor.fetchall()
        print(f"Query returned {len(rows)} rows.")
        for r in rows:
            print(r)
        conn.close()
        cursor.close()
    else:
        print("Connection created but is_connected() returned False")


if __name__ == "__main__":
    connect_to_database()