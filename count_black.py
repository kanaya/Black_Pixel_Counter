from PIL import Image

img = Image.open('sample.png')
print('Reading image of {} pixels.'.format(img.size))
(img_size_x, img_size_y) = img.size

n_black = 0
for y in range(0, img_size_y):
    for x in range(0, img_size_x):
        p = (x, y)
        v = img.getpixel(p)
        if v == (0, 0, 0):
            n_black += 1

print('I found {} black pixels.'.format(n_black))


