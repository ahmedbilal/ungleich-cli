import argparse
import ipaddress
import json
import urllib.request
import pprint

# RIPE_URL = "https://rest.db.ripe.net/{source}/{objecttype}/{key}"
RIPE_URL = "https://rest.db.ripe.net/ripe"
RIPE_URL = "https://rest-test.db.ripe.net/test"

class ungleichRIPE(object):
    def __init__(self, parser, parents):
        self.parser = parser

        self.parser['ripe-add-route6'] = self.parser['sub'].add_parser(
            'ripe-add-route6',
            parents=[parents],
            help="Create route6 object in the ripe database")

        self.parser['ripe-add-route6'].add_argument('--network',
                                                    required=True)
        self.parser['ripe-add-route6'].add_argument('--description',
                                                    required=True)
        self.parser['ripe-add-route6'].add_argument('--password',
                                                    required=True,
                                                    help="Password for accessing the RIPE rest API")
        self.parser['ripe-add-route6'].set_defaults(func=self.route6_add)

    def route6_add(self, args):
        try:
            net = ipaddress.IPv6Network(args.network)
        except Exception as e:
            print("Sorry, {} does not look like an IPv6 network: {}".format(args.network, e))
            raise

        url = "{}/route6/?password={}".format(RIPE_URL, args.password)

        ripe_object = {}
        ripe_object['route6'] = args.network
        ripe_object['origin'] = "AS209898"
        ripe_object['descr'] = args.description
        ripe_object['mnt-by'] = "mnt-ungleich"

        ripe_attributes = [{ "name": key, "value": value } for key, value in ripe_object.items() ]

        # Format according to API layout
        ripe_element = {}
        ripe_element['objects'] = []
        ripe_element['objects'].append(
            { "object":
              [
                  {
                      "attributes": {
                          "attribute": ripe_attributes
                      }
                  }
              ]
            }
        )

        data = json.dumps(ripe_element).encode('utf-8')

        # debug
        pprint.pprint(ripe_element)

        method = 'POST'

        req = urllib.request.Request(url=url,
                                     data=data,
                                     method='POST',
                                     headers={
                                         "Content-Type": "application/json",
                                         "Accept": "application/json"
                                     })

        print("Adding a v6 route object at {} for {} with {} req={}".format(url, args.network, data, str(req)))

        with urllib.request.urlopen(req) as f:
            print(f.read().decode('utf-8'))
