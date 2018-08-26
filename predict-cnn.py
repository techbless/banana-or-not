import os
import numpy as np
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.models import Sequential, load_model

img_width, img_height = 250, 250
model_path = './models/model.h5'
model_weights_path = './models/model_wieght.h5'
model = load_model(model_path)
model.load_weights(model_weights_path)

TARGET_PATH = "./target.jpg"

def predict(file):
  x = load_img(file, target_size=(img_width,img_height))
  x = img_to_array(x)
  x = np.expand_dims(x, axis=0)
  array = model.predict(x)
  #result = array[0]
  print(array)
  
  if array[0][0] == 1:
    print("Predicted answer: BANANA")
    answer = 'banana'
  else:
    print("Predicted answer: OTHER")
    answer = 'other'


print("-------------------------------")
predict("./banana (1).jpg")
predict("./banana (2).jpg")
predict("./banana (3).jpg")
predict("./banana (4).jpg")
predict("./banana (5).jpg")
print("-------------------------------")
predict("./other (1).jpg")
predict("./other (2).jpg")
predict("./other (3).jpg")
predict("./other (4).jpg")
predict("./other (5).jpg")

