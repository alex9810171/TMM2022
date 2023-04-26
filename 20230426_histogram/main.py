import os
import argparse
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import utils

def make_parser():
    parser = argparse.ArgumentParser('Histogram parser')
    parser.add_argument("-m", "--mode", type=int, default=1, help="Input format (1: txt input, 2: image input)")
    parser.add_argument("-i", "--image_path", type=str, default=None, help="Image path")
    parser.add_argument("-s", "--save_path", type=str, default=None, help="Save path")
    return parser

def main(args):
    if args.mode == 1:
        width, height, value = map(int, input().split())
        img_arr = []
        for _ in range(height):
            img_arr.append(list(map(int, input().split())))
        img_arr = utils.change_contrast(img_arr, width, height, value)
        for j in range(height):
            print(*img_arr[j])
        hist = utils.get_histogram(img_arr, width, height)
        utils.draw_histogram(hist, args.save_path)
        
    elif args.mode == 2:
        img = Image.open(args.image_path).convert('L')
        width = img.width
        height = img.height
        '''
        target_size = args.target_size
        if target_size <= 0:
            print(f"Not expected target size!")
            os._exit(0)
        img_arr = np.array(img).tolist()
        img_arr = nonogram.compress(img_arr, width, height, target_size)
        '''
        img_arr = np.array(img_arr, dtype=np.uint8)
        new_img = Image.fromarray(img_arr)
        new_img.save(args.save_path)
    else:
        print("Undefined Input format!")

if __name__ == "__main__":
    args = make_parser().parse_args()
    main(args)