import os
import numpy as np
import shutil

RATIO = 0.5

print("\n ---- Dataset Split Started ---- \n")

vehicle_list = os.listdir(os.path.join(os.getcwd(), "images"))
images_path = os.path.join(os.getcwd(), "images")
model_images_path = os.path.join(os.getcwd(), "classification_model/images")

if not os.path.isdir(model_images_path):
    os.mkdir(model_images_path)

for vehicle in vehicle_list:

    print(f"Splitting the dataset of: {vehicle}")

    os.makedirs(model_images_path + '/train/' + vehicle)
    os.makedirs(model_images_path + '/test/' + vehicle)
    os.makedirs(model_images_path + '/validate/' + vehicle)

    source = images_path + '/' + vehicle + '/duplicate_checked'

    if os.path.exists(source):
        allFileNames = os.listdir(source)
    else:
        continue

    np.random.shuffle(allFileNames)

    train_FileNames, remaining_FileNames = np.split(np.array(allFileNames),
                                            [int(len(allFileNames) * (1 - RATIO))])

    train_FileNames = [source+'/' + name for name in train_FileNames.tolist()]

    for name in train_FileNames:
        shutil.copy(name, model_images_path + '/train/' + vehicle)

    test_file_names, validate_file_names = np.split(np.array(remaining_FileNames),
                                            [int(len(remaining_FileNames) * (1 - RATIO))])

    test_file_names = [source+'/' + name for name in test_file_names.tolist()]
    validate_file_names = [source+'/' + name for name in validate_file_names.tolist()]

    for name in test_file_names:
        shutil.copy(name, model_images_path + '/test/' + vehicle)

    for name in validate_file_names:
        shutil.copy(name, model_images_path + '/validate/' + vehicle)

print("\n ---- Dataset Split Completed ---- ")