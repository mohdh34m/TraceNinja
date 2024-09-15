import argparse

def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--domain', type=str, help='Target Domain.')
    parser.add_argument('-l', '--domain-list', type=str, help='List of domains.')
    parser.add_argument('-o', '--output', type=str, required=False, help='Output to file.')
    args = parser.parse_args()
    return args
