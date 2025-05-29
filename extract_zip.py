import zipfile
import os

# === Train ZIP Extraction ===
train_zip_path = r"C:\Users\Rajeshwari\OneDrive\Desktop\SVM\train.zip"
train_extract_to = r"C:\Users\Rajeshwari\OneDrive\Desktop\SVM\train"

if not os.path.exists(train_extract_to):
    print("Extracting train.zip... Please wait.")
    with zipfile.ZipFile(train_zip_path, 'r') as zip_ref:
        zip_ref.extractall(train_extract_to)
    print("Train extraction complete!")
else:
    print("Train folder already exists. Skipping.")

# === Test1 ZIP Extraction ===
test_zip_path = r"C:\Users\Rajeshwari\OneDrive\Desktop\SVM\test1.zip"
test_extract_to = r"C:\Users\Rajeshwari\OneDrive\Desktop\SVM\test1"

if not os.path.exists(test_extract_to):
    print("Extracting test1.zip... Please wait.")
    with zipfile.ZipFile(test_zip_path, 'r') as zip_ref:
        zip_ref.extractall(test_extract_to)
    print("Test1 extraction complete!")
else:
    print("Test1 folder already exists. Skipping.")
