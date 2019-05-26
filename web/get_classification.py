import json
import random
import sys
import time
import base64
import cv2
from keras.models import load_model
import numpy as np
import json

def read_json_class_names():
  with open('class_labels/2020-05-25__21:33:02.665517-data.json') as f:
    data = json.load(f)
    return list(data.keys())

CLASS_NAMES = read_json_class_names()
print('class names: {}'.format(CLASS_NAMES))

model = load_model('models/weights-improvement-2019-05-25__21:33:02.665517-10-0.97.hdf5')

def readb64(uri):
  encoded_data = uri.split(',')[1]
  nparr = np.fromstring(base64.b64decode(encoded_data), np.uint8)
  img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
  return img

while True:
  request = input('Enter base64 image: ').split('||')
  client_id = request[0]
  base64_image = request[1]

  image = readb64(base64_image)
  image = cv2.resize(image, (150, 150))
  cv2.imwrite('screenshot.jpg', image)
  image = image / 255
  image = np.array([image])

  predictions = model.predict(image)[0]
  top_predictions = predictions.argsort()[::-1][:3]

  data = []
  for index in top_predictions:
    data.append({
      'value': ('Letter ' if index < 26 else '') + CLASS_NAMES[index],
      'probability': predictions[index].item(),
    })
  sys.stderr.write(client_id + '||' + json.dumps(data))
