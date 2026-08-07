# Automated Steel Surface Defect Detection Using CNN

## Project Overview

Manufacturing industries require automated quality inspection systems to identify surface defects in steel products. Manual inspection is time-consuming and prone to human error.

This project uses **Deep Learning and Computer Vision** to automatically detect and classify steel surface defects using a **Convolutional Neural Network (CNN)** model.

The system can classify steel defects into different categories and can be used as an AI-assisted visual inspection solution in manufacturing environments.

## Problem Statement

To develop an automated defect detection system that can identify and classify defects present on steel surfaces using image data.

## Objectives

* Detect defects from steel surface images
* Classify images into different defect categories
* Build a CNN-based image classification model
* Deploy the trained model using Streamlit for real-time prediction

## Defect Classes

The model classifies six types of steel surface defects:

* Crazing
* Inclusion
* Patches
* Pitted Surface
* Rolled-in Scale
* Scratches

## Technologies Used

### Programming Language

* Python

### Deep Learning

* TensorFlow
* Keras
* Convolutional Neural Network (CNN)

### Image Processing

* OpenCV
* PIL

### Data Processing

* NumPy
* Pandas
* Scikit-learn

### Deployment

* Streamlit

## Project Structure

steel-surface-defect-detection-cnn/

│
├── dataset/
│
├── notebooks/
│   └── steel_defect_cnn_training.ipynb
│
├── models/
│   └── steel_defect_model.keras
│
├── app.py
├── prediction.py
├── requirements.txt
├── README.md
└── .gitignore

## Project Workflow

1. Data Collection
2. Image Preprocessing

   * Resize images
   * Convert color format
   * Normalize pixel values
3. Data Splitting
4. CNN Model Building
5. Model Training
6. Model Evaluation
7. Model Deployment using Streamlit


## CNN Architecture

The CNN model consists of:

* Convolution Layers for feature extraction
* MaxPooling Layers for dimensionality reduction
* Flatten Layer
* Fully Connected Dense Layers
* Softmax Output Layer for multi-class classification

Architecture:

Input Image
    |
Conv2D
    |
MaxPooling
    |
Conv2D
    |
MaxPooling
    |
Conv2D
    |
Flatten
    |
Dense Layers
    |
Softmax Output (6 Classes)


## 📊 Model Performance

The model was evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

### Final Performance

| Metric | Score |
|---|---|
| Test Accuracy | 99.30% |
| Macro Precision | 0.99 |
| Macro Recall | 0.99 |
| Macro F1-score | 0.99 |

### Confusion Matrix

The confusion matrix shows that the CNN model correctly classified almost all steel surface defect images, with only 2 misclassifications out of 288 test images.

<img width="194" height="124" alt="image" src="https://github.com/user-attachments/assets/5e10e468-41ad-4fc9-9f1d-c13cab153399" />


## Deployment

The trained model is deployed using Streamlit.

Run the application:

streamlit run app.py


Upload a steel surface image and the model predicts the defect category with confidence score.


## Sample Prediction

Example:

<img width="291" height="343" alt="image" src="https://github.com/user-attachments/assets/b3f90f4a-9d4a-41e5-a7b0-df15cd2bced9" />


## Future Improvements

* Add object detection for locating defects
* Train on larger industrial datasets
* Deploy using cloud platforms
* Integrate with real-time camera inspection systems

## Author

Harish Alakuntla
