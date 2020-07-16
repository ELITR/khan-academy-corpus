import os
import tools
from collections import Counter
from itertools import chain
import argparse
import logging

logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')

# input args
parser = argparse.ArgumentParser()
parser.add_argument("--output_path", help="path to save metadata to", action="store", required=True)
parser.add_argument("--video_metadata_path", help="path to video metadata", action="store", required=True)

args = parser.parse_args()

output_data_path = args.output_path
video_metadata_path = args.video_metadata_path


video_metadata = tools.load_json(video_metadata_path)

authors_distribution = Counter(chain.from_iterable(map(lambda x: x["author_names"],
                                                       chain.from_iterable(video_metadata.values())))).most_common()

duration_distribution = Counter(map(lambda x: x["duration"],
                                    chain.from_iterable(video_metadata.values()))).most_common()

youtube_id_distribution = Counter(map(lambda x: x["youtube_id"],
                                      chain.from_iterable(video_metadata.values()))).most_common()

keywords_distribution = Counter(chain.from_iterable(map(lambda x: x["keywords"].split(','),
                                                        chain.from_iterable(video_metadata.values())))).most_common()


tools.save_json(os.path.join(output_data_path, 'authors_distribution.json'), authors_distribution)
tools.save_yaml(os.path.join(output_data_path, 'authors_distribution.yaml'), authors_distribution)
tools.save_json(os.path.join(output_data_path, 'duration_distribution.json'), duration_distribution)
tools.save_yaml(os.path.join(output_data_path, 'duration_distribution.yaml'), duration_distribution)
tools.save_json(os.path.join(output_data_path, 'youtube_id_distribution.json'), youtube_id_distribution)
tools.save_yaml(os.path.join(output_data_path, 'youtube_id_distribution.yaml'), youtube_id_distribution)
tools.save_json(os.path.join(output_data_path, 'keywords_distribution.json'), keywords_distribution)
tools.save_yaml(os.path.join(output_data_path, 'keywords_distribution.yaml'), keywords_distribution)
