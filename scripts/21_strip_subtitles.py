import pyvtt
import os
import sys
import tools
import argparse
import logging

logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')


subtitles_extension = '.vtt'
text_extension = '.txt'

# input args
parser = argparse.ArgumentParser()
parser.add_argument("--video_path", help="path to read subtitles from", action="store", required=True)
parser.add_argument("--subtitle_path", help="path to save striped subtitles to", action="store", required=True)

args = parser.parse_args()

input_subtitles_data_path = args.video_path
output_data_path = args.subtitle_path

# get youtube ids from stdin
prefixed_youtube_ids = [line.strip() for line in sys.stdin.readlines()]

processed_youtube_ids = []
failed_youtube_ids = {}

for prefixed_youtube_id in prefixed_youtube_ids:
    try:

        with os.scandir(os.path.join(input_subtitles_data_path, prefixed_youtube_id)) as it:
            for entry in it:
                if entry.name.startswith('.') or not entry.is_file():
                    continue
                _, extension = os.path.splitext(entry.name)
                if extension != subtitles_extension:
                    continue
                
                input_subtitles_path = entry.path

                root, _ = os.path.splitext(input_subtitles_path)
                output_subtitles_path = os.path.join(output_data_path, prefixed_youtube_id, os.path.basename(root) + text_extension)

                # prepare output audio dir
                try:
                    os.mkdir(os.path.join(output_data_path, prefixed_youtube_id))
                except FileExistsError:
                    pass

                subtitles = tools.subtitles2text(input_subtitles_path)

                with open(output_subtitles_path, 'w') as f:
                    f.write(subtitles)

    except Exception as e:
        logging.warning('Directory %s failed: %s', prefixed_youtube_id, str(e))
