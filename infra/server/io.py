from subprocess import Popen, PIPE

"""
"""
def internal():
    # TODO return stderr if not empty from rustc
    # TODO return stdout and stderr of executable
    process = Popen(['rustc', 'example.rs'],
    #process = subprocess.Popen(['./example'],#, 'More output'],
                stdout=PIPE, 
                stderr=PIPE)

    stdout, stderr = process.communicate()
    return stdout

def fun_with_bytes():
    #bts = b'\x61\x6c\x65\x78'
    process = Popen(['echo', 'hello world'],
                stdout=PIPE, 
                stderr=PIPE)
    stdout, stderr = process.communicate()
    #print(f'{stdout}, {stderr}')
    return stdout

if __name__ == '__main__':
    internal()
