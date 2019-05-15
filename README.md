# ungleich cli

This CLI is used for day-to-day tasks used at ungleich.
It is intended to be used by ungleich engineers and skilled customers.

## Requirements / Installation

* ensure you have python3
* git clone this repo

## Usage general

```
ungleich --help
```

## Usage: DNS

```
ungleich dns --set-reverse <ip> --user <username> --token <token> --realm <realm> --email <email> --name mirror.example.com
```

### Usage: RIPE

Creating a new route6 object:

```
ungleich ripe-add-route6 \
    --network 2a09:2947::/32
    --description "First REST /32"
    --password "very secure"
```
