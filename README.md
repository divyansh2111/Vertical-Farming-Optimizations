# Vertical Farming Optimizations

### Introduction

<p align="justify"> 
Vertical farms are intensive plant production systems with vertically stacked or vertically inclined shelves. They incorporate controlled-environment agriculture, aiming to optimize plant growth while trying to use soilless farming techniques such as aquaponics, hydroponics, etc. Some common choices of structures to house vertical farming systems include buildings, shipping containers, tunnels, and abandoned mine shafts. As of 2020, there is the equivalent of about 74 acres of operational vertical farmland in the world. Current applications of vertical farmings coupled with other state-of-the-art technologies, such as specialized LED lights, have resulted in over 10 times the crop yield than would receive through traditional farming methods.
</p>

### Problem Statement

<p align="justify">
In traditional farming, many of the farmers are unaware of the amount of fertilizers and other chemicals which should be used, thus resulting in excess amount of soil erosion, agricultural runoff, and a lot of other issues. While vertical farming has numerous advantages over traditional farming, there exist some similarities between the two such as the amount of chemicals which are to be used while growing crops. Looking at the effects of excess use of fertilizers, it is essential that during vertical farming, this amount of chemicals be regulated. The issue which arises while obtaining an optimal amount of chemicals is that this amount is also based on the area in which crops are being grown. Further, many times in indoor environments a disease in a single crop can propagate to other plants as well as it is thus important to take care of diseased crops on a regular basis for which an autonomous system capable of real time disease detection is often needed for good turnout. <strong>Summing up, the problem statement of our project is to develop an Artificial Intelligence model to obtain the optimal amount of fertilizers which are to be used for a given crop, given the weather conditions of the area in which we are growing the crop, as well as developing an autonomous system capable of detecting whether a certain crop contains a disease, and further specifying the type of disease as well.<strong>
</p>

### Technology Stack
* Python
* HTML and CSS 
* Bootstrap
* Tensorflow and Keras

### Methodology

<p align="justify">
After fixing the problem statement, we trained and tested the dataset using a couple of different already existing, common models. Out of the ones which we tried, linear regression gave the best R-score (of 0.95), and hence we decided to deploy it for the initial stages. In the second phase of our project which included image processing and computer vision for which the basic methodology included training various models, all having already working and optimized layers in between available open source. The final model that is to be deployed is a decision based on the combination of how good the accuracy is, as well as how reliable the model would be when given a slightly different distribution of images(data) over which it shouldn't show tendencies to overfit (which can be checked using other reliable uses of such models in other cases). We trained the Densenet and Efficient-Net models on the data and achieved an accuracy of 92% on the test data. Finally both models were deployed as web applications. 
</p>

### Final Presentation
[![Vertical Farming Optimizations](https://res.cloudinary.com/marcomontalbano/image/upload/v1621751473/video_to_markdown/images/google-drive--1JDcmMze5nIhutXsVoPkg9t8uC3074vVq-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://drive.google.com/file/d/1JDcmMze5nIhutXsVoPkg9t8uC3074vVq/view?usp=sharing "Vertical Farming Optimizations")
