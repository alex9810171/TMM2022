import matplotlib.pyplot as plt

def get_histogram(img_arr, width, height):
    hist = [0]*256
    for j in range(height):
        for i in range(width):
            hist[img_arr[j][i]] += 1
    return hist

def change_intensity(img_arr, width, height, value):
    for j in range(height):
        for i in range(width):
            img_arr[j][i] += value
            if img_arr[j][i] > 255:
                img_arr[j][i] = 255
            elif img_arr[j][i] < 0:
                img_arr[j][i] = 0
    return img_arr

def change_contrast(img_arr, width, height, value):
    sum = 0
    for j in range(height):
        for i in range(width):
            sum += img_arr[j][i]
    avg = sum//(width*height)
    for j in range(height):
        for i in range(width):
            img_arr[j][i] += (img_arr[j][i]-avg)*value//100
            if img_arr[j][i] > 255:
                img_arr[j][i] = 255
            elif img_arr[j][i] < 0:
                img_arr[j][i] = 0
    return img_arr

def draw_histogram(hist, path):
    x_axis = [i for i in range(256)]
    y_axis = hist
    plt.bar(x_axis, y_axis, width=1)
    plt.xlim(0, 255)
    plt.savefig(path)
   
