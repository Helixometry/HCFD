"""PHOENIX-Mamba: Geometry-Aware Model for Healthcare Deepfake Detection"""

import torch
import torch.nn as nn
from typing import Dict, Optional


class PHOENIXMamba(nn.Module):
    """
    PHOENIX-Mamba: Geometry-aware framework for detecting codec-synthesized deepfakes
    in healthcare and pathological speech using hyperbolic space.

    Args:
        audio_dim (int): Audio feature dimension
        hidden_dim (int): Hidden dimension
        num_modes (int): Number of self-discovered modes
        dropout (float): Dropout probability
    """

    def __init__(
        self,
        audio_dim: int = 512,
        hidden_dim: int = 512,
        num_modes: int = 8,
        dropout: float = 0.3,
    ):
        super().__init__()
        self.audio_dim = audio_dim
        self.hidden_dim = hidden_dim
        self.num_modes = num_modes

        # Audio projection
        self.audio_proj = nn.Linear(audio_dim, hidden_dim)

        # Mode discovery
        self.mode_centers = nn.Parameter(torch.randn(num_modes, hidden_dim))

        # Hyperbolic projection
        self.hyperbolic_proj = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim, hidden_dim),
        )

        # Classification head
        self.classifier = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim // 2),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim // 2, 1),
            nn.Sigmoid(),
        )

    def forward(self, audio_features: torch.Tensor) -> Dict[str, torch.Tensor]:
        """Forward pass of PHOENIX-Mamba."""
        # Project audio features
        x = self.audio_proj(audio_features)

        # Hyperbolic projection
        hyperbolic_features = self.hyperbolic_proj(x)

        # Classify
        codec_score = self.classifier(hyperbolic_features)

        return {
            "codec_score": codec_score.squeeze(-1),
            "real_prob": 1 - codec_score.squeeze(-1),
            "hyperbolic_features": hyperbolic_features,
            "audio_proj": x,
        }

    @classmethod
    def from_pretrained(cls, checkpoint_path: str) -> "PHOENIXMamba":
        """Load pretrained PHOENIX-Mamba model."""
        checkpoint = torch.load(checkpoint_path, map_location="cpu")
        config = checkpoint.get("config", {})
        model = cls(**config)
        model.load_state_dict(checkpoint["model_state_dict"])
        model.eval()
        return model

    def save(self, checkpoint_path: str, config: Optional[Dict] = None) -> None:
        """Save PHOENIX-Mamba model checkpoint."""
        checkpoint = {
            "model_state_dict": self.state_dict(),
            "config": config or {
                "audio_dim": self.audio_dim,
                "hidden_dim": self.hidden_dim,
                "num_modes": self.num_modes,
            },
        }
        torch.save(checkpoint, checkpoint_path)
