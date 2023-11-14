a = []
n = int(input())
while True:
    try:
        line = input()
    except EOFError:
        break
    for i in line.split():
        if i!= '' :
            a.append(int(i))
m = int(input())
a_list, b_list, c_list = [], [], []
tmp = 10000

for i in range(n // 2 + 1):
    if (m - int(a[i])) in a:
        a_list.append(int(a[i]))
        b_list.append(int(m - int(a[i])))
    if abs(m - 2*int(a[i])) < tmp:
        tmp = abs(m - 2*int(a[i]))
for i in range(len(a_list)):
    if abs(a_list[i] - b_list[i]) == tmp:
        print(a_list[i])
        print(b_list[i])
        break



    

        