# pylint: disable=import-error
from rusty.lib.const import STDOUT, STDERR
from rust import compile_, run_
from formatting import get_code_, format_

NAME='temp'

def internal_get():
    """Handles GET requests."""
    return '{ "healthy": true }'

def internal_post(byts):
    """Handles POST requests."""
    try:
        with open(f'{NAME}.rs', 'wb') as code_file:
            code_file.write(get_code_(byts))

        return rust_toolchain()

    except (ValueError, Exception) as err:
        print(err)
        return False

def rust_toolchain():
    """Compile <NAME>.rs and run NAME binary, returning output or stderr."""
    compiler_output, compiler_ok = compile_(NAME)

    if not compiler_ok:
        return format_(compiler_output, STDERR)

    runtime_output, runtime_ok = run_(NAME)

    if not runtime_ok:
        return format_(runtime_output, STDERR)

    return format_(runtime_output, STDOUT)

if __name__ == '__main__':
    with open('rusty/server/test/hello.json', 'rb') as code:
        print(internal_post(code.read()))
