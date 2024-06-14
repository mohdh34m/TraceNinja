import inquirer

def menu():
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

    questions = [
        inquirer.List('option',
            message="Choose your preferred option",
            choices=['Subdomain Enumeration (Beta)', 'Coming Soon', 'Coming Soon'],
        ),
    ]
    option = inquirer.prompt(questions)
    if option["option"] == "Subdomain Enumeration (Beta)":
        questions = [
            inquirer.Text("target", message="Enter the domain")
        ]
        target = inquirer.prompt(questions)
        return target['target']