import requests
import sys

def fetch(target):
    if len(target) < 3:
        print("Usage: python script.py <domain>")
        sys.exit(1)

    url = 'https://api.hackertarget.com/hostsearch/?q={}'.format(target)

    response = requests.get(url)

    data = response.text.strip()
    
    lines = data.splitlines()

    subdomains = [line.split(",")[0] for line in lines if "," in line]
    
    return list(subdomains)

if __name__ == '__main__':
    fetch()