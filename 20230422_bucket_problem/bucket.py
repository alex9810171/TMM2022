'''question
有3個1塊錢
1個5塊錢
11個10塊錢

要放到R,G,B這3個籃子
印出所有組合
'''
import time

start = time.time()

one = 15
five = 15
ten = 100

def put(money):
    table = []
    for i in range(money+1):
        for j in range(money-i+1):
            sol = [i, j, money-j-i]
            table.append(sol)
    return table

table_one = put(one)
table_five = put(five)
table_ten = put(ten)

ans = []
print(len(table_ten))

'''
for k in range(len(table_ten)):
    for j in range(len(table_five)):
        for i in range(len(table_one)):
            ans.append([table_one[i][0], table_five[j][0], table_ten[k][0]])
            ans.append([table_one[i][1], table_five[j][1], table_ten[k][1]])
            ans.append([table_one[i][2], table_five[j][2], table_ten[k][2]])
            #print(f'R: {table_one[i][0]} of one, {table_five[j][0]} of five, {table_ten[k][0]} of ten')
            #print(f'G: {table_one[i][1]} of one, {table_five[j][1]} of five, {table_ten[k][1]} of ten')
            #print(f'B: {table_one[i][2]} of one, {table_five[j][2]} of five, {table_ten[k][2]} of ten\n')
'''

end = time.time()

print(end-start)