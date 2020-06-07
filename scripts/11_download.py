import sys
import tools
import argparse

# input args
parser = argparse.ArgumentParser()
parser.add_argument("--videos_path", help="path to save videos to", action="store", required=True)

args = parser.parse_args()

videos_path = args.videos_path

# get youtube ids from stdin
youtube_ids = [line.strip() for line in sys.stdin.readlines()]

# download videos
failures = tools.download_youtube_video_and_subs(youtube_ids, videos_path)
