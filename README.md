# ungleich cli

This CLI is used for day-to-day tasks used at ungleich.
It is intended to be used by ungleich engineers and skilled customers.

## Requirements / Installation

* ensure you have python3
* git clone this repo
* cd into this repo
* run the following command
```
sudo pip3 install -r requirements.txt
```

## Usage general

```
ungleich --help
```
## Usage: Weather

```
ungleich weather
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

### Usage: Account

Creating a new account object:

```
ungleich account --create-user <username> --name <firstname> --lastname <lastname> --email <email>

```
