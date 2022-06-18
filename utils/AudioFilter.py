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
        normalized = filtering_noise(rawaudio, 450, 15000, 0)
        normalized = match_target_amplitude(normalized, -12.0)
        normalized.export(norma_wav_string, format="wav")
        rawaudio.export(wav_string, format = "wav")
    except:
        return False
    return True

def playNormalized(audio):
    play(audio)

