str = 'Amazing'
num_of_chars = 3

if len(str) < num_of_chars*2:
    print(' ')
else:
    result = str[:num_of_chars] + str[len(str)-num_of_chars:]
print(result)    
