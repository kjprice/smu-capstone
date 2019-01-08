# SMU Capstone

The primary goal of this project is train a model to recognize various sign languages using Convolution Neural Networks.

## Steps
1. First create the following folder structure (creating folder called "data" with the two subfolders):

```
data
 - fabricated
 - original
```

2. pull the [data](https://www.kaggle.com/grassknoted/asl-alphabet) down into the folder "data/original"

3. Run the preprocessing step to [split the data](notebooks/Preprocessing/ASL_Alphabet-Split.ipynb) into training/test datasets.

4. Run the preprocessing step to [add various data augmentations](notebooks/Preprocessing/ASL_Alphabet-Processing.ipynb) to the datasets.

### Data Sets

 - [11K Images of hands](https://sites.google.com/view/11khands)
 - [87K Kaggle Images of ASL Alphabet](https://www.kaggle.com/grassknoted/asl-alphabet)