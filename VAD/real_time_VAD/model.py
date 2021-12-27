import torch
import torch.nn as nn
from torch.nn import functional as F

class ModelVad(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 32, kernel_size=5, stride=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(32, 128, kernel_size=3, stride=1)
        self.fc1 = nn.Linear(6*6*128, 64)
        self.bilstm = nn.LSTM(1, hidden_size=128, bidirectional=True, batch_first = True)
        self.fc2 = nn.Linear(256, 2)
        self.bn1 = nn.BatchNorm2d(32)
        self.bn2 = nn.BatchNorm2d(128)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1,6*6*128)
        x = F.relu(self.fc1(x))
        x = x.view(-1,64,1)
        x, (h, c) = self.bilstm(x)
        x = torch.cat((h[0,:,:], h[1,:,:]), 1)
        x = x.view(-1,256)
        x = self.fc2(x)
        x = F.softmax(x, -1)
        return x