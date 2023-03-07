


n = int(input("n = "))
m = int(input("m = "))

one = [int(i) for i in input('Введите элементы множества 1: ').split()]
two = [int(i) for i in input('Введите элементы множества 2: ').split()]

# one = set([1,5,78,2,4,76,8,43,1,6])
# two = set([34,657,64,3443,2,7,33,6,0])

result = list(set(one) & set(two))
result.sort()

print(result)


n = int(input('n = '))
arr = list()
for i in range(n):
    x = int(input())
    arr.append (x)
arr_count = list()

for i in range(len(arr) - 1):
    arr_count.append(arr[i - 1] + arr[i] + arr[i + 1])
    arr_count.append(arr[-2] + arr [-1] + arr [0])

print (max(arr_count))