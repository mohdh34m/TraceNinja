from rich.console import Console
from rich import print as rprint

console = Console()

def banner():
    version = "0.1"
    rprint(fr"""
                                                               
                [cyan1]▀██▌
                [cyan1]  "▀▀▄       [white],▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
               [cyan1] ▄▄▄▄▄▄▄▄P [white]▄█▀-         `▀███▀-         -▀█▄
                [cyan1] ▀███▀'  [white]▐▌  [red1] █▄          [white]▀          [red1]▄▄   [white]▐▌
                         [white]╟▌  [red1]▐███▄                ▄▄███   [white]▐▌
                         [white]▐▌   [red1]▀█████M           ▀████▀▀   [white]▐▌
                         [white] █▄            ,▄█▄             [white]╓█ 
                           ▀▀&▄▄▄▄▄▄▄▄▄███████▄▄▄▄▄▄▄▄▄&▀▀

████████╗██████╗  █████╗  ██████╗███████╗███╗   ██╗██╗███╗   ██╗     ██╗ █████╗ 
╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██╔════╝████╗  ██║██║████╗  ██║     ██║██╔══██╗
   ██║   ██████╔╝███████║██║     █████╗  ██╔██╗ ██║██║██╔██╗ ██║     ██║███████║
   ██║   ██╔══██╗██╔══██║██║     ██╔══╝  ██║╚██╗██║██║██║╚██╗██║██   ██║██╔══██║
   ██║   ██║  ██║██║  ██║╚██████╗███████╗██║ ╚████║██║██║ ╚████║╚█████╔╝██║  ██║
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚══════╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═══╝ ╚════╝ ╚═╝  ╚═╝
                           ⚔ Subdomain Gathering Tool ⚔
                                by @mohdh34m with ❤
""")