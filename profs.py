import os
import sqlite3
import subprocess
import database

def open_app(app_name: str): # one of these functions needs to detect the OS
    subprocess.call(['open', app_name])

class Profile:
    def __init__(self, name: str, description: str, app_list: list):
        self.name = name
        self.description = description
        self.app_list = app_list


    def __str__(self):
        return f"{self.name}, {self.description}, {self.app_list}"

    @classmethod
    def create_profile(self):
        self.name = input("What do you want to call the profile?: ")
        self.description = input("Give the profile a description: ")
        self.app_list = []
    
        max_apps_per_profile = 2
        tracker = 1
  
        while tracker <= max_apps_per_profile:

            app_name = input(f"App name{tracker}: ")
            app_file_path = input(f"Filepath{tracker}: ")
            app_tuple = (app_name, app_file_path)
            self.app_list.append(app_tuple)
            tracker += 1

        new_profile = Profile(self.name, self.description, self.app_list)
        print(self.app_list)
        # function here that passes it to the other database table
        database.store_profile_apps(new_profile)
        database.store_profile(new_profile)


    def run_profile(choice):
        prof_name = choice[4:]
        print(prof_name)
        connection = sqlite3.connect('profiles.db')
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        sql_insert_query = """
            SELECT * FROM app_list WHERE profile_name=?
                            """
        cursor.execute(sql_insert_query, (prof_name,))
        result = cursor.fetchall()
        connection.commit
        
        for row in result:
            # function here
            print(row['filepath'])
            open_app(row['filepath'])

