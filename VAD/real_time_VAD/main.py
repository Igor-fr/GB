import pyaudio
import torchaudio
import torch
from model import ModelVad

#Размер пакета данных запсии в отсчетах
CHUNK = 14112
#Формат данных
FORMAT = pyaudio.paFloat32
#Количество каналов
CHANNELS = 1
#Частота записи
RATE = 44100


p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)
print("Start recording")

#Значения среднего и СКО, вычисленные для спектрограмм на тестовом датасете
mean = -2.4525
std = 3.9360

model = ModelVad()
model.load_state_dict(torch.load('./vad_model_4.pth'))

while True:
    data = stream.read(CHUNK, exception_on_overflow = False)
    data = torch.frombuffer(data, dtype=torch.float32).type(torch.FloatTensor)
    specgram = torchaudio.transforms.MelSpectrogram(sample_rate=RATE, win_length=441, n_mels=32, power=1,
                                                    hop_length=441, n_fft=441)(data)
    specgram = specgram.log2().detach().numpy()
    specgram = (specgram - mean) / std
    specgram = torch.FloatTensor(specgram.reshape(1, 1, 32, 32))
    out = model(specgram)
    print(float(out[0][0]))
    print('*'*int(float(out[0][0])*100))

stream.stop_stream()
stream.close()
p.terminate()