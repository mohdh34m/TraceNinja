# utils/handler/handler.py

from utils.banner.banner import banner  # Import banner function
from utils.cli.cli import cli           # Import cli function

# Call banner function here instead of storing its result
def handler():
    args = cli()
    domain = args.domain
    output = args.output

    # Just call banner without assigning it
    banner()  # Displays the banner directly

    return domain, output

    