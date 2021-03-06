<h1 align="center">Deep Computer Vision:<br>
Classification of 10 Image Classes using Convolution Neural Networks and Transfer Learning</h1>
<p align="center"><img src="https://github.com/three14consulting/Python/blob/main/DeepComputerVision/images/Animals-10.JPG?raw=true" height="300"></p>
<h1><a id='0.0'> Project Summary</a></h1>

In this project, I use the [**TensorFlow**](https://www.tensorflow.org/) and [**Keras**](https://keras.io/) APIs to build a [**Convolution Neural Network**](https://en.wikipedia.org/wiki/Convolutional_neural_network) (CNN) to classify the [**Animals-10 dataset**](https://www.kaggle.com/alessiocorrado99/animals10) (from Google Images; consisting of ~27k instances across 10 animal image classes). The dataset is **imbalanced** across the 10 classes (see below).

Rather than build a CNN architecture from scratch (which can be computationally expensive), I leverage neural network weights built from the [**ImageNet**](https://en.wikipedia.org/wiki/ImageNet) database using [**MobileNetV2 CNN architecture**](https://arxiv.org/abs/1801.04381) as the base model (an example of [**Transfer Learning**](https://en.wikipedia.org/wiki/Transfer_learning)).

I then go on to **fine-tune** the model by retraining the **top 10 layers** (of 154 layers), to achieve a classification **accuracy of 93.7%**.

Finally, the model is saved so that it may be used in a production environment.

Please see [here](https://github.com/three14consulting/Python/blob/main/DeepComputerVision/animals-10-v2.ipynb) for the notebook containing the project.

<h2>Diagnostics</h2>
<b><strong>Class Distribution</strong></b>

<p align="center"><img src="https://github.com/three14consulting/Python/blob/main/DeepComputerVision/images/class_distribution.JPG?raw=true"></p>
<b><strong>Fine-Tuning Accuracy and Loss Curves</strong></b>

<p align="center"><img src="https://github.com/three14consulting/Python/blob/main/DeepComputerVision/images/train_val_fine_tune.JPG?raw=true"></p>
