import pyvtt
import re

in_square_brackets = re.compile("[.*?]")


def subtitles2timestamps(input_path):
    return [(caption.text, caption.start.ordinal / 1000, caption.end.ordinal / 1000)
            for caption in pyvtt.open(input_path)]


def adjust_caption_text(caption_text):
    # strip leading and trailing dash
    caption_text = caption_text.strip('-')
    # remove [Voiceover] and such
    caption_text = re.sub(in_square_brackets, '', caption_text)
    # join multiple spaces and remove leading ad trailing spaces
    caption_text = ' '.join(caption_text.split())

    return caption_text


def subtitles2text(input_path):
    return '\n'.join(adjust_caption_text(caption.text) for caption in pyvtt.open(input_path))
