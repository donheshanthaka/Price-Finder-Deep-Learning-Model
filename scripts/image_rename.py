import os
count = 1
path = "D:\Projects\Python\Projects\Price Finder\web_scraper_for_image_collection\images\Wangon R stingray 2018"
print(os.listdir(path))
for dirname in os.listdir(path):
    print(path + "\\" + dirname)
    dirname = path + "\\" + dirname
    if os.path.isdir(dirname):
        for filename in (os.listdir(dirname)):
            os.rename(dirname + "/" + filename, dirname + "/" + "00" + str(count) + ".jpg")
            count += 1