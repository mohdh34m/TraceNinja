import argparse

def print_banner():
    version = "0.1"
    banner = f"""
 
███╗   ███╗██████╗ ███████╗███╗   ██╗██╗   ██╗███╗   ███╗
████╗ ████║██╔══██╗██╔════╝████╗  ██║██║   ██║████╗ ████║
██╔████╔██║██║  ██║█████╗  ██╔██╗ ██║██║   ██║██╔████╔██║
██║╚██╔╝██║██║  ██║██╔══╝  ██║╚██╗██║██║   ██║██║╚██╔╝██║
██║ ╚═╝ ██║██████╔╝███████╗██║ ╚████║╚██████╔╝██║ ╚═╝ ██║
╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝ {version} ╚═╝                                                                         
    """
    print(banner)
    print('{:^50s}'.format("⟸  Subdomain Gathering Tool ⟹"))
    print('{:^50s}'.format("by @mohdh34m with ❤\n"))

print_banner()

parser = argparse.ArgumentParser(usage="main.py [options] url")
parser.add_argument("-d", "--domain", help="Specify the target domain for subdomain enumeration.")
parser.add_argument("-l", "--list", help="Specify a file containing a list of root domains to enumerate.")
parser.add_argument("-o", "--output", help="Specify the output file to save the final enumeration results. Default filename format: <name>.txt.")
parser.add_argument("-hp", "--http-probe", action="store_true", help="Perform HTTP/HTTPS server probing.")

args = parser.parse_args()
