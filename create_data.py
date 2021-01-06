import string
import random
from PIL import Image

def random_generator(size = 8, chars = string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

def rotation(deg, name, label):
    img = Image.open('/home/xxx/tasse/images/normal.png')
    img = img.rotate(deg, expand = True)
    img.save('/home/xxx/tasse/test/' + label + '/' + name + '.jpg')


def fill(x):
    for i in range(x):
        rotation(i, random_generator(), '45')

    for i in range(x):
        rotation(i + 45, random_generator(), '90')

    for i in range(x):
        rotation(i + 90, random_generator(), '135')

    for i in range(x):
        rotation(i + 135, random_generator(), '180')

    for i in range(x):
        rotation(i + 180, random_generator(), '225')

    for i in range(x):
        rotation(i + 225, random_generator(), '270')

    for i in range(x):
        rotation(i + 270, random_generator(), '315')

    for i in range(x):
        rotation(i + 315, random_generator(), '360')


fill(2)