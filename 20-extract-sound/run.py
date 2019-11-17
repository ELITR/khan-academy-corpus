import os
import tools

input_data_path = '../10-download/data/'
output_data_path = 'data/'
video_extension = '.mp4'

try:
    os.mkdir(output_data_path)
except FileExistsError:
    pass

with os.scandir(input_data_path) as it:
    for entry in it:
        if entry.name.startswith('.') or not entry.is_dir():
            continue
        root, youtube_id = os.path.split(entry.path)
        video_path = os.path.join(root, youtube_id, youtube_id + video_extension)
        audio_path = os.path.join(output_data_path, youtube_id, youtube_id)

        try:
            os.mkdir(os.path.join(output_data_path, youtube_id))
        except FileExistsError:
            pass

        if os.path.isfile(video_path):
            tools.extract_audio(video_path, audio_path)
