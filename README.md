# PRODIGY_ML_TASK3
Task 3 – Image Classification Using SVM Implemented a Support Vector Machine (SVM) model to classify cat and dog images from the Kaggle dataset. The task involved image preprocessing, model training, evaluation, and visualization using Python and scikit-learn.

# SVM Classification Internship Task

Welcome to my internship project of  Task 3, where I implemented a Support Vector Machine (SVM) classifier to solve a real-world machine learning problem.

---

In this project, I developed a machine learning pipeline using SVM to classify data from given training and testing datasets. The key objectives were:

- To preprocess and extract data from zipped files  
- To build, train, and evaluate an SVM classification model  
- To deliver clean, maintainable, and well-documented code  

This repository contains the core scripts and configuration files necessary to run the project.

---

## Repository Contents

- **`extract_zip.py`**  
  Python script to automate the extraction of zipped dataset files (`train.zip` and `test1.zip`). Run this before training to prepare your data folders.

- **`svm_classifier.py`**  
  Main script that implements the SVM model, handles training and prediction on the datasets.

- **`sampleSubmission.csv`**  
  Example submission file to showcase the format required for model predictions.

- **`.gitignore`**  
  Ensures large dataset files (zip files and extracted folders) are excluded from version control to keep the repository clean and efficient.

---

## Dataset & Large Files Handling

Due to file size constraints, the large datasets (`train.zip`, `test1.zip`) and their extracted folders (`train/`, `test1/`) are **excluded** from this GitHub repository using `.gitignore`. This avoids uploading heavy files that could slow down or break Git operations.

## Accessing the Dataset Files

Due to file size limits, the datasets are hosted on Google Drive.

Please download the files from the links below:

- [Download train.zip] (https://drive.google.com/file/d/1tJZGm79fEbr4hB6LMhGhOIvOka5BuWwa/view?usp=sharing).
- [Download test1.zip] (https://drive.google.com/file/d/1mHrfGRjejHeQ5KD9bEhA76RGMTKuyDxF/view?usp=sharing).

After downloading, place the zip files in the root directory of this project and run the following command to extract them:


python extract_zip.py


### How to Access and Use the Dataset:

1. **Download the zipped datasets** (`train.zip` and `test1.zip`) separately as shared by the internship team or from the designated location.  
2. Place the downloaded `.zip` files inside the root folder of this project.  
3. Run the `extract_zip.py` script to automatically extract the zipped contents into `train/` and `test1/` directories.  
4. Once extracted, you can run the `svm_classifier.py` script to train and test the SVM model on the datasets.

---

## Project Status & Demonstration

- The code is fully functional, clean, and ready for evaluation.  
- I have uploaded a **video demonstration of the model’s output** on my LinkedIn profile for your convenience:  
  [LinkedIn Video Demo] (https://www.linkedin.com/posts/yada-rajeshwari-022b8530b_machinelearning-svm-computervision-activity-7331378423610683394-Y7Wf?utm_source=share&utm_medium=member_desktop&rcm=ACoAAE8EndoBu65vprjIb-hNbUtHSPP2hiW1WU8) .
  
  (Please check the video to see the step-by-step working and results of the model in action.)

---

## How to Run


# Extract dataset zip files
python extract_zip.py

# Train and evaluate the SVM classifier
python svm_classifier.py
