import requests
import argparse


VERSION = "0.0.2"

def msg(name=None):
    return '''ungleich-cli --set-reverse <ipv6adrress> --user <username> --token <token> --name <hostname>'''


class ungleichCLI(object):
    def __init__(self):
        self._init_parser()

    def _init_parser(self):

        self.parser = {}

        # Options _all_ parsers have in common
        self.parser['loglevel'] = argparse.ArgumentParser(add_help=False)
        self.parser['loglevel'].add_argument(
            '-v', '--verbose',
            action='count',
            dest='verbose',
            required=False)

        # Main subcommand parser
        self.parser['main'] = argparse.ArgumentParser(
            description='ungleich-cli ' + VERSION)
        self.parser['main'].add_argument(
            '-V', '--version', help='Show version.', action='version',
            version='%(prog)s ' + VERSION)
        self.parser['sub'] = self.parser['main'].add_subparsers(
            title="Commands", dest="command")

        # Parents used for all parsers
        self.parser_parents = self.parser['loglevel']

    def _init_ripe(self):
        self.parser['ripe'] = self.parser['sub'].add_parser(
            'ripe', parents=[self.parser_parents])

    def _init_dns(self):
        self.parser['dns'] = self.parser['sub'].add_parser(
            'dns', parents=[self.parser_parents])

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

    def commandline(self):
        args = self.parser['main'].parse_args()



if __name__ == '__main__':
    cli = ungleichCLI()
    cli.commandline()
