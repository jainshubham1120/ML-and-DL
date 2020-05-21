Digit Recognizer 
------------------
 
One of the most exciting applications of Deep Neural Networks is character recognition. This repository contains the dataset and code file for a Digit recognizer model.
The basic concept used in developing this model is Convolutional Neural Networks(CNNs). CNN is a very efficient way of reducing the number of parameters while increasing the depth of Neural Networks. The Model is inspired by the famous LeNet which was published in a paper in 1998 by Yann LeCun. 
The model that I made was able to achieve 99.043% accuracy.
 
Dataset
This dataset is a classic dataset of handwritten digits, released in 1999 by MNIST ("Modified National Institute of Standards and Technology"), which can be found at http://yann.lecun.com/exdb/mnist/ .
 
The data files train.csv and test.csv contain gray-scale images of hand-drawn digits, from zero through nine.
Each image is 28 pixels in height and 28 pixels in width, for a total of 784 pixels in total. This pixel-value is an integer between 0 and 255, inclusive.The training data set, (train.csv), has 785 columns. The first column, called "label", is the digit that was drawn by the user. The rest of the columns contain the pixel-values of the associated image.
 
The test data set, (test.csv), is the same as the training set, except that it does not contain the "label" column.

Other details:
Optimizer used: SGD

5 Fold Cross Validation

Activation Function: ReLU

Hidden Layers(Nodes) : 3(32,64,64)

Learning Rate : 0.01

Epochs : 10
