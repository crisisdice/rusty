from json import loads as decode

def parse_rust(res):
    json = decode(res)
    return (json.get('stdout') if json.get('success') 
        else json.get('stderr') or 'No jsonponse')
