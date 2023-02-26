from PIL import Image, ImageStat, ImageDraw

def minmax(im):
	stat = ImageStat.Stat(im)
	min, max = [], []
	for band in stat.extrema:
		min.append(band[0])
		max.append(band[1])
	if len(stat.extrema) == 1:
		return min[0], max[0]
	else:
		return tuple(min), tuple(max)

path_image = "paris.jpg"
image = Image.open(path_image)
print(minmax(image)[0], minmax(image)[1])

img = Image.new('RGB', (500, 300), minmax(image)[1])
draw = ImageDraw.Draw(img)

draw.rectangle(
   (200, 125, 300, 200),
   fill=minmax(image)[0],
   outline=(0, 0, 0))
img.save(f"min-max-{path_image[:-4]}.png")#.show()


def most_frequent_colour(image):
    w, h = image.size
    pixels = image.getcolors(w * h)

    most_frequent_pixel = pixels[0]

    for count, colour in pixels:
        if count > most_frequent_pixel[0]:
            most_frequent_pixel = (count, colour)

    return most_frequent_pixel[1]

def least_frequent_colour(image):
    w, h = image.size
    pixels = image.getcolors(w * h)

    most_frequent_pixel = pixels[0]

    for count, colour in pixels:
        if count < most_frequent_pixel[0]:
            most_frequent_pixel = (count, colour)

    return most_frequent_pixel[1]


print(most_frequent_colour(image))
print(least_frequent_colour(image))

img = Image.new('RGB', (500, 300), most_frequent_colour(image))
draw = ImageDraw.Draw(img)

draw.rectangle(
   (200, 125, 300, 200),
   fill=least_frequent_colour(image),
   outline=(0, 0, 0))
img.save(f'most-least-{path_image[:-4]}.png')#.show()