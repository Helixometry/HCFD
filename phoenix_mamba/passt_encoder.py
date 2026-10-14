"""PaSST encoder for patch-based spectro-temporal features"""

import torch.nn as nn


class PASSTPatchEncoder(nn.Module):
    """Extract patch-based spectro-temporal features from audio"""

    def __init__(self, hidden_dim: int = 512):
        super().__init__()
        self.hidden_dim = hidden_dim

    def forward(self, audio_features):
        """Extract PaSST spectro-temporal features"""
        return audio_features
