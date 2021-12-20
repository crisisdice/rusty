import subprocess

def main():
    # TODO return stderr if not empty from rustc
    process = subprocess.Popen(['rustc', 'example.rs'],

    # TODO return stdout and stderr of executable
    #process = subprocess.Popen(['./example'],#, 'More output'],
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE)

    stdout, stderr = process.communicate()

    print(f'{stdout}, {stderr}')


if __name__ == '__main__':
    main()
