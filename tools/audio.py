import ffmpeg
import os


def extract_audio(input_path, audio_path, audio_extension='mp3', force_output=False):
    audio_path = '{}.{}'.format(audio_path, audio_extension)

    # check if audio already exists
    if force_output or not os.path.isfile(audio_path):
        video = ffmpeg.input(input_path)
        out = ffmpeg.output(video, audio_path)
        out.overwrite_output().run()
