# Fritzer
Update Unblock-US with IP reported by FritzBox

Requires Python 3

# Usage
Just do a `pip install https://github.com/fettlaus/fritzer/archive/master.zip` and you are good to go.

# Command line arguments
```
  usage: fritzer [-h] [--config CONFIG] [--reset]
  
  Update IP for Unblock-US by reading from Fritzbox.
  
  optional arguments:
    -h, --help       show this help message and exit
    --config CONFIG  path to config file
    --reset          reset stored infos
```

# Known problems
Currently there is a bug within the library `fritzconnection` which this script uses. I opened a [pull request](https://bitbucket.org/kbr/fritzconnection/pull-request/5/) to fix this.
