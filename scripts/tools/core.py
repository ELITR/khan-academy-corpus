import ujson
import yaml


def save_json(path, value):
    with open(path, 'w') as f:
        f.write(ujson.dumps(value))


def load_json(path):
    with open(path, 'r') as f:
        return ujson.loads(f.read())


def save_yaml(path, value):
    with open(path, 'w') as f:
        f.write(yaml.safe_dump(value, default_flow_style=False))


def load_yaml(path):
    with open(path, 'r') as f:
        return yaml.load(f.read())


def save_dump(path, value):
    with open(path, 'w') as f:
        try:
            for item in value:
                f.write(str(item) + '\n')
        except TypeError:
            f.write(str(value))


def prefix(string, prefix='kac'):
    return prefix + string