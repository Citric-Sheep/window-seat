from PIL import Image

# This is a way to get the exif data from heic files but there's a licencing
# / bug that makes it difficult to do from an uploaded file.
# So lets just support jpeg
my_image = 'resources/IMG_0446.heic'
image = Image.open(my_image)
metadata = image.getexif()
created = metadata[306]
print(created)
from datetime import datetime
dt = datetime.strptime(created, '%Y:%m:%d %H:%M:%S')
print(dt)
