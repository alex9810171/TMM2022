from PIL import Image

img = Image.open('image/input1.jpg')
data = img.getdata()

# Suppress specific bands (e.g. (255, 120, 65) -> (0, 120, 0) for g)
r = [(d[0], 0, 0) for d in data]
g = [(0, d[1], 0) for d in data]
b = [(0, 0, d[2]) for d in data]

img.putdata(r)
img.save('image/r.png')
img.putdata(g)
img.save('image/g.png')
img.putdata(b)
img.save('image/b.png')