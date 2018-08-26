# Banana_Image_Classifier
  It is Image Classifier that recognize banana. but It could be used for multi categorical classifier 
  because of using not sigmoid or something, but softmax. If you want to use as multi categorical classifier.
  Add your own additional image data_set (which is categorized with directory name) to './data/train/' and './data/validation/'.


## Status

[![Travis](https://img.shields.io/jenkins/s/https/jenkins.qa.ubuntu.com/view/Precise/view/All%20Precise/job/precise-desktop-amd64_default.svg)]() [![apm](https://img.shields.io/apm/l/vim-mode.svg)]()

## What you need before starting

  * python
  * tensorflow
  * keras
  * numpy
  * Anaconda (recommended)
  
  
## Image Dataset Information

  Image Dataset should be 250px squared size.  
  If you want to use other Image Size, Change values of variable in train-binary.py
  
  ```python
    # dimensions of our images.
    img_width, img_height = 250, 250 # Change 250 to your own data_set image size value.
  ```
  
  
## Dataset Directory-Tree
  
  First of all, collect your own training data and replace origin banana and other dataset with your own. The dataset is categorized with directory name and could be multi category as well as binomial category.
  
```
./data/  
train/  
  banana/  
    banana (1).jpg  
    banana (2).jpg  
    ...  
  other/  
    other (1).jpg  
    other (2).jpg  
    ...  
validation/  
  banana/  
    banana (1).jpg  
    banana (2).jpg  
    ...  
  other/  
    other (1).jpg  
    other (2).jpg  
    ...  
 ```
  Second of all, train your dataset by running train script.
  
  ```
  python src/train-binary2.py
  ```
 
 the model and weights will be saved to './model'
 
  Last, Predict any image with your learned model.
  
  ```
  python src/predict-binary2.py
  ```