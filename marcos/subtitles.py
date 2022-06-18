import wave
import json

from vosk import Model, KaldiRecognizer, SetLogLevel
import word as custom_Word


model = Model('modelo')

wf = wave.open('./output/wav/video.wav', "rb") #rb stands for read only
rec = KaldiRecognizer(model, wf.getframerate())
rec.SetWords(True)

# create the list of JSON dictionaries
results = []
# recognize speech using vosk model
while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        part_result = json.loads(rec.Result())
        results.append(part_result)
part_result = json.loads(rec.FinalResult())
results.append(part_result)

# convert list of JSON dictionaries to list of 'Word' objects
list_of_Words = []
for sentence in results:
    if len(sentence) == 1:
        # sometimes there are bugs in recognition 
        # and it returns an empty dictionary
        # {'text': ''}
        continue
    for obj in sentence['result']:
        w = custom_Word.Word(obj)  # create custom Word object
        list_of_Words.append(w)  # and add it to list

wf.close()  # close audiofile

# output to the screen
for words in list_of_Words:
    print(words.to_string())