import PIL
from PIL import Image, ImageDraw, ImageFont


im = Image.open('c:/py/cards/yukina.png')

font = ImageFont.truetype("c:/py/OpenSans-Light.ttf", 25)
im = im.convert("RGB")
drawer = ImageDraw.Draw(im)
drawer.text(
	(50, 100),
	"Hello World!\nПривет мир!",
	font=font,
    fill= (255,0,0)
)  

im.save('new_yukina.png')

im.show()
 