import os
import tools
import random
import argparse

# input args
parser = argparse.ArgumentParser()
parser.add_argument("--topic_tree_url", help="url of Khan academy topic tree", action="store", required=True)
parser.add_argument("--topic_tree_backup", help="path to backup of Khan academy topic tree", action="store", required=True)
parser.add_argument("--youtube_ids_backup", help="path to backup of youtube ids", action="store", required=True)

args = parser.parse_args()

topic_tree_url = args.topic_tree_url
topic_tree_backup = args.topic_tree_backup
youtube_ids_backup = args.youtube_ids_backup

# download topic tree if not already downloaded
if os.path.isfile(topic_tree_backup):
    topic_tree = tools.load_json(topic_tree_backup)
else:
    topic_tree = tools.download_topic_tree(topic_tree_url)
    tools.save_json(topic_tree_backup, topic_tree)

youtube_ids = tools.get_youtube_ids(topic_tree)
tools.save_dump(youtube_ids_backup, youtube_ids)
tools.save_json(youtube_ids_backup+'.json', youtube_ids)
tools.save_yaml(youtube_ids_backup+'.yaml', youtube_ids)
