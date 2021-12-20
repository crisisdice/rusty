from json import loads as decode

def parse_rust_external(res):
    json = decode(res)
    return (json.get('stdout') if json.get('success') 
        else json.get('stderr') or 'No Response')

def parse_rust(res):
    json = decode(res)
    return json.get('stdout') or json.get('stderr')
