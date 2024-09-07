import requests
import sys

def fetch(target):
    if len(target) < 3:
        print("Usage: python script.py <domain>")
        sys.exit(1)

    subdomains = set()
    url = 'https://crt.sh/?q={}&output=json'.format(target)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return []


    data = response.json()
    for item in data:
        sub = item['name_value']
        sub = sub.split('\n')
        for s in sub:
            if s.startswith('*'):
                subdomains.add(s[2:])
            else:
                subdomains.add(s)
    
    return list(subdomains)

if __name__ == '__main__':
    fetch()
