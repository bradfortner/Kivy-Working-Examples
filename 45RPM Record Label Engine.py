# Modified from http://pillow.readthedocs.io/en/3.1.x/reference/ImageDraw.html

from PIL import Image, ImageDraw, ImageFont

base_image = Image.open("45rpm.png")
text_overlay = Image.new('RGBA', base_image.size, (255,255,255,0))
fnt = ImageFont.truetype('FreeSansBold.ttf', 110)
draw_overlay = ImageDraw.Draw(text_overlay)
draw_overlay.text((1078,680), "Hello", font=fnt, fill=(0,0,0,255))
draw_overlay.text((1053,790), "World", font=fnt, fill=(0,0,0,255))
draw_overlay.text((948,1470), "....brad....", font=fnt, fill=(0,0,0,255))
fnt = ImageFont.truetype('FreeSansBold.ttf', 57)
draw_overlay.text((948,1590), "And His Binarians", font=fnt, fill=(0,0,0,255))
output_file = Image.alpha_composite(base_image, text_overlay)

output_file.save("new.png")