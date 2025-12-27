import os
import subprocess
import pathlib
import profiles
import database
import navigation

# create database
database.create_profile_list_db()
database.create_app_list_db()
# navigation.print_logo()
navigation.main_menu()
profiles.Profile.create_profile()

# need to look to ask them about/create profile