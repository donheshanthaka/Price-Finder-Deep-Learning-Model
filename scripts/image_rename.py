from difPy import dif
import os
import shutil
from random import randint

PATH = "D:\Projects\Python\Projects\Price Finder\web_scraper_for_image_collection\images\hero collection"
TEMP_COLLECTION_PATH = PATH + "\collection"
os.mkdir(TEMP_COLLECTION_PATH)
DST_PATH = "D:\Projects\Python\Projects\Price Finder\web_scraper_for_image_collection\images\\Hero Dash 2016"
#os.mkdir(DST_PATH)

# print(os.listdir(PATH))

for dirname in os.listdir(PATH):
    #print(PATH + "\\" + dirname)
    dirname = PATH + "\\" + dirname
    if os.path.isdir(dirname) and dirname != TEMP_COLLECTION_PATH:
        for filename in (os.listdir(dirname)):
            #print(DST_PATH + "/" + "0" + str(COUNT) + ".jpg")
            #os.rename(dirname + "/" + filename, DST_PATH + "/" + "0" + str(COUNT) + ".jpg")
            src = dirname + "\\" + filename
            #dst =  DST_PATH + "/" + "0" + str(COUNT) + ".jpg"
            dst = TEMP_COLLECTION_PATH + "\\" + str(randint(0, 999)) + filename
            shutil.copy(src, dst)
            print(dirname + "\\" + filename)


# search = dif(TEMP_COLLECTION_PATH, similarity="low",
#              show_progress=True, delete=True, silent_del=True)


# COUNT = 1
# for filename in (os.listdir(TEMP_COLLECTION_PATH)):
#     print(DST_PATH + "\\" + "0" + str(COUNT) + ".jpg")
#     src = TEMP_COLLECTION_PATH + "/" + filename
#     dst =  DST_PATH + "\\" + "0" + str(COUNT) + ".jpg"
#     shutil.copy(src, dst)
#     COUNT += 1
