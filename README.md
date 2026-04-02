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

<p align="center">
  <img src="[https://github.com/user-attachments/assets/e05ae507-1afa-49a9-b382-f04303ce5979](https://github.com/user-attachments/assets/e05ae507-1afa-49a9-b382-f04303ce5979)" width="100%" alt="Main Dashboard Preview">
  <br>
  <i><b>The Production Dashboard:</b> Real-time identification of plant species, disease classification, and health status.</i>
</p>

---

## 🔬 Explainable AI (XAI): Grad-CAM Visualization
To move beyond "Black Box" AI, I implemented **Grad-CAM (Gradient-weighted Class Activation Mapping)**. This validates that the models are focusing on biological symptoms (lesions, mold, necrosis) rather than background noise.

### **The Multi-Architecture Consensus**
| Architecture | Type | XAI Focus | Logic |
| :--- | :--- | :--- | :--- |
| **ResNet18** | Residual CNN | Local Textures | Focuses on sharp edges and pixel gradients. |
| **EfficientNet-B0** | Optimized CNN | Scaled Features | Balanced depth and width for efficient extraction. |
| **ViT-B/16** | **Transformer** | **Global Attention** | Evaluates long-range dependencies across the leaf. |

<p align="center">
  <img src="[https://github.com/user-attachments/assets/ae765ef9-0557-47e5-a055-a04458645e04](https://github.com/user-attachments/assets/ae765ef9-0557-47e5-a055-a04458645e04)" width="100%" alt="Triple Heatmap Comparison">
  <br>
  <i><b>Visualizing the "Why":</b> Side-by-side comparison of attention maps. Note how the Transformer (Right) evaluates the global context of the leaf structure compared to the localized focus of the CNNs.</i>
</p>

---

## 📊 Dataset & Methodology
This project is built upon the **New Plant Diseases Dataset**, optimized for real-world robustness.
* **Scale:** 87,000+ RGB Images.
* **Diversity:** 38 classes across 14 unique species (Apple, Corn, Grape, Orange, Tomato, etc.).
* **Data Engineering:** Handling 87k images required significant optimization in data pipelines and heavy augmentation (rotation, shearing, color jitter) to ensure the model generalizes across diverse lighting and environmental conditions.

### **Performance Benchmarks**
| Model | Accuracy | F1-Score | Parameter Count |
| :--- | :---: | :---: | :--- |
| **ViT-B/16 (v2.0)** | **99.85%** | **0.999** | ~86M |
| **EfficientNet-B0** | 99.82% | 0.998 | ~5.3M |
| **ResNet18** | 99.58% | 0.996 | ~11.7M |

<p align="center">
  <img src="[https://github.com/user-attachments/assets/d8994216-197a-4183-a351-b31ad49cbd2b](https://github.com/user-attachments/assets/d8994216-197a-4183-a351-b31ad49cbd2b)" width="80%" alt="Performance Results">
</p>

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
**LinkedIn:** [Connect on LinkedIn](https://www.linkedin.com/in/YOUR_LINKEDIN_ID)  
**Project Hub:** [Hugging Face Profile](https://huggingface.co/Anthony5787)

***
