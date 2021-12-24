STDOUT = 'stdout'
STDERR = 'stderr'
CONTROL = b'\x5c' # \
ESC = {
    b'\x08' : b'\x5c\x62', # BACKSPACE \b
    b'\x0c' : b'\x5c\x66', # FORM_FEED \f
    b'\x0a' : b'\x5c\x6e', # NEW_LINE  \n
    b'\x0d' : b'\x5c\x72', # CARRIAGE  \r
    b'\x09' : b'\x5c\x74', # TAB       \t
    b'\x22' : b'\x5c\x22', # DOUBLE_QT \"
    b'\x2f' : b'\x5c\x2f'  # BACKSLASH \/
}
