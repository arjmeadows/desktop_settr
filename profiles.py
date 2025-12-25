import os
import sqlite3
import database

# profile contains a series of apps - which all contain: a title, a description, up to 6 app names, each with their own filename (probs a tuple?) object needs a list one app, obtain can contain the necesary tuples

# a profile is an object. contains list of tuples, cycle through list to launch profile contents

class Profile:
    def __init__(self, name: str, description: str, app_list: list):
        self.name = name
        self.description = description
        self.app_list = app_list


    def __str__(self):
        return f"{self.name}, {self.description}, {self.app_list}"


def create_profile(self):
    name = input("What do you want to call the profile?: ")
    description = input("Give the profile a description: ")
    max_apps_per_profile = 6
    tracker = 0
    temp_app_list = []

    while tracker <= max_apps_per_profile:

        app_name = input("")
        app_file_path = input("Filepath: ")
        app_tuple = (app_name, app_file_path)
        temp_app_list.append(app_tuple)

    new_profile = Profile(name, description, temp_app_list)
    
    
    # database.store_profile(new_profile)


    def run_profile(profile: Profile):
        # needs a loop that iterates through - object probably needs to store number of apps it adds somewhere, use list len.
        os.subprocess.run(["open", profile.]) #this needs to look in the dictionary/object for the corresponding value. objects seem cleaner?
        


                


 # path = "/Users/adammeadows/game_app_git/dist/GAME COLLECTR"

# This is the macOS equivalent of os.startfile
# subprocess.run(["open", path])           