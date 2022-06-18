from utils import audiogroup, audiofilter, audiographicmanager
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
    try:
        print("Abrindo arquivo: "+input_path)
        rawaudio = AudioSegment.from_file(file = input_path, type = extension)
    except:
        print("Erro ao abrir o arquivo.")
        return False
    try:
        audiofilter.filteringAudio(rawaudio, wav_string, norma_wav_string)
    except:
        print("Erro controler1.")
        return False

    # audio data
    data, sampleRate = sf.read(wav_string)
    normaData, normaSampleRate = sf.read(norma_wav_string)

    audiographicmanager.showing_audiotrack(data, sampleRate, img1_name)
    audiographicmanager.showing_audiotrack(normaData, normaSampleRate, img2_name)

    audiogroup.merge_files(input_path, norma_wav_string, output_path)

    #trancription
    rec = sr.Recognizer()
    with sr.AudioFile(wav_string) as fonte:
        audio = rec.record(fonte)

    file = open("output/txt/trascricao.txt", 'w')
    file.write(rec.recognize_google(audio, language='pt'))
    file.close()