from subprocess import Popen

EMPTY = b''
PIPE = -1

def pros_(args):
    """Spawn a process."""
    process = Popen(args, stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()

    # test for errors
    status_ok = stderr == EMPTY
    output = stdout if status_ok else stderr

    # return status object
    return (output, status_ok)

def io():
    """Test echo builtin."""
    args = ['echo', 'hello world']
    process = Popen(args, stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    print(f'NO ERROR: { stderr == EMPTY }')
    return stdout

if __name__ == '__main__':
    print(io())
