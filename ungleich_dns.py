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
        self.parser['dns'].add_argument('--email', help='registered email', metavar='', required=True)
        self.parser['dns'].add_argument('--realm', help='Otp realm', metavar='', required=True)
        self.parser['dns'].set_defaults(func=self._handle_dns)

    def _handle_dns(self, args):
        """A dev endpoint for reverse-dns service."""
        r = requests.post(
            'https://dev.william.ungleich.cloud',
            json={
                'username': args.user,
                'token': args.token,
                'ipaddress': args.set_reverse,
                'name': args.name,
                'email': args.email,
                'realm': args.realm
            })
        print(r.text)
