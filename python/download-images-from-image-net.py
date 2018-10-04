from itertools import islice
import os
import re
import requests

URL_FILENAME='data/urls.txt'
IMAGE_DIRECTORY='data/images'
NUMBER_URLS=50000


### Extract text from file
def take_top_rows_of_text_file():
  with open(URL_FILENAME) as url_file:
    return list(islice(url_file, NUMBER_URLS))

def split_file_line(file_line):
  try:
    items = re.split('\s+', file_line)
    return items[:2]
  except:
    print('cannot split({})'.format(file_line))
    return [None, None]

### Download Images From Url
def make_sure_image_directory_exists():
  print('trying to create directory(ies) {}'.format(IMAGE_DIRECTORY))
  try:
    os.makedirs(IMAGE_DIRECTORY)
  except:
    print('{} directory already exists'.format(IMAGE_DIRECTORY))

def get_local_filename(id, url):
  file_extension = os.path.splitext(url)[1]
  filename = id + file_extension
  return os.path.join(IMAGE_DIRECTORY, filename)

def download_images_from_urls(file_lines):
  make_sure_image_directory_exists()
  count = 0
  for line in file_lines:
    count += 1
    id, url = split_file_line(line)
    if id is None:
      continue;
    try:
      image = requests.get(url).content
    except:
      print('could not download {}'.format(url))
    filename = get_local_filename(id, url)
    with open(filename, 'wb') as local_file:
      print('downloaded {} of {} "{}"'.format(count, NUMBER_URLS, filename))
      local_file.write(image)

### Main Method
def main():
  lines = take_top_rows_of_text_file()
  download_images_from_urls(lines)
  print(len(lines))
  print(lines[0])

main()