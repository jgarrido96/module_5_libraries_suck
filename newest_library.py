import mysql.connector

# ================================ ADD ============================

def add_book(title, author):
    db_name = "library_management"
    user = "root"
    password = "itsyapassword69"
    host = "127.0.0.1" # or 127.0.0.1

    try: 
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password=password,
            host=host        
        )

        cursor = conn.cursor()
        new_book = (title, author)
        query = "INSERT INTO Book (title, author) VALUES (%s, %s)"
        cursor.execute(query, new_book)
        conn.commit()



    except mysql.connector.Error as e:
        print(f"Error: {e}")

    finally:
        if conn and conn.is_connected():
            conn.close()

def add_author(author, title):
    db_name = "library_management"
    user = "root"
    password = "itsyapassword69"
    host = "127.0.0.1" 

    try: 
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password=password,
            host=host        
        )

        cursor = conn.cursor()
        new_author = (author, title)
        query = "INSERT INTO Author (author, books) VALUES (%s, %s)"
        cursor.execute(query, new_author)
        conn.commit()



    except mysql.connector.Error as e:
        print(f"Error: {e}")

    finally:
        if conn and conn.is_connected():
            conn.close()

def add_user(username, book_count):
    db_name = "library_management"
    user = "root"
    password = "itsyapassword69"
    host = "127.0.0.1"

    try: 
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password=password,
            host=host        
        )

        cursor = conn.cursor()
        new_user = (username, book_count)
        query = "INSERT INTO Book (username, book_count) VALUE (%s, %s)"
        cursor.execute(query, new_user)
        conn.commit()

    except mysql.connector.Error as e:
        print(f"Error: {e}")

    finally:
        if conn and conn.is_connected():
            conn.close()


# ================================== GET =============================

def get_book():
    db_name = "library_management"
    user = "root"
    password = "itsyapassword69"
    host = "127.0.0.1"

    try: 
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password=password,
            host=host        
        )

        cursor = conn.cursor()
        query = "SELECT * FROM Book"
        cursor.execute(query)
        for row in cursor.fetchall():
            print(row)

    finally:
        cursor.close()
        conn.close()

def get_author():
    db_name = "library_management"
    user = "root"
    password = "itsyapassword69"
    host = "127.0.0.1"

    try: 
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password=password,
            host=host        
        )

        cursor = conn.cursor()
        query = "SELECT * FROM Author"
        cursor.execute(query)
        for row in cursor.fetchall():
            print(row)

    finally:
        cursor.close()
        conn.close()

def get_user():
    db_name = "library_management"
    user = "root"
    password = "itsyapassword69"
    host = "127.0.0.1"

    try: 
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password=password,
            host=host        
        )

        cursor = conn.cursor()

        query = "SELECT * FROM User"

        cursor.execute(query)

        for row in cursor.fetchall():
            print(row)

    finally:
        cursor.close()
        conn.close()
