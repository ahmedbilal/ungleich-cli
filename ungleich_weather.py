import argparse
import requests
import json
from apixu.client import ApixuClient


def get_loc():
    response = requests.get('http://ip-api.com/json/')
    data = json.loads(response.content)

    return data['city'], data['countryCode']


class ungleichWeather(object):
    def __init__(self, parser, parents):
        self.parser = parser

        self.parser['weather'] = self.parser['sub'].add_parser(
            'weather',
            help="Weather Enquiries",
            parents=[parents])
        self.parser['weather'].set_defaults(func=ungleichWeather.forecast_weather)

    def forecast_weather(args):
        _city, _country_code = get_loc()

        client = ApixuClient("cc33a1e3237a4b78b3174104190206")

        forecast = client.forecast(q=f'{ _city},{_country_code}', days=7)
        print(f"{'Date':^12}|{'Min Temp':^10}|{'Max Temp':^10}|{'Condition':^15}")
        print(f"{'*'*47:^47}")
        for day in forecast['forecast']['forecastday']:
            print(f"{day['date']:^12}|{day['day']['mintemp_c']:^10}|{day['day']['maxtemp_c']:^10}|{day['day']['condition']['text']:^15}")