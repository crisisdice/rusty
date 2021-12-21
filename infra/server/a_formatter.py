from json import dumps as to_string

"""
    format bytes to JSON
    --------------------
    params:
        byts: byte[]
        tty: 'stdout' or 'stderr'

    returns: 
        json: '{
            "stdout" | "stderr": boolean
        }' | '{}'
"""
def format_(byts, tty=None):
    return ('{}' if (tty != 'stdout' and tty != 'stderr') else
        f'{{ "{tty}": {to_string(byts.decode("utf8"))} }}'.encode('utf8')
    )

if __name__ == '__main__':
    print(format_(b'\x61\x73\x73', 'stdout'))
    print(format_(b'\x62\x61\x6c\x6c\x73', 'stderr'))

