from utils import audiogroup, audiofilter, audiographicmanager
from pydub import AudioSegment
import soundfile as sf

name_file = "audio"
output_wav_folder = "./audios/temp/"
wav_string = "" + output_wav_folder + name_file + "." + "wav"
norma_wav_string = "" + output_wav_folder + "norma" + name_file + "." + "wav"

def control(input_path, output_path, extension):
    rawaudio = AudioSegment.from_file(file = input_path, type = extension)
    audiofilter.filteringAudio(rawaudio, wav_string, norma_wav_string)

    # audio data
    data, sampleRate = sf.read(wav_string)
    normaData, normaSampleRate = sf.read(norma_wav_string)

    audiographicmanager.showing_audiotrack(data, sampleRate, wav_string)
    audiographicmanager.showing_audiotrack(normaData, normaSampleRate, norma_wav_string)

    audiogroup.merge_files(input_path, norma_wav_string, output_path)