# import ffmpeg
import moviepy.editor as mp
def merge_files(input_string_video, string_audio, output_string_video):
    audio = mp.AudioFileClip(string_audio)
    video = mp.VideoFileClip(input_string_video)
    
    final_video = video.set_audio(audio)

    final_video.write_videofile(output_string_video)

# def merge_files(input_string_video, string_audio, output_string_video):
#     stream_video = ffmpeg.input(input_string_video)
#     stream_audio = ffmpeg.input(string_audio)

#     merged = ffmpeg.concat(stream_video, stream_audio, v = 1, a = 1).output(output_string_video).run()
