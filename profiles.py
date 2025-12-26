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
        self.temp_app_list = []
        
        max_apps_per_profile = 1
        tracker = 1
  
        while tracker <= max_apps_per_profile:

            app_name = input(f"App name{tracker}: ")
            app_file_path = input(f"Filepath{tracker}: ")
            app_tuple = (app_name, app_file_path)
            self.temp_app_list.append(app_tuple)
            tracker += 1

        new_profile = Profile(self.name, self.description, self.temp_app_list)
        print(new_profile)
        database.store_profile(new_profile)

# def run_profile(profile: Profile):
    # needs a loop that iterates through - object probably needs to store number of apps it adds somewhere, use list len.
    # os.subprocess.run(["open", profile.]) #this needs to look in the dictionary/object for the corresponding value. objects seem cleaner?
        
 # path = "/Users/adammeadows/game_app_git/dist/GAME COLLECTR"

# This is the macOS equivalent of os.startfile
# subprocess.run(["open", path])           