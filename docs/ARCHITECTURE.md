# PHOENIX-Mamba Architecture

## Overview

PHOENIX-Mamba detects neural audio codec-synthesized deepfakes in healthcare and pathological speech using hyperbolic geometry.

## Key Innovation

**Hyperbolic Space + Mode Discovery**: PHOENIX-Mamba leverages:
- **Patch-based Features** (PaSST) - Spectro-temporal representations
- **Hyperbolic Projection** - Poincaré ball embeddings for hierarchical patterns
- **Mode Discovery** - Self-discovered codec-fake modes in hyperbolic space

## Architecture

```
Input Pathological Speech
    ↓
PaSST Encoder
(Spectro-Temporal Features)
    ↓
Audio Projection (512-dim)
    ↓
Hyperbolic Projection
(Poincaré Ball)
    ↓
Mode Discovery
(Self-Discovered Modes)
    ↓
Classification Head
    ↓
Output: Real/Synthetic Probability
```

## Results on HCFD

- Baseline: 54.5% average accuracy
- PaSST: 81.9% average accuracy
- PHOENIX-Mamba: 97.0% average accuracy
- English conditions: ~97% accuracy
- Chinese conditions: 93-94% accuracy

## Clinical Conditions Supported

- Depression
- Alzheimer's Disease
- Dysarthria
- Parkinsonian Speech
- Other neurological conditions
