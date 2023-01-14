n = int(input())

array = []
for i in range(n):
    name, score = input().split()
    array.append((name, int(score)))
    
def setting(data):
    return data[1]
    
result = sorted(array, key=setting)
for i in range(n):
    name, score = result[i]
    print(name, end=' ')
