from difPy import dif
import os
import shutil
from random import randint

PARENT_DIR = os.getcwd()
IMAGES_DIR = os.path.join(PARENT_DIR, "images")

temp_collection = []

print("\n>> Started moving images to the temp folders")
for root, dirs, files in os.walk(IMAGES_DIR):
    for dir in dirs:
        path = os.path.join(root, dir)
        temp_collection_path = os.path.join(path, "temp")
        for dirname in os.listdir(path):
            dirname = path + "\\" + dirname
            if os.path.isdir(dirname) and dirname != temp_collection_path:
                for filename in (os.listdir(dirname)):
                    src = dirname + "\\" + filename
                    dst = temp_collection_path + "\\" + str(randint(0, 999)) + filename
                    if not os.path.isdir(temp_collection_path):
                        os.mkdir(temp_collection_path)
                        temp_collection.append(temp_collection_path)
                    shutil.copy(src, dst)


print("<< Done moving images to the temp folders\n")

for collection in temp_collection:
    print("\n>> Started removing duplicates in: ")
    print(f"[{collection}]")
    dif(collection, similarity="low", show_progress=True, delete=True, silent_del=True)
    os.chdir(collection)
    vehicle_folder_path = os.path.normpath(os.getcwd() + os.sep + os.pardir)
    os.chdir(vehicle_folder_path)
    new_folder_path = os.path.join(vehicle_folder_path, "duplicate_checked")
    os.mkdir(new_folder_path)

    COUNT = 1
    for filename in (os.listdir(collection)):
        src = collection + "/" + filename
        dst =  new_folder_path + "\\" + "0" + str(COUNT) + ".jpg"
        shutil.copy(src, dst)
        COUNT += 1
    shutil.rmtree(collection)
    print("<< Finished removing duplicates\n")
    
print("\n------ Images processed successfully ------")
print("** Always go through the 'duplicate_checked' folders manually to remove unrelated images for respective vehicle models **\n")
