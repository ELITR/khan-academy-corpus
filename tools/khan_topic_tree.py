import ujson
import requests


def download_topic_tree(url):
    return ujson.loads(requests.get(url).text)


def save_json(path, value):
    with open(path, 'w') as f:
        f.write(ujson.dumps(value))


def load_json(path):
    with open(path, 'r') as f:
        return ujson.loads(f.read())


def make_map(topic_tree):
    def get_children(parent):
        if 'children' in parent:
            return parent['title'], {child_title: child_children for child_title, child_children
                                     in map(get_children, parent['children'])}
        else:
            return parent['title'], parent

    title, tree = get_children(topic_tree)
    return {title: tree}


def get_leafs(topic_tree):
    """
    recursively walks the entire tree and returns all the leafs which are videos
    """
    leafs = []

    def get_children(parent):
        if 'children' in parent:
            any(get_children(child) for child in parent['children'])
        else:
            leafs.append(parent)

    get_children(topic_tree)
    return leafs


def get_youtube_ids(topic_tree):
    leafs = get_leafs(topic_tree)
    return {leaf['youtube_id'] for leaf in leafs}
