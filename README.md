# HCFD: Audio Deepfake Detection in Healthcare

<div align="center">

[![Paper](https://img.shields.io/badge/Paper-ACL%202026%20Findings-blue)](https://aclanthology.org/2026.findings-acl.1739/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.x-ee4c2c)](https://pytorch.org/)

Detecting codec-synthesized deepfakes in healthcare and pathological speech

</div>

## Overview

**HCFD (Healthcare Codec-Fake Detection)** is the first benchmark for detecting neural audio codec-synthesized speech deepfakes in patients with medical conditions. We introduce **PHOENIX-Mamba**, a geometry-aware framework using hyperbolic space for robust pathological speech deepfake detection.

### Key Problem

Current deepfake detectors:
- Trained exclusively on healthy speaker data
- Fail dramatically on pathological speech
- Don't account for acoustic differences in clinical conditions
- Lack pathology-aware training data

### Key Solution

**PHOENIX-Mamba**: A geometry-aware audio model that:
1. **Pathology-Aware** - Trained on HCFD benchmark with clinical conditions
2. **Hyperbolic Geometry** - Models codec-fakes as self-discovered modes in hyperbolic space
3. **Multi-Condition Support** - Handles depression, Alzheimer's, dysarthria, and more
4. **Multi-Codec** - Works across multiple neural audio codec architectures
5. **Strong Performance** - ~97% accuracy on English pathological speech

Achieves **state-of-the-art results** on HCFD benchmark across clinical conditions.

## Paper

**HCFD: A Benchmark for Audio Deepfake Detection in Healthcare**

- **Authors**: Mohd Mujtaba Akhtar, Girish, Muskaan Singh
- **Conference**: ACL 2026 Findings, Pages 34829–34843
- **Paper Link**: [ACL Anthology](https://aclanthology.org/2026.findings-acl.1739/)

## HCFD Dataset

### Coverage

- **Clinical Conditions**: Pathological and healthy speech
  - Depression
  - Alzheimer's Disease
  - Dysarthria
  - Parkinsonian Speech
  - Other neurological conditions

- **Languages**: English and Chinese pathological speech
- **Codecs**: Multiple neural audio codec families
- **Speakers**: Diverse clinical populations
- **Task**: Binary classification (Real/Synthetic)

### Performance Results

- English conditions: ~97% accuracy
- Chinese conditions: 93-94% accuracy

## PHOENIX-Mamba Framework

### Architecture

- **Patch-based Features** (PaSST) - Spectro-temporal representations
- **Hyperbolic Projection** - Poincaré ball embeddings
- **Mode Discovery** - Self-discovered codec-fake modes in hyperbolic space
- **Classification Head** - Real/Synthetic detection

### Key Design Principles

1. **Pathology-Aware** - Captures clinical speech characteristics
2. **Hyperbolic Geometry** - Better representation of hierarchical audio patterns
3. **Codec-Aware** - Detects codec-specific artifacts
4. **Multi-Condition** - Works across diverse clinical conditions
5. **Effective** - ~97% accuracy on pathological speech detection

## Quick Start

### Installation

```bash
git clone https://github.com/Helixometry/HCFD.git
cd HCFD
pip install -r requirements.txt
```

### Training

```bash
python scripts/train.py --config configs/config_phoenix_mamba.yaml
```

### Evaluation

```bash
python scripts/evaluate.py --checkpoint models/phoenix_mamba_best.pt --test-data data/hcfd_test
```

### Inference

```bash
python scripts/inference.py --audio pathological_speech.wav --checkpoint models/phoenix_mamba_best.pt
```

## Results

### Performance on HCFD

| Model | Healthy Speech | Depression | Alzheimer's | Dysarthria | Average |
|-------|----------------|-----------|------------|-----------|---------|
| Baseline | 92.1% | 45.3% | 38.7% | 42.1% | 54.5% |
| PaSST | 94.5% | 78.2% | 75.8% | 79.1% | 81.9% |
| **PHOENIX-Mamba** | **96.8%** | **97.3%** | **96.9%** | **97.1%** | **97.0%** |

## Repository Structure

```
HCFD/
├── README.md
├── LICENSE
├── setup.py
├── requirements.txt
├── phoenix_mamba/
│   ├── __init__.py
│   ├── phoenix_mamba.py
│   ├── passt_encoder.py
│   ├── hyperbolic_projection.py
│   ├── mode_discovery.py
│   ├── utils.py
│   └── metrics.py
├── data/
├── scripts/
│   ├── train.py
│   ├── evaluate.py
│   └── inference.py
├── configs/
│   └── config_phoenix_mamba.yaml
├── tests/
└── docs/
    └── ARCHITECTURE.md
```

## Citation

```bibtex
@inproceedings{akhtar2026hcfd,
  title={HCFD: A Benchmark for Audio Deepfake Detection in Healthcare},
  author={Akhtar, Mohd Mujtaba and Girish and Singh, Muskaan},
  booktitle={Findings of the Association for Computational Linguistics: ACL 2026},
  pages={34829--34843},
  year={2026},
  address={San Diego, California}
}
```

## License

MIT License - see [LICENSE](LICENSE) for details.

## Authors

- **Mohd Mujtaba Akhtar**
- **Girish**
- **Muskaan Singh**

## Key Features

🏥 **Healthcare Focus** - First benchmark for pathological speech deepfake detection  
🧠 **Clinical Conditions** - Supports depression, Alzheimer's, dysarthria, and more  
🔷 **Hyperbolic Geometry** - Poincaré ball embeddings for audio patterns  
📊 **State-of-the-Art** - 97% accuracy on pathological speech  
🌍 **Multi-Lingual** - English and Chinese support  
🎤 **Codec-Aware** - Detects multiple neural audio codec artifacts  
⚕️ **Medical-Grade** - Designed for clinical applications  

---

<div align="center">

**Advancing deepfake detection for healthcare and clinical applications**

</div>
