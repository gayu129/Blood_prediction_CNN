# 🩸 Blood Group Prediction using CNN

A Convolutional Neural Network (CNN)-based machine learning model that predicts an individual's blood group using input features derived from medical and physiological data.

## 📌 Project Overview

This project aims to develop a deep learning model to classify human blood groups (A, B, AB, O) using a dataset of medical attributes. Accurate blood group prediction is crucial for healthcare applications, especially in emergency scenarios and rural diagnostics.

## 🧠 Key Features

- Built using **TensorFlow** and **Keras**
- Utilizes **CNN** architecture for classification
- Performs data preprocessing and normalization
- Evaluates model performance using accuracy and confusion matrix
- Visualizes training history (accuracy and loss)

## 🔧 Tech Stack

- Python
- TensorFlow / Keras
- NumPy
- Pandas
- Matplotlib
- Scikit-learn

## Installation

   1. **Clone the repository:**
        ```bash
        git clone https://github.com/yourusername/blood-group-classification.git
        cd blood-group-classification
        ```

   2. **Install dependencies:**
        ```bash
        pip install -r requirements.txt
        ```

   3. **Add the model:**
        - Place your trained model file named `blood_group_model.h5` in the project root directory.

   4. **Create upload directory (if not auto-created):**
        ```bash
        mkdir -p static/upload
        ```

   ## Usage

   1. **Run the application:**
        ```bash
        python app.py
        ```

   2. **Open your browser and go to:**
        ```
        http://127.0.0.1:5000/
        ```

   3. **Upload an image** and view the predicted blood group.



    
