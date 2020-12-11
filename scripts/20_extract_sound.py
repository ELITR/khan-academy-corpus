import os
import sys
import tools
import argparse

video_extension = '.mp4'
audio_extension = '.aac'

# input args
parser = argparse.ArgumentParser()
parser.add_argument("--video_path", help="path to read videos from", action="store", required=True)
parser.add_argument("--audio_path", help="path to save audio to", action="store", required=True)

args = parser.parse_args()

input_data_path = args.video_path
output_data_path = args.audio_path

# get youtube ids from stdin
prefixed_youtube_ids = [line.strip() for line in sys.stdin.readlines()]

for prefixed_youtube_id in prefixed_youtube_ids:
    video_path = os.path.join(input_data_path, prefixed_youtube_id, prefixed_youtube_id + video_extension)
    audio_path = os.path.join(output_data_path, prefixed_youtube_id, prefixed_youtube_id + audio_extension)
    if not os.path.isfile(video_path):
        continue

    # prepare audio dir
    try:
        os.mkdir(os.path.join(output_data_path, prefixed_youtube_id))
    except FileExistsError:
        pass

    tools.extract_audio(video_path, audio_path)
