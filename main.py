import concurrent.futures
from utils import cli
from modules import crtsh

def main():
    
    target = cli.menu()

    scripts = [crtsh]
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_script = {executor.submit(script.cli, target): script for script in scripts}
        all_subdomains = []
        for future in concurrent.futures.as_completed(future_to_script):
            script = future_to_script[future]
            subdomains = future.result()
            if subdomains:
                all_subdomains.extend(subdomains)

    for subdomain in all_subdomains:
        print(subdomain)


if __name__ == '__main__':
    main()
