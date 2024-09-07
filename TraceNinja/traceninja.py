import time
import datetime
import concurrent.futures
from TraceNinja.utils.handler import handler
from rich import print as rprint
from TraceNinja.modules import crtsh, alienvault, hackertarget, jldc, securitytrails, rapidapi

def main():
    domain, output = handler()
    
    now = datetime.datetime.now()

    print("-----------------------------------------------------------------------------")
    print("🛠️ Version: Beta")
    print("🎯 Target Domain:" , domain)
    print("⏰ Starting:", now.strftime("%Y-%m-%d %H:%M:%S"))
    print("-----------------------------------------------------------------------------")

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