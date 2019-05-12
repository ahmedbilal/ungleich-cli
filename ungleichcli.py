#!/usr/bin/env python3

import argparse

from ungleich_dns import ungleichDNS
from ungleich_ripe import ungleichRIPE

VERSION = "0.0.2"

class ungleichCLI(object):
    def __init__(self):
        self._init_parser()

        # FIXME: make it generic
        dns = ungleichDNS(self.parser, self.parser_parents)
        ripe = ungleichRIPE(self.parser, self.parser_parents)

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

    def commandline(self):
        args = self.parser['main'].parse_args()
        args.func(args)


if __name__ == '__main__':
    cli = ungleichCLI()
    cli.commandline()
