import os
import subprocess
import pathlib
import profiles
import navigation

# Create simple, menu, ability to store profiles, profiles store a list of commands that run when that profile is ran. Profiles stored in database.

navigation.print_logo()
profiles.Profile.create_profile()