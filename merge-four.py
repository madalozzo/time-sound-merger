import wave

def merge_wav_files(pre, hour, minute, pos, outfile):
    data = []
    with wave.open(hour, 'rb') as hour, wave.open(minute, 'rb') as minute, wave.open(pre, 'rb') as pre, wave.open(pos, 'rb') as pos:
        data.append([pre.getparams(), pre.readframes(pre.getnframes())])
        data.append([hour.getparams(), hour.readframes(hour.getnframes())])
        data.append([minute.getparams(), minute.readframes(minute.getnframes())])
        data.append([pos.getparams(), pos.readframes(pos.getnframes())])

    with wave.open(outfile, 'wb') as output:
        output.setparams(data[0][0])
        for i in range(len(data)):
            output.writeframes(data[i][1])

for hours in range(24):
    for minutes in range(60):
        print(str(hours) + ":" + str(minutes))
        merge_wav_files(
            f"in/PRE.wav", 
            f"in/H{hours:02d}.wav", 
            f"in/M{minutes:02d}.wav", 
            f"in/POS.wav", 
            f"out/{hours:02d}H{minutes:02d}M.wav"
        )