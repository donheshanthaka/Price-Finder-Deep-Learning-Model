import os

import numpy as np

import shutil

rootdir = "C:/Users/Don Hesha/Desktop/model_images" # path of the original folder

classes = ["Alto 2015", "Hero Dash 2016", "Toyota Aqua 2014", "Wagon R Stingray 2018"]

for i in classes:

    os.makedirs(rootdir + '/train/' + i)

    os.makedirs(rootdir + '/test/' + i)

    source = rootdir + '/' + i

    allFileNames = os.listdir(source)

    np.random.shuffle(allFileNames)

    test_ratio = 0.20

    train_FileNames, test_FileNames = np.split(np.array(allFileNames),
                                            [int(len(allFileNames) * (1 - test_ratio))])

    train_FileNames = [source+'/' + name for name in train_FileNames.tolist()]
    test_FileNames = [source+'/' + name for name in test_FileNames.tolist()]

    print(train_FileNames)

    for name in train_FileNames:
        shutil.copy(name, rootdir + '/train/' + i)

    for name in test_FileNames:
        shutil.copy(name, rootdir + '/test/' + i)
