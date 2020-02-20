import sys
from PIL import Image

file_name = sys.argv[1]
new_name = sys.argv[2]
picture = Image.open(file_name)
width = picture.size[1]
height = picture.size[0]
if width >= height:
	new_size = width
else:
	new_size = height
new_picture = picture.resize((new_size, new_size))
new_picture.save(new_name)