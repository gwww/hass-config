import re

def svg(filename):
    with open(filename, 'r') as file:
        data = file.read()
    return re.sub(r"\n\s*", " ", data)
