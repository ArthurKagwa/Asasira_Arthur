# tensorflow , numpy , matplotlib, keras, sklearn
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.image import ImageDataGenerator # type: ignore
from tensorflow.keras.models import Sequential # type: ignore
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout # type: ignore
from tensorflow.keras.optimizers import Adam # type: ignore
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint       # type: ignore

print("TensorFlow version:", tf.__version__)
print("NumPy version:", np.__version__)
print("Keras version:", keras.__version__)

# set random seeds for reproducibility
tf.random.set_seed(42)
np.random.seed(42)

IMAGE_SIZE = (256,256)
BATCH_SIZE = 32