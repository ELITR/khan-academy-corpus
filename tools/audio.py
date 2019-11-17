import ffmpeg
import os


def extract_audio(input_path, audio_extension='mp3', force_output=False):
    root, extension = os.path.splitext(input_path)
    audio_path = '{}.{}'.format(root, audio_extension)

    # check if audio already exists
    if force_output or not os.path.isfile(audio_path):
        video = ffmpeg.input(input_path)
        out = ffmpeg.output(video, audio_path)
        out.overwrite_output().run()
