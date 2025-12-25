import sqlite3
import profiles

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
            app4 TEXT      
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


def store_profile(new_profile):
    connection = sqlite3.connect("profiles.db")
    cursor = connection.cursor()
    sql_query = """
        INSERT INTO profils (title, description, app1)
        VALUES (?,?,?)
        """
    cursor.execute(sql_query, (new_profile.name, new_profile.title, new_profile.app1, new_profile.app1))
    connection.commit()       



def store_profile_apps(profile_name, app_list):
    connection = sqlite3.connect("profiles.db")
    cursor = connection.cursor()
    
    for app in app_list:
         sql_query = """
         INSERT INTO profiles_list (app_name, app_directory)
         VALUES (?,?,?)
    """
    cursor.execute(sql_query, (app))


    # need to get it out the list somehow?