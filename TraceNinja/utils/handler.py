
from TraceNinja.utils.banner.banner import banner  # Import banner function
from TraceNinja.utils.cli.cli import cli           # Import cli function

def handler():
    args = cli()
    domain = args.domain
    output = args.output

    # Just call banner without assigning it
    banner()  # Displays the banner directly

    return domain, output
    