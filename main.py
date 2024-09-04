import concurrent.futures
import inquirer
from modules import crtsh
from modules import alienvault
from modules import hackertarget
from modules import jldc
from modules import securitytrails
from modules import rapidapi

def main(target):
    scripts = [crtsh, alienvault, hackertarget, jldc, securitytrails, rapidapi]
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_script = {executor.submit(script.cli, target): script for script in scripts}
        all_subdomains = []
        for future in concurrent.futures.as_completed(future_to_script):
            script = future_to_script[future]
            subdomains = future.result()
            if subdomains:
                all_subdomains.extend(subdomains)

    subdomains = list(set(all_subdomains)) 
    for subdomain in subdomains:
        print(subdomain)
        
    print(len(subdomains))

if __name__ == '__main__':
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
    main(target["target"])
