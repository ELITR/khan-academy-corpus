import ffmpeg
import os


def extract_audio(input_path, audio_path_template, audio_extension='mp3', force_output=False):
    audio_path = '{}.{}'.format(audio_path_template, audio_extension)

    # check if audio already exists
    if force_output or not os.path.isfile(audio_path):
        video = ffmpeg.input(input_path)
        out = ffmpeg.output(video, audio_path)
        out.overwrite_output().run()


def split_audio(input_path, output_path_template, timestamps):
    _, extension = os.path.splitext(input_path)
    for start_second, end_second in timestamps:
        audio = ffmpeg.input(input_path).filter('atrim', start=start_second, end=end_second)
        out = ffmpeg.output(audio, '{}_{:010.0f}_{:010.0f}{}'.format(output_path_template, start_second*1000,
                                                                     end_second*1000, extension))
        out.overwrite_output().run(quiet=True)
