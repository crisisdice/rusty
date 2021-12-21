from subprocess import Popen

EMPTY = b''
PIPE = -1

"""
    spawn a process
    ---------------
    params:
        args: string[]
    
    returns:
        (output, status_ok): (byte[], boolean)
"""
def pros_(args):
    # start and pipe process
    process = Popen(args, stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()

    # test for errors
    status_ok = stderr == EMPTY
    output = stdout if status_ok else stderr

    # return status object
    return (output, status_ok)

"""
    tests gnu/echo
    --------------
    returns:
        stdout: bytes[]

"""
def io():
    args = ['echo', 'hello world']
    process = Popen(args, stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    print(f'NO ERROR: { stderr == EMPTY }')
    return stdout

if __name__ == '__main__':
    print(io())
