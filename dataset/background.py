from PIL import Image
from pathlib import Path
import os

for things in os.walk('./'):
	print(things[0])
	for j in things[2]:
		if(j[-4:] == '.png'):
			name = things[0]+'/'+j
			print(name)
			image = Image.open(name)
			print(image.size)
			image.convert("RGBA")
			canvas = Image.new("RGBA",image.size,(255,255,255,255))
			canvas.paste(image,mask=image)
			canvas.thumbnail(image.size,Image.ANTIALIAS)
			print(Path(name))
			canvas.save(Path(name),format="PNG")
