# PRODIGY_ML_TASK3 – Image Classification Using SVM 🐶🐱

This project was developed as part of my internship with **Prodigy InfoTech**, under **Machine Learning Task 3**. The objective was to implement an image classification system using a **Support Vector Machine (SVM)** to classify images of **cats and dogs** using a dataset from **Kaggle**.

---

## 📌 Project Description

The goal of this project is to demonstrate my ability to solve real-world machine learning problems using classical ML techniques. I used the **Support Vector Machine (SVM)** algorithm to classify images of cats and dogs based on pixel-level features. While deep learning is typically preferred for image tasks, this project focuses on building a **simple yet effective image classifier** using SVM, highlighting traditional ML workflow.

The major steps in this project include:

- **Data Preparation**: 
  - Handling large `.zip` datasets for training and testing
  - Extracting image files from `train.zip` and `test1.zip`
  - Resizing and flattening images into vectors suitable for ML

- **Model Building**:
  - Feature extraction by converting images to grayscale and resizing to 64x64
  - Flattening pixel data into 1D feature vectors
  - Using `SVM (sklearn.SVC)` with a linear kernel for classification

- **Model Evaluation**:
  - Splitting the dataset into training and validation sets
  - Accuracy and classification reports
  - Predictions on test data for submission

This project demonstrates how **traditional ML models can still be effective** when applied with proper preprocessing and structured data pipelines.

---

## 📁 Repository Contents

- `extract_zip.py`  
  Python script to **automatically extract** dataset files (`train.zip` and `test1.zip`) into usable folders.

- `svm_classifier.py`  
  Core ML script that builds the image classifier using **SVM**, handles preprocessing, training, and prediction.

- `sampleSubmission.csv`  
  A sample template showing how predictions should be formatted for submission.

- `.gitignore`  
  Keeps large files like datasets (`train.zip`, `test1.zip`) and extracted folders from being tracked in Git.

---

## 📦 Dataset & Large Files

Due to GitHub size restrictions, the following files are **excluded** from the repo:

- `train.zip`, `test1.zip`
- Extracted folders: `train/`, `test1/`

To use the full project, please download them from Google Drive:

- 🔗 [Download `train.zip`](https://drive.google.com/file/d/1tJZGm79fEbr4hB6LMhGhOIvOka5BuWwa/view?usp=sharing)  
- 🔗 [Download `test1.zip`](https://drive.google.com/file/d/1mHrfGRjejHeQ5KD9bEhA76RGMTKuyDxF/view?usp=sharing)

Place both files in the root folder of this project.

---

## 🚀 How to Run This Project

1. Download the zip files linked above.
2. Place them in the project’s root directory.
3. Extract them using:

   python extract_zip.py


4. Train and evaluate the SVM model:


   python svm_classifier.py

---

## 📊 Output & Results

The SVM classifier was able to distinguish between cat and dog images with reasonable accuracy, considering the limitations of classical ML for image tasks. Key techniques such as grayscale conversion, resizing, and flattening were used to convert image data into meaningful input for the SVM model.

---

## 🎥 Demonstration Video

I’ve uploaded a **step-by-step video demonstration** on my LinkedIn profile showing:

* Dataset extraction
* Model training
* Classification results

▶️ [Watch Demo on LinkedIn](https://www.linkedin.com/posts/yada-rajeshwari-022b8530b_machinelearning-svm-computervision-activity-7331378423610683394-Y7Wf)

---

## ✅ Project Status

* ✅ Fully implemented and functional
* ✅ Clean and modular Python code
* ✅ Dataset handled via external download
* ✅ Output demo available for evaluation

---

Feel free to review the code and steps above. This project was a fantastic learning experience during my internship, and I hope it reflects my skills in data preparation, classical machine learning, and project structuring.
