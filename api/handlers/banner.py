# banner.py

from colorama import Fore, Style

def print_banner():
    banner_text = """
 😁 ░██ ███╗░ ███╗░░██╗██╗  ██╗░█████╗░██╗░░██╗░█████╗░███╗░░██╗
██╔══██╗ ████╗░██║██║██║   ██╔══██╗██║░░██║██╔══██╗████╗░██║
██║░░██║ ██╔██╗██║██║██║   ██║░░╚═╝███████║███████║██╔██╗██║
██║░░██║ ██║╚████║██║██║   ██║░░██╗██╔══██║██╔══██║██║╚████║
╚█████╔╝ ██║░╚███║██║██║   ╚█████╔╝██║░░██║██║░░██║██║░╚███║
░╚════╝░╚═╝░░╚══╝╚═╝╚═╝   ░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝

   😁Onii Chan!
    GPT-4 API
    """

    # Print the banner with colors
    print(Fore.BLUE + banner_text + Style.RESET_ALL)
