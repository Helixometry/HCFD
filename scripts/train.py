"""Training script for PHOENIX-Mamba"""

import argparse
import torch
import yaml

from phoenix_mamba.phoenix_mamba import PHOENIXMamba
from phoenix_mamba.utils import seed_everything, get_device

def main():
    parser = argparse.ArgumentParser(description="Train PHOENIX-Mamba")
    parser.add_argument("--config", type=str, required=True)
    parser.add_argument("--output-dir", type=str, default="results")

    args = parser.parse_args()

    with open(args.config) as f:
        config = yaml.safe_load(f)

    seed_everything(config.get('seed', 42))
    device = get_device()

    model = PHOENIXMamba(**config['model']).to(device)
    print(f"Training PHOENIX-Mamba on {device}")

if __name__ == "__main__":
    main()
