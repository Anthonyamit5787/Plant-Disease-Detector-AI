# 🌿 Plant Disease AI Diagnostic Suite
![Status](https://img.shields.io/badge/Status-Live_Demo-green)
![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![PyTorch](https://img.shields.io/badge/Framework-PyTorch-EE4C2C?logo=pytorch)

An end-to-end Computer Vision solution for automated agricultural health monitoring. This project identifies **38 distinct plant diseases** across 14 crop species with integrated **Explainable AI (XAI)** to validate model decisions.

---

## 🚀 Live Interactive Demo
Experience the model in real-time. Upload a leaf image to see a side-by-side comparison of our two primary architectures:
👉 **[Launch Hugging Face Space](https://huggingface.co/spaces/Anthony5787/Plant-Disease-Diagnostic-Suite)**
<img width="1917" height="822" alt="Screenshot 2026-03-31 020232" src="https://github.com/user-attachments/assets/ebc0f392-1a7b-4c80-a47a-0037a498cb74" />

---

## 🔬 Explainable AI: Grad-CAM Visualization
To ensure the models are learning biological features (like lesions and mold) rather than background noise, I implemented **Grad-CAM (Gradient-weighted Class Activation Mapping)**.

| Original Leaf | ResNet18 Attention | EfficientNet-B0 Attention |
| :---: | :---: | :---: |
|<img width="256" height="256" alt="image" src="https://github.com/user-attachments/assets/724f016b-085a-4ccb-82b5-d33b242283c1" /> | <img width="389" height="411" alt="image" src="https://github.com/user-attachments/assets/eeed36c3-2ca3-4884-9dc7-59dddff2832d" /> | <img width="389" height="411" alt="image" src="https://github.com/user-attachments/assets/cbc4169f-cd42-4883-9fa1-818c11633b8d" /> |

* **Insight:** The heatmaps confirm that both models correctly localize their "attention" on the symptomatic areas of the leaf, proving the robustness of the 99.8% accuracy.

---

## 📊 Dataset & Methodology
* **Dataset:** [New Plant Diseases Dataset](https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset) (87,000+ images).
* **Architectures:** Benchmarked **ResNet18** vs. **EfficientNet-B0**.
* **Weights:** Model weights are hosted on Hugging Face due to LFS size constraints.

### **Performance Benchmarks**
| Model | Accuracy | F1-Score | Parameters |
| :--- | :---: | :---: | :---: |
| **EfficientNet-B0** | **99.82%** | **0.998** | ~5.3M |
| **ResNet18** | 99.58% | 0.996 | ~11.7M |

---

## 📂 Repository Structure
* `training.ipynb`: Full training pipeline and augmentation logic.
* `testing.ipynb`: Evaluation metrics and **Grad-CAM implementation**.
* `app.py`: Production-ready script powering the Gradio web interface.

**Developed by:** [Anthony Amit Biswas]
