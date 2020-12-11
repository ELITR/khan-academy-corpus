import requests
import ujson


def download_topic_tree(url):
    return ujson.loads(requests.get(url).text)


def make_map(topic_tree):
    def get_children(parent):
        if 'children' in parent:
            return parent['title'], {child_title: child_children for child_title, child_children
                                     in map(get_children, parent['children'])}
        else:
            return parent['title'], parent['youtube_id']

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
