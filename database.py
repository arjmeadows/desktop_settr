import sqlite3
import profiles

def create_profile_list_db():
    connection = sqlite3.connect('profiles.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS profiles (
            name TEXT,
            description TEXT
        )
    ''')
    connection.commit()


def create_app_list_db():
    connection = sqlite3.connect('profiles.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS app_list (
            profile_name TEXT,
            app_name TEXT,
            filepath TEXT    
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

# this writes the profile and description to a table - name needs to be unique because it's being used as a reference for the 
def store_profile(new_profile):
    connection = sqlite3.connect('profiles.db')
    cursor = connection.cursor()
    sql_query = """
        INSERT INTO profiles (name, description)
        VALUES (?,?)
        """
    cursor.execute(sql_query, (new_profile.name, new_profile.description))
    connection.commit()       

# this includes 
def store_profile_apps(new_profile):
    connection = sqlite3.connect("profiles.db")
    cursor = connection.cursor()
    
    for app in new_profile.app_list:
         sql_query = """
         INSERT INTO app_list (app_name, filepath)
         VALUES (?,?)
    """
    cursor.execute(sql_query, (app[0], app[1]))
    print(new_profile.app_list[0][0])



 print(new_profile.app_list[0][0])

this works, but nothing seems to be writing to the table