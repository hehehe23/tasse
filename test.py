from PIL import Image
import os
import string
import random
from PIL import Image

def random_generator(size = 8, chars = string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

def rotation(deg, name):
    img = Image.open('/home/xxx/tasse/0.png')
    img = img.rotate(deg, expand = True)
    img.save('/home/xxx/tasse/data/45/' + name + '.jpg')

for i in range(45):
    rotation(i + 150, random_generator())