import io

import whatimage
import pyheif
from PIL import Image


import os
import sys
from PIL import Image
from PIL.ExifTags import TAGS


def decode_image(bytesIo):
    # bites = io.BytesIO(bytesIo)
    # bites.seek(0)
    # image = Image.open(bites)
    # print("therer")
    #
    # for (tag, value) in Image.open(bytesIo)._getexif().iteritems():
    #     print('%s = %s' % (TAGS.get(tag), value))


    fmt = whatimage.identify_image(bytesIo)
    if fmt in ['heic', 'avif']:
        i = pyheif.read_heif(bytesIo)

        # Extract metadata etc
        for metadata in i.metadata or []:
            if metadata['type'] == 'Exif':
                print(metadata)
        # do whatever
        s = io.BytesIO()
        pi = Image.frombytes(mode=i.mode, size=i.size, data=i.data)

        return i.metadata