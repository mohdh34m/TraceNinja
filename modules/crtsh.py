import requests
import sys
from utils import loader

def cli(target):
    if len(target) < 3:
        print("Usage: python script.py <domain>")
        sys.exit(1)

    subdomains = set()
    url = 'https://crt.sh/?q={}&output=json'.format(target)
    response = requests.get(url)

    if response.status_code != 200:
        print("Error: Failed to retrieve data from crt.sh")
        sys.exit(1)

    data = response.json()
    for item in data:
        sub = item['name_value']
        sub = sub.split('\n')
        for s in sub:
            if s.startswith('*'):
                subdomains.add(s[2:])
            else:
                subdomains.add(s)
    
    loader.progressBar()
    return list(subdomains)

if __name__ == '__main__':
    cli()
