# Ungleich dns cli tool

A python package to set reverse dns in ungleich vm.

## Requirements

You need at least python 3.

## Usage

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
