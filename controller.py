from utils import audiogroup, AudioFilter, AudioGraphicManager
from pydub import AudioSegment
import soundfile as sf
import speech_recognition as sr

name_file = "audio"
output_wav_folder = "./audios/temp/"
wav_string = "" + output_wav_folder + name_file + "." + "wav"
norma_wav_string = "" + output_wav_folder + "norma" + name_file + "." + "wav"
img1_name = "img1"
img2_name = "img2"

def control(input_path, output_path, extension):
    rawaudio = AudioSegment.from_file(file = input_path, type = extension)
    arrays = rawaudio.get_array_of_samples()
    teste = arrays
    print(teste)
    audio = AudioSegment.from_file(file = norma_wav_string, type = "wav")
    print(audio.get_array_of_samples())

    AudioFilter.filteringAudio(rawaudio, wav_string, norma_wav_string)
    

    # audio data
    data, sampleRate = sf.read(wav_string)
    normaData, normaSampleRate = sf.read(norma_wav_string)

    AudioGraphicManager.showing_audiotrack(data, sampleRate, img1_name)
    AudioGraphicManager.showing_audiotrack(normaData, normaSampleRate, img2_name)

    audiogroup.merge_files(input_path, norma_wav_string, output_path)

    #trancription
    rec = sr.Recognizer()
    with sr.AudioFile(wav_string) as fonte:
        audio = rec.record(fonte)

    file = open("output/txt/trascricao.txt", 'w')
    file.write(rec.recognize_google(audio, language='pt'))
    file.close()