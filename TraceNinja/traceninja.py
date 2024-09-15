import time
import datetime
import concurrent.futures
import requests
from TraceNinja.utils.handler import handler
from rich import print as rprint
from TraceNinja.modules import crtsh, alienvault, hackertarget, jldc, securitytrails, rapidapi
from importlib.metadata import version as get_installed_version
from packaging.version import Version
import subprocess
import sys
import os

CURRENT_VERSION = get_installed_version("TraceNinja")

current_dir = os.path.dirname(__file__)

domain, domains_file, output = handler()

def read_domains_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def save_subdomains(subdomains, output, current_dir):
    if output and output.lower() != "none":
        file_path = os.path.abspath(output) if os.path.isabs(output) else os.path.join(os.getcwd(), output)
        
        try:
            with open(file_path, "w") as file:
                for subdomain in subdomains:
                    file.write(f"{subdomain}\n")
            rprint(f"[spring_green1][SUCCESS] Subdomains have been saved to {file_path}")
        except IOError as e:
            rprint(f"[red1][ERROR] Failed to save subdomains to file: {e}")

def updater():
    update = input("Do you want to update TraceNinja? (yes/no): ").lower().strip()

    if update == "yes":
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "TraceNinja"])
            print("TraceNinja has been successfully updated!")
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while updating: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    elif update == "no":
        print("Update cancelled.")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

def process_domain(target_domain):
    rprint("[deep_sky_blue1][INFO]", f"Starting subdomain enumeration for target: {target_domain}")
    scripts = [crtsh, alienvault, hackertarget, jldc, securitytrails, rapidapi]
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        start_time = time.time()
        future_to_script = {executor.submit(script.fetch, target_domain): script for script in scripts}
        all_subdomains = []
        rprint("[deep_sky_blue1][INFO]", "Querying subdomains")
        for future in concurrent.futures.as_completed(future_to_script):
            script = future_to_script[future]
            subdomains = future.result()
            if subdomains:
                all_subdomains.extend(subdomains)

    subdomains = list(set(all_subdomains))
    rprint("[spring_green1][SUCCESS]", "Retrieved subdomains")
    elapsed_time = time.time() - start_time
    rprint("[deep_sky_blue1][INFO]", f"Subdomain enumeration completed in {elapsed_time:.2f} seconds")
    rprint("[deep_sky_blue1][INFO]", f"Total unique subdomains found: {len(subdomains)}")
    return subdomains

def main():
    now = datetime.datetime.now()

    print("-----------------------------------------------------------------------------")
    print("🛠️ Version:", CURRENT_VERSION)
    print("⏰ Starting:", now.strftime("%Y-%m-%d %H:%M:%S"))
    print("-----------------------------------------------------------------------------")

    contents = requests.get('https://pypi.org/pypi/TraceNinja/json')
    data = contents.json()
    latest_version = data['info']['version']

    if Version(CURRENT_VERSION) < Version(latest_version):
        print("Update available. Current version:", CURRENT_VERSION, "Latest version:", latest_version)
        updater()
    elif Version(latest_version) == Version(CURRENT_VERSION):
        print(f"You are running the latest version of TraceNinja. (Version: {CURRENT_VERSION})")

    all_subdomains = []
    if domains_file:
        domains = read_domains_from_file(domains_file)
        rprint("[deep_sky_blue1][INFO]", f"Read {len(domains)} domains from file: {domains_file}")
        for target_domain in domains:
            all_subdomains.extend(process_domain(target_domain))
    else:
        all_subdomains = process_domain(domain)

    if output:
        save_subdomains(all_subdomains, output, current_dir)

    for subdomain in all_subdomains:
        print(subdomain)

if __name__ == '__main__':
    main()