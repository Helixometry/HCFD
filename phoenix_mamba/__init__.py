"""HCFD: Healthcare Audio Deepfake Detection"""

__version__ = "1.0.0"
__author__ = "Mohd Mujtaba Akhtar, Girish, Muskaan Singh"

from .phoenix_mamba import PHOENIXMamba
from .hyperbolic_projection import HyperbolicProjection

__all__ = ["PHOENIXMamba", "HyperbolicProjection"]
