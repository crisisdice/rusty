from json import loads as decode, dumps as encode
from requests import post
import sys
from pprint import pprint

bod = """
{
  "channel":"stable",
  "mode":"debug",
  "edition":"2021",
  "crateType":"bin",
  "tests":false,
  "code": $code,
  "backtrace":false
}
"""

def main():
    url  = 'https://play.rust-lang.org/execute'
    code = encode(open(sys.argv[1]).read())
    body = bod.replace('$code', code)
    res  = decode(post(url, json=decode(body)).text)
    out  = res['stdout'] if res['success'] else res['stderr']

    pprint(out)

if __name__ == '__main__':
    main()
