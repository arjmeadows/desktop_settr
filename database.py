import sqlite3


def create_db():
    connection = sqlite3.connect('profiles.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS profiles (
            title TEXT,
            description TEXT,
            filepath TEXT,
            app1 TEXT,
            app2 TEXT,
            app3 TEXT,
            app4 TEXT,
            app5 TEXT,
            app6 TEXT,
            app7 TEXT,        
        )
    ''')

    connection.commit()


def db_read_one(choice: str):
        connection = sqlite3.connect('game_collection.db')
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        sql_insert_query = """
            SELECT * FROM collection WHERE title=?;
                            """
        cursor.execute(sql_insert_query, (choice,))
        result = cursor.fetchone()

        return result        