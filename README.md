# 🌿 Plant Disease AI Diagnostic Suite
![Status](https://img.shields.io/badge/Status-Live_Demo-green)
![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![PyTorch](https://img.shields.io/badge/Framework-PyTorch-EE4C2C?logo=pytorch)

An end-to-end Computer Vision solution for automated agricultural health monitoring. This project identifies **38 distinct plant diseases** across 14 crop species using state-of-the-art Deep Learning architectures.

---

## 🚀 Live Interactive Demo
Experience the model in real-time. Upload a leaf image to see a side-by-side comparison of our two primary architectures:
👉 **[Launch Hugging Face Space](https://huggingface.co/spaces/Anthony5787/Plant-Disease-Diagnostic-Suite)**

---

## 📊 Dataset Context
This project utilizes the **New Plant Diseases Dataset**, a comprehensive collection of leaf images reconstructed from the original PlantVillage dataset.

* **Source:** [Kaggle - New Plant Diseases Dataset](https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset)
* **Scale:** 87,000+ RGB images covering 38 distinct disease/healthy categories.

---

## 🧠 Model Weights & Large Files
Due to GitHub's file size limitations for standard uploads, the trained `.pth` model weights are hosted on the Hugging Face infrastructure alongside the live app. 

**To download the weights for local use:**
1. Navigate to the [Hugging Face Files Tab](https://huggingface.co/spaces/Anthony5787/Plant-Disease-Diagnostic-Suite/tree/main).
2. Download `ResNet18_final.pth` (~45MB).
3. Download `EfficientNet_final.pth` (~20MB).
4. Place them in the root directory of this project to run `app.py` locally.

---

## 🔬 Methodology & Performance
I implemented and benchmarked two distinct models to evaluate the trade-off between computational efficiency and classification accuracy:

| Model | Accuracy | F1-Score | Parameters |
| :--- | :---: | :---: | :---: |
| **EfficientNet-B0** | **99.82%** | **0.998** | ~5.3M |
| **ResNet18** | 99.58% | 0.996 | ~11.7M |

## 🛠️ Tech Stack
* **Core:** PyTorch, Torchvision
* **Deployment:** Gradio (UI), Hugging Face Spaces (Hosting)
* **Explainability:** Grad-CAM (Visualizing model attention)

## 📂 Repository Structure
* `training.ipynb`: Full training pipeline and augmentation logic.
* `testing.ipynb`: Evaluation metrics, Confusion Matrix, and Grad-CAM heatmaps.
* `app.py`: Production-ready script powering the Gradio web interface.
* `requirements.txt`: List of dependencies for environment replication.

---
**Developed by:** Anthony Amit Biswas  
**Academic/Project Context:** Deep Learning Comparative Analysis
