import tensorflow as tf
import pathlib
import matplotlib.pyplot as plt
import numpy as np
import config

model = tf.keras.models.load_model('saved_model/gen1_1')


def predict(image_path):
  image = tf.keras.preprocessing.image.load_img(image_path,color_model=config.color_mode,
                                                target_size=(config.img_height,config.img_width))
  input_arr = tf.keras.preprocessing.image.img_to_array(image)
  input_arr = np.array([input_arr])  # Convert single image to a batch.
  predictions = model.predict(input_arr)
  tf.keras.losses.MeanAbsoluteError()

  return predictions

# print(predict("dataset/facture/inv-0003.jpg"))
# print(predict("dataset/other/inv-0000.jpg"))
# print(predict("dataset/other/inv-0001.jpg"))
# print(predict("dataset/other/inv-0002.jpg"))
# print(predict("dataset/other/inv-0003.jpg"))