n = int(input())
arr = [0] * n

for i in range(n):
    elem = int(input())
    arr[i] = elem

end_of_array = n
BLANK = 0

for _ in range(2):
    s, e = map(int, input().split())
    end_of_temp_array = 0
    temp = [0] * n
    for i in range(s-1, e):
        arr[i] = 0
    
    for i in range(end_of_array):
        if arr[i] != BLANK:
            temp[end_of_temp_array] = arr[i]
            end_of_temp_array += 1

    for i in range(n):
       arr[i] = temp[i]

    end_of_array = end_of_temp_array
    
print(end_of_array)
for elem in arr:
    if elem != 0:
        print(elem)