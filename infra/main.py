from json import loads as decode, dumps as encode
from requests import post

import sys

jsn = """
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
    url  = 'https://play.rust-lang.org/execute'
    code = encode(open(sys.argv[1]).read())
    body = jsn.replace('$code', code)
    res  = decode(post(url, json=decode(body)).text)
    out  = res.get('stdout') if res.get('success') else res.get('stderr') or 'No response'

    print(out)

if __name__ == '__main__':
    main()
