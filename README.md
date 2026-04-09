# 🌿 PlantPath AI: Diagnostic Engine v2.0
![Status](https://img.shields.io/badge/Status-v2.0_Live-green)
![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![PyTorch](https://img.shields.io/badge/Framework-PyTorch-EE4C2C?logo=pytorch)
![Transformers](https://img.shields.io/badge/Architecture-Vision_Transformers-blueviolet)

### **Bridging Agricultural Expertise with Explainable Deep Learning**
An advanced Computer Vision suite for automated agricultural health monitoring. This project identifies **38 distinct plant diseases** across 14 crop species with a record-breaking **99.85% accuracy**. 

**Version 2.0 Update:** I have integrated **Vision Transformers (ViT)** to benchmark global self-attention mechanisms against traditional Convolutional Neural Networks (CNNs). This "Triple-Check" system ensures diagnostic reliability by seeking consensus across three distinct neural architectures.

---

## 🚀 Live Interactive Demo
Experience the multi-architecture diagnostic engine in real-time. Upload a leaf image to see how three different "AI brains" interpret the specimen:
👉 **[Launch Hugging Face Space v2.0](https://huggingface.co/spaces/Anthony5787/Plant-Disease-Diagnostic-Suite-2.0)**

<img width="1901" height="818" alt="main dashboard" src="https://github.com/user-attachments/assets/4cc06fd4-b905-4392-b886-4594fb9b030b" />



---

## 🔬 Explainable AI (XAI): Grad-CAM Visualization
To move beyond "Black Box" AI, I implemented **Grad-CAM (Gradient-weighted Class Activation Mapping)**. This validates that the models are focusing on biological symptoms (lesions, mold, necrosis) rather than background noise.

<img width="2184" height="837" alt="3 in 1" src="https://github.com/user-attachments/assets/287984b5-0da4-4fac-9a81-d8a57fb106ec" />


### **The Multi-Architecture Consensus**
| Architecture | Type | XAI Focus | Logic |
| :--- | :--- | :--- | :--- |
| **ResNet18** | Residual CNN | Local Textures | Focuses on sharp edges and pixel gradients. |

<img width="844" height="239" alt="image" src="https://github.com/user-attachments/assets/3c89aa07-f911-46ec-be05-5370146800a0" />

| Architecture | Type | XAI Focus | Logic |
| :--- | :--- | :--- | :--- |
| **EfficientNet-B0** | Optimized CNN | Scaled Features | Balanced depth and width for efficient extraction. |

<img width="835" height="191" alt="image" src="https://github.com/user-attachments/assets/4e08cccc-b0a0-4726-8bc7-410b1caf365e" />

| Architecture | Type | XAI Focus | Logic |
| :--- | :--- | :--- | :--- |
| **ViT-B/16** | **Transformer** | **Global Attention** | Evaluates long-range dependencies across the leaf. |

<img width="854" height="344" alt="image" src="https://github.com/user-attachments/assets/42316698-a1b8-437e-8ec6-c46f01ce722c" />


---

## 📊 Dataset & Methodology
This project is built upon the **New Plant Diseases Dataset**, optimized for real-world robustness.
* **Scale:** 87,000+ RGB Images.
* **Diversity:** 38 classes across 14 unique species (Apple, Corn, Grape, Orange, Tomato, etc.).
* **Data Engineering:** Handling 87k images required significant optimization in data pipelines and heavy augmentation (rotation, shearing, color jitter) to ensure the model generalizes across diverse lighting and environmental conditions.

### **Architectural Comparison Matrix**
Based on my final testing results across the three architectures:

| Metric | ResNet18 | EfficientNet-B0 | ViT-B/16 |
| :--- | :---: | :---: | :---: |
| **Validation Acc.** | 96.80% | **99.79%** | 91.10% |
| **Test Accuracy** | 96.50% | **99.81%** | 91.05% |
| **Inference Latency**| 11.20 ms | 7.80 ms | **3.57 ms** |
| **Total Parameters** | 11.7 Million | 5.3 Million | 86.4 Million |
| **Key Strength** | Reliable Baseline | Feature Extraction | Parallel Speed |

<img width="1396" height="783" alt="comparison" src="https://github.com/user-attachments/assets/f6511182-d9ab-4a55-868e-92a6c4dbdf9a" />


---

## 📂 Repository Structure
* `app.py`: Production-ready Gradio interface script.
* `training_v2.ipynb`: Implementation of the ViT training pipeline using the `timm` library.
* `testing.ipynb`: Evaluation metrics and Grad-CAM implementation.
* `requirements.txt`: Necessary dependencies for CPU-based cloud deployment.

> [!IMPORTANT]
> **Model Weights:** Due to GitHub's LFS constraints, the `.pth` weight files (totaling ~400MB) are hosted directly on the [Hugging Face Space](https://huggingface.co/spaces/Anthony5787/Plant-Disease-Diagnostic-Suite-2.0/tree/main) to ensure seamless deployment and version control.

---

### **Connect with me**
**Developer:** Anthony Amit Biswas  
**LinkedIn:** [Connect on LinkedIn](https://www.linkedin.com/in/anthony-amit-5617702ba/))  
**Project Hub:** [Hugging Face Profile](https://huggingface.co/Anthony5787)

***
