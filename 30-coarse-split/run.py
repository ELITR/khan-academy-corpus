import os
import tools

input_audio_path = '../20-extract-sound/data/'
input_subtitles_path = '../10-download/data/'

output_data_path = 'data/'
audio_extension = '.mp3'

try:
    os.mkdir(output_data_path)
except FileExistsError:
    pass


with os.scandir(input_audio_path) as it:
    for entry in it:
        if entry.name.startswith('.') or not entry.is_dir():
            continue

        root, youtube_id = os.path.split(entry.path)

        output_audio_path = os.path.join(output_data_path, youtube_id, youtube_id)

        try:
            os.mkdir(os.path.join(output_data_path, youtube_id))
        except FileExistsError:
            pass

        # TODO: read subtitles for timestamps

        audio_path = os.path.join(root, youtube_id, youtube_id + audio_extension)
        if os.path.isfile(audio_path):
            tools.split_audio(audio_path, output_audio_path, [(1, 2), (10, 20)])

