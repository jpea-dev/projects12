import mysql.connector
import traceback

conn = None
try:
    print("Attempting to connect...", flush=True)
    conn = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="1234",
        database="mydb",
        connection_timeout=5,
        use_pure=True,
    )
    print("Connected object:", conn, flush=True)
except Exception as e:
    print("Connection error:", repr(e))
    traceback.print_exc()
finally:
    
    print('FF', flush=True)

if conn:
    print('done')
else:
    print('conn is None - skipping DB operations')

if conn and conn.is_connected():
    print('connected')
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM student")
        rows = cursor.fetchall()
        print(f"Total number of rows in student is: {len(rows)}")
        for row in rows:
            print(row)
    except Exception as e:
        print('Query error:', repr(e))
        traceback.print_exc()
    finally:
        cursor.close()
        conn.close()
