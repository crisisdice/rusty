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
def internal_post():
    compiler_output, compiler_ok = compile_()

    if not compiler_ok:
        return format(compiler_output, STE)

    runtime_output, runtime_ok = run_()

    if not runtime_ok:
        return format_(runtime_output, STE)

    return format_(runtime_output, STO)

if __name__ == '__main__':
    print(internal_get())
