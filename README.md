# Web-Based Cardiac Delayed Enhanced MRI Segmentation Using Deep Learning and Synthetic Data Augmentation

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange.svg)](https://tensorflow.org/)
[![React](https://img.shields.io/badge/React-18.x-blue.svg)](https://reactjs.org/)

## Project Overview

This graduation project presents an innovative end-to-end solution for automated myocardial infarction segmentation in Late Gadolinium Enhancement (LGE) Cardiac Magnetic Resonance (CMR) images. Our system bridges the gap between AI research and clinical application by integrating advanced deep learning techniques with a user-friendly web-based platform.

### 🏥 Clinical Impact

Cardiovascular disease remains the leading cause of global mortality. Accurate segmentation of myocardial infarction is crucial for:
- **Diagnosis and Treatment Planning**: Precise identification of infarcted tissue
- **Therapeutic Guidance**: Essential for procedures like ventricular tachycardia ablation
- **Clinical Decision Support**: Standardized, reproducible analysis for optimal patient care

### 🔬 Technical Innovation

Our approach addresses critical challenges in medical AI:
- **Data Scarcity**: Novel synthetic data generation using GANs and mathematical simulation
- **Class Imbalance**: Advanced loss functions and attention mechanisms
- **Clinical Integration**: Web-based DICOM viewer with interactive segmentation refinement

## 🏗️ System Architecture

![System Architecture Diagram](/placeholder.svg?height=400&width=800&query=cardiac%20MRI%20segmentation%20system%20architecture%20diagram%20showing%20data%20pipeline%20GAN%20training%20segmentation%20model%20mathematical%20simulator%20evaluation%20metrics%20and%20web%20platform)

*Complete system workflow from data preprocessing through synthetic data generation to clinical deployment*

## 📁 Repository Structure

```
GP_InfDE/
├── Code/
│   ├── Data_Preprocessing/          # Image preprocessing and normalization
│   ├── Data_Simulation_Pipeline/    # Mathematical simulator for mask generation
│   ├── GANs/                       # Pix2Pix and CycleGAN implementations
│   ├── Segmentation/               # U-Net models and training scripts
│   └── main.py                     # Main execution script
├── Web_Platform/                   # React-based DICOM viewer (separate repo)
├── docs/                          # Documentation and research papers
├── models/                        # Trained model weights
├── results/                       # Experimental results and visualizations
└── requirements.txt               # Python dependencies
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- CUDA-compatible GPU (recommended)
- Node.js 16+ (for web platform)
- Docker (optional)

For detailed installation and setup instructions, please refer to the individual README files in each component directory:
- [Data Preprocessing Setup](Code/Data_Preprocessing/README.md)
- [GAN Models Setup](Code/GANs/README.md)
- [Segmentation Models Setup](Code/Segmentation/README.md)
- [Web Platform Setup](Web_Platform/README.md)

## 📊 Results and Performance

### Segmentation Performance (Dice Score)

| Class | Real Data Only | Real + GAN Data | Improvement |
|-------|----------------|-----------------|-------------|
| Background | 0.9891 | 0.9881 | -0.10% |
| LV Cavity | 0.9350 | 0.9365 | +0.16% |
| Normal Myocardium | 0.8222 | 0.8119 | -1.25% |
| **Infarcted Myocardium** | **0.6126** | **0.6165** | **+0.64%** |
| **No-Reflow Area** | **0.5376** | **0.6076** | **+13.02%** |
| **Mean Dice Score** | **0.7793** | **0.7921** | **+1.64%** |

### GAN Performance Metrics

| Model | FID ↓ | IS ↑ | LPIPS ↓ | PSNR ↑ |
|-------|-------|------|---------|--------|
| Baseline Pix2Pix | 512.4 | 1.32 | 0.682 | 10.3 |
| **Our Final Model** | **198.15** | **2.192** | **0.5382** | **16.42** |

### Key Achievements

- ✅ **13% improvement** in no-reflow region segmentation
- ✅ **61% reduction** in FID score for synthetic image quality
- ✅ **66% increase** in Inception Score for image diversity
- ✅ **Web-based platform** for clinical integration

## 🔧 Technical Components

### 1. Mathematical Simulator
- **Fully Synthetic Masks**: Physiologically-based myocardium generation
- **Hybrid Injection**: Real anatomy with synthetic pathology
- **Cross-Subject Fusion**: Novel infarction patterns via k-NN matching

### 2. GAN Models
- **Pix2Pix**: Conditional image generation from segmentation masks
- **CycleGAN**: Domain adaptation between cine and LGE sequences
- **Custom Loss Functions**: Weighted L1 loss addressing class imbalance

### 3. Segmentation Architecture
- **Attention Residual U-Net**: Enhanced feature learning with attention gates
- **Class-Weighted Loss**: Emphasis on clinically important regions
- **Multi-Scale Processing**: 128×128 ROI extraction for efficiency

### 4. Web Platform Features
- **DICOM Compatibility**: Full study upload and visualization
- **Interactive Editing**: Brush-based segmentation refinement
- **AI Integration**: Real-time model inference and overlay
- **Clinical Reporting**: Automated quantification and PDF export

## 🎥 System Demonstration

[![System Demo Video](/placeholder.svg?height=300&width=500&query=video%20thumbnail%20cardiac%20MRI%20segmentation%20demo)](https://placeholder-video-link.com)

*Watch our comprehensive demonstration showing the complete workflow from DICOM upload to AI-powered segmentation and clinical reporting*

## 🌐 Web Platform

The web-based DICOM viewer provides a seamless clinical interface with the following capabilities:

### Platform Features
- 📁 **DICOM Study Management**: Upload and organize cardiac MR studies
- 🖼️ **Multi-Series Visualization**: Side-by-side comparison of sequences
- 🎨 **Interactive Segmentation**: Real-time editing with brush tools
- 🤖 **AI-Powered Analysis**: Automated infarction detection and quantification
- 📊 **Clinical Reporting**: Structured reports with quantitative metrics

For detailed setup and usage instructions, see the [Web Platform README](Web_Platform/README.md).

## 📄 Published Research

This project has resulted in comprehensive research documentation:

### Conference Papers
- **"Web-Based Cardiac Delayed Enhanced MRI Segmentation Using Deep Learning and Synthetic Data Augmentation"**
  - *Submitted to: [Conference Name]*
  - *Status: [Under Review/Accepted/Published]*
  - [📄 Paper PDF](docs/conference_paper.pdf)

### Technical Reports
- **"Comprehensive Technical Report: Cardiac MRI Segmentation System"**
  - *Detailed methodology, experimental validation, and clinical evaluation*
  - [📄 Technical Report PDF](docs/technical_report.pdf)

### Research Contributions
1. **Mathematical Simulation Framework**: Novel approach for generating realistic cardiac pathology patterns
2. **Hybrid GAN Architecture**: Innovative combination of Pix2Pix and CycleGAN for medical image synthesis
3. **Clinical Integration Platform**: First-of-its-kind web-based system for AI-powered cardiac MRI analysis
4. **Performance Validation**: Comprehensive evaluation on EMIDEC dataset with clinical relevance metrics

## 🔬 Research Contributions

### Novel Methodologies
1. **Mathematical Simulation Framework**: Systematic generation of realistic infarction patterns
2. **Hybrid Data Augmentation**: Combination of synthetic and real data for improved generalization
3. **Clinical Integration Platform**: Seamless AI deployment in clinical workflows

### Impact and Significance
- **Clinical Workflow Integration**: Bridges the gap between AI research and clinical practice
- **Data Scarcity Solution**: Addresses fundamental challenge in medical AI through synthetic data generation
- **Performance Enhancement**: Demonstrates significant improvement in rare class segmentation (13% for no-reflow regions)

## 🤝 Contributing

We welcome contributions to improve this project! Please follow these guidelines:

1. **Fork the repository** and create a feature branch
2. **Follow coding standards** (PEP 8 for Python, ESLint for JavaScript)
3. **Add tests** for new functionality
4. **Update documentation** as needed
5. **Submit a pull request** with detailed description

### Development Setup
```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
python -m pytest tests/

# Check code style
flake8 Code/
black Code/
