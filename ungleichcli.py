import requests
import argparse


def msg(name=None):
    return '''ungleich-cli --set-reverse <ipv6adrress> --user <username> --token <token> --name <hostname>'''


parser = argparse.ArgumentParser(description="This script set the reverse dns for your VM", usage=msg())

parser.add_argument('--set-reverse', help='REQUIRED: IPv6 Address of your VM', metavar='', required=True)
parser.add_argument('--user', help='Your ungleich username', metavar='', required=True)
parser.add_argument('--token', help='Your ungleich 6 digit OTP generated token', metavar='', type=int, required=True)
parser.add_argument('--name', help='Hostname', metavar='', required=True)

args = parser.parse_args()


def cli():
    """A dummy endpoint, to check what endpoint will be reverse-dns service."""
    r = requests.post(
        'https://en53kfc0hydpg.x.pipedream.net',
        json={'username': args.user, 'token': args.token, 'ipaddress': args.set_reverse, 'name': args.name})
    return r.text
