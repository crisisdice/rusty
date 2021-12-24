from requests import post

# pylint: disable=import-error
from inputs import parse_args, get_config
from rusty.lib.json import get_, unescape_
from rusty.lib.const import STDOUT, STDERR

def parse_rust(res):
    return unescape_((get_(res, STDOUT.encode())) or get_(res, STDERR.encode()) or res).decode()

def main():
    # setup
    path, config_file = parse_args()
    config = get_config(config_file)

    with open(path) as data:
        # send
        response = post(config['url'], json={"code": data.read()}).content

        # interpret
        print(parse_rust(response))

if __name__ == '__main__':
    main()
