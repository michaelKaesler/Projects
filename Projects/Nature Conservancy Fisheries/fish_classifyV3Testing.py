import numpy as np
import cv2
import glob
import os
import matplotlib.pyplot as plt
from time import time
from sklearn.cross_validation import train_test_split
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.constraints import maxnorm
from keras.optimizers import SGD
from keras.layers.convolutional import Convolution2D, MaxPooling2D, ZeroPadding2D
from keras.utils import np_utils

"""
When testing the model, advise using all of the training data, when I cut it short
it gives ridiculously high accuracy, so I think theres something going on there, like
maybe the first 100 in each are only from one boat or something.

It takes approx 150s to load training pics.

The parameters and image sizes right now are ridiculously small, just for testing/quick turn
around purposes.

The current accuracy is 94% (note skepticism about boats)
"""


train_path = '/Users/home/Desktop/FishProject/Train/'
test_path = '/Users/home/Desktop/FishProject/test_stg1/'


def load_training(path):
    # so this loops through the directories (ignoring any hidden files that start with '.'
    # *note* also, at this time, reading images in as RGB
    t0 = time()
    X_train = []
    Y_train = []
    # counter = 0

    print "reading training images..."
    folders = ['ALB', 'BET', 'DOL', 'LAG', 'NoF', 'OTHER', 'SHARK', 'YFT']
    for fld in folders:
        # need the classes to be stored as numbers not strings for keras
        index = folders.index(fld)
        path = os.path.join('..', 'Train', fld, '*.jpg')
        files = glob.glob(path)
        for fil in files:
            X_train.append(cv2.imread(fil))
            Y_train.append(index)

            # using smaller set of data (not adding this in the main)
            # if counter > 300:
            #     break
            # counter += 1

    print "total time elapsed:", round(time() - t0, 3), "s"

    return X_train, Y_train


def load_test():
    t0 = time()
    path = os.path.join('..','test_stg1', '*.jpg')
    files = glob.glob(path)
    X_test = []
    # counter = 0

    print "reading testing images..."
    for fil in files:
        X_test.append(cv2.imread(fil))
        # if counter > 300:
        #     break
        # counter += 1

    print "total time elapsed:", round(time()-t0, 3), "s"

    return X_test


# takes an 'image' and resizes it to 670 x 1192, this is planning to take the imgage
# as the numpy array in the X_train list
def resize_images(X_train, X_test):
    print "resizing images..."
    t0 = time()
    resize_x_train = []
    resize_x_test = []

    for im in X_train:          # going to need to change these image sizes (go 32x32 to start)
        new_im = cv2.resize(im, (256, 256))
        resize_x_train.append(new_im)

    for im in X_test:
        new_im1 = cv2.resize(im, (256, 256))
        resize_x_test.append(new_im1)

    print "total time elapsed:", round(time()-t0, 3), "s"

    return resize_x_train, resize_x_test


# normalize the images before putting them into the net, may beed to transpose them as well
def normalize_data(X_train, X_test, Y_train):
    X_train1 = np.array(X_train).astype('float32')
    X_test1 = np.array(X_test).astype('float32')
    Y_train1 = np.array(Y_train)

    # divide by 255 b/c pixel numbers go from 0 to 255
    X_train1 = X_train1 / 255.0
    X_test1 = X_test1 / 255.0

    Y_train1 = np_utils.to_categorical(Y_train1, 8)


    return X_train1, X_test1, Y_train1


def create_our_test(X_train, Y_train):

    data_train, data_test, labels_train, labels_test = train_test_split(X_train, Y_train,
                                                                        test_size=0.2, random_state=42)
    return data_train, data_test, labels_train, labels_test


def createModel():

    model = Sequential()
    # for conv2D, args are num filters, num rows, num columns (3x3 is standard)
    # input shape is our height x width x rgb
    model.add(Convolution2D(32, 3, 3, input_shape=(256, 256, 3), activation= 'relu', border_mode= 'same', W_constraint=maxnorm(3)))
    model.add(Dropout(0.2))
    model.add(Convolution2D(32, 3, 3, activation= 'relu', border_mode= 'same', W_constraint=maxnorm(3)))
    # pool size of 2,2 is standard
    model.add(MaxPooling2D(pool_size=(2, 2)))
    # flatten image
    model.add(Flatten())
    model.add(Dense(512, activation = 'relu'))
    model.add(Dropout(0.5))
    model.add(Dense(512, activation='relu'))
    model.add(Dropout(0.5))
    # the final output later, softmax b/c classification
    model.add(Dense(8, activation='softmax'))

    epochs = 30 # note, this should probably be higher (started at 5)
    lrate = 0.01
    decay = lrate/epochs
    sgd = SGD(lr=lrate, momentum=0.9, decay=decay, nesterov=False)
    model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

    return model, epochs


if __name__ == '__main__':
    # load the training and testing data
    X_train, Y_train = load_training(train_path)
    X_test = load_test()

    # resize and normalize the images
    new_train, new_test = resize_images(X_train, X_test)
    X_trainNorm, X_testNorm , Y_trainNorm = normalize_data(new_train, new_test, Y_train)

    # create our own evaluation set for class purposes
    our_dat_train, our_dat_test, our_lab_train, our_lab_test = create_our_test(X_trainNorm, Y_trainNorm)

    # create the model
    model, epochs = createModel()
    print "starting training..."
    print ""
    t0 = time()
    model.fit(our_dat_train, our_lab_train, validation_data=(our_dat_test, our_lab_test),
              nb_epoch=epochs, batch_size = 64)
    print "total training time elapsed:", round(time()-t0, 3), "s"
    scores = model.evaluate(our_dat_test, our_lab_test, verbose = 0)
    print "Accuracy:", scores[1]*100








