import os
from rich.console import Console
from rich.panel import Panel
import profiles

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
        "[bold cyan]get[/bold cyan] [italic white]<title>[/italic white] | "
        "[bold cyan]add[/bold cyan] [italic white]<title>[/italic white] | "
        "[bold red]remove[/bold red] [italic white]<title>[/italic white] | "
        "[bold green]list[/bold green] | "
        "[bold blue]search[/bold blue] [italic white]<term>[/italic white] | "
        "[bold purple]export (CSV)[/bold purple] [italic white]<filename>[/italic white] | "
        "[bold yellow]import (CSV)[/bold yellow] [italic white]<filename.csv>[/italic white] | "
        "[bold white]exit[/bold white]\n"
        "──────────────────────────────────────────────────────────────────────────────────────────\n"
        "[dim]Examples:[/dim]  [bold blue]search[/bold blue] [white]Halo 2[/white]  •  "
        "[bold cyan]add[/bold cyan] [white]Halo 2[/white]  •  "
        "[bold purple]export[/bold purple] [white]games[/white]  •  "
        "[bold yellow]import[/bold yellow] [white]games.csv[/white]"
    )

    console.print(Panel(menu_content, title="GAME COLLECTR MENU", expand=False))
    choice = console.input("[bold green]>>> [/bold green]").strip()
    print()

    if "run " in choice:
        profiles.run_profile()
    elif "create profile" in choice:
        profiles.create_profile()
        main_menu()
    elif "remove " in choice:
        profiles.remove_profile()
        main_menu()
    elif choice == "exit":
        print("Thank you for using DESKTOP SETTR!")
        sys.exit

    else:
        print("That is not a valid request.")
        print()
        main_menu()


