import os

# profile contains a series of apps - which all contain: a title, a description, up to 6 app names, each with their own filename (probs a tuple?) object needs a list one app, obtain can contain the necesary tuples

class Profile:
    def __init__(self, name, description, app_1):
        self.name = name
        self.description = description
        self.app_1 = ("","")
        self.app_2 = ("","")
        self.app_3 = ("","")
        self.app_4 = ("","")


    def create_profile():
        profile_name = input("What do you want to call your profile?")
        description = input("Give it a description:")
        max = 6
        profile_list = []
        tracker = 0

        while tracker <= max:

            profile = {}
            app_name = input("")
            app_file_path = input("Filepath: ")
            profile["app_name"] = app_name
            profile["app_file_path"] = app_file_path
            profile_list.append(profile)

        print(profile)


    def run_profile(choice):
        os.subprocess.run(["open", path]) #this needs to look in the dictionary/object for the corresponding value. objects seem cleaner?
        




 # path = "/Users/adammeadows/game_app_git/dist/GAME COLLECTR"

# This is the macOS equivalent of os.startfile
# subprocess.run(["open", path])           