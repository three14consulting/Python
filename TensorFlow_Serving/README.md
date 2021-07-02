<h1 align="center">Model Deployment using TensorFlow Serving<br> and REST API</h1>
<p align="center"><img src="https://github.com/three14consulting/Python/blob/main/TensorFlow_Serving/images/production_images.JPG?raw=true" height="300"></p>
<h1><a id='0.0'> Project Summary</a></h1>

This project uses the image classifier model (built in this [project](https://github.com/three14consulting/Python/tree/main/DeepComputerVision)) and deploys it using **TensorFlow Serving**. 

I submit a sample of 10 images in JSON format to the (locally hosted) server to retrieve the classifier\'s predictions, via **REST API**.

With the TensorFlow Serving implementation working, I submit my own image (a dog of a relative) to see what the classifier returns.

Please see [**here**](https://github.com/three14consulting/Python/blob/main/TensorFlow_Serving/TF_Serving_REST_API.ipynb) for the notebook containing the project.
<br>
<p align="center"><img src="https://github.com/three14consulting/Python/blob/main/TensorFlow_Serving/images/dog_success.JPG?raw=true"></p>
