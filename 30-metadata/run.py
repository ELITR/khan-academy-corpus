import os
import tools
from collections import defaultdict, Counter

youtube_ids_to_process = '../21-strip-subtitles/data/youtube_ids.json'
youtube_ids_processed_report = 'data/youtube_ids.json'
topic_tree_backup = '../10-download/data/topic_tree.json'

output_data_path = 'data/'
failed_youtube_ids_report = 'data/failed_youtube_ids_report_metadata.json'

failed_youtube_ids = {}
processed_youtube_ids = []

youtube_ids = tools.load_json(topic_tree_backup)
topic_tree = tools.load_json(topic_tree_backup)


metadata_mask = ['author_names', 'creation_date', 'date_added', 'description', 'description_html', 'duration',
                 'image_url', 'ka_url', 'keywords', 'readable_id', 'slug', 'thumbnail_urls', 'title',
                 'translated_description', 'translated_description_html', 'translated_title', 'translated_youtube_id',
                 'translated_youtube_lang', 'youtube_id']

topic_tree_leafs = tools.get_leafs(topic_tree)

print('video metadata')
video_metadata = defaultdict(list)
for leaf in topic_tree_leafs:
    video_metadata[leaf['youtube_id']].append({key: leaf[key] for key in metadata_mask})

video_metadata = dict(video_metadata)

print('make map')
topic_tree_map = tools.make_map(topic_tree)

print('output')
tools.save_json(os.path.join(output_data_path, 'video_metadata.json'), video_metadata)
tools.save_yaml(os.path.join(output_data_path, 'video_metadata.yaml'), video_metadata)
tools.save_json(os.path.join(output_data_path, 'topic_tree_map.json'), topic_tree_map)
tools.save_yaml(os.path.join(output_data_path, 'topic_tree_map.yaml'), topic_tree_map)

print('individual videos')
for youtube_id in youtube_ids:
    print(youtube_id)
    try:
        prefix_youtube_id = tools.prefix(youtube_id)

        output_path = os.path.join(output_data_path, prefix_youtube_id, prefix_youtube_id + '_metadata')

        # prepare output audio dir
        try:
            os.mkdir(os.path.join(output_data_path, prefix_youtube_id))
        except FileExistsError:
            pass

        tools.save_json(output_path + '.json', video_metadata[youtube_id])
        tools.save_yaml(output_path + '.yaml', video_metadata[youtube_id])
    except Exception as e:
        print('failed')
        failed_youtube_ids[youtube_id] = str(e)
    else:
        processed_youtube_ids.append(youtube_id)


tools.save_json(youtube_ids_processed_report, processed_youtube_ids)
tools.save_json(failed_youtube_ids_report, failed_youtube_ids)
