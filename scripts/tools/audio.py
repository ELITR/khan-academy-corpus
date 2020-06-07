import ffmpeg
import os
import subprocess
import re


def extract_audio(video_path, audio_path, force_output=False):
    # check if audio already exists
    if force_output or not os.path.isfile(audio_path):
        video = ffmpeg.input(video_path)
        out = ffmpeg.output(video, audio_path, acodec='copy')
        out.overwrite_output().run()


def get_me_to_silence(timestamp, silence_starts, silence_ends):
    for silence_start, silence_end in zip(silence_starts, silence_ends):
        if silence_start <= timestamp <= silence_end:
            return timestamp
        elif silence_start > timestamp:
            return silence_start


def split_audio_and_text(input_path, output_audio_path_template, output_text_path_template, timestamps,
                         silence_starts, silence_ends, pre_seconds=0.3, post_seconds=0.8):
    for text, start_second, end_second in timestamps:
        try:
            silence = get_me_to_silence(end_second, silence_starts, silence_ends)
        except StopIteration:
            continue
        #print(end_second, silence_start_after)
        audio = ffmpeg.input(input_path).filter('atrim', start=start_second-pre_seconds, end=silence)
        out = ffmpeg.output(audio, output_audio_path_template.format(start_second*100,
                                                                     silence*100))

        with open(output_text_path_template.format(start_second * 100, silence * 100), 'w') as f:
            f.write(text)

        out.overwrite_output().run(quiet=True)


def get_silence_starts(input_path, noise=0.01, duration=0.5):
    """
    https://github.com/kkroening/ffmpeg-python/blob/master/examples/split_silence.py
    """
    p = subprocess.Popen(
        (ffmpeg
            .input(input_path).filter('silencedetect', noise=noise, d=duration)
            .output('pipe:', format='null')
            .compile()
         ) + ['-nostats'],
        stderr=subprocess.PIPE
    )
    output = p.communicate()[1].decode('utf-8')
    if p.returncode != 0:
        raise ValueError('Cannot detect silence for %s', input_path)

    lines = output.splitlines()

    silence_start_re = re.compile(' silence_start: (?P<start>[0-9]+(\.?[0-9]*))$')
    silence_end_re = re.compile(' silence_end: (?P<end>[0-9]+(\.?[0-9]*)) ')

    silence_starts = []
    silence_ends = []
    for line in lines:
        silence_start_match = silence_start_re.search(line)
        silence_end_match = silence_end_re.search(line)
        if silence_start_match:
            silence_starts.append(float(silence_start_match.group('start')))
        if silence_end_match:
            silence_ends.append(float(silence_end_match.group('end')))

    return silence_starts, silence_ends
