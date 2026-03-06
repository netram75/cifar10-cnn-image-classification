# CIFAR-10 Image Classification using CNN

This project implements a **Convolutional Neural Network (CNN)** to classify images from the **CIFAR-10 dataset**.  
The model is trained using deep learning techniques including **data augmentation** and **batch normalization** to improve performance and generalization.

---

## Project Overview

The goal of this project is to build a deep learning model capable of classifying images into one of the **10 CIFAR-10 classes**.

The project demonstrates a complete deep learning workflow:

- Dataset exploration
- Building a baseline CNN model
- Improving model performance with **data augmentation**
- Stabilizing training using **batch normalization**
- Evaluating performance with **accuracy curves, confusion matrix, and error analysis**

---

## Dataset

The model is trained on the **CIFAR-10 dataset**, a widely used benchmark dataset for computer vision tasks.

Dataset characteristics:

- **60,000 images**
- **10 classes**
- **32 × 32 RGB images**

Classes included in the dataset:
Airplane
Automobile
Bird
Cat
Deer
Dog
Frog
Horse
Ship
Truck

---

## Model Architecture

The CNN architecture consists of multiple convolutional blocks:

- Convolutional Layers
- ReLU Activation
- Max Pooling
- Batch Normalization
- Fully Connected Dense Layers
- Dropout for regularization

These layers allow the model to learn hierarchical visual features from the input images.

---

## Model Improvements

Three versions of the model were implemented during experimentation:

| Model Version | Test Accuracy |
|---------------|--------------|
| Baseline CNN | ~75% |
| CNN + Data Augmentation | ~78% |
| CNN + Data Augmentation + Batch Normalization | **~80.8%** |

These improvements demonstrate how training techniques can significantly enhance CNN performance.

---

## Results

The final model achieves approximately **80% test accuracy** on the CIFAR-10 dataset using a relatively simple CNN architecture.

Evaluation includes:

- Training vs Validation Accuracy
- Training vs Validation Loss
- Confusion Matrix
- Misclassified Image Analysis

---

## Kaggle Notebook

You can explore the full notebook with explanations and experiments here:

**Kaggle Notebook:**  
https://www.kaggle.com/code/netramfaran/cifar-10-image-classification-using-cnn

---


## Future Improvements

Possible future improvements include:

- Transfer learning using **ResNet / EfficientNet**
- Advanced data augmentation techniques
- Learning rate scheduling
- Early stopping
- Training on larger image datasets

These techniques can push accuracy beyond **90%** on CIFAR-10.

---

## Technologies Used

- Python
- TensorFlow / Keras
- NumPy
- Matplotlib
- Seaborn
- Streamlit (for deployment)

---