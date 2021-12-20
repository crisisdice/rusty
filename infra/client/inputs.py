import sys

from json import loads as decode

def get_config(path):
    with open(path) as config:
        return decode(config.read())

def parse_args():
    path = '../infra/client/config.json'

    if '--config' in sys.argv:
        # What is config, and what is arguments?
        #set config file to path
        pass    

    return (sys.argv[1], path)
