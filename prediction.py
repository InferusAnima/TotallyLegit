import tensorflow as tf
import pathlib
import matplotlib.pyplot as plt
import numpy as np
import config

model = tf.keras.models.load_model('models')

batch_size = 32
img_height = 500
img_width = 500

def predict(image_path):
  normalization_layer = tf.keras.layers.Rescaling(1. / 255)
  image = tf.keras.preprocessing.image.load_img(image_path,color_mode="grayscale",
                                                img_height=config.img_height,img_width=config.img_width)
  input_arr = tf.keras.preprocessing.image.img_to_array(image)
  input_arr = normalization_layer(input_arr)
  input_arr = np.array([input_arr])  # Convert single image to a batch.
  predictions = model.predict(input_arr)
  tf.keras.losses.MeanAbsoluteError()

  print(predictions)