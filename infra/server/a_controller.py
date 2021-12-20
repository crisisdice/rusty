from json import loads as to_dict

# pylint: disable=import-error
from a_formatter import format_
from a_rustlib import compile_, run_

STE='stderr'
STO='stdout'

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
    json = to_json(byts)
    return json 

def to_json(data):
    return to_dict(data.decode('utf8'))

def rust_toolchain():
    compiler_output, compiler_ok = compile_()

    if not compiler_ok:
        return format(compiler_output, STE)

    runtime_output, runtime_ok = run_()

    if not runtime_ok:
        return format_(runtime_output, STE)

    return format_(runtime_output, STO)

if __name__ == '__main__':
    print(internal_post(b'\x7b\x22\x61\x22\x3a\x30\x7d'))
    print(rust_toolchain())

