import librosa
import matplotlib.pyplot as plt
#Loading an audio file
waveform, sample_rate = librosa.load(r'C:\Users\user\OneDrive\Desktop\Denish Pradhan\Music\final products\final one\final one.AAC')

# create a window
plt.figure(figsize=(10, 4))

# plot the waveform
librosa.display.waveshow(waveform, sr=sample_rate,color='blue')

# Add titel and labels
plt.title('Waveform of the Audio')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')

#adjust the layout
plt.tight_layout()

# show the plot
plt.show()