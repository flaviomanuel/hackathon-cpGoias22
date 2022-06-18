# %% [markdown]
# # Normalizing Audio Files

# %%
from pydub import AudioSegment, scipy_effects
from pydub.playback import play
import ffmpeg

def match_target_amplitude(sound, target_dBFS):
    change_in_dBFS = target_dBFS - sound.dBFS
    return sound.apply_gain(change_in_dBFS)

# Returning AudioSegment type
def filtering_noise(sound: AudioSegment, lower_limit, upper_limit, order = 3):
    sound = scipy_effects.low_pass_filter(sound, upper_limit, order)
    sound = scipy_effects.high_pass_filter(sound, lower_limit, order)
    return sound


# %% [markdown]
# ## Control Variables

# %%

def filteringAudio():
    extension = "mp4"
    name_file = "video"
    input_folder = "./audios/"
    output_mp3_folder = "./output/mp4/"
    output_wav_folder = "./output/wav/"

    input_string = "" + input_folder + name_file + "." + extension
    wav_string = "" + output_wav_folder + name_file + "." + "wav"
    norma_wav_string = "" + output_wav_folder + "norma" + name_file + "." + "wav"
    output_string = "" + output_mp3_folder + name_file + "." + extension

    # %% [markdown]
    # ## Getting Raw File

    # %%
    rawaudio = AudioSegment.from_file(file = input_string, type = extension)
    type(rawaudio)

    # %% [markdown]
    # ## Normalizing Audio

    # %%
    normalized = filtering_noise(rawaudio, 240, 18000, 0)
    normalized = match_target_amplitude(normalized, -6.0)

    # %% [markdown]
    # ## Exporting to .WAV

    # %%
    normalized.export(norma_wav_string, format="wav")

    # %%
    rawaudio.export(wav_string, format = "wav")
    
    return normalized

# %% [markdown]
# ## Exporting Normalized File

# %%

# normalized.export(output_string, format=extension)

# %% [markdown]
# ## Playing audios file


# %%
# play(rawaudio)

def playNormalized():
    play(normalized)

