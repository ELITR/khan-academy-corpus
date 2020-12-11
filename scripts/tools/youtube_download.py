import os
import youtube_dl

# https://willdrevo.com/downloading-youtube-and-soundcloud-audio-with-python-and-pandas

# one liner:
# python -c 'from tools import download_youtube_video_and_subs; download_youtube_video_and_subs(["youtube_id"])'


def download_youtube_video_and_subs(youtube_ids, directory='', prefix='kac'):
    options = {
        'simulate': False,
        'ignoreerrors': False,
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': os.path.join(directory, prefix + '%(id)s', prefix + '%(id)s'),  # name the file the ID of the video
        'noplaylist': True,  # only download video, not playlist
        'allsubtitles': True,  # download all subtitles
        'writesubtitles': True,
        'writeautomaticsub': False, # avoid automatic subtitles
        'skip_download': False, # avoid even the video (so do just subtitles)
    }

    failures = {}

    with youtube_dl.YoutubeDL(options) as ydl:
        for youtube_id in youtube_ids:
            print(options["outtmpl"])
            outdir = options["outtmpl"]
            outdir = os.path.dirname(outdir.replace("%(id)s", youtube_id))
            try:
                ydl.download(['http://www.youtube.com/watch?v={}'.format(youtube_id)])
            except Exception as e:
                print('Exception: {}'.format(e))
                failures[youtube_id] = str(e)

    return failures
