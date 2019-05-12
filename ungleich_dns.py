import requests
import argparse

class ungleichDNS(object):
    def __init__(self, parser, parents):
        self.parser = parser

        self.parser['dns'] = self.parser['sub'].add_parser(
            'dns',
            help="Manage DNS entries @ ungleich",
            parents=[parents])

        self.parser['dns'].add_argument('--set-reverse', help='REQUIRED: IPv6 Address of your VM', metavar='', required=True)
        self.parser['dns'].add_argument('--user', help='Your ungleich username', metavar='', required=True)
        self.parser['dns'].add_argument('--token', help='Your ungleich 6 digit OTP generated token', metavar='', type=int, required=True)
        self.parser['dns'].add_argument('--name', help='Hostname', metavar='', required=True)

    def _handle_dns(self):
        """A dummy endpoint, to check what endpoint will be reverse-dns service."""
        r = requests.post(
            'https://en53kfc0hydpg.x.pipedream.net',
            json={'username': args.user, 'token': args.token, 'ipaddress': args.set_reverse, 'name': args.name})
        return r.text
