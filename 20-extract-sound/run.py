import os
import tools

youtube_ids_to_process = '../10-download/data/youtube_ids.json'
youtube_ids_processed_report = 'data/youtube_ids.json'
input_data_path = '../10-download/data/'
output_data_path = 'data/'
video_extension = '.mp4'
audio_extension = '.aac'

try:
    os.mkdir(output_data_path)
except FileExistsError:
    pass

youtube_ids = tools.load_json(youtube_ids_to_process)
processed_youtube_ids = []

for youtube_id in youtube_ids:
    prefix_youtube_id = tools.prefix(youtube_id)

    video_path = os.path.join(input_data_path, prefix_youtube_id, prefix_youtube_id + video_extension)
    audio_path = os.path.join(output_data_path, prefix_youtube_id, prefix_youtube_id + audio_extension)
    if not os.path.isfile(video_path):
        continue

    # prepare audio dir
    try:
        os.mkdir(os.path.join(output_data_path, prefix_youtube_id))
    except FileExistsError:
        pass

    tools.extract_audio(video_path, audio_path)
    processed_youtube_ids.append(youtube_id)
    
tools.save_json(youtube_ids_processed_report, processed_youtube_ids)
