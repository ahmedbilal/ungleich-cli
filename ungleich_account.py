import requests
import argparse


class Account_Create(object):
    def __init__(self, parser, parents):
        self.parser = parser

        self.parser['account'] = self.parser['sub'].add_parser(
            'account',
            help="Create a valid ungleich account",
            parents=[parents])

        self.parser['account'].add_argument('--create-user', help='REQUIRED: Username', required=True)
        self.parser['account'].add_argument('--name', help='User\'s firstname', type=str, required=True)
        self.parser['account'].add_argument('--lastname', help='User\'s lastname', type=str, required=True)
        self.parser['account'].add_argument('--email', help='Email', required=True)
        self.parser['account'].set_defaults(func=self._handle_account)

    def _handle_account(self, args):
        """Reverse account endpoint."""
        r = requests.post(
            'https://account.ungleich.ch/create/',
            data={
                'username': args.create_user,
                'firstname': args.name,
                'lastname': args.lastname,
                'email': args.email
            })
        print(r.text)
