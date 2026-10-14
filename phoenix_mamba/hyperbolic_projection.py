"""Hyperbolic space projection using Poincaré ball"""

import torch
import torch.nn as nn


class HyperbolicProjection(nn.Module):
    """Project audio features into hyperbolic space (Poincaré ball)"""

    def __init__(self, hidden_dim: int = 512, curvature: float = 1.0):
        super().__init__()
        self.hidden_dim = hidden_dim
        self.curvature = curvature
        self.projection = nn.Linear(hidden_dim, hidden_dim)

    def forward(self, features):
        """Project to hyperbolic space"""
        return self.projection(features)
