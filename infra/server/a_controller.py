from json import loads as to_dict, dumps as to_string

# pylint: disable=import-error
from a_formatter import format_
from a_rustlib import compile_, run_

STE='stderr'
STO='stdout'
NAME='temp'

"""
    GET /
    -----
    returns:
        json: '{
            "healty": boolean
        }'
"""
def internal_get():
    return '{ "healthy": true }'

"""
    POST /
    ------
    returns:
        json: '{
            "stdout" | "stderr": string
        }'
"""
def internal_post(byts):
    try:
        json = to_dict(byts.decode('utf8'))

        with open(f'{NAME}.rs', 'w') as data:
            data.write(str(json['code']))

        return rust_toolchain()

    except KeyError or ValueError as err:
        print(err)
        return False

def rust_toolchain():
    compiler_output, compiler_ok = compile_(NAME)

    if not compiler_ok:
        return format_(compiler_output, STE)

    runtime_output, runtime_ok = run_(NAME)

    if not runtime_ok:
        return format_(runtime_output, STE)

    return format_(runtime_output, STO)

if __name__ == '__main__':
    with open('./test/hello.rs') as code:
        source = to_string(code.read())
        payload = f'{{ "code": {source} }}'.encode('utf8')
        print(internal_post(payload))

    #print(internal_post(b'\x7b\x22\x63\x6f\x64\x65\x22\x3a\x22\x7b\x7d\x22\x7d'))
    #print(rust_toolchain())

