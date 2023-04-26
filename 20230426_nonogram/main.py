import os
import argparse
import numpy as np
from PIL import Image
import nonogram

def make_parser():
    parser = argparse.ArgumentParser('Nonogram parser')
    parser.add_argument("-m", "--mode", type=int, default=1, help="Input format (1: txt input, 2: image input)")
    parser.add_argument("-i", "--image_path", type=str, default=None, help="Image path")
    parser.add_argument("-t", "--target_size", type=int, default=0, help="Target size")
    parser.add_argument("-s", "--save_path", type=str, default=None, help="Save path")
    return parser

def stage_1_mode_1():
    width, height, target_size = map(int, input().split())
    img_arr = []
    for _ in range(height):
        img_arr.append(list(map(int, input().split())))
    img_arr = nonogram.compress(img_arr, width, height, target_size)
    [print(*img_arr[i]) for i in range(target_size)]

def stage_1_mode_2(img, args):
    img = Image.open(args.image_path).convert('L')
    width = img.width
    height = img.height
    target_size = args.target_size
    if target_size <= 0:
        print(f"Not expected target size!")
        os._exit(0)
    img_arr = np.array(img).tolist()
    img_arr = nonogram.compress(img_arr, width, height, target_size)
    img_arr = np.array(img_arr, dtype=np.uint8)
    new_img = Image.fromarray(img_arr)
    new_img.save(args.save_path)

def stage_2_mode_1():
    width, height = map(int, input().split())
    img_arr = []
    for _ in range(height):
        img_arr.append(list(map(int, input().split())))
    img_arr = nonogram.binarize(img_arr, width, height)
    [print(*img_arr[i]) for i in range(height)]
    
def stage_3_mode1():
    width, height = map(int, input().split())
    img_arr = []
    for _ in range(height):
        img_arr.append(list(map(int, input().split())))
    row, col = nonogram.get_row_and_col(img_arr, width, height)
    for i in range(len(row)):
        if len(row[i]) > 0:
            print(*row[i])
        else:
            print('0')
    for i in range(len(col)):
        if len(col[i]) > 0:
            print(*col[i])
        else:
            print('0')
    
def main(args):
    if args.mode == 1:
        width, height = map(int, input().split())
        img_arr = []
        for _ in range(height):
            img_arr.append(list(map(int, input().split())))
        row, col = nonogram.get_row_and_col(img_arr, width, height)
        for i in range(len(row)):
            if len(row[i]) > 0:
                print(*row[i])
            else:
                print('0')
        for i in range(len(col)):
            if len(col[i]) > 0:
                print(*col[i])
            else:
                print('0')
    elif args.mode == 2:
        img = Image.open(args.image_path).convert('L')
        width = img.width
        height = img.height
        target_size = args.target_size
        if target_size <= 0:
            print(f"Not expected target size!")
            os._exit(0)
        img_arr = np.array(img).tolist()
        img_arr = nonogram.compress(img_arr, width, height, target_size)
        img_arr = np.array(img_arr, dtype=np.uint8)
        new_img = Image.fromarray(img_arr)
        new_img.save(args.save_path)
    else:
        print("Undefined Input format!")
        
if __name__ == "__main__":
    args = make_parser().parse_args()
    main(args)