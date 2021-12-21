from a_process import pros_

COMPILER = 'rustc'
DIR = 'test/'
EXT = 'rs'
OUT = f'--out-dir={DIR}'

"""
    compile test.rs
    ---------------
        returns:
            pros_(string[])
"""
def compile_(name):
    return pros_([COMPILER, f'{DIR}{name}.{EXT}', OUT])

"""
    run ./test
    ---------------
        returns:
            pros_(string[])
"""
def run_(name):
    return pros_([f'./{DIR}{name}'])

if __name__ == '__main__':
    compile_('hello')
    print(run_('hello'))

