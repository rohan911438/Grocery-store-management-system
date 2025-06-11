import mysql.connector
from mysql.connector import Error

__cnx = None

def get_sql_connection():
    global __cnx
    if __cnx is None:
        try:
            __cnx = mysql.connector.connect(
                host='127.0.0.1',
                database='gs',
                user='root',
                password=''  # Update this with your correct password
            )
            if __cnx.is_connected():
                print("Connected to MySQL database")
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            raise
    return __cnx

def close_connection():
    global __cnx
    if __cnx is not None and __cnx.is_connected():
        __cnx.close()
        __cnx = None
        print("MySQL connection closed")

if __name__ == '__main__':
    # Test different common passwords
    passwords = ['', 'root', 'MYsql@1432', 'password', 'mysql', '123456']
    
    for pwd in passwords:
        try:
            print(f"Trying password: {'(empty)' if pwd == '' else pwd}")
            test_conn = mysql.connector.connect(
                host='127.0.0.1',
                port=3306,  # Try 3307 if 3306 doesn't work
                database='mysql',  # Connect to default mysql database first
                user='root',
                password=pwd
            )
            print(f"✅ Connection successful with password: {'(empty)' if pwd == '' else pwd}")
            
            # Test if 'gs' database exists
            cursor = test_conn.cursor()
            cursor.execute("SHOW DATABASES LIKE 'gs'")
            result = cursor.fetchone()
            if result:
                print("✅ Database 'gs' exists")
            else:
                print("❌ Database 'gs' does not exist - you need to create it")
                print("Run: CREATE DATABASE gs;")
            
            cursor.close()
            test_conn.close()
            
            # Update the password in the connection function
            print(f"\n🔧 Update your password in sql_connection.py to: {'(empty string)' if pwd == '' else pwd}")
            break
            
        except Error as e:
            print(f"❌ Failed with password {'(empty)' if pwd == '' else pwd}: {e}")
    else:
        print("❌ All password attempts failed")