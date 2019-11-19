import ffmpeg
import os


def extract_audio(video_path, audio_path, force_output=False):
    # check if audio already exists
    if force_output or not os.path.isfile(audio_path):
        video = ffmpeg.input(video_path)
        out = ffmpeg.output(video, audio_path)
        out.overwrite_output().run()


def split_audio_and_text(input_path, output_audio_path_template, output_text_path_template, timestamps,
                         pre_seconds=0.5, post_seconds=0.8):
    for text, start_second, end_second in timestamps:
        audio = ffmpeg.input(input_path).filter('atrim', start=start_second-pre_seconds, end=end_second+post_seconds)
        out = ffmpeg.output(audio, output_audio_path_template.format(start_second*100,
                                                                     end_second*100))

        with open(output_text_path_template.format(start_second * 100, end_second * 100), 'w') as f:
            f.write(text)

        out.overwrite_output().run(quiet=True)
