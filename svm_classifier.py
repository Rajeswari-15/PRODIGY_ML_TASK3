import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

# -----------------------------
# Step 1: Load and Preprocess Images
# -----------------------------
def load_images(dataset_path, image_size=(64, 64), max_images=1000):
    X = []
    y = []
    count = 0

    files = os.listdir(dataset_path)
    np.random.shuffle(files)  # Shuffle files for mixed classes

    print(f"Looking inside folder: {dataset_path}")
    print(f"Files found (sample): {files[:10]}")

    for filename in files:
        label = 1 if 'dog' in filename else 0  # 1 = Dog, 0 = Cat
        print(f"Filename: {filename} | Label: {label}")
        img_path = os.path.join(dataset_path, filename)
        img = cv2.imread(img_path)

        if img is not None:
            img = cv2.resize(img, image_size)
            X.append(img.flatten())   # Flatten to 1D
            y.append(label)
            count += 1

        if count >= max_images:
            break

    return np.array(X), np.array(y)

# -----------------------------
# Step 2: Main Function
# -----------------------------
def main():
    # Path to the dataset folder (pointing to inner train folder with images)
    dataset_path = r"C:\Users\Rajeshwari\OneDrive\Desktop\SVM\train\train"

    print("Loading images...")
    X, y = load_images(dataset_path)

    print(f"Loaded {len(X)} images.")
    print("Labels distribution:", np.bincount(y))  # Check classes count

    # Normalize the pixel values
    X = X / 255.0

    # Split into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train SVM classifier
    print("Training SVM classifier...")
    svm = SVC(kernel='linear')  # You can also try kernel='rbf'
    svm.fit(X_train, y_train)

    # Predict on test set
    print("Predicting...")
    y_pred = svm.predict(X_test)

    # Evaluate model
    print("\nEvaluation Results:")
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("\nClassification Report:\n", classification_report(y_test, y_pred))

    # Show predictions visually
    print("\nDisplaying sample predictions...")
    show_predictions(X_test, y_test, y_pred)

# -----------------------------
# Step 3: Visualize Results
# -----------------------------
def show_predictions(X_test, y_test, y_pred, image_size=(64, 64)):
    for i in range(5):
        img = X_test[i].reshape(*image_size, 3)
        plt.imshow(img)
        plt.title(f"Predicted: {'Dog' if y_pred[i] else 'Cat'} | Actual: {'Dog' if y_test[i] else 'Cat'}")
        plt.axis('off')
        plt.show()

# -----------------------------
# Run the script
# -----------------------------
if __name__ == "__main__":
    main()

