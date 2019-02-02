import json
import random
import sys
import time
import base64
import cv2
from keras.models import load_model
import numpy as np

ALPHABET = [
  'A','B','C','D','E','F','G','H','I','J','K','L','M',
  'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
  'del','space','nothing',
]

model = load_model("weights-improvement-10-0.83.hdf5")

def readb64(uri):
  encoded_data = uri.split(',')[1]
  nparr = np.fromstring(base64.b64decode(encoded_data), np.uint8)
  img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
  return img

while True:
  base64_image = input('Enter base64 image: ')
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
      'value': ('Letter ' if index < 26 else '') + ALPHABET[index],
      'probability': predictions[index].item(),
    })
  sys.stderr.write(json.dumps(data))
