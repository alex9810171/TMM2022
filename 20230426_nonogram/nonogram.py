def compress(img_arr, width, height, target_size):
    new_arr = [[0]*target_size for _ in range(target_size)]
    binning_size_width = width//target_size
    binning_size_height = height//target_size
    for j in range(height-height%target_size):
        for i in range(width-width%target_size):
            #print(f"Put ({i}, {j}) to ({i//binning_size_width}, {j//binning_size_height})")
            new_arr[j//binning_size_height][i//binning_size_width] += img_arr[j][i]
    for j in range(target_size):
        for i in range(target_size):
            new_arr[j][i] //= binning_size_width*binning_size_height
    return new_arr

def binarize(img_arr, width, height):
    for j in range(height):
        for i in range(width):
            if img_arr[j][i] < 128:
                img_arr[j][i] = 0
            else:
                img_arr[j][i] = 1
    return img_arr

def get_row_and_col(img_arr, width, height):
    row = []
    col = []
    for i in range(width):
        ele = []
        cnt = 0
        for j in range(height):
            if img_arr[j][i] == 1:
                cnt += 1
                if j == height-1:
                    ele.append(cnt)
            else:
                if cnt > 0:
                    ele.append(cnt)
                    cnt = 0
        row.append(ele)
    for j in range(height):
        ele = []
        cnt = 0
        for i in range(width):
            if img_arr[j][i] == 1:
                cnt += 1
                if i == width-1:
                    ele.append(cnt)
            else:
                if cnt > 0:
                    ele.append(cnt)
                    cnt = 0
        col.append(ele)
    return row, col