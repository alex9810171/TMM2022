def sort_height(height_list):
    # TO_DO
    for i in range(num_of_student):
        key = i
        for j in range(i+1, num_of_student):
            if i%2 == 0:
                if height_list[key] > height_list[j]:
                    key = j
            else:
                if height_list[key] < height_list[j]:
                    key = j
        height_list[i], height_list[key] = height_list[key], height_list[i]
    return height_list

num_of_student = int(input())
height_list = [0]*num_of_student
for i in range(num_of_student):
    height_list[i] = int(input())
sort_list = sort_height(height_list)
print(' '.join([str(height) for height in sort_list]))

path = 'answer/ans_9.txt'
f = open(path, 'w')
print(' '.join([str(height) for height in sort_list]), file=f)
f.close()