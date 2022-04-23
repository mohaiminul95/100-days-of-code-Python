str = 'Coding'
result = ''

for i in range(len(str)):
    if i % 2 != 0:
        result += str[i]

print(result)
