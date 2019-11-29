import os
import tools
from collections import Counter
from itertools import chain

video_metadata_path = '../30-metadata/data/video_metadata.json'
output_data_path = 'data/'


try:
    os.mkdir(output_data_path)
except FileExistsError:
    pass


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
