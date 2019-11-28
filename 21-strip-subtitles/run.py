import pyvtt
import os
import tools

youtube_ids_to_process = '../20-extract-sound/data/youtube_ids.json'
youtube_ids_processed_report = 'data/youtube_ids.json'
input_subtitles_data_path = '../10-download/data/'

output_data_path = 'data/'
subtitles_extension = '.vtt'
text_extension = '.txt'

failed_youtube_ids_report = 'data/failed_youtube_ids_report_sub2test.json'

try:
    os.mkdir(output_data_path)
except FileExistsError:
    pass

youtube_ids = tools.load_json(youtube_ids_to_process)
processed_youtube_ids = []
failed_youtube_ids = {}

for youtube_id in youtube_ids:
    print(youtube_id)
    try:

        with os.scandir(os.path.join(input_subtitles_data_path, youtube_id)) as it:
            for entry in it:
                if entry.name.startswith('.') or not entry.is_file():
                    continue
                _, extension = os.path.splitext(entry.name)
                if extension != subtitles_extension:
                    continue

                prefix_youtube_id = tools.prefix(youtube_id)
                
                input_subtitles_path = entry.path

                root, _ = os.path.splitext(input_subtitles_path)
                output_subtitles_path = os.path.join(output_data_path, prefix_youtube_id, os.path.basename(root) + text_extension)

                # prepare output audio dir
                try:
                    os.mkdir(os.path.join(output_data_path, prefix_youtube_id))
                except FileExistsError:
                    pass

                subtitles = tools.subtitles2text(input_subtitles_path)

                with open(output_subtitles_path, 'w') as f:
                    f.write(subtitles)

    except Exception as e:
        print('failed')
        failed_youtube_ids[youtube_id] = str(e)
    else:
        processed_youtube_ids.append(youtube_id)

tools.save_json(youtube_ids_processed_report, processed_youtube_ids)
tools.save_json(failed_youtube_ids_report, failed_youtube_ids)
