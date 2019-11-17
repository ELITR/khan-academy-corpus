import os
import tools

data_path = '../10-download/data/'
video_extension = '.mp4'


with os.scandir(data_path) as it:
    for entry in it:
        if entry.name.startswith('.') or not entry.is_dir():
            continue
        root, youtube_id = os.path.split(entry.path)
        video_path = os.path.join(root, youtube_id, youtube_id + video_extension)
        if os.path.isfile(video_path):
            tools.extract_audio(video_path)
