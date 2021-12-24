from rusty.lib.const import ESC, CONTROL

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
