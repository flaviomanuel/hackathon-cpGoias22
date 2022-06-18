from pydub import AudioSegment, scipy_effects
from pydub.playback import play

def match_target_amplitude(sound, target_dBFS):
    change_in_dBFS = target_dBFS - sound.dBFS
    return sound.apply_gain(change_in_dBFS)

# Returning AudioSegment type
def filtering_noise(sound: AudioSegment, lower_limit, upper_limit, order = 3):
    sound = scipy_effects.low_pass_filter(sound, upper_limit, order)
    sound = scipy_effects.high_pass_filter(sound, lower_limit, order)
    return sound

def filteringAudio(rawaudio, wav_string, norma_wav_string):
    try:
        print("Iniciando conversão.")
        print(type(rawaudio))
        normalized = match_target_amplitude(rawaudio, -6.0)
        filtered = filtering_noise(normalized, 450, 18000, 0)
        try:
            filtered.export(norma_wav_string, format="wav")
            print("Salvando na pasta: "+ norma_wav_string)
        except:
            print("Erro 02.")
        try:
            rawaudio.export(wav_string, format = "wav")
            print("Salvando na pasta: "+ wav_string)
        except:
            print("Erro 02.")
        return True
    except:
        print("ERROOOR")
        return False

def playNormalized(audio):
    play(audio)

