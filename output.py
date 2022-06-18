import ffmpeg
def merge_files(string_video, string_audio):
    stream_video = ffmpeg.input(string_video)
    stream_audio = ffmpeg.input(string_audio)

    merged = ffmpeg.concat(stream_video, stream_audio, v = 1, a = 1)
    merged.output(merged[0], merged[1], "output.mp4")
    merged.run()
