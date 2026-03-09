import os
import random
import matplotlib.pyplot as plt
from pycocotools.coco import COCO
from PIL import Image
import matplotlib.pyplot as plt


print("Current working directory:", os.getcwd())
print("Folders here:", os.listdir())

# FULL ABSOLUTE PATH (change if needed)


data_dir = r"C:\Users\andre\Downloads\archive (1)\coco2017"

ann_file = os.path.join(data_dir, "annotations", "captions_val2017.json")
img_dir = os.path.join(data_dir, "val2017")
ann_file_instances = os.path.join(data_dir, "annotations", "instances_val2017.json")

# Check files exist BEFORE loading
print("Caption file exists:", os.path.exists(ann_file))
print("Image folder exists:", os.path.exists(img_dir))


# Load COCO captions
coco = COCO(ann_file)

# Get all image IDs
img_ids = coco.getImgIds()
print("Total images:", len(img_ids))

# Pick a random image
img_id = random.choice(img_ids)
img_info = coco.loadImgs(img_id)[0]

# Load image
img_path = os.path.join(img_dir, img_info['file_name'])
image = Image.open(img_path)

# Load captions
ann_ids = coco.getAnnIds(imgIds=img_id)
anns = coco.loadAnns(ann_ids)
captions = [ann['caption'] for ann in anns]

# Display
plt.imshow(image)
plt.axis("off")
plt.title("\n".join(captions), fontsize=8)
plt.show()



ann_file_instances = os.path.join(data_dir, "annotations/instances_val2017.json")
coco_instances = COCO(ann_file_instances)

categories = coco_instances.loadCats(coco_instances.getCatIds())
print("Number of classes:", len(categories))




caption_lengths = [len(ann['caption'].split()) 
                   for ann in coco.dataset['annotations']]

print("Average caption length:", sum(caption_lengths)/len(caption_lengths))






plt.hist(caption_lengths, bins=30)
plt.xlabel("Caption Length (words)")
plt.ylabel("Frequency")
plt.title("COCO Caption Length Distribution")
plt.show()
