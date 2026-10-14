"""Evaluation script for PHOENIX-Mamba"""

import argparse
from phoenix_mamba.phoenix_mamba import PHOENIXMamba
from phoenix_mamba.utils import get_device

def main():
    parser = argparse.ArgumentParser(description="Evaluate PHOENIX-Mamba")
    parser.add_argument("--checkpoint", type=str, required=True)
    parser.add_argument("--test-data", type=str, required=True)

    args = parser.parse_args()
    device = get_device()
    model = PHOENIXMamba.from_pretrained(args.checkpoint).to(device)
    print(f"Evaluating on {args.test_data}")

if __name__ == "__main__":
    main()
