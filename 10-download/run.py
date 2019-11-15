import os
import tools

topic_tree_url = 'https://www.khanacademy.org/api/v1/topictree'
topic_tree_backup = 'data/topic_tree.json'
youtube_ids_backup = 'data/youtube_ids.json'

videos_path = 'data/'
batch_size = 10
failed_youtube_ids_report = 'data/failed_youtube_ids_report.json'


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


print('Downloading video and subtitles')
all_done = False
failed_youtube_ids = {}

while not all_done:
    downloaded_youtube_ids = set(os.listdir(videos_path))

    not_yet_downloaded_youtube_ids = [youtube_id for youtube_id in youtube_ids
                                      if youtube_id not in downloaded_youtube_ids
                                      and youtube_id not in failed_youtube_ids]

    print('remaining {} out of total {}; downloading {} more'.format(
        len(not_yet_downloaded_youtube_ids), len(youtube_ids), batch_size))

    if not_yet_downloaded_youtube_ids:
        failures = tools.download_youtube_video_and_subs(not_yet_downloaded_youtube_ids[:batch_size], videos_path)
        failed_youtube_ids.update(failures)
    else:
        all_done = True

tools.save_json(failed_youtube_ids_report, failed_youtube_ids)
