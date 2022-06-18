import ffmpeg
def merge_files(string_video, string_audio, input_transcription, outpu):
    stream_video = ffmpeg.input(string_video)
    stream_audio = ffmpeg.input(string_audio)

    merged  = ffmpeg.concat(stream_video, stream_audio, v=1, a=1)
    output  = ffmpeg.output(merged[0], merged[1], "merged.mp4")
