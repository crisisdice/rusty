# pylint: disable=import-error
from rusty.lib.const import STDOUT, STDERR
from rusty.lib.json import escape_, unescape_, get_, concatenate_bytes_

def get_code_(byts):
    """Return 'code' JSON element."""
    return unescape_(get_(byts, b'code'))

def format_(byts, tty=None):
    """Insert bytes into JSON byte template.
    
    Keyword arguments:
        byts -- unescaped bytes
        tty -- 'stdout' or 'stderr'
    """
    if tty not in [STDOUT, STDERR]:
        raise ValueError('tty should be stdout or stderr')

    encoded_tty = b'err' if tty == STDERR else b'out'

    return concatenate_bytes_([b'{ "std', encoded_tty, b'" : "', escape_(byts), b'" }'])

if __name__ == '__main__':
    with open('rusty/server/test/hello.rs', 'rb') as code:
        p_string = lambda step, b: print(f'{step}: {b.decode("utf8")}')
        escaped   = escape_(code.read())
        p_string('escaped', escaped)
        json      = format_(escaped, 'stdout')
        p_string('json', json)
        text      = get_(json, b'stdout')
        p_string('text', text)
        unescaped = unescape_(text)
        p_string('unescaped', unescaped)

