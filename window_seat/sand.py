from PIL import Image

my_image = 'resources/IMG_0446.heic'
image = Image.open(my_image)
metadata = image.getexif()
created = metadata[306]
print(created)
from datetime import datetime
dt = datetime.strptime(created, '%Y:%m:%d %H:%M:%S')
print(dt)
