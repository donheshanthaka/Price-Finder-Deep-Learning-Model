import os
count = 1
path = "copy paste the directory here"
for dirname in os.listdir(path):
    if os.path.isdir(dirname):
        for filename in (os.listdir(dirname)):
            os.rename(dirname + "/" + filename, dirname + "/" + "0" + str(count) + ".jpg")
            count += 1