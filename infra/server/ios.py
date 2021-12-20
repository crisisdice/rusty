from subprocess import Popen, PIPE

# TODO put stuff up to doc string in modules
EMPTY = b''
COMPILER = 'rustc'
NAME = 'temp'
EXT = '.rs'

def format_err(err):
    return f'{{ "stderr": {err.decode("utf8")} }}'

def format_out(out):
    return f'{{ "stdout": {out.decode("utf8")} }}'

"""
"""
def internal():
    compiler_output, compiler_ok = compile_()

    if not compiler_ok:
        return format_err(compiler_output)

    runtime_output, runtime_ok = run_()

    if not runtime_ok:
        return format_err(runtime_output)

    return format_out(runtime_output)

"""
    return stdout and stderr of executable
"""
def pros_(args):
    process = Popen(args, stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    status_ok = stderr == EMPTY
    byte_output = stdout if status_ok else stderr
    return (byte_output, status_ok)

def run_():
    return pros_([f'./{NAME}'])

def compile_():
    form = lambda name, extension : f'{name}.{extension}'
    path = form(NAME, EXT)
    return pros_([COMPILER, path])

def io():
    process = Popen(['echo', 'hello world'],
                stdout=PIPE, 
                stderr=PIPE)
    stdout, stderr = process.communicate()
    print(f'NO ERROR: { stderr == EMPTY }')
    return stdout

if __name__ == '__main__':
    print(io())
