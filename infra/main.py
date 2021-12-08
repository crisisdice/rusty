import sys

from json import loads as decode, dumps as encode
from requests import post

RUST_URL = 'https://play.rust-lang.org/execute'
HEADER   = {'Content-type': 'application/json'}
JSN = """
    {
      "channel": "stable",
      "mode": "debug",
      "edition": "2021",
      "crateType": "bin",
      "tests": false,
      "code": $code,
      "backtrace": false
    }
      """

def main():
    with open(sys.argv[1]) as code:
        esc = encode(code.read())
        bod = JSN.replace('$code', esc)
        req = post(
                RUST_URL,
                data=bod,
                headers=HEADER
              )
        res = decode(req.text)
        out = (
                res.get('stdout') 
                    if res.get('success') 
                    else res.get('stderr') 
                    or 'No response'
               )

        print(out)

if __name__ == '__main__':
    main()
