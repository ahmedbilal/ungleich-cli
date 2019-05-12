import argparse

class ungleichRIPE(object):
    def __init__(self, parser, parents):
        self.parser = parser

        self.parser['ripe-route6'] = self.parser['sub'].add_parser(
            'ripe-route6',
            parents=[parents],
            help="Create route6 object in the ripe database")

        self.parser['ripe-route6'].add_argument('--network', required=True)
        self.parser['ripe-route6'].set_defaults(func=self.route6)

    def route6(self, args):
        print("Adding a v6 route object at RIPE for {}".format(args.network))
