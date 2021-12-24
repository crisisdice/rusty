from json import loads as to_dict
from requests import post

# pylint: disable=import-error
from inputs import parse_args, get_config

def parse_rust(res):
    json = to_dict(res)
    return json.get('stdout') or json.get('stderr') or json

def main():
    # setup
    path, config_file = parse_args()
    config = get_config(config_file)

    with open(path) as data:
        # send
        response = post(config['url'], json={"code": data.read()}).text

        # interpret
        print(parse_rust(response))

if __name__ == '__main__':
    main()
