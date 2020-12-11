import os
import sys
import tools
from collections import defaultdict
import argparse
import logging

logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')

# input args
parser = argparse.ArgumentParser()
parser.add_argument("--output_path", help="path to save metadata to", action="store", required=True)
parser.add_argument("--topic_tree_backup", help="path to backup of Khan academy topic tree", action="store", required=True)

args = parser.parse_args()

output_data_path = args.output_path
topic_tree_backup = args.topic_tree_backup

topic_tree = tools.load_json(topic_tree_backup)


metadata_mask = ['author_names', 'creation_date', 'date_added', 'description', 'description_html', 'duration',
                 'image_url', 'ka_url', 'keywords', 'readable_id', 'slug', 'thumbnail_urls', 'title',
                 'translated_description', 'translated_description_html', 'translated_title', 'translated_youtube_id',
                 'translated_youtube_lang', 'youtube_id']

topic_tree_leafs = tools.get_leafs(topic_tree)

logging.info('Gathering video metadata')
video_metadata = defaultdict(list)
for leaf in topic_tree_leafs:
    video_metadata[leaf['youtube_id']].append({key: leaf[key] for key in metadata_mask})

video_metadata = dict(video_metadata)

logging.info('Creating simplified map of the topic tree')
topic_tree_map = tools.make_map(topic_tree)

logging.info('Writing common metadata files')
tools.save_json(os.path.join(output_data_path, 'video_metadata.json'), video_metadata)
tools.save_yaml(os.path.join(output_data_path, 'video_metadata.yaml'), video_metadata)
tools.save_json(os.path.join(output_data_path, 'topic_tree_map.json'), topic_tree_map)
tools.save_yaml(os.path.join(output_data_path, 'topic_tree_map.yaml'), topic_tree_map)

logging.info('Writing metadata files for individual videos')
for youtube_id in video_metadata.keys():
    try:
        prefixed_youtube_id = tools.prefix(youtube_id)

        output_path = os.path.join(output_data_path, prefixed_youtube_id, prefixed_youtube_id + '_metadata')

        # prepare output audio dir
        try:
            os.mkdir(os.path.join(output_data_path, prefixed_youtube_id))
        except FileExistsError:
            pass

        tools.save_json(output_path + '.json', video_metadata[youtube_id])
        tools.save_yaml(output_path + '.yaml', video_metadata[youtube_id])
    except Exception as e:
        logging.warning('Youtube id %s failed: %s', youtube_id, str(e))
