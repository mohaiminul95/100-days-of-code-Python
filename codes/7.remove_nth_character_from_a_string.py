str = 'Rabid'
n= 3
result = ''

if len(str) == 0 or n >= len(str):
    print('Enter proper string')
else:
    for i in range(len(str)):
        if i != n:
            result += str[i]
print(result)            

