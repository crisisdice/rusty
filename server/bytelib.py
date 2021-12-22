# pylint: disable=import-error
from const import STDOUT, STDERR

ESC = {
    b'\x08' : b'\x5c\x62', # BACKSPACE
    b'\x0c' : b'\x5c\x66', # FORM_FEED
    b'\x0a' : b'\x5c\x6e', # NEW_LINE 
    b'\x0d' : b'\x5c\x72', # CARRIAGE 
    b'\x09' : b'\x5c\x74', # TAB      
    b'\x22' : b'\x5c\x22', # DOUBLE_QT
    b'\x2f' : b'\x5c\x2f'  # BACKSLASH
}

def get_code_(byts):
    clean = lambda b: b.strip()[1:-1]
    kvp = [ clean(byt) for byt in clean(byts).split(b':')]

    if kvp[0] != b'code':
        raise ValueError('Code element not found.')

    return kvp[1]

def concatenate_bytes_(byte_array):
    return b''.join(byte_array)

def escape_(byts):
    """Escape JSON special chars in bytes."""
    # TODO iterate over bytes or convert tables to int
    escaped_byts = [ESC[char] if char in ESC else char for char in [byts[i:i+1] for i in range(len(byts))]]
    return concatenate_bytes_(escaped_byts)

def format_(byts, tty=None):
    """Insert bytes into JSON byte template.
    
    Keyword arguments:
        byts -- unescaped json bytes
        tty -- 'stdout' or 'stderr'
    """
    if tty not in [STDOUT, STDERR]:
        raise ValueError('tty should be stdout or stderr')

    encoded_tty = b'err' if tty == STDERR else b'out'

    return concatenate_bytes_([b'{ "std', encoded_tty, b'" : "', escape_(byts), b'" }'])

if __name__ == '__main__':
    p_string = lambda b: print(b.decode('utf8'))
    p_string(format_(b'good', 'stdout'))
    p_string(format_(b'bad', 'stderr'))
    p_string(format_(b'\x61\x0a\x0a\x61', 'stdout'))

