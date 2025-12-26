import os
import subprocess
import pathlib
import profiles
import database
import navigation

# Create simple, menu, ability to store profiles, profiles store a list of commands that run when that profile is ran. Profiles stored in database.

database.create_profile_list_db()
database.create_app_list_db()
navigation.print_logo()
profiles.Profile.create_profile()