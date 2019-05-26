# SMU Capstone

The primary goal of this project is train a model to recognize various sign languages using Convolution Neural Networks.

##  Original Steps
We originally trained our model from [87K Kaggle Images of ASL Alphabet](https://www.kaggle.com/grassknoted/asl-alphabet). Which is greaat in the faact that it is ready-to-go. We were able to achieve 100% accuracy using this dataset. However, there is considerable genetic bias within this dataset (as it is taken from a single caucasion individual). In an attempt to broaden the scope of the dataset, follow below to create your own dataset.

1. First create the following folder structure (creating folder called "data" with the two subfolders):

```
data
 - fabricated
 - original
```

2. pull the [data](https://www.kaggle.com/grassknoted/asl-alphabet) down into the folder "data/original"

3. Run the preprocessing step to [split the data](notebooks/Preprocessing/ASL_Alphabet-Split.ipynb) into training/test datasets.

4. Run the preprocessing step to [add various data augmentations](notebooks/Preprocessing/ASL_Alphabet-Processing.ipynb) to the datasets.


## New DataSet
We can create our own dataset of images. To do this we can follow these steps:

1. Record a movie of an actor performing the handsign (this can easily be done with QuickTime for example).
2. Save the movie in the format `{sign}--{actor}--{version}.mov` within the directory `data/original/movies/` as an example `data/original/movies/A--kj--1.mov`. This would be interpreted as "The `first` movie using sign `A` performed by `kj`".
3. Now that we have a series of movies, we can extract images from the frames of the movie by running `notebooks/Preprocessing/Extract Images From Video.ipynb`. This will leave us with a series of images within the directory `data/fabricated/movies/{sign}/` and the filename `{actor}-{version}-{count}.png` (example `kj-1-0.png`).
4. Run the preprocessing step to [split the data](notebooks/Preprocessing/ASL_Alphabet-Split.ipynb) into training/test datasets.
5. Run the preprocessing step to [add various data augmentations](notebooks/Preprocessing/ASL_Alphabet-Processing.ipynb) to the datasets.

## Train The Model
...TODO
