import time
import datetime
import concurrent.futures
from TraceNinja.utils.handler import handler
from rich import print as rprint
from TraceNinja.modules import crtsh, alienvault, hackertarget, jldc, securitytrails, rapidapi
from importlib_metadata import version as get_installed_version
from packaging.version import Version
import subprocess
import sys
import pkg_resources

CURRENT_VERSION = pkg_resources.require("TraceNinja")[0].version

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

installed_version = get_installed_version('TraceNinja')

def main():

    domain, output = handler()
    
    now = datetime.datetime.now()

    print("-----------------------------------------------------------------------------")
    print("🛠️ Version:", CURRENT_VERSION)
    print("🎯 Target Domain:" , domain)
    print("⏰ Starting:", now.strftime("%Y-%m-%d %H:%M:%S"))
    print("-----------------------------------------------------------------------------")

    if Version(CURRENT_VERSION) < Version(installed_version):
        print("update your package")
        updater()
    elif Version(installed_version) == Version(CURRENT_VERSION):
        print(f"You are running the latest version of TraceNinja. (Version: {CURRENT_VERSION})")

    scripts = [crtsh, alienvault, hackertarget, jldc, securitytrails, rapidapi]
    rprint("[deep_sky_blue1][INFO]","Starting subdomain enumeration for target: {}".format(domain))
    with concurrent.futures.ThreadPoolExecutor() as executor:
        start_time = time.time()
        future_to_script = {executor.submit(script.fetch, domain): script for script in scripts}
        all_subdomains = []
        rprint("[deep_sky_blue1][INFO]","Querying subdomains")
        for future in concurrent.futures.as_completed(future_to_script):
            script = future_to_script[future]
            subdomains = future.result()
            if subdomains:
                all_subdomains.extend(subdomains)

    subdomains = list(set(all_subdomains)) 
    rprint("[spring_green1][SUCCESS]","Retrieved subdomains")
    elapsed_time = time.time() - start_time
    rprint("[deep_sky_blue1][INFO]","Subdomain enumeration completed in {} seconds".format(elapsed_time))
    rprint("[deep_sky_blue1][INFO]","Total unique subdomains found: {}".format(len(subdomains)))
    for subdomain in subdomains:
        print(subdomain)

if __name__ == '__main__':
    main()