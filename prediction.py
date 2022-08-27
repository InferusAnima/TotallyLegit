import os
import pathlib
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

img_height = 500
img_width = 500
img_size = (img_height, img_width)
batch_size = 32
epochs = 5
data_dir = pathlib.Path('./dataset')
num_classes = len(os.listdir(data_dir))
name = 'gen_1'


def learn(model_name):
    train_ds = tf.keras.utils.image_dataset_from_directory(
      data_dir,
      validation_split=0.2,
      subset="training",
      seed=123,
      image_size=img_size,
      batch_size=batch_size,
      color_mode="grayscale")

    val_ds = tf.keras.utils.image_dataset_from_directory(
      data_dir,
      validation_split=0.1,
      seed=123,
      subset="validation",
      image_size=img_size,
      batch_size=batch_size,
      color_mode="grayscale")

    AUTOTUNE = tf.data.AUTOTUNE
    train_ds = train_ds.cache().prefetch(buffer_size=AUTOTUNE)
    val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)
    input_1 = tf.keras.layers.Input(shape=(img_height, img_width,1), name='photo')
    #input_2 = tf.keras.layers.Input(shape=1, name='text')
    tf.keras.layers.Rescaling(1. / 255)(input_1)
    tf.keras.layers.Conv2D(16, 3, padding='same', activation='relu')(input_1)
    tf.keras.layers.MaxPooling2D()(input_1)
    tf.keras.layers.Conv2D(32, 3, padding='same', activation='relu')(input_1)
    tf.keras.layers.MaxPooling2D()(input_1)
    tf.keras.layers.Conv2D(64, 3, padding='same', activation='relu')(input_1)
    tf.keras.layers.MaxPooling2D()(input_1)
    f1 = tf.keras.layers.Flatten()(input_1)
    x = tf.keras.layers.concatenate([f1])
    x = tf.keras.layers.Dense(128, activation='relu')(x)
    model = tf.keras.Model(inputs=[input_1], outputs=[x])

    model.compile(
      optimizer='adam',
      loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
      metrics=['accuracy'])

    history = model.fit(
      train_ds,
      validation_data=val_ds,
      epochs=epochs,
    )

    model.save(f'models/{model_name}/')

    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']

    loss = history.history['loss']
    val_loss = history.history['val_loss']

    epochs_range = range(epochs)

    plt.figure(figsize=(8, 8))
    plt.subplot(1, 2, 1)
    plt.plot(epochs_range, acc, label='Training Accuracy')
    plt.plot(epochs_range, val_acc, label='Validation Accuracy')
    plt.legend(loc='lower right')
    plt.title('Training and Validation Accuracy')

    plt.subplot(1, 2, 2)
    plt.plot(epochs_range, loss, label='Training Loss')
    plt.plot(epochs_range, val_loss, label='Validation Loss')
    plt.legend(loc='upper right')
    plt.title('Training and Validation Loss')
    plt.show()


def predict(model_name, image_path):
    model = tf.keras.models.load_model(f'models/{model_name}')
    probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])
    image = tf.keras.preprocessing.image.load_img(image_path, color_mode="grayscale", target_size=img_size)
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    # input_arr = normalization_layer(input_arr)
    input_arr = np.array([input_arr])
    predictions = probability_model.predict(input_arr)
    return predictions[0]


def test(model_name):
    data = '220120100022020110000010201020001210010101002100021100000000120110002010000001020020201020020210102000100' \
           '200020122100200010002020010201021110000010011010000000000101000102002000100000021001002020221120120021102' \
           '210100001110010200011000000110100001001001202100010001020110100020211120001000100001101100202020000012211' \
           '10'
    result = 0
    try:
        for i, img in enumerate(os.listdir('./test_images')):
            pred = predict(model_name, f'./test_images/{img}')
            print(img, pred, sep='\t', end='\t')
            if pred[0] == max(pred) and data[i] == '0':
                result += 1
                print('Bill')
            elif pred[1] == max(pred) and data[i] == '1':
                result += 1
                print('Facture')
            elif pred[2] == max(pred) and data[i] == '2':
                result += 1
                print('Error')
            else:
                print('X')
    except KeyboardInterrupt:
        print('Тестирование прервано')
    print(f'{round((result / len(data) * 100), 4)}% Accuracy')
# print(learn("gen_1"))