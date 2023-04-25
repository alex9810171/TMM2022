def count_avg(matrix):
  width = len(matrix[0])
  height = len(matrix)
  sum = 0
  pixel_count = width*height
  for j in range(height):
    for i in range(width):
      sum += matrix[j][i]
  avg = sum//pixel_count
  return avg

def pixel_binning(image, binning_size):
  # TO_DO
  new_image_width = len(image[0])//binning_size
  new_image_height = len(image)//binning_size
  new_image = [[0]*new_image_width for i in range(new_image_height)]
  for j in range(new_image_height):
    for i in range(new_image_width):
      matrix = [[0]*binning_size for i in range(binning_size)]
      for y in range(binning_size):
        for x in range(binning_size):
          # print(x+i*binning_size, y+j*binning_size)
          matrix[y][x] = image[y+j*binning_size][x+i*binning_size]
      new_image[j][i] = count_avg(matrix)
  return new_image