# 🌱 Plant Disease Detection using Deep Learning

![Status](https://img.shields.io/badge/Status-v2.0_Live-green)
![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![PyTorch](https://img.shields.io/badge/Framework-PyTorch-EE4C2C?logo=pytorch)
![Transformers](https://img.shields.io/badge/Architecture-Vision_Transformers-blueviolet)

An end-to-end deep learning system that detects plant diseases from leaf images using CNNs and Vision Transformers.  
Achieves up to **99.81% accuracy** and is deployed as a real-time web application with explainable AI (Grad-CAM).

Designed to bridge the gap between controlled datasets and real-world agricultural conditions.

---

## 📌 Overview

This project presents a deep learning-based system for detecting **38 plant diseases across 14 crop species** using leaf images.

It compares three architectures:
- ResNet18  
- EfficientNet-B0  
- Vision Transformer (ViT-B/16)  

👉 Best performance achieved: **99.81% accuracy (EfficientNet-B0)**  

The system also includes:
- Explainable AI (Grad-CAM)  
- Real-world testing  
- Live deployment  

---

## 🚀 Live Demo

👉 https://huggingface.co/spaces/Anthony5787/Plant-Disease-Diagnostic-Suite-2.0  

<img width="1901" height="818" alt="dashboard" src="https://github.com/user-attachments/assets/4cc06fd4-b905-4392-b886-4594fb9b030b" />

---

## ✨ Key Features

- 🌿 Multi-model comparison (CNN vs Transformer)
- 📊 High accuracy classification (up to **99.81%**)
- ⚡ Real-time inference (Hugging Face)
- 🔍 Grad-CAM visual explanations
- 🌍 Tested on real-world images
- 🧠 Detailed evaluation (F1, confusion matrix)

---

## 🧠 Models Used

| Model | Type | Strength |
|------|------|----------|
| ResNet18 | CNN | Strong baseline |
| EfficientNet-B0 | CNN | Best accuracy & efficiency |
| ViT-B/16 | Transformer | Global attention |

---

## 📊 Results

| Model | Accuracy |
|------|--------|
| ResNet18 | 96.50% |
| EfficientNet-B0 | **99.81%** |
| ViT-B/16 | 91.05% |

<img width="1396" height="783" alt="comparison" src="https://github.com/user-attachments/assets/f6511182-d9ab-4a55-868e-92a6c4dbdf9a" />

---

## 🔬 Explainable AI (Grad-CAM)

Grad-CAM is used to visualize model attention, ensuring predictions are based on **disease regions rather than background noise**.

<img width="2184" height="837" alt="gradcam" src="https://github.com/user-attachments/assets/287984b5-0da4-4fac-9a81-d8a57fb106ec" />

---

## 📦 Dataset

- **Source:** New Plant Diseases Dataset (Kaggle)  
- **Size:** 87,000+ images  
- **Classes:** 38  
- **Preprocessing:**
  - Resize (224×224)  
  - Normalization  
  - Augmentation (flip, rotation, color jitter)

---

## ⚙️ Installation

```bash
git clone https://github.com/Anthonyamit5787/Plant-Disease-Detector-AI
cd Plant-Disease-Detector-AI
pip install -r requirements.txt 
```
---

## ▶️ Usage

```bash
python app.py
```
Then:

- Upload a leaf image
- Get prediction + confidence
- Compare model outputs

---

## 📂 Repository Structure

```bash
├── app.py                 # Web app (Gradio)
├── training_v2.ipynb      # Model training
├── testing.ipynb          # Evaluation + Grad-CAM
├── requirements.txt       # Dependencies
```
⚠️ Model weights are hosted on Hugging Face due to size limits.

---

## ⚠️ Limitations

- Performance may drop on real-world images (domain shift)
- Similar diseases can be confused
- ViT requires larger datasets for optimal performance

---

🔮 **Future Work**

- Improve robustness with more diverse data
- Explore hybrid CNN + Transformer models
- Deploy on mobile / edge devices

---

## 🌍 Impact

This system can support:
- Early disease detection
- Reduced crop loss
- Smart agriculture solutions

---

## 🤝 Connect

Anthony Amit Biswas
🔗 https://www.linkedin.com/in/anthony-amit-5617702ba/
🤗 https://huggingface.co/Anthony5787
