import requests
import sys


def fetch(target):
    if len(target) < 3:
        print("Usage: python script.py <domain>")
        sys.exit(1)

    url = 'https://otx.alienvault.com/api/v1/indicators/domain/{}/passive_dns'.format(target)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return []

    data = response.json()

    subdomains = []
    for entry in data["passive_dns"]:
        subdomains.append(entry["hostname"])

    return list(subdomains)

if __name__ == '__main__':
    fetch()