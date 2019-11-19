import pyvtt


def subtitles2timestamps(input_path, pause_length_seconds=1):
    batched_subtitles = []
    text = ''
    start = None
    end = None

    for caption in pyvtt.open(input_path):
        current_start = caption.start.ordinal / 1000
        current_end = caption.end.ordinal / 1000

        if start is None:
            start = current_start

        if end is None:
            end = current_end

        if current_start - end > pause_length_seconds:
            batched_subtitles.append((text, start, end))
            text = ''
            start = current_start

        end = current_end
        text += '\n\n' + caption.text

    return batched_subtitles
