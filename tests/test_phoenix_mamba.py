"""Unit tests for PHOENIX-Mamba"""

import unittest
import torch
from phoenix_mamba.phoenix_mamba import PHOENIXMamba

class TestPHOENIXMamba(unittest.TestCase):
    def setUp(self):
        self.model = PHOENIXMamba(audio_dim=512, hidden_dim=512, num_modes=8)

    def test_forward(self):
        audio = torch.randn(4, 100, 512)
        output = self.model(audio)
        self.assertIn('codec_score', output)
        self.assertEqual(output['codec_score'].shape[0], 4)

if __name__ == '__main__':
    unittest.main()
