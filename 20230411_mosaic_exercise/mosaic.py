from PIL import Image
import os
import process

def main():
    # ----------stage 1----------
    ## read input size, target binning size
    size_x, size_y = map(int, input().split())
    
    ## read image info
    image_list = [[0]*size_x for _ in range(size_y)]
    for y in range(size_y):
        image_list[y] = list(map(int, input().split()))
    
    # ----------stage 2----------
    ## process image
    print('\nprocessing...')
    
    '''
    ## phase 1
    print(process.count_avg(image_list))
    '''
    ## phase 2
    l_1 = [image_list[i][:size_x//2] for i in range(size_y//2)]
    l_2 = [line[size_x//2:] for line in image_list[:size_y//2]]
    l_3 = [line[:size_x//2] for line in image_list[size_y//2:]]
    l_4 = [line[size_x//2:] for line in image_list[size_y//2:]]
    binning_1 = process.count_avg(l_1)
    binning_2 = process.count_avg(l_2)
    binning_3 = process.count_avg(l_3)
    binning_4 = process.count_avg(l_4)
    
    
    ## phase 3
    #binning_r = process.pixel_binning(image_list, binning_size)

    # ----------stage 3----------
    ## check image size and save image
    save_path = 'stage_3_answer'
    f = open(os.path.join(save_path, '10.out'), 'w')
    
    
    ## phase 2
    arr = [[binning_1, binning_2], [binning_3, binning_4]]
    
    print(*arr[0])
    print(*arr[1])
    
    
    '''
    ## phase 3
    for i in range(len(binning_r)):
        print(*binning_r[i])
    f.close()
    '''

if __name__ == '__main__':
    main()
