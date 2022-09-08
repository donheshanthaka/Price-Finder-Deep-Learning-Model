
# Vehicle Image Classification (Price Finder APP)

[![Python Versions](https://img.shields.io/badge/python-3.8_|_3.9-blue?style=for-the-badge)](https://github.com/donheshanthaka/Price-Finder-Deep-Learning-Model/blob/main/LICENSE)
[![GitHub License](https://img.shields.io/github/license/donheshanthaka/Price-Finder-Deep-Learning-Model?style=for-the-badge)](https://github.com/donheshanthaka/Price-Finder-Deep-Learning-Model/blob/main/LICENSE)
[![GitHub Repo Stars](https://img.shields.io/github/stars/donheshanthaka/Price-Finder-Deep-Learning-Model?style=for-the-badge)](https://github.com/donheshanthaka/Price-Finder-Deep-Learning-Model/blob/main/LICENSE)
[![GitHub Repo Size](https://img.shields.io/github/repo-size/donheshanthaka/Price-Finder-Deep-Learning-Model?style=for-the-badge)](https://github.com/donheshanthaka/Price-Finder-Deep-Learning-Model/blob/main/LICENSE)

This project contains the development of a vehicle image classification model based on convolutional neural network (CNN). The model is capable of classifying vehicle models based on images.
It is the AI model used in the [Flask API](https://github.com/donheshanthaka/Price-Finder-Flask-API) that is developed to facilitate the image recognition capabilities of the [Price Finder](https://github.com/donheshanthaka/Price-Finder-Flutter-APP) mobile application.

## 🧱 Tech Stack

* Python - 3.8
* tensorflow - 2.9
* numpy - 1.20
* scikit_learn - 1.1
* matplotlib - 3.4
* Pillow - 9.2
* beautifulsoup4 - 4.11
* requests - 2.27
* selenium - 4.4
* difPy - 2.4
## 📚 Dataset

The dataset used in this project was sourced from google images with the use of a custom web scraper which is explained in detail during the [Collect image data](#collect-image-data) section.

For the current version of the model, the dataset consists of 4,138 images across 4 classes. The data is then split up into train, test and validation sets which each contains 4 sub directories of the 4 image classes.

The above process is mentioned in detail in the [split dataset](#split-dataset) section.

**Overview of the image data:**

|     Class     |     Train     |      Test     |    Validate   |     Total     |
| ------------- | :-------------: | :-------------: | :-------------: | :-------------: |
| Alto 2015  | 1,252  | 139  | 140  | 1531  |
| Hero Dash 2016  | 405  | 51  | 51  | 507  |
| Toyota Aqua 2014  | 897  | 113  | 112  | 1,122  |
| Wagon R Stingray 2018  | 782  | 98  | 98  | 978  |
| **Grand Total**  | -  |  - |  -  | 4,138  |


**Few example images from each class:**

| Alto 2015 | Hero Dash 2016 | Toyota Aqua 2014 | Wagon R Stingray 2018 |
| ---  |  --- | --- | --- |
|![Alto 2015](https://user-images.githubusercontent.com/61963664/189027432-f2097048-98e4-4d99-bb48-51346430d5ce.jpg)| ![Hero Dash 2016](https://user-images.githubusercontent.com/61963664/189027704-d84a3b68-47b0-4f5c-8e41-1d7f95d3dfc0.jpg) | ![Toyota Aqua 2014](https://user-images.githubusercontent.com/61963664/189027885-bab0d3f1-0fb9-46ac-aced-399ee1e248db.jpg) | ![Wagon R Stingray 2018](https://user-images.githubusercontent.com/61963664/189027996-e0f54463-deab-44d2-8aad-d6da64b6be25.jpg) |


📍 *Note: The images used in the current project are not shared with the repository since i do not own the rights to the images downloaded through google images. However, that would not be an issue for anyone following this project since the webscraper script and instructions are given.*
## ⚙ Setup Instructions

The project is based on two main environments, one for the image data collection and another for developing the model.
The image data collection is handled through a python web scraper script and the model is developed on a jupyter notebook.

**Clone the repository**

```bash
  git clone https://github.com/donheshanthaka/Price-Finder-Deep-Learning-Model.git
```

### ⛺ Setup the environment to collect image data

*Prerequisites:*

* [Chrome](https://www.google.com/chrome/)


📌 *Make sure that you chrome is updated, if not the browser will close automatically during the start of the script*

**Step 1:**

* Create a python virtual environment inside the `web_scraper_for_image_collection` folder.
* Navigate to the folder and open up a terminal and insert the following command.


```bash
  python -m venv env
```

* Navigate to the activation path

```bash
  cd env/Scripts
```

* Activate the virtual environment *(Run either one, not both)*

```bash
  activate.bat //In CMD
  Activate.ps1 //In Powershell
```

**Step 2:**

* Install the required dependencies

```bash
  pip install -r requirements.txt
```

### 📸 Collect image data

**Step 1:**

*This script uses selenium webdriver module to scrape images from Google Images.*

* Open the web_scraping_google_images.py script
* You have to edit two fields inside the script according to the preferred vehicle model.

`folder_name` = The name of the folder where downloaded images are saved (add iteration value at the end of the name).

`search_URL` = URL of the search query made using google images with the vehicle model

*Example: (Vehicle model = Toyota Aqua 2014)*

* Go to google images and search the vehicle: [example](https://www.google.lk/search?q=Toyota+Aqua+2014&hl=en&tbm=isch&source=hp&biw=1920&bih=937&ei=bqQOY86EIeDC3LUPmM-x8Ac&iflsig=AJiK0e8AAAAAYw6yflZNGqMgg9_919n1rURVPTysRTjB&ved=0ahUKEwjO857k4u_5AhVgIbcAHZhnDH4Q4dUDCAY&uact=5&oq=Toyota+Aqua+2014&gs_lcp=CgNpbWcQAzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgYIABAeEAgyBggAEB4QCFDWAVjWAWCPCGgAcAB4AIABiwGIAYsBkgEDMC4xmAEAoAECoAEBqgELZ3dzLXdpei1pbWewAQC4AQE&sclient=img)
* Use that url for `search_URL`

```
folder_name = "images\\aqua 01".

search_URL = "https://www.google.lk/search?q=Toyota+Aqua+2014&hl...."
```

* Run the script inside the virtual environment.
* A Chrome browser will open with the given url, **Do not click on the images**, instead scroll to the very bottom of the webpage.
* Then press enter on the python terminal where the script is running.
* The browser will scroll up automatically and start downloading each image.
* After downloading the images, the browser will close itself.

**Repeate the above steps until you have collected sufficient amount of images per vehicle (4-5 times) and do the same for all the vehicle models you want the cnn model to be trained on.**

📌 *Hint: Use different keywords on every search (Toyota Aqua 2014 Front / Toyota Aqua 2014 Japan / Prius C 2014)* > Prius C is another name used for Aqua in international markets.


### 🛠 Preprocess downloaded images

The `download_image_preprocessor.py` script is used to make image collections of each vehicle model by combining the subsets of each run such as (aqua 01, aqua 02 ...) as well as identify duplicate images downloaded when running the image collection script and delete them.

**Step 01:**

* Copy all the sub folders (aqua 01, aqua 02.. ) into a parent folder. *E.g. -> `aqua collection`*
* Repeat the above step for all the vehicle image sets collected.

An example of the directory structure of images folder:

```
images <- top level folder 
│
└───aqua collection <- the collection folder that was created using the above step
│   │
│   └───aqua 01
│   │   |   001.jpg
│   │   |   002.jpg
│   │   |   ...
│   └───aqua 02
│   │   |   001.jpg
│   │   |   002.jpg
│   │   |   ...
│   │
└───prius collection
│   │
│   └───prius 01
│   │   |   001.jpg
│   │   |   002.jpg
│   │   |   ...
│   └───prius 02
│   │   |   001.jpg
│   │   |   002.jpg
│   │   |   ...
│   │ ...

```

**Step 02:**

* Run the `download_image_preprocessor.py` script.
* It will create a `duplicate_checked` folder inside every vehicle model collection folder which contain the processed images after deleting the duplicates, however it is **Highly recommended to manually check that folder and delete unwanted images that are downloaded from the webscraper since it is quite normal for the google images to contain unrelated images with every search and the webscraper has no intelligence in identifying images before download, therefore it will download all the results.**

### ⚖ Split dataset

The image dataset will be divided among three sections with the below mentioned split ratios.

- Train -> 50%
- Test -> 25%
- Validation -> 25%

**Step 01:**

* Rename the image dataset folders with proper vehicle names including the model year instead of 'collection'

Example:

```
aqua collection > Toyota Aqua 2014
prius collection > Toyota Prius 2016
```

**Step 02:**

* Run the `dataset_split.py` script.

The script will split the dataset and create the new folder structure inside the `classification model` folder where the model will be developed.

Dataset directory structure of the images folder inside classification_model after the above step:

```
images <- top level folder
└───train <- training images
│   └───Alto 2015
│   │   │   01005.jpg
│   │   │   08445.jpg
│   │   │   ...      
│   └───Toyota Aqua 2014
│       │   01654.jpg
│       │   05422.jpg
│       │   ...
│   
└───test <- testing images
│   └───Alto 2015
│   │   │   01545.jpg
│   │   │   01985.jpg
│   │   │   ...      
│   └───Toyota Aqua 2014
│       │   09655.jpg
│       │   01054.jpg
│       │   ...
│
└───validate <- validation images
│   └───Alto 2015
│   │   │   96505.jpg
│   │   │   01655.jpg
│   │   │   ...      
│   └───Toyota Aqua 2014
│       │   09866.jpg
│       │   35444.jpg
│       │   ...
```

### 🐍 Setup the anaconda virtual environment

*Prerequisites:*

* [Anaconda](https://www.anaconda.com/products/distribution) - Don't need to install if you are following the Nvidia guide, since you will be downloading the miniconda version there.

If you have an Nvidia GPU then follow this amazing guide mentioned below by [Jeff Heaton](https://github.com/jeffheaton) both in video and in markdown for a full in-depth explanation of the setup process.

* [Setting Up CUDA, CUDNN, Keras, and TensorFlow on Windows 11 for GPU Deep Learning (Video)](https://www.youtube.com/watch?v=OEFKlRSd8Ic) - Does work for Windows 10 as well.
* [Markdown format setup](https://github.com/jeffheaton/t81_558_deep_learning/blob/master/install/manual_setup2.ipynb)


**Step 01:**

* Install [Anaconda](https://www.anaconda.com/products/distribution)

**Step 02:**

* Open Anaconda Prompt
* Navigate to the `classification_model` folder inside the project
* Type the following command inside anaconda prompt to create a virtual environment for anaconda -> *The environment will be created according to the specifications mentioned in the `environment.yml` file*


```bash
    conda env create
```


* Activate the environment with the following command

```bash
    activate vehicle-image-cnn-env
```

**Step 03:**

* Open jupyter notebook

```bash
    jupyter notebook
```
## 🧠 Convolutional Neural Network (CNN)

The model in this project is developed using transfer learning method known as feature extraction. A pre-trained model is used as the starting point to the current model.

**Transfer Learning:**

Transfer learning is the reuse of a pre-trained model on a new problem. It's currently very popular in deep learning because it can train deep neural networks with comparatively little data. This is very useful in the data science field since most real-world problems typically do not have millions of labeled data points to train such complex models. And it can be considered a valid statement for the current project as well since the data was collected through a web scraper.

**Feature Extraction:**

Feature extraction transfer learning is when the underlying patterns (also called weights) of a pretrained model has learned are taken and adjusted its output to be more suited to the current problem.

For the current project, a pre-trained model from [Keras Applications](https://keras.io/api/applications/) library is used. Which is the [EfficientNetB1](https://keras.io/api/applications/efficientnet/#efficientnetb1-function) model.

*** 
For example, EfficientNetB0 has 236 layers, but the top layer outputs 1000 classes because it was pretrained on ImageNet. To adjust this to the current scenario, the original activation layer has been removed the and replaced with the amount of output classes according to the vehicle models gathered. The important part here is that only the top few layers become trainable, the rest remain frozen.

This way all the underlying patterns remain in the rest of the layers and the rest can be utilized according to the current scenario. This method of transfer learning is highly efficient when the data is similar to the data the model has been pretrained on (*data = images*).

***

**EfficientNet:**

EfficientNets rely on AutoML and compound scaling to achieve superior performance without compromising resource efficiency. The AutoML Mobile framework has helped develop a mobile-size baseline network, EfficientNet-B0, which is then improved by the compound scaling method to obtain EfficientNet-B1 to B7.

<img src="https://user-images.githubusercontent.com/61963664/188676387-8d48bf4d-bd20-477f-b04a-83c33d9cc480.png" alt="EfficientNet performance chart" width="50%" />

EfficientNets achieve state-of-the-art accuracy on ImageNet with an order of magnitude with better efficiency.

## ⚒ Development

**Building the feature extraction model:**

Since the model is created using a jupyter notebook, all the relevant steps and decisions made are mentioned in the notebook itself, therefore it will not be repeated in this documentation. However, since the notebook is available in github it can be viewed without running the project through an anaconda instance.

[The model develeopment notebook](https://github.com/donheshanthaka/Price-Finder-Deep-Learning-Model/blob/main/classification_model/Price_Finder_AI_Model.ipynb)

*For users who are following this project from the initial steps can start running the notebook and continue to work there if you have followed up to step 3 in setting up the anaconda virtual environment.*
## 📈 Evaluation

After successful build on the model and fitting for 5 epochs with train and validation datasets an accuracy of **97.26%** was achieved when being evaluated on the test dataset.

**Evaluating the model based on training and validation loss:**

![model training and validation loss](https://user-images.githubusercontent.com/61963664/188704934-d6e1df4e-d1ba-47f2-9088-ae0cf73ad015.png)

**Evaluating the model based on training and validation accuracy:**


![model training and validation accuracy](https://user-images.githubusercontent.com/61963664/188705011-a0030ac4-a242-40a3-a294-6ab028ecb28a.png)

**Confusion Matrix:**

![confusion matrix](https://user-images.githubusercontent.com/61963664/188705076-584c3be0-0e59-43f5-b04b-e948de794fed.png)

It seems that the model do get confused with `Toyota Aqua 2014` and `Wagon R Stingray 2018` with `Alto 2015` on certain occasions. It suggest that more diverse images of `Toyota Aqua 2014` and `Wagon R Stingray 2018` are needed for the model to be trained more efficiently.


**Visualizing predictions on test images:**

![predictions on test images](https://user-images.githubusercontent.com/61963664/188705160-35af6cfc-59b4-4acf-b507-413b0078ba3c.png)


## 🚀 Deployment

This model is deployed using a flask API in google cloud platform that facilitates the image recognition capabilities of a mobile application that I have developed.

Feel free to checkout those projects as well mentioned on the links below:

* [Flask API](https://github.com/donheshanthaka/Price-Finder-Flask-API)
* [Price Finder APP](https://github.com/donheshanthaka/Price-Finder-Flutter-APP)

