"""
Collect images from Esp32-cam web server
"""
from logging import basicConfig, INFO
from everywhereml.data import ImageDataset

base_folder = 'line_types'
# copy here the address printed on the Serial Monitor
# (the one after "MJPEG stream available at")
basicConfig(level=INFO)

# if our dataset folder already exists, load it
image_dataset = ImageDataset.from_nested_folders(
    name='Dataset',
    base_folder=base_folder
)

print(image_dataset)

"""
Display a preview of the captured images
"""
image_dataset.preview(
    samples_per_class=10,
    rows_per_class=2,
    figsize=(20, 10)
)
