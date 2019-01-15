import json
import random
import sys
import time

def random_letter():
  return random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

def random_probability():
  return random.random() * 100

while True:
  image = input('Enter base64 image: ')
  time.sleep(1)
  data = [
    { 'value': random_letter(), 'probability': random_probability() },
    { 'value': random_letter(), 'probability': random_probability() },
    { 'value': random_letter(), 'probability': random_probability() },
  ]
  sortedData = sorted(data, key=lambda k: k['probability'], reverse=True)
  sys.stderr.write(json.dumps(sortedData))
