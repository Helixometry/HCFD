"""Self-discovered modes in hyperbolic space"""

import torch
import torch.nn as nn


class ModeDiscovery(nn.Module):
    """Discover self-supervised modes of codec-fakes in hyperbolic space"""

    def __init__(self, hidden_dim: int = 512, num_modes: int = 8):
        super().__init__()
        self.hidden_dim = hidden_dim
        self.num_modes = num_modes
        self.mode_centers = nn.Parameter(torch.randn(num_modes, hidden_dim))

    def forward(self, hyperbolic_features):
        """Discover modes"""
        return hyperbolic_features
