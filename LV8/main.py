
import numpy as np

testCSV = "/Users/karlobuhinjak/Desktop/PSU_LV/LV8/archive/Test.csv"
testDir = "/Users/karlobuhinjak/Desktop/PSU_LV/LV8/archive/Test "

os.makedirs(testDir, exist_ok=True)

rows=open(testCSV).read().strip().split("\n")[1:]


for r in rows:
    (label, imagePath)=r.strip().split(",")[-2:]
    os.makedirs(os.path.join(testDir, label), exist_ok=True)
    shutil.copy(os.path.join("gtsrb_dataset",imagePath),os.path.join(testDir, label))


# ucitavanje podataka iz odredenog direktorija
train_ds = image_dataset_from_directory(
    directory='/Users/karlobuhinjak/Desktop/PSU_LV/LV8/archive',
    labels='inferred',
    label_mode='categorical',
    batch_size=32,
    image_size=(48, 48))

test_ds = image_dataset_from_directory(
    directory=' /Users/karlobuhinjak/Desktop/PSU_LV/LV8/archive/Train',
    labels='inferred',
    label_mode='categorical',
    batch_size=1,
    image_size=(48, 48))