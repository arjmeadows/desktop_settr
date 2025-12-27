import os
import sqlite3
import database

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
        # database.store_profile(new_profile)


    def run_profile(profile_name: str): # row here somewhere, or something like that

        connection = sqlite3.connect('profiles.db')
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        sql_insert_query = """
            SELECT filepath FROM app_list WHERE title=?;
                            """
        cursor.execute(sql_insert_query, (profile_name,))
        result = cursor.fetchone()
        print(result)



        


# def run_profile(profile: Profile):
    # needs a loop that iterates through - object probably needs to store number of apps it adds somewhere, use list len.
    # os.subprocess.run(["open", profile.]) #this needs to look in the dictionary/object for the corresponding value. objects seem cleaner?
        
 # path = "/Users/adammeadows/game_app_git/dist/GAME COLLECTR"

# This is the macOS equivalent of os.startfile
# subprocess.run(["open", path])           