import os
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
import profs
import navigation

os.system("program_name") # To open any program by their name recognized by windows
#for example
os.system("notepad")


def print_logo():
    logo = r"""

 _____   _______    _    _    _ _______ _____  ______        _    _______ _______ _______ ______  
(____ \ (_______)  | |  | |  / |_______) ___ \(_____ \      | |  (_______|_______|_______|_____ \ 
 _   \ \ _____      \ \ | | / / _     | |   | |_____) )      \ \  _____   _       _       _____) )
| |   | |  ___)      \ \| |< < | |    | |   | |  ____/        \ \|  ___) | |     | |     (_____ ( 
| |__/ /| |_____ _____) ) | \ \| |____| |___| | |         _____) ) |_____| |_____| |_____      | |
|_____/ |_______|______/|_|  \_)\______)_____/|_|        (______/|_______)\______)\______)     |_|
                                                                                                                                                                                                                                                                                                          
    Store, review, and export your game collection with this retro Python program!                       

    This program was written by Adam Meadows (adamrjmeadows.com).
    """

    print(logo)


# how to edit a profile, list a profile, delete a profile. What happens if an app is missing. Needs to extract each in the list as a variable and implant it into the os oPEN FILE COMMMAND.

def main_menu():
    print("Welcome to DESKTOP SETTR")
    print("Use this to create profiles that allow you to open sets of apps -- such as 'developer' profile.")
    print("You can add up to 7 apps to a single profile.")


def main_menu():

    console = Console()

    menu_content = (
        "[bold cyan]run[/bold cyan] [italic white]<profile>[/italic white] | "
        "[bold cyan]create profile[/bold cyan] | "
        "[bold cyan]list profiles[/bold cyan] | "
        "[bold red]remove[/bold red] [italic white]<profile>[/italic white] | "
        "[bold white]exit[/bold white]\n"
        "──────────────────────────────────────────────────────────────────────────────────────────\n"
        "[dim]Examples:[/dim]  [bold cyan]run[/bold cyan] [white]Gaming[/white]  •  "
        "[bold cyan]list profiles[/bold cyan]  •  "
        "[bold red]remove[/bold red] [white]Work[/white]"
    )

    # Change title to match the "SETTR" branding in your exit message
    console.print(Panel(menu_content, title="DESKTOP SETTR MENU", expand=False))
    choice = console.input("[bold green]>>> [/bold green]").strip()
    print()

    if "run " in choice:
        profs.run_profile(choice)
        main_menu()
    elif "create profile" in choice:
        profs.Profile.create_profile()
        main_menu()
    elif "remove " in choice:
        profs.remove_profile()
        main_menu()
    elif "show " in choice:
        profs.show_profile(choice)
        main_menu()    
    elif choice == "list":
        profs.list_profiles()
        main_menu()
    elif choice == "exit":
        print("Thank you for using DESKTOP SETTR!")
        os.sys.exit
    else:
        print("That is not a valid request.")
        print()
        main_menu()


def profile_table():
    table = Table(show_header=True, show_lines=True, header_style="bold magenta")
    table.add_column("Profile name", style="bold", width=12)
    table.add_column("Description")
    table.add_column("App name", justify="left")
    table.add_column("App file path", justify="left")
    return table