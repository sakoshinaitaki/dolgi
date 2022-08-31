def buble_sort(l1st):
    length = len(l1st)
    for i in range(length):
        for j in range(0, length-i-1):
            if l1st[j] > l1st[j+1]:
                temp = l1st[j]
                l1st[j] = l1st[j+1]
                l1st[j+1] = temp

a = [35, 67, 23, 89, 5, 7, 48, 4, 85, 30]
print(a)
buble_sort(a)
print(a)