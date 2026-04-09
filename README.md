# 🌱 Plant Disease Detection using Deep Learning

![Status](https://img.shields.io/badge/Status-v2.0_Live-green)
![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![PyTorch](https://img.shields.io/badge/Framework-PyTorch-EE4C2C?logo=pytorch)
![Transformers](https://img.shields.io/badge/Architecture-Vision_Transformers-blueviolet)

### **Bridging Agricultural Expertise with Explainable Deep Learning**

An advanced Computer Vision system for automated plant disease detection. This project classifies **38 plant diseases across 14 crop species** with a peak performance of **99.81% test accuracy** using EfficientNet-B0.

**Version 2.0 Update:** Integration of **Vision Transformers (ViT)** enables comparison between convolutional feature extraction and global self-attention. A multi-model “consensus system” improves reliability by analysing predictions from three distinct architectures.

---

## 🚀 Live Interactive Demo

Experience real-time plant disease diagnosis:

👉 **[Launch Hugging Face Space v2.0](https://huggingface.co/spaces/Anthony5787/Plant-Disease-Diagnostic-Suite-2.0)**

<img width="1901" height="818" alt="main dashboard" src="https://github.com/user-attachments/assets/4cc06fd4-b905-4392-b886-4594fb9b030b" />

---

## ✨ Key Features

- 🌿 Multi-model architecture (ResNet18, EfficientNet-B0, ViT-B/16)
- 📊 High accuracy classification (up to **99.81%**)
- ⚡ Real-time prediction via Hugging Face deployment
- 🔍 Explainable AI using Grad-CAM
- 🌍 Robustness testing on real-world images
- 🧠 Comparative analysis of CNN vs Transformer models

---

## 🔬 Explainable AI (Grad-CAM)

To enhance interpretability, **Grad-CAM (Gradient-weighted Class Activation Mapping)** is used to visualise model attention.

This ensures the model focuses on biologically relevant features such as:
- lesions  
- discoloration  
- fungal patterns  

<img width="2184" height="837" alt="gradcam" src="https://github.com/user-attachments/assets/287984b5-0da4-4fac-9a81-d8a57fb106ec" />

---

## 🧠 Multi-Architecture Comparison

| Model | Type | Key Strength |
|------|------|-------------|
| **ResNet18** | Residual CNN | Strong baseline, captures local textures |
| **EfficientNet-B0** | Optimized CNN | Best accuracy and efficiency |
| **ViT-B/16** | Transformer | Captures global dependencies |

---

## 📊 Results

| Metric | ResNet18 | EfficientNet-B0 | ViT-B/16 |
| :--- | :---: | :---: | :---: |
| **Validation Accuracy** | 96.80% | **99.79%** | 91.10% |
| **Test Accuracy** | 96.50% | **99.81%** | 91.05% |
| **Inference Latency** | 11.20 ms | 7.80 ms | **3.57 ms** |
| **Parameters** | 11.7M | 5.3M | 86.4M |

<img width="1396" height="783" alt="comparison" src="https://github.com/user-attachments/assets/f6511182-d9ab-4a55-868e-92a6c4dbdf9a" />

---

## 📦 Dataset

- **Dataset:** New Plant Diseases Dataset (Kaggle)  
- **Size:** 87,000+ images  
- **Classes:** 38 disease categories  
- **Crops:** 14 species  

### Data Processing:
- Image resizing (224×224)  
- Normalization (ImageNet standards)  
- Data augmentation:
  - Rotation  
  - Horizontal flipping  
  - Color jitter  

---

## ⚙️ Installation

```bash
git clone https://github.com/Anthonyamit5787/Plant-Disease-Detector-AI
cd Plant-Disease-Detector-AI

pip install -r requirements.txt
