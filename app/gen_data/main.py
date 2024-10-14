import os, glob

from PIL import Image
from sklearn.model_selection import train_test_split
import numpy as np


klasses = ["toy_poodle", "border_collie", "pomeranian"]
num_classes = len(klasses)
image_size = 50

X = []
Y = []

for index, klass in enumerate(klasses):
    files = glob.glob(f"./data/raw/{klass}/*.jpg")
    for i, file in enumerate(files):
        if i >= 200:
            break
        image = Image.open(file)
        image = image.convert("RGB")
        image = image.resize((image_size, image_size))
        data = np.asarray(image)
        X.append(data)
        Y.append(index)

X = np.array(X)
Y = np.array(Y)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y)

np.savez("./data/interim/dogs.npz", X_train=X_train, X_test=X_test, Y_train=Y_train, Y_test=Y_test)
