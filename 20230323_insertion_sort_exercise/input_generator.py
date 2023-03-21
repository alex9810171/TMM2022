import random

print(f'Generate student number: ', end='')
num_of_student = int(input())
height_list = [0]*num_of_student
for i in range(num_of_student):
    height_list[i] = random.randint(140, 180)

height_list = sorted(height_list)
height_list.reverse()
print(f'Swap student number: ', end='')
swap_time = int(input())
for i in range(swap_time):
    x = random.randint(0, num_of_student)
    y = random.randint(0, num_of_student)
    height_list[x], height_list[y] = height_list[y], height_list[x]

path = 'test/test.txt'
f = open(path, 'w')
print(num_of_student, file=f)
print('\n'.join([str(height) for height in height_list]), file=f)
f.close()