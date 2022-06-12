# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 06:31:19 2022

@author: HariOm12
"""

# test cases (t1 --- t6, jpg, raw)
# 1. t3.jpg and t6.jpg removed manually and ran code --- done
# 2. all files intact no files to delete --------------- done
# 3. no files in raw
# 4. no files in jpg
# 5. names different between jpg and raw folder
# 6. jpg folder does not exist
# 7. raw folder does not exist
# 8. different extentions other than jpg in folder
# 9. different extentions other than raw in folder
# 10. deletes only within the specified root folder

import os

### Make a list of raw images to delete

DEL_PATH = "C://test//deleted"
FAM_PATH = "C://test//Family"
DIR_PATH = "C://test"
del_list = os.listdir(DEL_PATH)
fam_list = os.listdir(FAM_PATH)
dir_list = os.listdir(DIR_PATH)
raw_del_list = []

for i in del_list:
    raw_del_list.append(i.replace(".JPG",".RAF"))

for i in fam_list:
    raw_del_list.append(i.replace(".JPG",".RAF"))

raw_del_list.sort()

print(raw_del_list)

### Delete the raw images
"""
for directory in dir_list:
    for file in raw_del_list:
        full_path = DIR_PATH + "//" + directory + "//raw//" + file
        if os.path.exists(full_path):
            os.remove(full_path)
"""