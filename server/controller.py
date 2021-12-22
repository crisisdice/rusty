# pylint: disable=import-error
from const import STDOUT, STDERR
from rustlib import compile_, run_
from bytelib import get_code_, format_

NAME='temp'

def internal_get():
    """Handles GET requests."""
    return '{ "healthy": true }'

def internal_post(byts):
    """Handles POST requests."""
    try:
        with open(f'{NAME}.rs', 'wb') as data:
            data.write(get_code_(byts))

        return rust_toolchain()

    except (ValueError, Exception) as err:
        print(err)
        return False

"""
    returns:
        json: '{
            "stdout" | "stderr": string
        }'
"""
def rust_toolchain():
    compiler_output, compiler_ok = compile_(NAME)

    if not compiler_ok:
        return format_(compiler_output, STDERR)

    runtime_output, runtime_ok = run_(NAME)

    if not runtime_ok:
        return format_(runtime_output, STDERR)

    return format_(runtime_output, STDOUT)

if __name__ == '__main__':
    with open('./test/hello.json', 'rb') as code:
        print(internal_post(code.read()))
