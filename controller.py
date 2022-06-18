import output
from pydub import AudioSegment
name_file = "audio"
output_wav_folder = "./audios/temp/"
wav_string = "" + output_wav_folder + name_file + "." + "wav"
norma_wav_string = "" + output_wav_folder + "norma" + name_file + "." + "wav"

def control(input_path, output_path, extension):
    rawaudio = AudioSegment.from_file(file = input_path, type = extension)
    output.merge_files(input_path, norma_wav_string, output_path)