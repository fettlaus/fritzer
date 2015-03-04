# Fritzer
[![Build Status](https://travis-ci.org/fettlaus/fritzer.svg?branch=master)](https://travis-ci.org/fettlaus/fritzer)  
Update Unblock-US with IP as reported by FritzBox

Requires Python 3

# Usage

> **Note**  
> Because `fritzconnection` is currently broken you have to install the dependency by yourself first by issuing a `pip install https://bitbucket.org/Fettlaus/fritzconnection/get/default.zip`

Just do a `pip install https://github.com/fettlaus/fritzer/archive/master.zip` and you are good to go.

# Command line arguments
```
usage: fritzer [-h] [--reset] [config]

Update IP for Unblock-US by reading from Fritzbox.

positional arguments:
  config      path to config file

optional arguments:
  -h, --help  show this help message and exit
  --reset     reset stored infos
```

# Known problems
- Currently there is a bug within the library `fritzconnection` which this script uses. I opened a [pull request](https://bitbucket.org/kbr/fritzconnection/pull-request/5/) to fix this.
- There are no test cases yet (they would fail anyway because of `fritzconnection`)
- IP adress of FritzBox is not yet usable
