import os
import deepspeech
from scipy.io import wavfile
import csv

files = []
only_name = []
for file in os.listdir("test_wavs"):
    if file.endswith(".wav"):
        only_name.append(file)
        files.append(os.path.join("test_wavs", file))



ds = deepspeech.Model("deepspeech-0.9.3-models.pbmm")
ds.enableExternalScorer("deepspeech-0.9.3-models.scorer")

result_ds = []
for i in files:
    sr, data = wavfile.read(i)
    result_ds.append(ds.stt(data))

with open('results.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for i in range(0, len(files)):
        row = [only_name[i], result_ds[i]]
        writer.writerow(row)
