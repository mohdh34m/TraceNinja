import requests
import sys

def fetch(target):
    if len(target) < 3:
        print("Usage: python script.py <domain>")
        sys.exit(1)

    url = 'https://jldc.me/anubis/subdomains/{}'.format(target)

    response = requests.get(url)

    if response.status_code != 200:
        return []
    
    data = response.json()

    subdomains = []
    for subdomain in data:
        subdomains.append(subdomain)

    return list(subdomains)


if __name__ == '__main__':
    fetch()