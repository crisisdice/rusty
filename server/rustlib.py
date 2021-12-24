# pylint: disable=import-error
from process import pros_

COMPILER = 'rustc'
EXT = 'rs'

def compile_(name):
    """Compile a txt file or return stderr."""
    return pros_([COMPILER, f'{name}.{EXT}'])

def run_(name):
    """Run binary."""
    return pros_([f'./{name}'])

if __name__ == '__main__':
    compile_('test/hello')
    print(run_('hello'))

