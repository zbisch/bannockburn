import os, json

def get_pomos(user=None):
    return get_pomos_from_file(user)


def get_pomos_from_file(user=None):
    contents = open(os.path.join("app/data/", user), "r").read()
    return json.loads(contents)
