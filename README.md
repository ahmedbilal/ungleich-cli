# ungleich cli

This CLI is used for day-to-day tasks used at ungleich.
It is intended to be used by ungleich engineers and skilled customers.

## Requirements / Installation

* ensure you have python3
* git clone this repo
* python ungleich-cli.py

## Usage: DNS

installing the package via pip (python3 required)

```angular2
python3 -m pip install ungleich-cli
```
after installed you can set the reverse dns by typing

```angular2
ungleich-cli dns --set-reverse <ip> --user <username> --token <token> --name mirror.example.com
```

### Usage: RIPE

Creating a new route6 object:

```
ungleichcli.py ripe-add-route6 \
    --network 2a09:2947::/32
    --description "First REST /32"
    --password "very secure"
```
