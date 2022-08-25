import tensorflow as tf
import pathlib
import matplotlib.pyplot as plt
import numpy as np

model = tf.keras.models.load_model('saved_model/my_model')

batch_size = 32
img_height = 500
img_width = 500

def predict(image_path):
  image = tf.keras.preprocessing.image.load_img(image_path)
  input_arr = tf.keras.preprocessing.image.img_to_array(image)
  input_arr = np.array([input_arr])  # Convert single image to a batch.
  predictions = model.predict(input_arr)
  tf.keras.losses.MeanAbsoluteError()

  print(predictions)