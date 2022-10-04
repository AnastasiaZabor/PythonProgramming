import json

def serialize(content):
    return json.dumps(content, default=lambda o: o.__dict__, sort_keys=True, indent=4)

def deserialize(content):
    return json.loads(content)


