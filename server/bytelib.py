# pylint: disable=import-error
from const import STDOUT, STDERR, ESC, CONTROL

def get_code_(byts):
    """Return 'code' JSON element."""
    return unescape_(get_(byts, b'code'))

def get_(byts, node):
    """Return JSON element 'node'."""
    search_after = byts.index(node) + len(node) + 1
    bytelist = to_list_(byts[search_after:])
    end_quote = False
    start_index = 0
    end_index = 0
    
    for index, byte in enumerate(bytelist):
        non_escape_quote = byte == b'"' and bytelist[index-1] != CONTROL

        if non_escape_quote and end_quote:
            end_index = index
            break
        if non_escape_quote:
            start_index = index + 1
            end_quote = True
    return concatenate_bytes_(bytelist[start_index:end_index])

def to_list_(byts):
    return [byts[i:i+1] for i in range(len(byts))]

def concatenate_bytes_(byte_array):
    """Concatenate a list of bytes."""
    return b''.join(byte_array)

def unescape_(byts):
    """Simultaneously convert escapes to UTF-8 characters."""
    reverse_escape = {ESC[node]: node for node in ESC}
    bytelist = to_list_(byts)

    for index, byte in enumerate(bytelist):
        if index == len(bytelist) - 1:
            break
        if byte == CONTROL:
            joined = CONTROL + bytelist[index+1]
            if joined in reverse_escape:
                bytelist[index] = None
                bytelist[index+1] = reverse_escape[joined]

    return concatenate_bytes_([byte for byte in bytelist if byte is not None])

def escape_(byts):
    """Escape JSON special chars in bytes."""
    return concatenate_bytes_([ESC[char] if char in ESC else char for char in to_list_(byts)])

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
    with open('./test/hello.rs', 'rb') as code:
        p_string = lambda step, b: print(f'{step}: {b.decode("utf8")}')
        escaped   = escape_(code.read())
        p_string('escaped', escaped)
        json      = format_(escaped, 'stdout')
        p_string('json', json)
        text      = get_(json, b'stdout')
        p_string('text', text)
        unescaped = unescape_(text)
        p_string('unescaped', unescaped)

