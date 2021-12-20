from requests import post

from rust import parse_rust
from inputs import parse_args, get_config

def main():
    # setup
    path, config_file = parse_args()
    config = get_config(config_file)
    template = config['template']

    with open(path) as data:
        # format
        template['code'] = data.read()

        # send
        response = post(config['url'], json=template).text

        # interpret
        print(parse_rust(response))

if __name__ == '__main__':
    main()
