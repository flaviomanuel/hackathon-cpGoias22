import time

import matplotlib.pyplot as plt
import numpy as np
from pydub import AudioSegment
from pydub.playback import play

def playing_audio(audioFilePath):
    song = AudioSegment.from_file(file = audioFilePath, type="wav")
    play(song)

def showing_audiotrack(data, samplerate, path):

    # We use a variable previousTime to store the time when a plot update is made
    # and to then compute the time taken to update the plot of the audio data.
    previousTime = time.time()
    dataLenght = len(data);
    # Working with stereo audio, there are two channels in the audio data.
    # Let's retrieve each channel seperately:
    ch1 = np.array([data[i][0] for i in range(dataLenght)])  # channel 1
    ch2 = np.array([data[i][1] for i in range(dataLenght)])  # channel 2


    time_axis = np.linspace(0, dataLenght / samplerate, dataLenght, endpoint=False)
    sound_axis = ch1

    # # Turning the interactive mode on
    # plt.ion()

    # Each time we go through a number of samples in the audio data that corresponds to one second of audio,
    # we increase spentTime by one (1 second).
    spentTime = 0

    # Let's the define the update periodicity
    updatePeriodicity = 10 # expressed in seconds

    # Plotting the audio data and updating the plot
    for i in range(dataLenght):
        # Each time we read one second of audio data, we increase spentTime :
        if i // samplerate != (i-1) // samplerate:
            spentTime += 1
        # We update the plot every updatePeriodicity seconds
        if spentTime == updatePeriodicity:
            # Clear the previous plot
            plt.clf()
            # Plot the audio data
            plt.plot(time_axis, sound_axis)
            # Plot a red line to keep track of the progression
            # plt.axvline(x=i / samplerate, color='r')
            plt.xlabel("Time (s)")
            plt.ylabel("Audio")
            # plt.show()  # shows the plot
            # plt.pause(updatePeriodicity-(time.time()-previousTime))
            # a forced pause to synchronize the audio being played with the audio track being displayed
            # previousTime = time.time()
            spentTime = 0
            plt.savefig("./img/"+path+".png")
        
# def startAudioGraphic(audioFilePath):
#     print("ola")
#     # Retrieve the data from the wav file

#     data, samplerate = sf.read(audioFilePath) 

#     n = len(data)  # the length of the arrays contained in data
#     Fs = samplerate   # the sample rate

#     playing_audio(audioFilePath)
#     # x-axis and y-axis to plot the audio data


#     # plt.plot(time_axis, sound_axis)
#     # plt.show()
