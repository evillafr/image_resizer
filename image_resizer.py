import sys
from PIL import Image

file_name = sys.argv[1]
picture = Image.open(file_name)
width = picture.size[1]
height = picture.size[0]
if width >= height:
	new_size = width
else:
	new_size = height