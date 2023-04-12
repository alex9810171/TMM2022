from PIL import Image
import numpy as np
import process


def main():
    # ----------stage 1----------
    ## read input size
    size_x, size_y = map(int, input().split())

    ## input target binning size
    binning_size = int(input('Binning size: '))
    
    ## read image info
    image_list = [[0]*size_x for _ in range(size_y)]
    for y in range(size_y):
        image_list[y] = list(map(int, input().split()))
    
    # ----------stage 2----------
    ## process image
    print('\nprocessing...')
    binning_r = process.pixel_binning(image_list, binning_size)

    # ----------stage 3----------
    ## check image size and save image
    save_path = ''
    for y in range(len(binning_r)):
        print(*binning_r[y])

if __name__ == '__main__':
    main()
