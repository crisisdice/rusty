from a_process import pros_

COMPILER = 'rustc'
NAME = 'test/hello'
EXT = 'rs'

"""
    compile test.rs
    ---------------
        returns:
            pros_(string[])
"""
def compile_():
    return pros_([COMPILER, f'{NAME}.{EXT}'])

"""
    run ./test
    ---------------
        returns:
            pros_(string[])
"""
def run_():
    return pros_([f'./{NAME}'])

if __name__ == '__main__':
    compile_()
    print(run_())

