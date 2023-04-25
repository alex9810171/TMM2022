import os
import random
import numpy as np
from PIL import Image

def main():
    # initial settings
    image_path = '20230411_mosaic_exercise/image'
    image_filename = 'input2.jpg'
    save_path = '20230411_mosaic_exercise/test'
    test_name = str(input('test name: '))
    is_random = True
    
    if is_random:
        size_x, size_y = map(int, input('image size x y: ').split())
        ri = random.randint
        image_array = [[ri(0, 255) for _ in range(size_x)] for _ in range(size_y)]

        image = Image.new(mode='L', size=(size_x, size_y))
        for y in range(len(image_array)):
            for x in range(len(image_array[0])):
                image.putpixel((x, y), image_array[x][y])

        f = open(os.path.join(save_path, test_name)+'.in', 'w')
        print(f'{size_x} {size_y}', file=f)
        print('\n'.join([' '.join([str(cell) for cell in row]) for row in image_array]), file=f)
        f.close()
        image.save(os.path.join(save_path, test_name)+'.png')
    else:
        r, g, b = Image.open(os.path.join(image_path, image_filename)).split()
        width = r.width
        height = r.height
        r.save(os.path.join(save_path, test_name)+'_b.png')
        
        r = np.asarray(r).tolist()
        g = np.asarray(g).tolist()
        b = np.asarray(b).tolist()
        
        f = open(os.path.join(save_path, test_name)+'.in', 'w')
        print(f'{width} {height}', file=f)
        print('\n'.join([' '.join([str(cell) for cell in row]) for row in b]), file=f)
        f.close()

if __name__ == '__main__':
    main()