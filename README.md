# 🚧 AI-Based Concrete Crack Detection System
### Deep Learning + Explainable AI for Automated Infrastructure Inspection

---

## 🚀 Overview

Manual inspection of concrete structures is time-consuming, subjective, and prone to human error.  
This project presents an **AI-powered crack detection system** that automates inspection using deep learning and computer vision.

Built using a fine-tuned **ResNet-18 model**, the system classifies images as **Crack / No Crack** and provides **visual explanations using Grad-CAM**, making predictions interpretable and reliable.

---

## 💡 Key Highlights

- ✅ **95.7% Accuracy** on crack classification  
- ⚡ Reduced manual inspection effort significantly  
- 🧠 Explainable AI using **Grad-CAM visualization**  
- 🏗️ Designed for **real-world infrastructure inspection scenarios**  
- 🔍 Identifies crack regions instead of just predicting labels  

---

## 🎯 Problem Statement

Traditional crack detection methods:
- Require manual inspection by experts  
- Are slow and expensive  
- Lack consistency and scalability  

👉 This system solves these issues using **automated, scalable AI-based inspection**

---

## 🧠 Solution Approach

This project builds an end-to-end pipeline



### 🔧 Model Details
- **Architecture:** ResNet-18 (pretrained, fine-tuned)
- **Task:** Binary Classification (Crack / No Crack)
- **Framework:** PyTorch
- **Explainability:** Grad-CAM

---

## 📊 Results

| Metric        | Value   |
|--------------|--------|
| Accuracy     | 95.7%  |
| Model Type   | CNN (ResNet-18) |
| Output       | Crack / No Crack |

👉 The model performs reliably on real-world crack images and highlights defect regions effectively.

---

## 🔍 Explainability with Grad-CAM

Unlike traditional black-box models, this system provides **visual explanations**:

- Highlights crack-affected regions  
- Improves trust in predictions  
- Assists engineers in validation  

---

## 🖼️ Sample Output
<img width="1567" height="744" alt="WhatsApp Image 2026-05-03 at 9 20 18 PM" src="https://github.com/user-attachments/assets/69975127-d5f9-4bdd-9ba2-abf17927aed6" />
<img width="993" height="673" alt="Screenshot 2025-07-20 124943" src="https://github.com/user-attachments/assets/d8507885-40c3-48f1-a56d-97f0be20871c" />
<img width="732" height="408" alt="Screenshot 2025-07-20 124556" src="https://github.com/user-attachments/assets/7af27364-1fab-4fd4-abcb-2114d6efd5e3" />
<img width="1920" height="1080" alt="Screenshot 2025-06-24 151134" src="https://github.com/user-attachments/assets/bd0803da-7c0e-4284-951e-4a61116ef4c8" />



## 📁 Dataset

- Concrete surface image dataset  
- Classes:
  - Crack  
  - No Crack  

### Preprocessing:
- Image resizing  
- Normalization  
- Data augmentation  

---

## 🛠️ Tech Stack

- Python  
- PyTorch  
- OpenCV  
- NumPy  
- Matplotlib  
- Grad-CAM  

---

## ⚙️ How to Run

```bash
git clone https://github.com/Janicebenita/Crack-detection-using-deep-learning-.git
cd Crack-detection-using-deep-learning-
pip install -r requirements.txt
