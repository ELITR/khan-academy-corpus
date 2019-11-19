import os
import tools

youtube_ids_to_process = '../20-extract-sound/data/youtube_ids.json'
youtube_ids_processed_report = 'data/youtube_ids.json'
input_data_path = '../20-extract-sound/data/'
input_subtitles_data_path = '../10-download/data/'

output_data_path = 'data/'
audio_extension = '.mp3'
subtitles_extension = '.vtt'
text_extension = '.txt'


try:
    os.mkdir(output_data_path)
except FileExistsError:
    pass

youtube_ids = tools.load_json(youtube_ids_to_process)
processed_youtube_ids = []

for youtube_id in youtube_ids:
    print(youtube_id)
    input_audio_path = os.path.join(input_data_path, youtube_id, youtube_id + audio_extension)
    output_audio_path_template = os.path.join(output_data_path, youtube_id,
                                              youtube_id + '_{:010.0f}_{:010.0f}' + audio_extension)

    input_subtitles_path = os.path.join(input_subtitles_data_path, youtube_id, youtube_id + '.en' + subtitles_extension)

    output_text_path_template = os.path.join(output_data_path, youtube_id,
                                             youtube_id + '_{:010.0f}_{:010.0f}' + text_extension)

    if not os.path.isfile(input_audio_path):
        continue

    # prepare output audio dir
    try:
        os.mkdir(os.path.join(output_data_path, youtube_id))
    except FileExistsError:
        pass

    batched_subtitles = tools.subtitles2timestamps(input_subtitles_path)

    tools.split_audio_and_text(
        input_audio_path, output_audio_path_template, output_text_path_template, batched_subtitles)

    processed_youtube_ids.append(youtube_id)

tools.save_json(youtube_ids_processed_report, processed_youtube_ids)
