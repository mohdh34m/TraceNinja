import concurrent.futures
from modules import crtsh
from modules import alienvault
from modules import hackertarget
from modules import jldc
from modules import securitytrails
from modules import rapidapi
from utils.handler import handler

domain, output = handler()

def main(target):

    scripts = [crtsh, alienvault, hackertarget, jldc, securitytrails, rapidapi]
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_script = {executor.submit(script.fetch, target): script for script in scripts}
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
    main(domain)
