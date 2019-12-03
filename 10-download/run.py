#!/usr/bin/env python3

import os
import tools
import random

topic_tree_url = 'https://www.khanacademy.org/api/v1/topictree'
topic_tree_backup = 'data/topic_tree.json'
youtube_ids_backup = 'data/youtube_ids.json'

videos_path = 'data/'
batch_size = 10


print('List of YouTube ids')
# get list of youtube ids to download
if os.path.isfile(youtube_ids_backup):
    print('\t reading backup {}'.format(youtube_ids_backup))
    youtube_ids = tools.load_json(youtube_ids_backup)
else:
    # download topic tree if not already downloaded
    print('\t getting from topic tree')
    if os.path.isfile(topic_tree_backup):
        print('\t\t reading topic tree backup {}'.format(topic_tree_backup))
        topic_tree = tools.load_json(topic_tree_backup)
    else:
        print('\t\t getting topic tree from {}'.format(topic_tree_url))
        topic_tree = tools.download_topic_tree(topic_tree_url)
        tools.save_json(topic_tree_backup, topic_tree)

    youtube_ids = tools.get_youtube_ids(topic_tree)
    tools.save_json(youtube_ids_backup, youtube_ids)


print('Downloading video and subtitles in random order; can be run concurrently')
random.shuffle(youtube_ids)
failures = tools.download_youtube_video_and_subs(youtube_ids, videos_path)
