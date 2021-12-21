from a_process import pros_

COMPILER = 'rustc'
EXT = 'rs'

"""
    params:
        name: string

    returns:
        pros_(string[])
"""
def compile_(name):
    return pros_([COMPILER, f'{name}.{EXT}'])

"""
    params:
        name: string

    returns:
        pros_(string[])
"""
def run_(name):
    return pros_([f'./{name}'])

if __name__ == '__main__':
    compile_('test/hello')
    print(run_('hello'))

