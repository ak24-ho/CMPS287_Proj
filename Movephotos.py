import shutil
import  os
from pathlib import Path
target = r'C:\\Users\\student\\Desktop\\dataSet3'
original = r'C:\\Users\\student\\Desktop\\dataSet1'
counter1=0
for folder in os.listdir(original):
    for image in os.listdir(original+"\\"+folder):
        counter1+=1
        print(counter1)
    if counter1<6:
        shutil.move(original+"\\"+folder, target)
        counter1=0
    counter1=0

